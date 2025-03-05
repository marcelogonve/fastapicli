from cli.translations import detect_system_language, load_translations

lang = detect_system_language()
messages = load_translations(lang)