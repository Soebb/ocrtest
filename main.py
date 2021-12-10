import os
from pyrogram import Client, filters
from agentocr import OCRSystem

if 'BOT_TOKEN' in os.environ:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
else:
    BOT_TOKEN = "2097075744:AAEoJkufai1wNseDI-N_eXqvxcnZSfw"
    API_ID = "432888"
    API_HASH = "3230ec801f78c9a2ad6beb7f7b4"


Bot = Client(
    "Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

ocr = OCRSystem(config='fa')

@Bot.on_message(filters.photo)
async def OCR(_, m):
    await m.download('out.jpg')
    results = ocr.ocr('out.jpg')
    text = ""
    for result in results:
        text += result + " | "
    await m.reply(text)
    

Bot.run()
