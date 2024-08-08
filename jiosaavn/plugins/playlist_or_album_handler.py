import html
import logging
import traceback

from api.jiosaavn import Jiosaavn
from jiosaavn.bot import Bot

from humanfriendly import format_timespan
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

@Client.on_callback_query(filters.regex(r"^(playlist|album)#"))
async def playlist_or_album(client: Bot, callback: CallbackQuery):
    await callback.answer()
    
    data = callback.data.split("#")
    item_id = data[1]
    page_no = int(data[2]) if len(data) > 2 and data[2].isdigit() else 1
    back_type = data[2] if len(data) > 2 and not data[2].isdigit() else None
    search_type = "album" if data[0] == "album" else "playlist"
    album_id = item_id if search_type == "album" else None
    playlist_id = item_id if search_type == "playlist" else None
    
    try:
        response = await Jiosaavn().get_playlist_or_album(album_id=album_id, playlist_id=playlist_id, page_no=page_no)
        if not response or not response.get("list"):
            return await callback.message.edit(f"**ᴛʜᴇ ʀᴇϙᴜᴇsᴛᴇᴅ {search_type} ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ғᴏᴜɴᴅ.**")
    except RuntimeError as e:
        logger.error(e)
        traceback.print_exc()
        return await callback.message.edit("ᴄᴏɴɴᴇᴄᴛɪᴏɴ ʀᴇғᴜsᴇᴅ ʙʏ ᴀᴘɪ. ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ, ᴏʀ sᴇᴀʀᴄʜ ᴀɴᴏᴛʜᴇʀ")

    title = html.unescape(response.get("title", ""))
    total_results = int(response.get("list_count", 0))
    image_url = response.get("image", "").replace("150x150", "500x500")
    perma_url = response.get("perma_url", "")
    more_info = response.get("more_info", {})
    followers = int(more_info.get("follower_count", 0))
    duration = int(more_info.get("duration", 0))
    release_year = response.get("year", "")
    songs = response.get("list", [])
    
    buttons = []
    for song in songs:
        try:
            song_title = html.unescape(song.get("title", ""))
            song_id = song.get("perma_url", "").rsplit("/", 1)[1]
            if song_id:
                callback_data = f"song#{song_id}#{item_id}#{search_type}"
                if back_type:
                    callback_data += f"#{back_type}"
                buttons.append([InlineKeyboardButton(f"🎙 {song_title}", callback_data=callback_data)])
        except IndexError:
            pass

    navigation_buttons = []
    if page_no > 1:
        navigation_buttons.append(InlineKeyboardButton("⇇", callback_data=f"{search_type}#{item_id}#{page_no-1}"))
    if total_results > 10 * page_no:
        navigation_buttons.append(InlineKeyboardButton("⇉", callback_data=f"{search_type}#{item_id}#{page_no+1}"))
    if navigation_buttons:
        buttons.append(navigation_buttons)

    buttons.append([InlineKeyboardButton('ᴜᴘʟᴏᴀᴅ ᴀʟʙᴜᴍ 📤', callback_data=f'upload#{item_id}#{search_type}')])
    buttons.append([InlineKeyboardButton('ᴄʟᴏsᴇ ❌', callback_data="close")])
    back_callback_data = f"search#{back_type}" if back_type else f"search#{search_type}s"
    buttons.append([InlineKeyboardButton("⇋ ʙᴀᴄᴋ ⇋", callback_data=back_callback_data)])

    search_type_text = "💾 ᴘʟᴀʏʟɪsᴛ" if playlist_id else "📚 ᴀʟʙᴜᴍ"
    text_data = (
        f"[\u2063]({image_url})"
        f"**{search_type_text}:** [{title}]({perma_url})",
        f"**📜 ᴘᴀɢᴇ ɴᴏ:** {page_no}",
        f"**🕰 ᴅᴜʀᴀᴛɪᴏɴ:** {format_timespan(duration)}" if duration else "",
        f"**🔊 ᴛᴏᴛᴀʟ sᴏɴɢs:** {total_results}" if total_results else "",
        f"**👥 ғᴏʟʟᴏᴡᴇʀs:** {followers:,}" if followers else "",
        f"**📆 ʀᴇʟᴇᴀsᴇ ʏᴇᴀʀ:** __{release_year}__" if release_year else ''
    )
    text = "\n\n".join(filter(None, text_data))

    await callback.message.edit(text, reply_markup=InlineKeyboardMarkup(buttons))
