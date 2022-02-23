import discord
from discord.ext import commands
#pip install requests
import requests

bot = commands.Bot(command_prefix = "m!")

@bot.event
async def on_ready():
	print("準備完了")
    
@bot.command()
async def trans(ctx, *, msg):
    trans_now = await ctx.send("日本語から英語に翻訳中です...")
    api_key = "7238d01a-a7e1-750b-031c-26d3f5817920:fx"
    params = {
                "auth_key": api_key,
                "text": str(msg),
                "source_lang": "JA",
                "target_lang": "EN"
            }

    request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    result = request.json()
    await trans_now.edit(content="JA → EN\n" + result["translations"][0]["text"])

bot.run(OTQ1OTU2ODU2NjEyOTI1NDcx.YhXs-Q.Ibt03FT3w4JvfENQrBxQIaxlFLY)
