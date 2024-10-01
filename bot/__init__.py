import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID","26415213"))
    API_HASH = os.environ.get("API_HASH","a3e87c0ef3abb7bdbd653e7f17d9cbad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7737057503:AAHx_ywxRHneVpzczBTAd_lbmNm5tHsPF8Y")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","SnappchatStoriesBot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
