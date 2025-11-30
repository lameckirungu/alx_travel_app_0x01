# ALX Travel App

A Django REST Framework-based travel booking application that allows users to browse property listings, make bookings, and leave reviews.

## 🚀 Features

- **Property Listings**: Browse available properties with detailed descriptions and pricing
- **Booking Management**: Create and manage bookings with status tracking (pending, confirmed, canceled)
- **Review System**: Users can leave ratings and comments for properties
- **RESTful API**: Complete REST API with Swagger documentation
- **Database Seeding**: Management command to populate database with sample data
- **CORS Enabled**: Configured for cross-origin requests

## 📋 Table of Contents

- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Management Commands](#management-commands)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Technologies

- **Django 5.2.8**: Web framework
- **Django REST Framework 3.16.1**: REST API toolkit
- **MySQL**: Database (via mysqlclient)
- **drf-yasg**: Swagger/OpenAPI documentation
- **django-cors-headers**: CORS support
- **python-dotenv**: Environment variable management
- **Celery**: Task queue (configured but optional)
- **Redis**: Caching and task broker (optional)

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MySQL Server 5.7 or higher
- pip (Python package manager)
- Git

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lameckirungu/alx_travel_app_0x00.git
   cd alx_travel_app_0x00
   ```

2. **Navigate to the project directory**
   ```bash
   cd alx_travel_app/alx_travel_app
   ```

3. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

## ⚙️ Configuration

1. **Create a `.env` file** in the `alx_travel_app/alx_travel_app/` directory:
   ```bash
   cd alx_travel_app/alx_travel_app
   touch .env
   ```

2. **Add your database credentials** to the `.env` file:
   ```env
   DB_NAME=your_database_name
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

3. **Create the MySQL database**
   ```sql
   CREATE DATABASE your_database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

## 🗄️ Database Setup

1. **Run migrations**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

3. **Seed the database** with sample data
   ```bash
   python manage.py seed
   ```
   
   To clear existing data before seeding:
   ```bash
   python manage.py seed --clear
   ```

## 🏃 Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - API Base URL: `http://127.0.0.1:8000/api/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`
   - Swagger Documentation: `http://127.0.0.1:8000/swagger/`

## 📚 API Documentation

The API documentation is available via Swagger UI at:
```
http://127.0.0.1:8000/swagger/
```

### API Endpoints

The API endpoints are organized under `/api/`:

- **Listings**: Property listings with booking and review counts
- **Bookings**: Booking management with status tracking
- **Reviews**: Property reviews and ratings

### Example API Response

**Listing Response:**
```json
{
  "id": "uuid",
  "title": "Cozy Beachfront Villa",
  "description": "Beautiful villa with ocean view...",
  "price_per_night": "150.00",
  "booking_count": 2,
  "review_count": 3
}
```

## 📁 Project Structure

```
alx_travel_app_0x00/
├── alx_travel_app/
│   ├── alx_travel_app/
│   │   ├── __init__.py
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # Main URL configuration
│   │   ├── wsgi.py              # WSGI configuration
│   │   ├── asgi.py              # ASGI configuration
│   │   └── .env                 # Environment variables (not in git)
│   ├── listings/
│   │   ├── __init__.py
│   │   ├── models.py            # Listing, Booking, Review models
│   │   ├── serializers.py       # DRF serializers
│   │   ├── views.py             # API views
│   │   ├── admin.py             # Admin configuration
│   │   ├── tests.py             # Unit tests
│   │   ├── migrations/          # Database migrations
│   │   └── management/
│   │       └── commands/
│   │           └── seed.py      # Database seeding command
│   ├── manage.py                # Django management script
│   └── requirement.txt          # Python dependencies
├── .gitignore
└── README.md
```

## 🔨 Management Commands

### Seed Database

Populate the database with sample data:

```bash
python manage.py seed
```

Options:
- `--clear`: Clear existing data before seeding

This command creates:
- 3 sample users
- 5 property listings
- 4 bookings
- 5 reviews

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

To run tests for a specific app:

```bash
python manage.py test listings
```

## 📝 Models

### Listing
- Property listings with title, description, and price per night
- UUID primary key
- Related bookings and reviews

### Booking
- Links users to listings
- Tracks start/end dates, total price, and status
- Status options: pending, confirmed, canceled

### Review
- Ratings (1-5 stars) and comments for listings
- UUID primary key
- Timestamp tracking

## 🔐 Security Notes

⚠️ **Important**: This project is configured for development. Before deploying to production:

1. Change `DEBUG = False` in `settings.py`
2. Set a secure `SECRET_KEY` (use environment variable)
3. Configure proper `ALLOWED_HOSTS`
4. Set up proper CORS policies (currently allows all origins)
5. Use environment variables for sensitive data
6. Enable HTTPS
7. Review and configure security middleware properly

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is part of the ALX Software Engineering program.

## 👤 Author

**Lameck Irungu**
- GitHub: [@lameckirungu](https://github.com/lameckirungu)

## 🙏 Acknowledgments

- ALX Software Engineering Program
- Django and Django REST Framework communities

---

**Note**: Make sure to keep your `.env` file secure and never commit it to version control. It's already included in `.gitignore`.

