import os
import discord
from bot.client import create_client

if __name__ == "__main__":
    token = os.environ.get("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN environment variable is not set.")

    client = create_client()
    client.run(token)