import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import openai

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

async def start(update: Update, context):
    await update.message.reply_text(
        "🤖 AIVisionGen Bot Ready!\n\n"
        "Hindi ya English me likho:\n"
        "A fantasy castle\n"
        "Ek sundar pahadi gaon\n\n"
        "⚠️ Sirf safe prompts allowed."
    )

async def generate_image(update: Update, context):
    prompt = update.message.text
    try:
        result = openai.images.generate(
            model="gpt-image-1",
            prompt=prompt,
            size="1024x1024"
        )
        await update.message.reply_photo(result.data[0].url)
    except:
        await update.message.reply_text(
            "❌ Error ya unsafe prompt.\nSafe prompt use karein."
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))

app.run_polling()
