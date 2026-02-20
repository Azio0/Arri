import discord
from bot.config import LIBRETRANSLATE_LANGG

def build_translation_embed(
    original_text: str,
    translated_text: str,
    detected_lang: str,
    author_name: str,
) -> discord.Embed:
    embed = discord.Embed(
        title="Translation",
        color=discord.Color.blurple(),
    )
    embed.add_field(
        name=f"Original (`{detected_lang}`)",
        value=original_text[:1024],
        inline=False,
    )
    embed.add_field(
        name=f"Translated (`{LIBRETRANSLATE_LANGG}`)",
        value=translated_text[:1024],
        inline=False,
    )
    embed.set_footer(text=f"Powered by LibreTranslate • {author_name}")
    return embed

def build_error_embed(message: str) -> discord.Embed:
    return discord.Embed(
        title="Translation Failed",
        description=message,
        color=discord.Color.red(),
    )