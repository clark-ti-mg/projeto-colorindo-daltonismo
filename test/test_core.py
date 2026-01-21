# test/test_core.py
import pytest
from app.data.repository import ColorRepository
from app.services.translation import GoogleTranslationService
from app.core.math_utils import PerceptualColorMath # Importe o serviço aqui

def test_busca_fuzzy_rigorosa_95_percent_RD05():
    """
    Valida o novo requisito de similaridade de 95% (RD05).
    Evidência de Injeção de Dependência (SOLID - DIP).
    """
    # Passo 1: Instanciar a dependência
    math_service = PerceptualColorMath()
    
    # Passo 2: Injetar a dependência no repositório
    repo = ColorRepository(csv_path="color_names.csv", math_service=math_service)
    
    # Caso 1: Nome idêntico (deve passar)
    result_exact, sim_exact = repo.find_by_name_fuzzy("Red")
    
    assert result_exact is not None
    assert sim_exact >= 0.95

def test_calculo_distancia_hsl_RF06():
    math_service = PerceptualColorMath()
    
    # Cores idênticas devem ter distância zero
    cor_a = (120, 50, 50) # Verde
    assert math_service.calculate_distance(cor_a, cor_a) == 0
    
    # Verde (120) deve ser mais perto de Ciano (180) do que de Vermelho (0)
    dist_verde_ciano = math_service.calculate_distance((120, 100, 50), (180, 100, 50))
    dist_verde_vermelho = math_service.calculate_distance((120, 100, 50), (0, 100, 50))
    assert dist_verde_ciano < dist_verde_vermelho

def test_traducao_e_cache_RD03():
    service = GoogleTranslationService()
    
    # Teste de tradução simples
    resultado = service.translate("Red", target="pt")
    assert resultado.lower() == "vermelho"
    
    # O segundo chamado deve vir do cache (comportamento interno do Python)
    resultado_cache = service.translate("Red", target="pt")
    assert resultado_cache == resultado