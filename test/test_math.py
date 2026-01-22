import pytest
import math
from app.core.math_utils import PerceptualColorMath

@pytest.fixture
def math_tool():
    """Fixture para instanciar a ferramenta de cálculo (DIP)."""
    return PerceptualColorMath()

# --- Testes de Conversão RGB/HSL ---

def test_rgb_to_hsl_pure_red(math_tool):
    """Valida conversão da cor primária Vermelha (RF01)."""
    # Act: Red (255,0,0) -> HSL (0, 1.0, 0.5)
    h, s, l = math_tool.rgb_to_hsl(255, 0, 0)
    
    # Assert usando math.isclose para evitar erros infinitesimais de float
    assert math.isclose(h, 0.0, abs_tol=1e-7)
    assert math.isclose(s, 1.0, abs_tol=1e-7)
    assert math.isclose(l, 0.5, abs_tol=1e-7)

def test_rgb_to_hsl_grayscale(math_tool):
    """
    Garante que tons de cinza tenham saturação zero.
    Ajustado para a precisão real de 8 bits (128/255 ≈ 0.50196).
    """
    # Arrange: Gray (128, 128, 128)
    # Act
    _, s, l = math_tool.rgb_to_hsl(128, 128, 128)
    
    # Assert
    # Saturação deve ser zero para cores acromáticas
    assert math.isclose(s, 0.0, abs_tol=1e-9)
    
    # Luminosidade para 128/255 é aproximadamente 0.50196078
    expected_l = 128 / 255.0
    assert math.isclose(l, expected_l, abs_tol=1e-9)

# --- Testes de Conversão HEX ---

def test_hex_to_rgb_valid(math_tool):
    """Valida conversão de HEX para RGB com e sem símbolo #."""
    assert math_tool.hex_to_rgb("#FF0000") == (255, 0, 0)
    assert math_tool.hex_to_rgb("00FF00") == (0, 255, 0)

def test_hex_to_rgb_invalid_length(math_tool):
    """Valida erro para HEX com tamanho diferente de 6 caracteres."""
    with pytest.raises(ValueError, match="HEX"):
        math_tool.hex_to_rgb("ABC")

def test_hex_to_rgb_invalid_chars(math_tool):
    """Valida erro para HEX com caracteres não-hexadecimais."""
    # Corrigido para aceitar a mensagem do math_utils: "HEX contém caracteres inválidos"
    with pytest.raises(ValueError, match="HEX"):
        math_tool.hex_to_rgb("GHIJKL")

# --- Testes de Distância Perceptual ---

def test_calculate_distance_identical_colors(math_tool):
    """A distância entre cores idênticas deve ser exatamente zero."""
    hsl = (0.5, 0.5, 0.5)
    distance = math_tool.calculate_distance(hsl, hsl)
    
    assert math.isclose(distance, 0.0, abs_tol=1e-9)

def test_calculate_distance_perceptual_logic(math_tool):
    """
    Valida se a distância reflete os pesos perceptuais (RF06).
    Mudança de Hue (peso 3.0) pesa mais que Luminosidade (peso 0.3).
    """
    base = (0.0, 1.0, 0.5)
    diff_h = (0.1, 1.0, 0.5) # Variação no Hue
    diff_l = (0.0, 1.0, 0.6) # Variação na Luminosidade
    
    dist_h = math_tool.calculate_distance(base, diff_h)
    dist_l = math_tool.calculate_distance(base, diff_l)
    
    assert dist_h > dist_l

def test_hue_circular_distance(math_tool):
    """
    Testa a natureza circular do Matiz (360º).
    A distância entre 0.01 e 0.99 deve ser 0.02.
    """
    c1 = (0.01, 1.0, 0.5)
    c2 = (0.99, 1.0, 0.5)
    
    distance = math_tool.calculate_distance(c1, c2)
    
    # Diferença de Hue esperada é 0.02 (não 0.98)
    expected_dh = 0.02
    expected_dist = math.sqrt((expected_dh * 3.0)**2)
    
    assert math.isclose(distance, expected_dist, abs_tol=1e-7)