import logging

# Configure logging
logging.basicConfig(
    filename="genai_pipeline.log",  # Log file name
    level=logging.INFO,  # Set logging level
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

def log_request(payload):
    """
    Logs the request payload before sending it.
    """
    logger.info("Request Payload: %s", payload)

def log_response(time_taken, response):
    """
    Logs only the response and execution time.
    """
    if time_taken == -1:
        logger.error("Error in response: %s", response)
    else:
        logger.info("Response received in %ss: %s", time_taken, response)
