import logging

ascii_chars = ('.', ',', ':', '+', '*', '?', '%', 'S', '#', '@')
good_relation = 0.55
default_width = 720
max_bright = 256

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
    )
logger = logging.getLogger(__name__)