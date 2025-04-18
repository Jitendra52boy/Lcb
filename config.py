import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29080362"))
API_HASH = getenv("API_HASH", "2af932be312ce9c4e4ecb84bce09109e")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7620897033:AAHvcnzvSN_qYDtYIgdpvqDfET00GdTdSvA")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 330))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002604755252))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID",7631783820))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Abhimusicss/Abhi-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "stable")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/the_amazing_zone")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/the_amazing_zone")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQG7uyoAZjHCRbQ8a51QQdaiHu1fLeobZeZbPh77kyqKRDwt2gSoRhcax2N0ZXSSumpucmE0DK7u6mMUbrcUeKuTZ4AG6cKOAfPc4CbfiZgck4wLOTcPZOKzzuIgL87t3sGepwNLpge254jPPvDmWxMS00LTgKuI2kloihisy_jOo_y4rBMqv0-EEIteiSppEAfIA6aFE60D4KXjIeDnIIU4TxOR8SgIQ7zanMgJ76Fe5YbfP8uoK872EArfLcjXHacNIrO9sOI9-Pv1XZ-6yo-cDuUzkLltJuuArS8THVer0QlGUMe0wE9q7bSMQt0JkTpxxwl6VM7_sEBqLW_EjF5wq_ueZQAAAAHR-qQFAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/9355a37178ac337a74f22-84e81139c63892bd73.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/f7e5d91a2deb7828f5c12-2146a446872584a98e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/7bb8139ec6c5740d4a308-c62fda2c9d116d87c3.jpg"
STATS_IMG_URL = "https://files.catbox.moe/yfvai0.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/nef735.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/51cb8a22e65caa4382879.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/nef735.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
