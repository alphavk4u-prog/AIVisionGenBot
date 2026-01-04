import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.getenv("8381392044:AAHXY2eSJtoSl7RHI3SFp-EqIPfPBUtV1yw")
HF_API_KEY = os.getenv("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")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.content

async def start(update: Update, context):
    await update.message.reply_text(
        "🎨 AIVisionGen Bot Ready!\n\n"
        "Hindi ya English me prompt bhejo:\n"
        "A fantasy castle\n"
        "Ek sundar pahadi gaon\n\n"
        "⚠️ NSFW allowed nahi."
    )

async def generate_image(update: Update, context):
    prompt = update.message.text
    try:
        image_bytes = query({"inputs": prompt})
        await update.message.reply_photo(image_bytes)
    except:
        await update.message.reply_text("❌ Image generate nahi ho payi.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))
app.run_polling()
