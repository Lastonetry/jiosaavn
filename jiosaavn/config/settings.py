from os import getenv

API_ID = getenv("API_ID", "20937630")
API_HASH = getenv("API_HASH", "3290b11b9246bff1ff44f13e9c7ffb45")
BOT_TOKEN = getenv("BOT_TOKEN", "7406695481:AAEdxn4x4wpAojgvjxvaICyrE46j8zxSxGw")
BOT_COMMANDS = (
    ("start", "ᴛᴏ ɪɴɪᴛɪᴀʟɪᴢᴇ ᴛʜᴇ ʙᴏᴛ ✨"),
    ("settings", "ᴛᴏ ᴄᴏɴғɪɢᴜʀᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʙᴏᴛ sᴇᴛᴛɪɴɢs"),
    ("help", "ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ"),
    ("about", "ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ"),
)

DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://tewem57544:LkAPl5h9kpy4sYUS@cluster0.2g2emyt.mongodb.net/?retryWrites=true&w=majority")
HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))
