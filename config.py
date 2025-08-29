import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8076820491:AAGnZ2lmXhU4_NrgPl_k_PTjAytV4MDikHw")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "24663422"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "723918463d17ff94e655e2cc53513c61)  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "24663422").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility

