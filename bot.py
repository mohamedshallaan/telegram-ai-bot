import os
from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "أنت مساعد ذكي يتحدث العربية."},
            {"role": "user", "content": user_text}
        ]
    )

    await update.message.reply_text(
        response.choices[0].message.content
    )

app = ApplicationBuilder().token(
    os.getenv("TELEGRAM_TOKEN")
).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
)

if __name__ == "__main__":
    app.run_polling()
