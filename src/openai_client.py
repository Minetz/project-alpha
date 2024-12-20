from openai import OpenAI
from config.load_env import load_api_key

def get_client():
    key = load_api_key()
    return OpenAI(api_key=key)