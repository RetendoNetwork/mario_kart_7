import logging
from dotenv import load_dotenv
import os

# Configure the logger
logger = logging.getLogger('Retendo')
logger.setLevel(logging.WARNING)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def connect_mongo():
    # Your MongoDB connection code here
    pass

def init():
    load_dotenv()
    if not os.getenv("MONGO_URI"):
        logger.warning("Error loading .env file")

    connect_mongo()

# Initialize
init()
