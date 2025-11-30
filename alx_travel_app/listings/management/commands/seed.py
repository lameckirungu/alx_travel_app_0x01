"""
Django Management Command: seed
================================

This command populates the database with sample data for testing and development.

Usage:
    python manage.py seed
    python manage.py seed --clear  # Clears existing data first

How Django Management Commands Work:
------------------------------------
1. Commands must be in: <app>/management/commands/<command_name>.py
2. The class must inherit from django.core.management.base.BaseCommand
3. Implement handle() method - this runs when command is executed
4. Use self.stdout.write() for output (not print())
5. Access command-line arguments via options dictionary

Key Concepts:
- BaseCommand: Base class for all Django management commands
- handle(): Main method that executes the command logic
- options: Dictionary containing parsed command-line arguments
- get_or_create(): Django ORM method that gets existing or creates new objects
"""

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from decimal import Decimal
from listings.models import Listing, Booking, Review

User = get_user_model()


class Command(BaseCommand):
    """
    Management command to seed the database with sample data.
    
    Attributes:
        help (str): Description shown when running 'python manage.py help seed'
    """
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def add_arguments(self, parser):
        """
        Add custom command-line arguments.
        
        This method allows you to define optional arguments that users
        can pass when running the command.
        
        Example: python manage.py seed --clear
        """
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before seeding',
        )

    def handle(self, *args, **options):
        """
        Main method that executes when the command is run.
        
        Args:
            *args: Positional arguments (not used here)
            **options: Dictionary of command-line options
        """
        if options['clear']:
            self.stdout.write(self.style.WARNING('Clearing existing data...'))
            Review.objects.all().delete()
            Booking.objects.all().delete()
            Listing.objects.all().delete()
            # Note: We don't delete users to avoid breaking authentication
            self.stdout.write(self.style.SUCCESS('Existing data cleared!'))

        self.stdout.write(self.style.SUCCESS('Starting to seed database...'))

        # Step 1: Create or get users
        users = self.create_users()
        
        # Step 2: Create listings
        listings = self.create_listings()
        
        # Step 3: Create bookings (requires listings and users)
        self.create_bookings(listings, users)
        
        # Step 4: Create reviews (requires listings)
        self.create_reviews(listings, users)

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully!'))

    def create_users(self):
        """
        Create sample users for bookings.
        
        Returns:
            list: List of User objects
        """
        self.stdout.write('Creating users...')
        
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com'},
            {'username': 'jane_smith', 'email': 'jane@example.com'},
            {'username': 'bob_wilson', 'email': 'bob@example.com'},
        ]
        
        users = []
        for user_data in users_data:
            # get_or_create returns (object, created) tuple
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email']}
            )
            if created:
                # Set a default password for created users
                user.set_password('password123')
                user.save()
                self.stdout.write(f'  ✓ Created user: {user.username}')
            else:
                self.stdout.write(f'  → User already exists: {user.username}')
            users.append(user)
        
        return users

    def create_listings(self):
        """
        Create sample property listings.
        
        Returns:
            list: List of Listing objects
        """
        self.stdout.write('Creating listings...')
        
        listings_data = [
            {
                'title': 'Cozy Beachfront Villa',
                'description': 'Beautiful villa with ocean view, 3 bedrooms, fully equipped kitchen.',
                'price_per_night': Decimal('150.00'),
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin in the mountains, perfect for hiking enthusiasts.',
                'price_per_night': Decimal('85.50'),
            },
            {
                'title': 'Downtown Luxury Apartment',
                'description': 'Modern apartment in city center, close to restaurants and nightlife.',
                'price_per_night': Decimal('200.00'),
            },
            {
                'title': 'Rustic Countryside Farmhouse',
                'description': 'Charming farmhouse with garden, ideal for families.',
                'price_per_night': Decimal('120.75'),
            },
            {
                'title': 'Modern Studio Loft',
                'description': 'Stylish studio with high ceilings and city views.',
                'price_per_night': Decimal('95.00'),
            },
        ]
        
        listings = []
        for listing_data in listings_data:
            listing, created = Listing.objects.get_or_create(
                title=listing_data['title'],
                defaults=listing_data
            )
            if created:
                self.stdout.write(f'  ✓ Created listing: {listing.title}')
            else:
                self.stdout.write(f'  → Listing already exists: {listing.title}')
            listings.append(listing)
        
        return listings

    def create_bookings(self, listings, users):
        """
        Create sample bookings.
        
        Args:
            listings: List of Listing objects
            users: List of User objects
        """
        self.stdout.write('Creating bookings...')
        
        today = timezone.now().date()
        
        bookings_data = [
            {
                'listing': listings[0],  # Beachfront Villa
                'user': users[0],  # john_doe
                'start_date': today + timedelta(days=5),
                'end_date': today + timedelta(days=8),
                'status': 'confirmed',
            },
            {
                'listing': listings[1],  # Mountain Cabin
                'user': users[1],  # jane_smith
                'start_date': today + timedelta(days=10),
                'end_date': today + timedelta(days=12),
                'status': 'pending',
            },
            {
                'listing': listings[2],  # Downtown Apartment
                'user': users[0],  # john_doe
                'start_date': today + timedelta(days=15),
                'end_date': today + timedelta(days=18),
                'status': 'confirmed',
            },
            {
                'listing': listings[0],  # Beachfront Villa
                'user': users[2],  # bob_wilson
                'start_date': today + timedelta(days=20),
                'end_date': today + timedelta(days=25),
                'status': 'pending',
            },
        ]
        
        for booking_data in bookings_data:
            # Calculate total price based on nights
            nights = (booking_data['end_date'] - booking_data['start_date']).days
            total_price = booking_data['listing'].price_per_night * nights
            booking_data['total_price'] = total_price
            
            # Create booking (using booking_id as unique identifier)
            booking = Booking.objects.create(**booking_data)
            self.stdout.write(
                f'  ✓ Created booking: {booking.user.username} → {booking.listing.title}'
            )

    def create_reviews(self, listings, users):
        """
        Create sample reviews for listings.
        
        Args:
            listings: List of Listing objects
            users: List of User objects (not used here, but could be for user reviews)
        """
        self.stdout.write('Creating reviews...')
        
        reviews_data = [
            {
                'listing': listings[0],  # Beachfront Villa
                'rating': 5,
                'comment': 'Absolutely amazing! The view was breathtaking and the place was spotless.',
            },
            {
                'listing': listings[0],  # Beachfront Villa
                'rating': 4,
                'comment': 'Great location, but could use better WiFi.',
            },
            {
                'listing': listings[1],  # Mountain Cabin
                'rating': 5,
                'comment': 'Perfect getaway! Very peaceful and well-maintained.',
            },
            {
                'listing': listings[2],  # Downtown Apartment
                'rating': 4,
                'comment': 'Nice place, excellent location. A bit noisy at night though.',
            },
            {
                'listing': listings[3],  # Farmhouse
                'rating': 5,
                'comment': 'Loved the garden! Great for families with kids.',
            },
        ]
        
        for review_data in reviews_data:
            review = Review.objects.create(**review_data)
            self.stdout.write(
                f'  ✓ Created review: {review.rating}★ for {review.listing.title}'
            )

