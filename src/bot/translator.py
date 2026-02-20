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

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(f"{LIBRETRANSLATE_URL}/translate", json=payload) as resp:
                if resp.status != 200:
                    error = await resp.text()
                    raise TranslationError(f"LibreTranslate returned {resp.status}: {error}")

                data = await resp.json()

                return {
                    "translatedText": data.get("translatedText", ""),
                    "detectedLanguage": data.get("detectedLanguage", {}).get("language", "unknown"),
                }

        except aiohttp.ClientError as e:
            raise TranslationError(f"Could not reach LibreTranslate: {e}")
