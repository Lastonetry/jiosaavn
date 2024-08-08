import logging
import random
from jiosaavn.bot import Bot

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

PICS = [
    "https://telegra.ph/file/d29775a7d90ef0df078eb.jpg",
    "https://telegra.ph/file/e84daa9262350a1aceaf1.jpg",
    "https://telegra.ph/file/caa42944be7f3642ea361.jpg",
    "https://telegra.ph/file/497274e0cc115b572443b.jpg",
    "https://telegra.ph/file/94d1384fcd6a3e9c1ce99.jpg",
    "https://telegra.ph/file/1d5aa8a00ff0f90eecff8.jpg",
    "https://telegra.ph/file/adb9fb93ad14f83a05527.jpg"
]

@Client.on_callback_query(filters.regex('^home$'))
@Client.on_message(filters.command('start') & filters.private & filters.incoming)
async def start_handler(client: Client, message: Message|CallbackQuery):
    text = (
        f"*ʜᴇʏᴀ! {message.from_user.mention} ✨\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"
        "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ  Bot! "
        "ᴛʜɪs ɪs ᴀ ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ, ᴀɴᴅ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇᴀʀᴄʜ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ғᴏʀ sᴏɴɢs, ᴘʟᴀʏʟɪsᴛs, ᴀʟʙᴜᴍs ᴀɴᴅ ᴀʀᴛɪsᴛs ᴅɪʀᴇᴄᴛʟʏ ғʀᴏᴍ sᴘᴏᴛɪғʏ\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"
        "ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ:\n"
        "- sᴇᴀʀᴄʜ ғᴏʀ sᴏɴɢs, ᴘʟᴀʏʟɪsᴛs, ᴀʟʙᴜᴍs ᴀɴᴅ ᴀʀᴛɪsᴛs\n"
        "- ᴅᴏᴡɴʟᴏᴀᴅ ʏᴏᴜʀ ғᴀᴠᴏᴜʀɪᴛᴇ ᴛʀᴀᴄᴋs ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ\n"
        "- ᴇxᴘʟᴏʀᴇ ᴠᴀʀɪᴏᴜs ғᴇᴀᴛᴜʀᴇs ᴛᴀɪʟᴏʀᴇᴅ ᴛᴏ ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n"
        "🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ:* [ᴍᴏɢɢᴇʀ](https://t.me/MoggerKing)"
    )

    buttons = [[
        InlineKeyboardButton('♡ ᴘʟᴀʏʟɪsᴛ', url='https://t.me/W_Collections'),
        InlineKeyboardButton('sᴇᴛᴛɪɴɢs ⚙', callback_data='settings')
        ],[
        InlineKeyboardButton('♻️ ʜᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('💠 ᴀʙᴏᴜᴛ', callback_data='about')
        ],[
        InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ 🧑‍💻', url='https://t.me/MoggerKing')
    ]]

    # Choose a random image from the list
    random_image = random.choice(PICS)
    if isinstance(message, Message):
        await message.reply_photo(random_image, caption=text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await message.message.edit_text(text, reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex('^help$'))
@Bot.on_message(filters.command('help') & filters.private & filters.incoming)
async def help_handler(client: Bot, message: Message | CallbackQuery):
    text = (
        "**ɪᴛ's ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ! 😉**\n\n"
        "1. sᴛᴀʀᴛ ʙʏ ᴄᴏɴғɪɢᴜʀɪɴɢ ʏᴏᴜʀ ᴘʀᴇғᴇʀᴇɴᴄᴇs ᴜsɪɴɢ ᴛʜᴇ `/settings` ᴄᴏᴍᴍᴀɴᴅ.\n"
        "2. sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴀ sᴏɴɢ, ᴘʟᴀʏʟɪsᴛ, ᴀʟʙᴜᴍ, ᴏʀ ᴀʀᴛɪsᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ.\n"
        "3. ɪ'ʟʟ ʜᴀɴᴅʟᴇ ᴛʜᴇ ʀᴇsᴛ ᴀɴᴅ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴛʜᴇ ʀᴇsᴜʟᴛs!\n\n"
        "ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴛʜᴇ ʙᴇᴀᴜᴛʏ ᴏғ ᴍᴜsɪᴄ ♡"
    )

    buttons = [[
        InlineKeyboardButton('💠 ᴀʙᴏᴜᴛ', callback_data='about'),
        InlineKeyboardButton('sᴇᴛᴛɪɴɢs ⚙', callback_data='settings')
        ],[
        InlineKeyboardButton('ʜᴏᴍᴇ ↺', callback_data='home'),
        InlineKeyboardButton('ᴄʟᴏsᴇ ❌', callback_data='close')
    ]]

    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons))

@Bot.on_callback_query(filters.regex('^about$'))
@Bot.on_message(filters.command('about') & filters.private & filters.incoming)
async def about(client: Bot, message: Message|CallbackQuery):
    me = await client.get_me()

    text = (
        f"**🤖 ᴍʏ ɴᴀᴍᴇ:** {me.mention()}\n\n"
        "**📝 ʟᴀɴɢᴜᴀɢᴇ:** [Python 3](https://www.python.org/)\n\n"
        "**🧰 ғʀᴀᴍᴇᴡᴏʀᴋ:** [Pyrogram](https://github.com/pyrogram/pyrogram)\n\n"
        "**🧑‍💻 ᴅᴇᴠ:** [Anonymous](https://t.me/Ns_AnoNymouS)\n\n"
        "**📢 ᴜᴘᴅᴀᴛᴇs:** [ʜᴇʟᴘᴇʀ ʜᴀɴᴅ](https://t.me/aHelperHand)\n\n"
        "**👥 sᴜᴘᴘᴏʀᴛ:** [ᴛᴇsᴛ sɪᴛᴇ](https://t.me/ProjectsSite)\n\n"
        "**🔗 sʀᴄ ᴄᴏᴅᴇ:** [ᴘʀɪᴠᴀᴛᴇ](https://t.me/BillionarieCult)\n\n"
    )

    buttons = [[
        InlineKeyboardButton('ʜᴇʟᴘ ♻️', callback_data='help'),
        InlineKeyboardButton('sᴇᴛᴛɪɴɢs ⚙', callback_data='settings')
        ],[
        InlineKeyboardButton('ʜᴏᴍᴇ ↻', callback_data='home'),
        InlineKeyboardButton('ᴄʟᴏsᴇ ❌', callback_data='close')
    ]]
    if isinstance(message, Message):
        await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True, quote=True)
    else:
        await message.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

@Bot.on_callback_query(filters.regex('^close$'))
async def close_cb(client: Bot, callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
