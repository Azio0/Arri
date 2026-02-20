# Arri - Discord Translate Bot

Right-click any message → Apps → **Translate** to translate it via your self-hosted LibreTranslate instance. Works in servers and DMs.

## Project Structure

```
translate_bot/
├── main.py               # Entry point
├── requirements.txt
└── bot/
    ├── __init__.py
    ├── client.py         # Bot setup & wiring
    ├── commands.py       # "Translate" context menu command
    ├── config.py         # Centralised settings (env vars)
    ├── embeds.py         # Discord embed builders
    └── translator.py     # LibreTranslate API calls
```

## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create a Discord App**
   - Go to https://discord.com/developers/applications
   - Create a new application → Bot → copy the token
   - Under **Installation** → enable **User Install** (required for DM support)
   - Under OAuth2 → URL Generator: scopes = `bot` + `applications.commands`
   - Bot permissions: `Send Messages`, `Read Messages`
   - Invite the bot to your server using the generated URL

3. **Configure environment variables**

   | Variable | Default | Description |
   |---|---|---|
   | `DISCORD_TOKEN` | *(required)* | Your bot token |
   | `LIBRETRANSLATE_LANG` | `en` | Language to translate into |
   | `LIBRETRANSLATE_URL` | *(blank)* | Your LibreTranslate instance |
   | `LIBRETRANSLATE_API_KEY` | *(blank)* | API key if your instance requires one |

4. **Run**
   ```bash
   DISCORD_TOKEN=your_token_here python main.py
   ```

## Usage

- **In a server:** Right-click any message → **Apps** → **Translate**
- **In a DM:** Right-click any message → **Apps** → **Translate**

Translations are ephemeral — only you can see them.