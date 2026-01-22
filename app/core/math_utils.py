import math
from .interfaces import IColorMath

class PerceptualColorMath(IColorMath):
    """
    Cálculos matemáticos para conversão e comparação de cores.
    Utiliza ponderação perceptual para melhor precisão em daltonismo.
    """

    # Pesos perceptuais para o cálculo de distância (RF06)
    HUE_WEIGHT = 3.0
    SATURATION_WEIGHT = 0.5
    LUMINANCE_WEIGHT = 0.3

    def hex_to_rgb(self, hex_code: str) -> tuple:
        """Converte HEX para tupla RGB (0-255)."""
        clean_hex = hex_code.lstrip('#').upper()
        
        if len(clean_hex) != 6:
            raise ValueError(f"HEX inválido: {hex_code}. Deve ter 6 caracteres.")
            
        try:
            return tuple(int(clean_hex[i:i+2], 16) for i in (0, 2, 4))
        except ValueError:
            raise ValueError(f"HEX contém caracteres inválidos: {hex_code}")

    def rgb_to_hsl(self, r: int, g: int, b: int) -> tuple:
        """Converte RGB para HSL (valores entre 0.0 e 1.0)."""
        # Normalização para escala 0-1
        r_norm, g_norm, b_norm = r / 255.0, g / 255.0, b / 255.0
        
        max_val = max(r_norm, g_norm, b_norm)
        min_val = min(r_norm, g_norm, b_norm)
        delta = max_val - min_val
        
        # Luminosidade
        l = (max_val + min_val) / 2.0
        
        # Caso a cor seja cinza (Acromática)
        if math.isclose(max_val, min_val, abs_tol=1e-7):
            return 0.0, 0.0, l

        # Saturação
        if l > 0.5:
            s = delta / (2.0 - max_val - min_val)
        else:
            s = delta / (max_val + min_val)

        # Matiz (Hue)
        if math.isclose(max_val, r_norm):
            h = (g_norm - b_norm) / delta + (6 if g_norm < b_norm else 0)
        elif math.isclose(max_val, g_norm):
            h = (b_norm - r_norm) / delta + 2
        else:
            h = (r_norm - g_norm) / delta + 4
            
        return h / 6.0, s, l

    def calculate_distance(self, hsl1: tuple, hsl2: tuple) -> float:
        """
        Calcula a distância euclidiana ponderada entre duas cores HSL.
        Leva em conta a sensibilidade humana (Perceptual Distance).
        """
        h1, s1, l1 = hsl1
        h2, s2, l2 = hsl2

        # Diferença de matiz considerando o círculo cromático (360º / 1.0)
        dh = min(abs(h1 - h2), 1.0 - abs(h1 - h2))
        
        # Diferenças individuais
        ds = s1 - s2
        dl = l1 - l2

        # Aplicação dos pesos perceptuais
        weighted_h = (dh * self.HUE_WEIGHT) ** 2
        weighted_s = (ds * self.SATURATION_WEIGHT) ** 2
        weighted_l = (dl * self.LUMINANCE_WEIGHT) ** 2

        return math.sqrt(weighted_h + weighted_s + weighted_l)