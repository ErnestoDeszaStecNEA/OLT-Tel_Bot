import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

token = '7519467549:AAHtb3vH1iq-05GJdDcweh07HhixgWwfm6Y'
OLT_Techs = [1222786527]




logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="This is the of OpenLabTech bot"
    )

    #Security
    user_id = update.effective_user.id
    if user_id not in OLT_Techs:
        await update.message.reply_text(f"Your ID={user_id} isn't on with list.")
        return ConversationHandler.END

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text[6:])


if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    echo_handler = CommandHandler('echo', echo)
    application.add_handler(echo_handler)
    
    application.run_polling()
