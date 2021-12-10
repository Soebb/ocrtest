import os, time
import glob
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message



default_cut = "00:00:00 02:00:04"


if 'BOT_TOKEN' in os.environ:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
else:
    BOT_TOKEN = "2097075744:AAEoJkufairh1wNseDI-N_eXqvxcnZSfw"
    API_ID = "4328988"
    API_HASH = "3230ec801f78c9a2ad6bebb7f7b4"


Bot = Client(
    "Bot",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

refresh_button = [
    InlineKeyboardButton(
        text='Refresh List',
        callback_data='refresh'
    )
]
id = 0
mid = 0
D = 0
t = 0
@Bot.on_message(filters.text)
async def start(bot, m):
    global id
    global mid
    id = m.chat.id
    mid = m.message_id
    keyboard = []
    keyboard.append(refresh_button)
    try:
        for file in glob.glob('videos/splits/*'):
            keyboard.append(
                [
                    InlineKeyboardButton(
                        text=file.rsplit('/', 1)[1].replace('1aa\\', ''),
                        callback_data=file.rsplit('/', 1)[1].replace('1aa\\', '')
                    )
                ]
            )
    except Exception as e:
        print(e)
        return
    keyboard.append(refresh_button)
    print(str(mid))
    #await bot.send_message(chat_id=id, text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
    await m.reply_text(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))


@Bot.on_callback_query()
async def callback(bot, update):
    global id
    global mid
    global D
    global t
    '''
    if update.data == "refresh":
        keyboard = []
        keyboard.append(refresh_button)
        try:
            for file in glob.glob('C:/dlmacvin/1aa/*'):
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            text=file.rsplit('/', 1)[1].replace('1aa\\', ''),
                            callback_data=file.rsplit('/', 1)[1].replace('1aa\\', '')
                        )
                    ]
                )
        except Exception as e:
            print(e)
            return
        keyboard.append(refresh_button)
        update.message.edit(text="Which one?", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    '''
    try:
        for file in glob.glob('videos/splits/*'):
            if file.rsplit('/', 1)[1].replace('1aa\\', '') == update.data:
                
                #await time.delete()
                #time.sleep(5)
                #await update.answer("process!", show_alert=True)
                #time.sleep(3)
                #R = await update.message.reply_text('@Pgffhjsejahjj')

                # prs: Message = await bot.ask(id,'proccesing..',filters=filters.text)
                #time.sleep(5)
                if t == 0:
                    R = await update.message.reply_text(str(t))
                    D = R.message_id
                #.sleep(4)
                elif t != 0:
                    await bot.edit_message_text(id, D, "gg")
                t = update.message.from_user.id
                return
                time = await bot.ask(id,'Now send start & end time! OR keep /default',filters=filters.text)
                if time.text == "/default":
                    start, end = default_cut.split()
                else:
                    start, end = time.text.split()

                await update.message.reply(text="Prcessing..")
                time.sleep(5)
                await update.message.delete()
                #msgs = len(bot.iter_history(chat_id=id, limit=None))
                #time.sleep(5)
                #await bot.delete_messages(chat_id=id, message_ids=mid+4)
                return
                ext = '.' + file.rsplit('.', 1)[1]
                name = file.rsplit('/', 1)[1].replace('1aa\\', '')
                input = 'C:/dlmacvin/1aa/' + name
                process_msg = await update.message.reply(text="Processing..")
                os.system(f"ffmpeg -i {input} -ss {start} -to {end} -c copy videos/{name}")
                os.system(f"ffmpeg -i videos/{name} -c copy -segment_time 00:00:10 -f segment videos/splits/{name.replace(ext, '')}%03d{ext}")
                #await update.message.edit(text="Successfully done, check /videos and /videos/splits folders")
                await process_msg.delete()
    except:
        pass



Bot.run()
