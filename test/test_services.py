from unittest.mock import patch
from app.services.translation import GoogleTranslationService

@patch("deep_translator.GoogleTranslator.translate")
def test_translation_error_fallback(mock_translate):
    # Força a API de tradução a lançar um erro
    mock_translate.side_effect = Exception("Erro de conexão")
    
    service = GoogleTranslationService()
    result = service.translate("Red")
    
    # Verifica se ele retornou o nome original em vez de quebrar
    assert result == "Red"