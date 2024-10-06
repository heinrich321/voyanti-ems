import os
import requests
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Home Assistant Supervisor API Configuration
HOME_ASSISTANT_URL = "http://supervisor/core/api"
SUPERVISOR_TOKEN = os.getenv("SUPERVISOR_TOKEN")  # Access the token from the environment variable

# VOYANTI Site ID (passed as add-on option)
VOYANTI_SITE_ID = os.getenv("VOYANTI_SITE_ID")  # Replace with default or add-on configuration
API_URL = f"https://xi1qbxerg8.execute-api.eu-north-1.amazonaws.com/prod/site-forecast?siteId={VOYANTI_SITE_ID}"

# Headers for Home Assistant API requests
HEADERS = {
    "Authorization": f"Bearer {SUPERVISOR_TOKEN}",
    "Content-Type": "application/json"
}

# Home Assistant sensor entity to update
UPDATE_SENSOR_URL = f"{HOME_ASSISTANT_URL}/states/sensor.solar_forecast"

# Function to fetch solar forecast from the API
def fetch_solar_forecast():
    logger.info(API_URL)
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            logger.info(f"Failed to fetch data from API: {response.status_code}")
            return None
    except Exception as e:
        logger.info(f"Error fetching data: {e}")
        return None

# Function to publish solar forecast to Home Assistant, including time series data
def publish_solar_forecast(total_today_kwh, day_profile):
    # Create a dictionary to hold the time series forecast
    time_series_forecast = {entry["period_end"]: entry["pv_energy_rooftop"] for entry in day_profile}

    # Create the payload with time series data as attributes
    payload = {
        "state": total_today_kwh,  # Total forecasted kWh for today
        "attributes": {
            "unit_of_measurement": "kWh",
            "friendly_name": "Voyanti Solar Energy Forecast",
            "device_class": "energy",
            "state_class": "measurement",
            "forecast": True,
            "time_series_forecast": time_series_forecast  # Add time series forecast as an attribute
        }
    }

    logger.info(payload)

    try:
        # Publish the forecast data to Home Assistant
        logger.info(UPDATE_SENSOR_URL)
        logger.info(HEADERS)
        response = requests.post(UPDATE_SENSOR_URL, headers=HEADERS, data=json.dumps(payload))
        if response.status_code == 200:
            logger.info("Solar forecast published successfully.")
        else:
            logger.info(f"Failed to publish forecast: {response.status_code}")
            logger.info(response.text)
    except Exception as e:
        logger.info(f"Error occurred while publishing forecast: {e}")