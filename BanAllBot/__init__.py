import os
import logging 
from pyrogram import Client
from config import Config 

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV",False))

if ENV:
    API_ID=int(os.environ.get("API_ID","25206101"))
    API_HASH=str(os.environ.get("API_HASH","2135724a8fdecb737f31d22ec8e6894b"))
    TOKEN=str(os.environ.get("TOKEN","7657159740:AAHjfaLL2CTyJKqsJqXQl55Fk5NY9EuhR3c"))
    SUDO = list(int(i) for i in os.environ.get("SUDO", "7601457849").split(" "))
    START_IMG=str(os.environ.get("START_IMG","https://graph.org/file/4308dcc94aacbdc3ed0c9-c04a9611c927588ddc.jpg"))
    BOT_ID=int(os.environ.get("BOT_ID","7657159740"))
    BOT_USERNAME=str(os.environ.get("BOT_USERNAME","http://t.me/Copyrightremover213bot"))
    BOT_NAME=str(os.environ.get("BOT_NAME","copyright Remover bot"))

else:
    API_ID=Config.API_ID
    API_HASH=Config.API_HASH
    TOKEN=Config.TOKEN
    SUDO=Config.SUDO
    START_IMG=Config.START_IMG
    BOT_ID=Config.BOT_ID
    BOT_USERNAME=Config.BOT_USERNAME
    BOT_NAME=Config.BOT_NAME



app=Client(
    "BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="BanAllBot.modules")
     )

LOG.info("starting the bot....")


