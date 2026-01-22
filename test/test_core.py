import pytest
import pandas as pd
import math
from unittest.mock import MagicMock

# Importações do projeto
from app.services.color_manager import ColorManager
from app.data.repository import ColorRepository
from app.services.translation import GoogleTranslationService
from app.core.math_utils import PerceptualColorMath

# --- FIXTURES (Arrange) ---

@pytest.fixture
def mock_color_df():
    """Cria um DataFrame em memória para isolar os testes do arquivo CSV real."""
    data = {
        'Name': ['Red', 'Deep Red', 'Blue', 'Amazonite'],
        'Hex (24 bit)': ['#FF0000', '#8B0000', '#0000FF', '#00C4B0']
    }
    return pd.DataFrame(data)

@pytest.fixture
def math_service():
    """Instância real do serviço de matemática para testes de lógica."""
    return PerceptualColorMath()

@pytest.fixture
def repo(mock_color_df, math_service):
    """Repositório configurado com dados em memória (Injeção de Dependência)."""
    return ColorRepository(data_source=mock_color_df, math_service=math_service)

@pytest.fixture
def manager(repo):
    """Manager configurado com um tradutor real (ou mockado se preferir)."""
    translator = GoogleTranslationService()
    return ColorManager(repo=repo, translator=translator)

# --- TESTES UNITÁRIOS E DE REQUISITOS ---

def test_find_by_name_fuzzy_rigorous_match(repo):
    """Valida o requisito RD05: busca fuzzy com rigor de 95%."""
    # Act
    result, similarity = repo.find_by_name_fuzzy("Red", threshold=0.95)
    
    # Assert
    assert result is not None
    assert result['Name'] == "Red"
    # Comparação segura para float (1.0 >= 0.95)
    assert similarity > 0.95 or math.isclose(similarity, 0.95)

def test_find_by_name_fuzzy_below_threshold(repo):
    """Garante que falha se a similaridade for menor que o threshold."""
    result, similarity = repo.find_by_name_fuzzy("XyZ", threshold=0.95)
    
    assert result is None
    assert similarity < 0.95

def test_find_nearest_by_hex_exact(repo):
    """Valida se encontra a cor exata com distância zero (RF01)."""
    result, distance = repo.find_nearest_by_hex("#00C4B0")
    
    assert result['Name'] == "Amazonite"
    assert math.isclose(distance, 0, abs_tol=1e-9)

def test_calculo_distancia_hsl_logic(math_service):
    """Valida a lógica de proximidade de cores no espaço HSL (RF06)."""
    verde = (120, 100, 50)
    ciano = (180, 100, 50)
    vermelho = (0, 100, 50)
    
    dist_verde_ciano = math_service.calculate_distance(verde, ciano)
    dist_verde_vermelho = math_service.calculate_distance(verde, vermelho)
    
    assert dist_verde_ciano < dist_verde_vermelho

def test_translation_service_cache_rd03():
    """Valida tradução e comportamento de cache (RD03)."""
    service = GoogleTranslationService()
    
    res1 = service.translate("Red", target="pt")
    res2 = service.translate("Red", target="pt")
    
    assert res1.lower() == "vermelho"
    assert res1 == res2  # Deve retornar o mesmo valor (vido do cache)

def test_full_flow_identification(manager):
    """Teste de integração: do HEX à tradução final."""
    # Act
    resultado = manager.identify_by_hex("#FF0000")
    
    # Assert
    assert resultado["name_en"].lower() == "red"
    assert "name_pt_br" in resultado
    assert resultado["name_pt_br"].lower() == "vermelho"

def test_commutative_distance(math_service):
    """Garante que a distância entre A-B é igual a B-A."""
    cor1 = (30, 80, 40)
    cor2 = (200, 20, 90)
    
    dist1 = math_service.calculate_distance(cor1, cor2)
    dist2 = math_service.calculate_distance(cor2, cor1)
    
    assert math.isclose(dist1, dist2)

def test_identify_by_hex_invalid_format(manager):
    """Valida se o sistema lida com inputs de HEX inválidos."""
    with pytest.raises(ValueError):
        manager.identify_by_hex("NOT_A_COLOR")