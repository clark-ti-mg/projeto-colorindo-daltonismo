import pytest
import pandas as pd
from unittest.mock import MagicMock
from app.data.repository import ColorRepository

@pytest.fixture
def sample_df():
    """Cria um DataFrame de exemplo para os testes."""
    return pd.DataFrame({
        'Name': ['Red', 'Blue'],
        'Hex (24 bit)': ['#FF0000', '#0000FF']
    })

@pytest.fixture
def repo(sample_df):
    """Instancia o repositório com um mock de math_service."""
    math_mock = MagicMock()
    # Configuração padrão para evitar erros em testes simples
    math_mock.hex_to_rgb.return_value = (255, 0, 0)
    math_mock.rgb_to_hsl.return_value = (0, 1.0, 0.5)
    math_mock.calculate_distance.return_value = 0.0
    return ColorRepository(data_source=sample_df, math_service=math_mock)

# --- Testes de Funcionalidade Core ---

import math

def test_find_by_name_fuzzy_exact(repo):
    """
    Valida busca exata com score próximo de 1.0.
    Evita o bad smell de comparação direta de ponto flutuante.
    """
    # Act
    result, score = repo.find_by_name_fuzzy("Red")
    
    # Assert
    assert result['Name'] == "Red"
    # Verificação segura para floats
    assert math.isclose(score, 1.0, abs_tol=1e-9)

def test_find_by_name_fuzzy_not_found(repo):
    """Valida o threshold rigoroso de 95% (RD05)."""
    result, score = repo.find_by_name_fuzzy("Nome Absurdo", threshold=0.95)
    assert result is None
    assert score < 0.95

# --- Testes de Cobertura de Exceções (Linhas 25, 73, 74) ---

def test_repository_invalid_data_source_type():
    """Cobre a linha 25: Erro ao passar tipo inválido no construtor."""
    math_mock = MagicMock()
    with pytest.raises(TypeError, match="data_source deve ser um caminho"):
        ColorRepository(data_source=123, math_service=math_mock)

def test_calculate_row_distance_exception_handling(repo):
    """Cobre as linhas 73-74: Retorno float('inf') em caso de erro na matemática."""
    # Forçamos o math_service a lançar um erro durante o processamento de uma linha
    repo._math.hex_to_rgb.side_effect = ValueError("Hex corrompido")
    
    # Act
    distance = repo._calculate_row_distance("INVALID", (0, 0, 0))
    
    # Assert
    assert distance == float('inf')

# --- Testes de Integração de Busca ---

import math

def test_find_nearest_by_hex_logic(repo):
    """
    Valida se o fluxo de busca por HEX retorna os dados do DataFrame.
    Utiliza math.isclose para garantir a segurança em operações de ponto flutuante.
    """
    # Arrange
    expected_distance = 0.123
    repo._math.calculate_distance.return_value = expected_distance
    
    # Act
    result, dist = repo.find_nearest_by_hex("#FF0000")
    
    # Assert
    assert result['Name'] in ['Red', 'Blue']
    # Substituição do equality check (==) por proximidade controlada
    assert math.isclose(dist, expected_distance, abs_tol=1e-9)