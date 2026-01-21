import os

# Estrutura de pastas
folders = [
    "app",
    "app/core",
    "app/data",
    "app/services",
    "templates",
    "templates/css",
    "templates/img"
]

# Conteúdo dos arquivos (Dicionário com caminho: conteúdo)
files = {
    "app/core/interfaces.py": """from typing import Protocol, Dict, Any, Optional

class IColorMath(Protocol):
    def hex_to_rgb(self, hex_code: str) -> tuple: ...
    def rgb_to_hsl(self, r: int, g: int, b: int) -> tuple: ...
    def calculate_distance(self, hsl1: tuple, hsl2: tuple) -> float: ...

class ITranslationService(Protocol):
    def translate(self, text: str, source: str, target: str) -> str: ...
""",

    "app/core/math_utils.py": """import math
from .interfaces import IColorMath

class PerceptualColorMath(IColorMath):
    def hex_to_rgb(self, hex_code: str) -> tuple:
        hex_code = hex_code.lstrip('#').upper()
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hsl(self, r, g, b):
        r, g, b = r/255.0, g/255.0, b/255.0
        mx, mn = max(r, g, b), min(r, g, b)
        l = (mx + mn) / 2.0
        if mx == mn: return 0.0, 0.0, l
        d = mx - mn
        s = d / (2.0 - mx - mn) if l > 0.5 else d / (mx + mn)
        if mx == r: h = (g - b) / d + (6 if g < b else 0)
        elif mx == g: h = (b - r) / d + 2
        else: h = (r - g) / d + 4
        return h / 6.0, s, l

    def calculate_distance(self, hsl1, hsl2):
        h1, s1, l1 = hsl1
        h2, s2, l2 = hsl2
        dh = min(abs(h1 - h2), 1.0 - abs(h1 - h2))
        return math.sqrt((dh * 3.0)**2 + ((s1 - s2) * 0.5)**2 + ((l1 - l2) * 0.3)**2)
""",

    "app/services/translation.py": """from functools import lru_cache
from deep_translator import GoogleTranslator
from ..core.interfaces import ITranslationService

class GoogleTranslationService(ITranslationService):
    @lru_cache(maxsize=500)
    def translate(self, text: str, source: str = 'en', target: str = 'pt') -> str:
        try:
            return GoogleTranslator(source=source, target=target).translate(text)
        except Exception:
            return text
""",

    "app/data/repository.py": """import pandas as pd
from ..core.interfaces import IColorMath

class ColorRepository:
    def __init__(self, csv_path: str, math_service: IColorMath):
        self.df = pd.read_csv(csv_path)
        self.math = math_service
        self._normalize_data()

    def _normalize_data(self):
        self.df['Hex (24 bit)'] = self.df['Hex (24 bit)'].astype(str).str.strip().str.upper()

    def find_nearest(self, target_hex: str):
        target_rgb = self.math.hex_to_rgb(target_hex)
        target_hsl = self.math.rgb_to_hsl(*target_rgb)
        
        def get_dist(row_hex):
            rgb = self.math.hex_to_rgb(row_hex)
            return self.math.calculate_distance(target_hsl, self.math.rgb_to_hsl(*rgb))
            
        distances = self.df['Hex (24 bit)'].apply(get_dist)
        idx = distances.idxmin()
        return self.df.loc[idx], distances[idx]
""",

    "app/services/color_manager.py": """from ..data.repository import ColorRepository
from ..core.interfaces import ITranslationService

class ColorManager:
    def __init__(self, repo: ColorRepository, translator: ITranslationService):
        self.repo = repo
        self.translator = translator

    def identify_color(self, hex_code: str):
        row, dist = self.repo.find_nearest(hex_code)
        name_pt = self.translator.translate(row['Name'])
        return {
            "input_hex": f"#{hex_code.upper()}",
            "name_en": row['Name'],
            "name_pt_br": name_pt,
            "matched_hex": f"#{row['Hex (24 bit)']}",
            "distance": float(dist)
        }
""",

    "app/main.py": """from fastapi import FastAPI, Query
from .core.math_utils import PerceptualColorMath
from .services.translation import GoogleTranslationService
from .data.repository import ColorRepository
from .services.color_manager import ColorManager
import os

app = FastAPI(title="Colorindo o Daltonismo 3.0")

# Caminho do CSV
csv_path = os.path.join(os.getcwd(), "color_names.csv")

# Injeção de Dependências
math_tool = PerceptualColorMath()
translator = GoogleTranslationService()
repo = ColorRepository(csv_path, math_tool)
manager = ColorManager(repo, translator)

@app.get("/color-name")
def get_color(hex: str = Query(..., description="Ex: FF0000")):
    return manager.identify_color(hex)

@app.get("/health")
def health():
    return {"status": "online", "engine": "SOLID Architecture"}
""",
    "app/__init__.py": "",
    "app/core/__init__.py": "",
    "app/data/__init__.py": "",
    "app/services/__init__.py": ""
}

print("🚀 Iniciando criação do projeto SOLID...")

# Criar pastas
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"📁 Pasta criada: {folder}")

# Criar arquivos
for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"📄 Arquivo criado: {path}")

print("\\n✅ Projeto configurado com sucesso!")
print("Dica: Certifique-se de que o arquivo 'color_names.csv' esteja nesta pasta raiz.")