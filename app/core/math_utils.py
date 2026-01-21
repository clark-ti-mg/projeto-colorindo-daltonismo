import math
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