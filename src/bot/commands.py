import discord
from discord import app_commands
from discord.ext import commands

from bot.translator import translate, TranslationError
from bot.embeds import build_translation_embed, build_error_embed

class TranslateCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.translate_ctx_menu = app_commands.ContextMenu(
            name="Translate",
            callback=self.translate_message,
        )
        self.translate_ctx_menu.allowed_contexts = app_commands.AppCommandContext(
            guild=True,
            dm_channel=True,
            private_channel=True,
        )
        self.translate_ctx_menu.allowed_installs = app_commands.AppInstallationType(
            guild=True,
            user=True,
        )
        self.bot.tree.add_command(self.translate_ctx_menu)

    async def cog_unload(self):
        self.bot.tree.remove_command(self.translate_ctx_menu.name, type=self.translate_ctx_menu.type)

    async def translate_message(self, interaction: discord.Interaction, message: discord.Message):
        await interaction.response.defer(ephemeral=True, thinking=True)

        text = message.content
        if not text:
            await interaction.followup.send(
                embed=build_error_embed("That message has no text to translate."),
                ephemeral=True,
            )
            return

        try:
            result = await translate(text)
        except TranslationError as e:
            await interaction.followup.send(
                embed=build_error_embed(str(e)),
                ephemeral=True,
            )
            return

        embed = build_translation_embed(
            original_text=text,
            translated_text=result["translatedText"],
            detected_lang=result["detectedLanguage"],
            author_name=message.author.display_name,
        )
        await interaction.followup.send(embed=embed, ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(TranslateCommands(bot))
