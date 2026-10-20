#!/usr/bin/env python3
"""Script de construcción para el sitio web de TobiXu."""
from pathlib import Path
from jinja2 import Template
import yaml

def build_site():
    web_dir = Path(".")
    template_path = web_dir / "template.html"
    i18n_dir = web_dir / "i18n"
    
    template_content = template_path.read_text(encoding="utf-8")
    template = Template(template_content)
    
    lang_configs = {
        'es': {'output': web_dir / 'index.html', 'dir': None},
        'en': {'output': web_dir / 'en' / 'index.html', 'dir': None},
        'zh': {'output': web_dir / 'zh' / 'index.html', 'dir': None},
    }
    
    languages = [
        {'url': '/', 'label': '🇲🇽 Español'},
        {'url': '/en', 'label': '🇬🇧 English'},
        {'url': '/zh', 'label': '🇨🇳 中文'},
    ]
    
    for lang_code, config in lang_configs.items():
        yaml_path = i18n_dir / f"{lang_code}.yaml"
        if not yaml_path.exists():
            print(f"⚠ {lang_code}.yaml no encontrado, saltando...")
            continue
        
        with open(yaml_path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)
        
        content['dir'] = config['dir']
        content['languages'] = languages
        
        html = template.render(**content)
        config['output'].parent.mkdir(parents=True, exist_ok=True)
        config['output'].write_text(html, encoding='utf-8')
        print(f"✓ {config['output']} generado ({len(html)} bytes)")

if __name__ == "__main__":
    build_site()
    print("\n✅ Sitio construido exitosamente")
