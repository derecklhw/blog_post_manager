import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler(filename='app.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.INFO)