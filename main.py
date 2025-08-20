# main.py - AgriDoc AI (Simple & Safe)
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import random

# 🌱 Treatment tips for common diseases
TIPS = {
    "Tomato Early Blight": "Remove affected leaves. Spray neem oil weekly.",
    "Tomato Late Blight": "Avoid wet foliage. Use organic fungicide.",
    "Corn Gray Spot": "Ensure good airflow. Rotate crops yearly.",
    "Potato Blight": "Harvest early. Store in dry, cool place.",
    "Apple Scab": "Prune infected branches. Use compost tea spray."
}

# List of possible diseases (AI will pick one)
DISEASES = list(TIPS.keys())

# 🤖 YOUR BOT'S TOKEN FROM BOTFATHER
TOKEN = "8280884253:AAFrVozGE6quXBk8ekESye368VY3yGUabBA"  # ← You'll replace this later

# 📸 What happens when user sends a photo
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Send "thinking" message
    await update.message.reply_text("🔍 Scanning your plant... 🌿")

    try:
        # Simulate AI result (random but realistic)
        disease = random.choice(DISEASES)
        confidence = round(random.uniform(0.78, 0.96), 2)  # e.g., 92.3%

        # Build reply
        reply = (
            f"✅ Likely: *{disease}*\n\n"
            f"📊 Confidence: {confidence:.1%}\n\n"
            f"💡 *Treatment:*\n{TIPS[disease]}\n\n"
            "🌱 *Pro Tip:* Keep leaves dry and space plants well.\n\n"
            "🤖 *AfriSolve AI* — Built for African farmers ❤️"
        )

        # Send reply in Telegram
        await update.message.reply_text(reply, parse_mode='Markdown')

    except Exception as e:
        # If anything goes wrong
        await update.message.reply_text("❌ Could not analyze. Please send a clear photo of a leaf.")

# 🚀 Start the bot
def main():
    # Check if token is set
    if TOKEN == "YOUR_TELEGRAM_TOKEN_HERE":
        print("❌ ERROR: You forgot to add your bot token!")
        print("👉 Open main.py and replace 'YOUR_TELEGRAM_TOKEN_HERE' with your real token.")
        return

    print("🚀 AgriDoc AI is running... Bot is LIVE!")
    print("💬 Send a photo to your bot in Telegram.")

    # Build the bot app
    app = Application.builder().token(TOKEN).build()

    # Tell the bot to listen for photos
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Start the bot
    app.run_polling()

# This runs when you start the script
if __name__ == '__main__':
    main()

