import pytest
from unittest.mock import MagicMock
from app.services.color_manager import ColorManager

def test_identify_by_hex_flow():
    repo = MagicMock()
    trans = MagicMock()
    
    # Configura retornos
    repo.find_nearest_by_hex.return_value = ({'Name': 'Amazonite', 'Hex (24 bit)': '00C4B0'}, 0.5)
    trans.translate.return_value = "Amazonita"
    
    manager = ColorManager(repo, trans)
    res = manager.identify_by_hex("00C4B0")
    
    assert res['name_pt_br'] == "Amazonita"
    assert res['status'] == "success"

def test_identify_by_name_error_flow():
    repo = MagicMock()
    repo.find_by_name_fuzzy.return_value = (None, 0.1)
    
    manager = ColorManager(repo, MagicMock())
    res = manager.identify_by_name("cor_que_nao_existe")
    
    assert res['status'] == "error"