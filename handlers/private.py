from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

@Client.on_message(filters.command("noinoi") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗡𝗼𝗶𝗻𝗼𝗶 𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n🌠𝗘𝗻𝗷𝗼𝘆 𝗠𝘂𝘀𝗶𝗰<3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝗢𝘄𝗻𝗲𝗿", url="https://t.me/BazigarYT")
                ]
            ]
        )
   )
