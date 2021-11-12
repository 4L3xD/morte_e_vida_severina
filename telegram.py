import telepot, json, time
from telepot.loop import MessageLoop
from severina import Severina

with open('token.json') as jsonFile:
    token = json.load(jsonFile)
telegram = telepot.Bot(token)
bot = Severina("memories")

def receiveMsg(msg):
    phrase = bot.listen(phrase=msg['text'])
    response = bot.think(phrase)
    bot.speak(response)
    msgType, chatType, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, response)

MessageLoop(telegram, receiveMsg).run_as_thread()
print ('Listening ...')

while 1:
    time.sleep(10)