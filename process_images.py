#!/usr/bin/env python3
"""
Processador de Imagens OCR
==========================
Script para processar automaticamente as imagens da pasta /img/
"""

import pytesseract
from PIL import Image
import os
import glob
from pathlib import Path

def extract_text_from_image(image_path):
    """
    Extrai texto de uma imagem usando OCR
    """
    try:
        print(f"Processando: {image_path}")
        
        # Abre a imagem
        image = Image.open(image_path)
        
        # Configurações do Tesseract para melhor precisão
        config = '--oem 3 --psm 6 -l por'
        
        # Extrai texto
        text = pytesseract.image_to_string(image, config=config)
        
        return text.strip()
        
    except Exception as e:
        return f"Erro ao processar {image_path}: {str(e)}"

def main():
    # Pasta das imagens
    img_folder = "img"
    
    # Verifica se a pasta existe
    if not os.path.exists(img_folder):
        print(f"Pasta '{img_folder}' não encontrada!")
        return
    
    # Busca todas as imagens na pasta
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff', '*.gif']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(img_folder, ext)))
        image_files.extend(glob.glob(os.path.join(img_folder, ext.upper())))
    
    # Ordena os arquivos
    image_files.sort()
    
    if not image_files:
        print(f"Nenhuma imagem encontrada na pasta '{img_folder}'")
        return
    
    print(f"Encontradas {len(image_files)} imagens:")
    for img in image_files:
        print(f"  - {img}")
    
    print("\n" + "="*60)
    print("INICIANDO PROCESSAMENTO OCR")
    print("="*60)
    
    # Processa cada imagem
    all_results = []
    
    for i, image_path in enumerate(image_files, 1):
        print(f"\n--- IMAGEM {i}/{len(image_files)} ---")
        
        text = extract_text_from_image(image_path)
        
        if text and not text.startswith("Erro"):
            print(f"Texto extraído ({len(text)} caracteres):")
            print("-" * 40)
            print(text)
            print("-" * 40)
            
            all_results.append(f"=== IMAGEM {i}: {os.path.basename(image_path)} ===\n{text}\n")
        else:
            print(f"Problema ao extrair texto: {text}")
            all_results.append(f"=== IMAGEM {i}: {os.path.basename(image_path)} ===\n{text}\n")
    
    # Salva todos os resultados
    output_file = "texto_extraido_todas_imagens.txt"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(all_results))
        print(f"\n✅ Todos os resultados salvos em: {output_file}")
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo: {str(e)}")
    
    print("\n" + "="*60)
    print("PROCESSAMENTO CONCLUÍDO!")
    print("="*60)

if __name__ == "__main__":
    main()