import discord
import requests
from discord import app_commands
from bs4 import BeautifulSoup
import re

#intents = discord.Intents.default()
#intents.message_content = True

intents = discord.Intents.all()
client = discord.Client(intents=intents)

tree = app_commands.CommandTree(client)
y = 1000


@client.event

async def on_ready(): #turn on the bot
    print('can loggin')
    channel = client.get_channel("channel ID")
    await channel.send('おはようございます　何かあったら聞いてみてね　気分がよかったら答えるかも？？')
    await tree.sync()  # slash command turn on


@client.event
async def on_message(message):
    if message.author.bot: #bot message dont contact
        return
    elif message.content == message.content: #recieve message in other people
        string  = message.content 
        a = 0
        string = re.sub(" ", "", string) #delete space
        print(string)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        
        url = f"https://www.bing.com/search?q={string}&form=ANSPH1&refig=482630ec047b486f976cb73127228c7e&pc=U531&sp=6&lq=0&qs=HS&sk=HS5&sc=10-0&cvid=482630ec047b486f976cb73127228c7e"#bing url
        res = requests.get(url, timeout=10, headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        topstories = soup.find('div', id='b_content')

        letter = len(topstories.get_text())
        print(letter)

        if letter >= 1000:
            dd = letter / 1000
        while a <= dd:
            s = topstories.get_text()[y*a:y*(a+1)]
            a = a+1
            await message.channel.send(f"{message.author.mention}さん{s}")
        if a == dd:
            a = 0

        elif letter < 1000:
            d = topstories.get_text()
            await message.channel.send(f"{message.author.mention}さん{d}")

        # await message.channel.send(f"こんにちは！{message.author.mention}さん！")
    elif message.content == 'hello':
        await message.channel.send(f"{message.author.mention}さん! hello world")
    if message.content == '1':
        await message.channel.send("一時停止させていただきます")

@tree.command(name="hello", description="テストコマンドです。")
async def test_command(interaction: discord.Interaction):
    # ephemeral=True→「これらはあなただけに表示されています
    await interaction.response.send_message("hello", ephemeral=True)


T0ken = "your token"
client.run(T0ken)
