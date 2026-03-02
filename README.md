# Weather App 🌤️

A simple and elegant weather application built with Django that provides real-time weather information for any city around the world. The app uses the OpenWeatherMap API to fetch current weather data and displays it in a clean, responsive interface.

## Features ✨

- **Real-time Weather Data**: Get current weather information for any city
- **Multiple Weather Metrics**: 
  - Temperature (in Celsius)
  - Atmospheric Pressure
  - Humidity
  - Geographic Coordinates
  - Country Code
- **Responsive Design**: Modern UI with Bootstrap framework
- **Easy to Use**: Simple search interface with city name input
- **Cloud Deployment Ready**: Configured for Vercel deployment

## Screenshots 📸

The app features a clean interface with:
- Navigation bar with weather icon
- Search form for city input
- Weather information display with icons
- Responsive design that works on all devices

## Technologies Used 🛠️

- **Backend**: Django 5.1.4
- **Frontend**: HTML, CSS, Bootstrap 3.4.0
- **API**: OpenWeatherMap API
- **Database**: SQLite3
- **Deployment**: Vercel
- **Icons**: Font Awesome & Bootstrap Glyphicons

## Prerequisites 📋

Before running this application, make sure you have:

- Python 3.9 or higher
- pip (Python package installer)
- An OpenWeatherMap API key

## Installation 🚀

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd weather_app
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Visit [OpenWeatherMap](https://openweathermap.org/)
2. Sign up for a free account
3. Get your API key from your account dashboard
4. Create a `.env` file in the root directory (alongside `manage.py`) and add your credentials:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
OPENWEATHER_API_KEY=your-api-key-here
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage 📖

1. Open your web browser and navigate to the application
2. Enter a city name in the search box
3. Click the search button or press Enter
4. View the weather information displayed below:
   - Geographic coordinates
   - Current temperature in Celsius
   - Atmospheric pressure
   - Humidity percentage

## Project Structure 📁

```
weather_app/
├── main/                    # Main Django app
│   ├── views.py            # View logic and API integration
│   ├── models.py           # Database models
│   ├── urls.py             # URL routing
│   └── admin.py            # Admin interface
├── templates/
│   └── main/
│       └── index.html      # Main template with UI
├── Wheather_App/           # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI application
├── .env                    # Environment variables (create this)
├── .gitignore              # Git ignored files
├── requirements.txt        # Python dependencies
├── vercel.json             # Vercel deployment configuration
└── manage.py               # Django management script
```

## API Integration 🔌

The app integrates with the OpenWeatherMap API to fetch weather data:

- **Endpoint**: `http://api.openweathermap.org/data/2.5/weather`
- **Parameters**: City name and API key
- **Response**: JSON data containing weather information
- **Temperature Conversion**: Automatically converts Kelvin to Celsius

## Deployment 🌐

### Vercel Deployment

This project is configured for deployment on Vercel:

1. Push your code to a Git repository
2. Connect your repository to Vercel
3. Vercel will automatically detect the Django project and deploy it
4. The `vercel.json` file contains the necessary configuration

### Environment Variables

For production deployment, consider setting these environment variables:
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Your domain name

## Configuration ⚙️

### API Key Setup

This application uses `python-dotenv` to securely manage secrets. Make sure your `.env` file contains your OpenWeatherMap API key:

```env
OPENWEATHER_API_KEY=your-api-key-here
```

The application automatically loads this key from the `.env` file via `Wheather_App/settings.py` and uses it in `main/views.py`.

### Customization

- **Styling**: Modify the CSS in `templates/main/index.html`
- **Weather Metrics**: Add more weather data in `main/views.py`
- **UI Components**: Update the Bootstrap classes and layout

## Contributing 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments 🙏

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Bootstrap](https://getbootstrap.com/) for the UI framework
- [Django](https://www.djangoproject.com/) for the web framework

## Support 💬

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/weather_app/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

---

**Note**: This is a demo project. For production use, ensure proper security measures, error handling, and API key management.
