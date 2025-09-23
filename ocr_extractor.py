#!/usr/bin/env python3
"""
OCR Text Extractor
==================
Script para extrair texto de imagens usando OCR (Optical Character Recognition)
Suporta múltiplos formatos de imagem e pré-processamento para melhor precisão.
"""

import cv2
import numpy as np
import pytesseract
from PIL import Image
import argparse
import os
import sys
from pathlib import Path

class OCRExtractor:
    def __init__(self, language='por'):
        """
        Inicializa o extrator OCR
        
        Args:
            language (str): Idioma para OCR (padrão: 'por' para português)
        """
        self.language = language
        
    def preprocess_image(self, image_path):
        """
        Pré-processa a imagem para melhorar a precisão do OCR
        
        Args:
            image_path (str): Caminho para a imagem
            
        Returns:
            numpy.ndarray: Imagem pré-processada
        """
        # Carrega a imagem
        img = cv2.imread(image_path)
        
        if img is None:
            raise ValueError(f"Não foi possível carregar a imagem: {image_path}")
        
        # Converte para escala de cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Aplica filtro gaussiano para reduzir ruído
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Aplica threshold adaptativo
        thresh = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )
        
        # Aplica operações morfológicas para limpar a imagem
        kernel = np.ones((1, 1), np.uint8)
        cleaned = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        return cleaned
    
    def extract_text_from_image(self, image_path, preprocess=True):
        """
        Extrai texto de uma imagem usando OCR
        
        Args:
            image_path (str): Caminho para a imagem
            preprocess (bool): Se deve aplicar pré-processamento
            
        Returns:
            str: Texto extraído da imagem
        """
        try:
            if preprocess:
                # Usa imagem pré-processada
                processed_img = self.preprocess_image(image_path)
                # Converte numpy array para PIL Image
                pil_img = Image.fromarray(processed_img)
            else:
                # Usa imagem original
                pil_img = Image.open(image_path)
            
            # Configurações do Tesseract para melhor precisão
            config = f'--oem 3 --psm 6 -l {self.language}'
            
            # Extrai texto
            text = pytesseract.image_to_string(pil_img, config=config)
            
            return text.strip()
            
        except Exception as e:
            return f"Erro ao processar {image_path}: {str(e)}"
    
    def extract_text_from_multiple_images(self, image_paths, preprocess=True):
        """
        Extrai texto de múltiplas imagens
        
        Args:
            image_paths (list): Lista de caminhos para as imagens
            preprocess (bool): Se deve aplicar pré-processamento
            
        Returns:
            dict: Dicionário com {caminho_da_imagem: texto_extraído}
        """
        results = {}
        
        for image_path in image_paths:
            print(f"Processando: {image_path}")
            text = self.extract_text_from_image(image_path, preprocess)
            results[image_path] = text
            
        return results
    
    def save_text_to_file(self, text, output_path):
        """
        Salva texto extraído em arquivo
        
        Args:
            text (str): Texto a ser salvo
            output_path (str): Caminho do arquivo de saída
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Texto salvo em: {output_path}")
        except Exception as e:
            print(f"Erro ao salvar arquivo: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Extrai texto de imagens usando OCR')
    parser.add_argument('images', nargs='+', help='Caminho(s) para a(s) imagem(ns)')
    parser.add_argument('-o', '--output', help='Arquivo de saída para o texto')
    parser.add_argument('-l', '--language', default='por', help='Idioma para OCR (padrão: por)')
    parser.add_argument('--no-preprocess', action='store_true', 
                       help='Desabilita pré-processamento da imagem')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Mostra informações detalhadas')
    
    args = parser.parse_args()
    
    # Verifica se as imagens existem
    valid_images = []
    for img_path in args.images:
        if os.path.exists(img_path):
            valid_images.append(img_path)
        else:
            print(f"Aviso: Imagem não encontrada: {img_path}")
    
    if not valid_images:
        print("Nenhuma imagem válida encontrada!")
        return
    
    # Inicializa o extrator OCR
    extractor = OCRExtractor(language=args.language)
    
    # Processa as imagens
    all_text = []
    
    for i, img_path in enumerate(valid_images, 1):
        if args.verbose:
            print(f"\n--- Processando imagem {i}/{len(valid_images)}: {img_path} ---")
        
        text = extractor.extract_text_from_image(img_path, not args.no_preprocess)
        
        if args.verbose:
            print(f"Texto extraído:\n{text}\n")
        
        all_text.append(f"=== IMAGEM {i}: {img_path} ===\n{text}\n")
    
    # Combina todo o texto
    combined_text = "\n".join(all_text)
    
    # Salva ou exibe o resultado
    if args.output:
        extractor.save_text_to_file(combined_text, args.output)
    else:
        print("\n" + "="*50)
        print("TEXTO EXTRAÍDO DAS IMAGENS:")
        print("="*50)
        print(combined_text)

if __name__ == "__main__":
    main()