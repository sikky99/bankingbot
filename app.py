from flask import Flask, render_template, request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.MongoDatabaseAdapter")




english_bot.set_trainer(ListTrainer)


for _file in os.listdir('files'):
	chats = open('files/' + _file, 'r').readlines()

	english_bot.train(chats)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
