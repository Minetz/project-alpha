import tomllib

def load_api_key():
    with open("./src/config/config.toml", "rb") as f:
        config = tomllib.load(f)
    return config["openai"]["api_key"]