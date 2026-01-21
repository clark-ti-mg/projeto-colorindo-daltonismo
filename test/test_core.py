# test/test_core.py
import pytest
from app.data.repository import ColorRepository
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