import tomllib
import os

def load_credentials():
    config_path = os.path.join(os.path.dirname(__file__), ".streamlit/secrets.toml")
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    username = config["credentials"]["username"]
    password = config["credentials"]["password"]
    return username, password