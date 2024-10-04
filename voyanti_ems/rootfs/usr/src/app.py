import time
import logging
import requests

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# The endpoint you want to fetch data from (example API)
API_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

def fetch_data():
    """Fetch data from the API endpoint."""
    try:
        # Send an HTTP GET request to the API
        logger.info(f"Fetching data from {API_URL}...")
        response = requests.get(API_URL)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Data fetched successfully: {data}")
        else:
            logger.error(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while fetching data: {e}")

if __name__ == "__main__":
    logger.info("Starting the Python data-fetching script...")

    # Infinite loop to fetch data every 60 seconds
    while True:
        fetch_data()

        # Wait 60 seconds before the next fetch
        time.sleep(60)