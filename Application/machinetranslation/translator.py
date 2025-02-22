"""
Simple EN-FR/FR-EN Translator
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    English To French Translation Func
    """
    translator = MyMemoryTranslator(source="en", target="fr")
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    French to English Translation Func
    """
    translator = MyMemoryTranslator(source="fr", target="en")
    english_text = translator.translate(french_text)
    return english_text
