import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

# Criamos o cliente fora das fixtures para simplificar
# Se o comando de upgrade acima funcionar, este erro de TypeError sumirá
client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "online"}

def test_get_color_no_params():
    response = client.get("/color-name")
    assert response.status_code == 400

@patch("app.main.manager")
def test_get_color_by_hex_success(mock_manager):
    mock_manager.identify_by_hex.return_value = {"name_pt_br": "Verde", "status": "success"}
    response = client.get("/color-name?hex=00FF00")
    assert response.status_code == 200
    assert response.json()["name_pt_br"] == "Verde"

@patch("app.main.manager")
def test_get_color_by_name_error(mock_manager):
    mock_manager.identify_by_name.return_value = {"status": "error"}
    response = client.get("/color-name?name=cor_fantasma")
    assert response.status_code == 404

@patch("app.main.FileResponse")
def test_read_index(mock_file):
    """Cobre a linha 23"""
    response = client.get("/")
    assert response.status_code == 200

@patch("app.main.FileResponse")
def test_read_converter(mock_file):
    """Cobre a linha 27"""
    response = client.get("/converter")
    assert response.status_code == 200

@patch("app.main.manager")
def test_get_color_by_name_success(mock_manager):
    """Cobre a linha 40"""
    mock_manager.identify_by_name.return_value = {"status": "success", "name_pt_br": "Azul"}
    response = client.get("/color-name?name=blue")
    assert response.status_code == 200