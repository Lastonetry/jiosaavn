import logging
from jiosaavn.bot import Bot

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageNotModified

logger = logging.getLogger(__name__)

@Bot.on_message(filters.command("settings"))
@Bot.on_callback_query(filters.regex(r"^settings"))
async def settings(client: Bot, message: Message|CallbackQuery):
    if isinstance(message, Message):
        msg = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...", quote=True)
    else:
        msg = message.message
        await message.answer()
        data = message.data.split("#")
        if len(data) > 1:
            _, key, value = data
            await client.db.update_user(message.from_user.id, key, value)

    user = await client.db.get_user(message.from_user.id)
    type = user['type']
    quality = user['quality']

    all = 'ᴀʟʟ ✅' if type == 'all' else 'All'
    albums = 'ᴀʟʙᴜᴍ ✅' if type == 'albums' else 'Albums' 
    songs = 'sᴏɴɢs ✅' if type == 'songs' else 'Songs'
    playlists = 'ᴘʟᴀʏʟɪsᴛ ✅' if type == 'playlists' else 'Playlist'
    
    quality_320 = '320kbps ✅' if quality == '320kbps' else '320kbps'
    quality_160 = '160kbps ✅' if quality == '160kbps' else '160kbps'
    
    buttons = [
        [
            InlineKeyboardButton("⇊ sᴇᴀʀᴄʜ ᴛʏᴘᴇ ⇊", callback_data="dummy"),
        ],
        [
            InlineKeyboardButton(all, callback_data='settings#type#all'),
            InlineKeyboardButton(albums, callback_data='settings#type#albums'),
        ],
        [
            InlineKeyboardButton(songs, callback_data='settings#type#songs'),
            InlineKeyboardButton(playlists, callback_data='settings#type#playlists'),
        ],
        [
            InlineKeyboardButton("⇊ ᴀᴜᴅɪᴏ ϙᴜᴀʟɪᴛʏ ⇊", callback_data="dummy"),
        ],
        [
            InlineKeyboardButton(quality_320, callback_data='settings#quality#320kbps'),
            InlineKeyboardButton(quality_160, callback_data='settings#quality#160kbps')
        ],
        [
            InlineKeyboardButton("↻ ʜᴏᴍᴇ", callback_data='home')
        ]
    ]

    text = '**sᴇʟᴇᴄᴛ ᴛʜᴇ sᴇᴀʀᴄʜ ᴛʏᴘᴇ ᴀɴᴅ ᴍᴜsɪᴄ ϙᴜᴀʟɪᴛʏ ʏᴏᴜ ᴡᴀɴᴛ 🧏‍♂️**'
    try:
        await msg.edit(text, reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified:
        pass

@Bot.on_callback_query(filters.regex(r"^dummy$"))
async def dummy(client: Bot, callback: CallbackQuery):
    await callback.answer("sᴇʟᴇᴄᴛ ғʀᴏᴍ ʙᴇʟᴏᴡ ᴅᴜᴍʙᴀss 🚸", show_alert=True)
