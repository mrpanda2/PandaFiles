# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
 API_ID = int(os.environ.get("API_ID", "26626715"))
 API_HASH = os.environ.get("API_HASH", "967f1c73aa77a29009bc364edd30b525")
 BOT_TOKEN = os.environ.get("BOT_TOKEN", "7437271868:AAHhFnm5VpOEj5RQp2vfBok-Ob3W8oRrG2k")
 BOT_USERNAME = os.environ.get("BOT_USERNAME", "@dm_file_bot")
 DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002174665826"))
 SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tnshort.net")
 SHORTLINK_API = os.environ.get('SHORTLINK_API', '3f8fa17494625948754b1f2667753833da7a9079')
 BOT_OWNER = int(os.environ.get("BOT_OWNER", "7216492043"))
 DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://filepanda:filepanda@filepanda.tldmx64.mongodb.net/?retryWrites=true&w=majority&appName=filepanda")
 UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002197998836")
 LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002178404711")
 BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
 FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
 BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
 BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
 OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
 ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{@dm_file_bot})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
├🔹 Hosted On: [Heroku](https://heroku.com)
│
├🔸 Developer: [Predator HackerzZ](https://t.me/pandawiz2) 
│
├🔹 Bot Support: [Support Group](https://t.me/+Yj-mWf3G0-RjZTM9)
│
├🔸 Bot Updates: [Bots Channel](https://t.me/+f5rYPEqX6Q9kMzVl)
│
╰──────[ 😎 ]───────────⍟
"""
 ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [@PredatorHackerzZ](https://github.com/PredatorHackerzZ)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/DonateXrobot) or teleroidgroup@axl``
"""
 HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent FileStore Bot.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from CopyRight Infringement Issue. I support Channel Also You Can Check About Bot.

❌ PORNOGRAPHY CONTENTS are strictly prohibited & get Permanent Ban.
"""
