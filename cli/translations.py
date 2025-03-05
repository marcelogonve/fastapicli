import os
import locale

TRANSLATIONS_DIR = os.path.join(os.path.dirname(__file__), "translations")

def detect_system_language():
    lang, _ = locale.getdefaultlocale()
    return "es" if lang and lang.startswith("es") else "en"

def load_translations(lang):
    file_path = os.path.join(TRANSLATIONS_DIR, f"{lang}.md")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Translation file not found: {file_path}")
    
    translations = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                translations[key.strip()] = value.strip()

    return translations