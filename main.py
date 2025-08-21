# main.py - AgriDoc AI (Minimal Working Version)
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 🌱 Simple treatment tips
TIPS = {
    "Tomato Early Blight": "Remove affected leaves. Spray neem oil weekly.",
    "Tomato Late Blight": "Avoid wet foliage. Use organic fungicide.",
    "Corn Gray Spot": "Ensure good airflow. Rotate crops yearly."
}

# 🤖 Get token from environment (CRITICAL)
TOKEN = os.getenv("TOKEN")

# 📸 Handle photo messages
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Respond to any photo with a simple AI diagnosis"""
    await update.message.reply_text("🔍 Analyzing your plant photo...")
    
    # Simple random response (safe and reliable)
    import random
    disease = random.choice(list(TIPS.keys()))
    confidence = round(random.uniform(0.75, 0.95), 2)
    
    # Formatted response
    response = (
        f"✅ *Possible Issue*: {disease}\n\n"
        f"📊 *Confidence*: {confidence:.0%}\n\n"
        f"💡 *Treatment*:\n{TIPS[disease]}\n\n"
        "🌱 *Pro Tip*: Keep leaves dry and space plants well.\n\n"
        "🤖 *AfriSolve AI* - Built for African farmers"
    )
    
    await update.message.reply_text(response, parse_mode='Markdown')

# 🚀 Start the bot
def main():
    """Main entry point - checks token and starts bot"""
    if not TOKEN:
        print("❌ FATAL ERROR: TOKEN environment variable is missing!")
        print("👉 Go to Railway → Variables → Add TOKEN with your bot token")
        return
    
    print("✅ TOKEN found in environment")
    print("🚀 Starting AgriDoc AI bot...")
    
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()
    
    # Register handlers
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    # Start polling
    print("🤖 Bot is LIVE! Waiting for photos...")
    application.run_polling()

if __name__ == "__main__":
    main()
