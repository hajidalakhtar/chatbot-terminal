from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('hajid')
trainer = ChatterBotCorpusTrainer(chatbot)

# trainer = ListTrainer(chatbot)
# trainer.train(
#     "./my_export.json",

# )
trainer.train(
    "chatterbot.corpus.indonesia.greetings",
    "chatterbot.corpus.indonesia.conversations"
)
trainer.export_for_training('./my_export.json')

while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break