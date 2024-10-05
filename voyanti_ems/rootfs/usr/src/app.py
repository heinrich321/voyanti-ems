import time
import logging
import requests
from solar import fetch_solar_forecast, publish_solar_forecast

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting the Python data-fetching script...")

    forecast_data = fetch_solar_forecast()

    logger.info(f"Solar Data: {forecast_data}")
    
    if forecast_data:
        # Extract relevant data
        total_today_kwh = forecast_data.get("total_today_kwh", 0)
        day_profile = forecast_data.get("day_profile", [])
        
        # Publish the forecast data to Home Assistant, including time series data
        publish_solar_forecast(total_today_kwh, day_profile)

    # Infinite loop to fetch data every 60 seconds
    while True:
        # Wait 60 seconds before the next fetch
        time.sleep(60)