#!/usr/bin/env python3
"""
Script OCR Simples
==================
Versão simplificada para teste rápido de OCR
"""

import pytesseract
from PIL import Image
import sys
import os

def extract_text_simple(image_path):
    """
    Extrai texto de uma imagem de forma simples
    """
    try:
        # Abre a imagem
        image = Image.open(image_path)
        
        # Extrai texto usando português
        text = pytesseract.image_to_string(image, lang='por')
        
        return text
    except Exception as e:
        return f"Erro: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print("Uso: python ocr_simple.py <caminho_da_imagem>")
        print("Exemplo: python ocr_simple.py imagem.jpg")
        return
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Arquivo não encontrado: {image_path}")
        return
    
    print(f"Processando: {image_path}")
    print("-" * 50)
    
    text = extract_text_simple(image_path)
    print(text)
    
    # Salva em arquivo se texto foi extraído
    if text and not text.startswith("Erro"):
        output_file = f"texto_extraido_{os.path.splitext(os.path.basename(image_path))[0]}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"\nTexto salvo em: {output_file}")

if __name__ == "__main__":
    main()