# Weather Forecast

## Description
This is a weather forecast website I built using **Flask** and the **OpenWeather API** in **Python**. The website provides users with an easy way to check the weather forecast for a specific location and day. Users can choose to see either temperature or sky conditions, and the website displays the forecast using interactive charts.

### Features
The website offers three main features:

1. **Location Selection**: Users can choose a location to check the weather forecast. The app queries the OpenWeather API to fetch real-time weather data for that location.
   
2. **Date Selection**: Users can select a specific day (up to 5 days in advance, as limited by the free API key) to get the weather forecast for that day.

3. **Weather Parameter Selection**: After choosing the location and day, users can select either:
   - **Temperature**: Displays the forecasted temperature.
   - **Sky Conditions**: Displays the forecasted weather condition (e.g., sunny, cloudy, rainy).

## Project Files and Structure

### `main.py`
This is the entry point for running the Flask application. It imports the necessary configurations and initializes the app. This file is responsible for running the Flask development server and ensuring that the app is ready to handle incoming requests.

### `__init__.py`
This file contains the **Flask app configuration** and is responsible for setting up essential components like the OpenWeather API key. It ensures that your Flask app is properly initialized with all necessary settings.

### `views.py`
The **views.py** file contains the **main page logic**. It handles user input, such as selecting a location, date, and weather parameter (temperature or sky conditions). The file also processes the data retrieved from the OpenWeather API and passes it to the front end, where the results are displayed to the user. It includes routes that render the HTML page, pass dynamic data to the template, and manage the form submissions.

### `templates/`
This folder contains the HTML files used for rendering the web pages. The primary template is:

- **`weather.html`**: This page serves as the main interface for users to select a location, choose a date, and select a weather parameter (temperature or sky conditions). The page also includes an interactive **Chart.js** line chart to display weather trends based on the user's selection.

### `static/`
The `static/` folder contains resources that are used for displaying the weather forecast. This folder includes:

- **Weather Sky Icons**: A collection of icons representing different weather conditions (e.g., sunny, cloudy, rainy, etc.). These icons are used to visually represent the weather forecast.

### `weather_api.py`
This Python file contains functions for interacting with the OpenWeather API. It sends requests to fetch the weather forecast for the selected location and processes the API's JSON responses. This file handles errors gracefully, ensuring that the app can provide meaningful messages when the API request fails (e.g., invalid location or quota exceeded).

## Design Choices

### Flask Framework
I chose **Flask** because of its simplicity and flexibility. Since this project is a small web application, Flask is an ideal choice due to its lightweight nature. Flask allowed me to focus on the essential features of the app without needing to worry about additional overhead.

### OpenWeather API
The **OpenWeather API** was selected for its free tier, which offers weather forecast data for up to 5 days. This perfectly suits the needs of this project, as it allows users to select a day within this 5-day window and view the forecast for that day.

### Chart.js for Visualization
I used **Chart.js** to display the weather trends in a visually appealing and interactive line chart. This choice was made to enhance the user experience by presenting weather data in an easy-to-understand format. Users can instantly see the weather forecast for a given day and compare trends across multiple days.

### Weather Icons
For representing sky conditions (e.g., clear, cloudy, rainy), I included a set of weather-related icons in the `static/` folder. These icons are used to add a visual element to the forecast, making it more intuitive for users to understand the forecasted conditions.

## Challenges and Future Improvements

### Challenges
- **API Limits**: One of the challenges was dealing with the limitation of the free OpenWeather API key, which restricts forecasts to 5 days. This required limiting the forecast functionality to a 5-day window.
- **Chart Integration**: Integrating **Chart.js** into the project was a new experience. It required understanding how to feed dynamic data into the chart and ensuring that the chart rendered cor
