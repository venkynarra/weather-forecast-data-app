# Weather Forecast Data App

**Tech Stack:** Python, Streamlit, Plotly, OpenWeather API

## Description
A simple web app that displays upcoming weather forecasts for any city using live data from the OpenWeatherMap API. Built with Streamlit and enhanced with Plotly for visualization.

## How It Works
- Enter a city name.
- Choose how many days to forecast (1 to 5).
- Select whether you want to view temperature trends or sky conditions.
- The app fetches weather data and renders either a Plotly line chart or weather icons based on sky status.

## Files
- `main.py` – Streamlit frontend logic and chart/image rendering
- `backend.py` – Fetches and filters API response from OpenWeatherMap
- `images/` – Contains local icon files (Clear, Cloud, Rain, Snow)

## Setup Instructions
1. Clone this repo
2. Install dependencies:
```bash
pip install streamlit plotly requests
