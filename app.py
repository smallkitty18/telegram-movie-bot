from flask import Flask, request
import telegram

TOKEN = "YOUR_BOT_TOKEN"
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route(f"/{TOKEN}", methods=["POST"])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text.startswith("/movie"):
        movie_name = text.replace("/movie", "").strip()
        if movie_name:
            reply = f"Here’s a download link for *{movie_name}*:\nhttps://example.com/download/{movie_name.replace(' ', '_')}"
        else:
            reply = "Please provide a movie name like `/movie Titanic`"
        bot.sendMessage(chat_id=chat_id, text=reply, parse_mode="Markdown")

    return "ok"
