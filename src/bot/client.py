import discord
from discord.ext import commands

def create_client() -> commands.Bot:
    intents = discord.Intents.default()

    bot = commands.Bot(
        command_prefix="!",  # Unused but required by commands.Bot
        intents=intents,
        help_command=None,
    )

    @bot.event
    async def on_ready():
        await bot.load_extension("bot.commands")
        await bot.tree.sync()
        print(f"Logged in as {bot.user} — context menu command synced.")

    return bot
