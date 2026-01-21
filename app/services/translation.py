from functools import lru_cache
from deep_translator import GoogleTranslator
from ..core.interfaces import ITranslationService

class GoogleTranslationService(ITranslationService):
    @lru_cache(maxsize=500)
    def translate(self, text: str, source: str = 'en', target: str = 'pt') -> str:
        try:
            return GoogleTranslator(source=source, target=target).translate(text)
        except Exception as e:
            print(f"Erro tradução: {e}")
            return text