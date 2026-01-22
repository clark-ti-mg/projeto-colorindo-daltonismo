import math
import pandas as pd
from difflib import SequenceMatcher
from ..core.interfaces import IColorMath

class ColorRepository:
    """
    Gerencia a busca e persistência de dados de cores.
    Aceita um caminho de arquivo CSV ou um DataFrame diretamente.
    """

    def __init__(self, data_source, math_service: IColorMath):
        # Resolve a fonte de dados: se for string, carrega o CSV. 
        # Se for DataFrame, faz uma cópia.
        self._df = self._load_data(data_source)
        self._math = math_service
        self._normalize_data()

    def _load_data(self, data_source) -> pd.DataFrame:
        """Helper para carregar os dados de diferentes fontes."""
        if isinstance(data_source, str):
            return pd.read_csv(data_source)
        if isinstance(data_source, pd.DataFrame):
            return data_source.copy()
        raise TypeError("data_source deve ser um caminho (str) ou um pandas.DataFrame")

    def _normalize_data(self) -> None:
        """Prepara os dados para otimizar as buscas."""
        self._df['Hex_Clean'] = (
            self._df['Hex (24 bit)']
            .astype(str)
            .str.replace('#', '', regex=False)
            .str.strip()
            .str.upper()
        )
        self._df['Name_Lower'] = self._df['Name'].str.lower().str.strip()

    def find_nearest_by_hex(self, target_hex: str):
        """Encontra a cor mais próxima usando distância perceptual no espaço HSL."""
        clean_target = target_hex.replace('#', '').upper()
        target_rgb = self._math.hex_to_rgb(clean_target)
        target_hsl = self._math.rgb_to_hsl(*target_rgb)
        
        distances = self._df['Hex_Clean'].apply(
            self._calculate_row_distance, 
            args=(target_hsl,)
        )
        
        idx = distances.idxmin()
        return self._df.loc[idx], distances[idx]

    def find_by_name_fuzzy(self, search_name: str, threshold: float = 0.95):
        """Busca por nome com rigor de threshold usando comparação segura de floats."""
        target_name = search_name.lower().strip()
        
        similarities = self._df['Name_Lower'].apply(
            lambda x: SequenceMatcher(None, target_name, str(x)).ratio()
        )
        
        idx = similarities.idxmax()
        score = similarities[idx]

        if score > threshold or math.isclose(score, threshold, rel_tol=1e-7):
            return self._df.loc[idx], score
        
        return None, score

    def _calculate_row_distance(self, row_hex: str, target_hsl: tuple) -> float:
        try:
            rgb = self._math.hex_to_rgb(row_hex)
            hsl = self._math.rgb_to_hsl(*rgb)
            return self._math.calculate_distance(target_hsl, hsl)
        except (ValueError, TypeError, KeyError):
            return float('inf')