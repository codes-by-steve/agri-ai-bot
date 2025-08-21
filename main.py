# main.py - AgriDoc AI
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import random

# 🌱 Treatment tips
TIPS = {
    "Tomato Early Blight": "Remove affected leaves. Spray neem oil weekly.",
    "Tomato Late Blight": "Avoid wet foliage. Use organic fungicide.",
    # ... rest of TIPS
}

DISEASES = list(TIPS.keys())

# 🤖 Get token from environment (Railway)
TOKEN = os.getenv("8280884253:AAFrVozGE6quXBk8ekESye368VY3yGUabBA")

# 📸 Handle photo
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 Scanning your plant... 🌿")
    # ... rest of code
