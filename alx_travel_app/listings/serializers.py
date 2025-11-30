from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    # Counts the no. of related booking and Review objects
    booking_count = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 
        'booking_count', 'review_count']

        # Methods to calculate booking and review counts (format is get_<field_name>)
    def get_booking_count(self, obj):
        # The 'bookings' is the related_name set on FK in Booking Model
        return obj.bookings.count()

    def get_review_count(self, obj):
        return obj.reviews.count()

class BookingSerializer(serializers.ModelSerializer):
    # Overrides the default PrimaryKeyRelatedField for 'listing'
    # Calls the __str__ method of the Listing Model
    listing = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'user', 'start_date',
         'end_date', 'total_price', 'status', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'listing', 'rating', 'comment', 'created_at']