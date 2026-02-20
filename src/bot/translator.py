import aiohttp
from bot.config import LIBRETRANSLATE_URL, LIBRETRANSLATE_API_KEY, LIBRETRANSLATE_LANG

class TranslationError(Exception):
    pass

async def translate(text: str, target: str = LIBRETRANSLATE_LANG, source: str = "auto") -> dict:
    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text",
    }

    if LIBRETRANSLATE_API_KEY:
        payload["api_key"] = LIBRETRANSLATE_API_KEY

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.post(f"{LIBRETRANSLATE_URL}/translate", json=payload) as resp:
                if resp.status != 200:
                    raise TranslationError(f"LibreTranslate returned HTTP {resp.status}. If this persists, your instance may be behind a bot challenge — check server logs.")

                data = await resp.json()

                return {
                    "translatedText": data.get("translatedText", ""),
                    "detectedLanguage": data.get("detectedLanguage", {}).get("language", "unknown"),
                }

        except aiohttp.ClientError as e:
            raise TranslationError(f"Could not reach LibreTranslate: {e}")