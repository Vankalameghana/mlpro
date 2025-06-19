import logging
import os
from datetime import datetime  # ✅ fixed import

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create "logs" folder in the current working directory
logs_path = os.path.join(os.getcwd(), "logs")  # ✅ fixed variable name
os.makedirs(logs_path, exist_ok=True)

# Complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setup basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # ✅ fixed 'label' to 'level'
)


