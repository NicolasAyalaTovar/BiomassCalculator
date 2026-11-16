# 🪲 Biomass Calculator

**Aplicación de escritorio para estimar la biomasa de insectos a partir de su abundancia y longitud corporal.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-informational)

Interfaz gráfica sencilla que aplica la relación longitud–peso propuesta por **Rogers et al. (1976)** y utilizada posteriormente por **Stork & Blackburn (1993)** en estudios de artrópodos de bosque tropical.

> ¿Prefieres trabajar en R o con tablas de muchas especies? Consulta la versión en R: [R-BiomassCalculator](https://github.com/NicolasAyalaTovar/R-BiomassCalculator).

## 📐 Modelo

$$
b = n \cdot \left(0.0305 \cdot l^{2.62}\right)
$$

| Símbolo | Significado |
|---|---|
| $b$ | Biomasa estimada |
| $n$ | Abundancia (número de individuos) |
| $l$ | Longitud corporal (cm) |

## ✨ Características

- Interfaz gráfica con Tkinter, sin dependencias externas.
- Validación de entradas: abundancia entera y longitud positiva (acepta coma o punto decimal).
- Cálculo con la tecla **Enter** o con el botón.
- Referencias bibliográficas visibles dentro de la aplicación.

## 🚀 Instalación y uso

Solo requiere Python 3.8+ con Tkinter (incluido en la instalación estándar de Python en Windows y macOS).

```bash
git clone https://github.com/NicolasAyalaTovar/BiomassCalculator.git
cd BiomassCalculator
python biomass.py
```

En Linux, si falta Tkinter: `sudo apt install python3-tk`.

### Ejemplo

| Abundancia (n) | Longitud (l) | Biomasa |
|---|---|---|
| 5 | 6.5 | 20.56 |

## 📚 Referencias

- Rogers, L. E., Hinds, W. T. & Buschbom, R. L. (1976). A general weight vs. length relationship for insects. *Annals of the Entomological Society of America*, 69(2), 387–389.
- Stork, N. E. & Blackburn, T. M. (1993). Abundance, body size and biomass of arthropods in tropical forest. *Oikos*, 67(3), 483–489.

## 👤 Autor

**Nicolás Ayala Tovar** · [GitHub](https://github.com/NicolasAyalaTovar)
