import configparser

config = configparser.ConfigParser()
config.read("config.conf")

def get_base_url():
    return config["default"]["base_url"]

def get_timeout():
    return int(config["default"].get("timeout", 10))

def get_browser():
    return config["default"].get("browser", "chrome")

def get_env():
    return config["default"].get("env", "local")

def is_headless():
    return config["default"].get("headless", "false").lower() == "true"
