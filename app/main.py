from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import FileResponse
from .core.math_utils import PerceptualColorMath
from .services.translation import GoogleTranslationService
from .data.repository import ColorRepository
from .services.color_manager import ColorManager
import os

app = FastAPI(title="Colorindo o Daltonismo 3.0")

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_dir, "color_names.csv")
index_path = os.path.join(base_dir, "templates", "index.html")
converter_path = os.path.join(base_dir, "templates", "converter.html")

math_tool = PerceptualColorMath()
translator = GoogleTranslationService()
repo = ColorRepository(csv_path, math_tool)
manager = ColorManager(repo, translator)

@app.get("/")
async def read_index():
    return FileResponse(index_path)

@app.get("/converter")
async def read_converter():
    return FileResponse(converter_path)

@app.get("/color-name")
def get_color(
    hex: str = Query(None), 
    name: str = Query(None)
):
    if hex:
        return manager.identify_by_hex(hex)
    elif name:
        result = manager.identify_by_name(name)
        if result.get("status") == "error":
            raise HTTPException(status_code=404, detail="Cor não encontrada")
        return result
    else:
        raise HTTPException(status_code=400, detail="Forneça 'hex' ou 'name'")

@app.get("/health")
def health():
    return {"status": "online"}