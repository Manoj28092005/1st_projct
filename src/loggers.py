import logging 
import os 
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)
LOG_FILE=os.path.join(os.getcwd(),"logs",LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filemode='w'
) 
  