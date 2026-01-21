import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from app.data.repository import ColorRepository

@pytest.fixture
def mock_repo():
    # Simulamos um CSV com 2 cores
    data = {
        'Name': ['Red', 'Blue'],
        'Hex (24 bit)': ['FF0000', '0000FF'],
        'Name_Lower': ['red', 'blue']
    }
    df = pd.DataFrame(data)
    
    with patch('pandas.read_csv', return_value=df):
        math_mock = MagicMock()
        # Mock do retorno da conversão para o teste de distância
        math_mock.hex_to_rgb.return_value = (255, 0, 0)
        math_mock.rgb_to_hsl.return_value = (0, 100, 50)
        math_mock.calculate_distance.return_value = 0
        
        repo = ColorRepository("fake.csv", math_mock)
        return repo

def test_find_by_name_fuzzy_exact(mock_repo):
    result, score = mock_repo.find_by_name_fuzzy("Red")
    assert result['Name'] == "Red"
    assert score == 1.0

def test_find_by_name_fuzzy_not_found(mock_repo):
    # Testando o threshold de 95% (RD05)
    result, score = mock_repo.find_by_name_fuzzy("XyZ123", threshold=0.95)
    assert result is None

def test_find_nearest_by_hex(mock_repo):
    result, dist = mock_repo.find_nearest_by_hex("#FF0000")
    assert result['Name'] == "Red"