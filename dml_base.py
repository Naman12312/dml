import discord
from discord.ext import commands
import threading
from playsound import playsound
intents = discord.Intents.default()
intents.typing = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
def play_noti_sound():
    playsound("/path/to/notification/sound/")
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.author.name == "your-username-on-discord": # replace your-username-on-discord with your discord username
        return
    print(f"message from {message.author.name}:\n{message.content}")
    with open("message_history.txt", "a") as f:
        f.write(f"message from {message.author.name}:\n{message.content}\n")
    
    t = threading.Thread(target=play_noti_sound)
    t.start()
    await bot.process_commands(message)

# Replace 'your-bot-token' with your actual bot token.
bot.run('your-bot-token')