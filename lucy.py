#Discord Library
import discord as dc

#Configurations
from dotenv import load_dotenv
import os

#Responses
from responses import get_response

#Others
import datetime

#--------------------------------------------------------------

#Loading .env
load_dotenv()
#Getting BOT Token
TOKEN: str = os.getenv('TOKEN')
LOGIN_CHANNEL: int = int(os.getenv('LOGIN_CHANNEL'))

#--------------------------------------------------------------

#BOT Setup
intents: dc.Intents = dc.Intents.default()
intents.message_content = True
lucy: dc.Client = dc.Client(intents=intents)

#--------------------------------------------------------------

#Message response
async def send_message(message: dc.Message, user_message: str) -> None:
    if not user_message:
        print('[Message was empty because intents were not enable probably]')
        return

    #Detect if user need a dm response
    if is_private := user_message[-2:] == '-p':
        user_message = user_message[-2:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)

#--------------------------------------------------------------

#Events

#Detect when bot is on
@lucy.event
async def on_ready() -> None:
    #Getting date
    date: datetime.datetime = datetime.datetime.now()

    #Logging login in chat
    channel = lucy.get_channel(LOGIN_CHANNEL)
    if channel:
        await channel.send(f'{lucy.user.name} is now runnig: {date}')
    else:
        print('Channel don\'t exist')

    #Logging login
    print(f'{lucy.user.name} is now runnig: {date}')

#Message logging
@lucy.event
async def on_message(message: dc.Message) -> None:
    #Detect if a user sent message
    if message.author == lucy.user:
        return
    
    #Getting message data
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    #Logging message
    print(f'[{channel}] - {username}: "{user_message}"')

    #Giving response
    await send_message(message, user_message)

#--------------------------------------------------------------

#Runnig Bot
def main():
    lucy.run(token=TOKEN)

if __name__ == '__main__':
    main()