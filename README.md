# TobiXu Web — vitrina trilingüe de la familia

Sitio público de TobiXu (https://tobixu.xyz). Una plantilla, un contenido por
idioma, un script de construcción: la deriva entre traducciones queda
imposibilitada por diseño.

## Estructura

    tobixu-web/
    ├── template.html      # Plantilla Jinja2 (estructura, CSS, conmutador, RTL)
    ├── build.py           # Construye los HTML desde template + i18n/*.yaml
    ├── i18n/
    │   ├── es.yaml        # Español (raíz del sitio)
    │   ├── en.yaml        # Inglés (/en/)
    │   └── zh.yaml        # Chino mandarín (/zh/)
    ├── assets/            # glifo.png, orbita-noche.png (rutas absolutas /assets/)
    ├── downloads/         # Notas históricas de rc25 (sin enlaces desde el sitio nuevo)
    ├── index.html         # Generado (no editar a mano)
    ├── en/index.html      # Generado
    └── zh/index.html      # Generado

## Flujo de trabajo

1. Editar contenido en `i18n/<lang>.yaml` (textos, variantes, tamaños, SHA256).
2. `python3 build.py`
3. Revisar en local: `python3 -m http.server 8080` → http://localhost:8080
4. `git add -A && git commit && git push` → GitHub Pages despliega tobixu.xyz.

Los HTML generados se commitean: Pages sirve directo del repo.

## Añadir un idioma

1. Crear `i18n/<code>.yaml` con las mismas claves que `es.yaml`.
2. En `build.py`: añadir entrada en `lang_configs` y en `languages`.
   - Idiomas RTL (árabe): `'dir': 'rtl'`; la plantilla espeja el CSS sola.
3. `python3 build.py` y commit.

## Contrato de traducción

- Glosario fijo: *rolling release* (sin traducir en es; 滚动发布 en zh),
  *stem* y *arts* (no se traducen), horneada = bake, glifo = glyph / 字符.
- Hashes SHA256 y URLs son idénticos en todos los idiomas: se copian, no se traducen.
- Cada ISO publicada obliga actualizar en TODOS los yaml:
  `size`, `download_url`, `sha_gnome`, `sha_plasma` y notas de versión.

## Familia de variantes

| Variante | Identifier en archive.org | Carácter | Estado |
|---|---|---|---|
| Plasma | tobixu-plasma | completa (todo instalado) | publicada |
| GNOME  | tobixu-gnome  | base (stem/arts instalables) | publicada |
| XFCE   | tobixu-xfce   | base ligera | próximamente |
| LXQt   | tobixu-lxqt   | base mínima | próximamente |

## Créditos

© 2026 Manuel López Mateos.
Desarrollado con la colaboración de Qwen (Alibaba Tongyi Lab).
