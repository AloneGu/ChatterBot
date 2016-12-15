from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

PORT = 8004

app = Flask(__name__)

#english_bot = ChatBot("English Bot")
#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")
cn_bot = ChatBot("Chinese Bot")
cn_bot.set_trainer(ChatterBotCorpusTrainer)
cn_bot.train("chatterbot.corpus.chinese")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(cn_bot.get_response(query))


if __name__ == "__main__":
    app.run(port=PORT, host='0.0.0.0')
