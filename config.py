from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split())

GROUP_SUPPORT = getenv("GROUP_SUPPORT") 

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL) 

OWNER_NAME = getenv("OWNER_NAME") 

BG_IMAGE = getenv("BG_IMAGE") 

ASSISTANT_NAME = getenv("ASSISTANT_NAME") 

LOG_CHANNEL = getenv("LOG_CHANNEL") 

DATABASE_URL = getenv("DATABASE_URL") 

OWNER_ID = getenv("OWNER_ID") 