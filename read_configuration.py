import os
from configparser import ConfigParser


def read_configuration():
    config = ConfigParser()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_dir, "config.ini")
    try:
        config.read(config_path)
        url = config.get("base_info", "base_url")
        return url
    except Exception as e:
        print(f'error: {e}')
