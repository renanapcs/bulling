#!/usr/bin/env python3
"""
Script de Download das Cartilhas
===============================
Script para facilitar o download das cartilhas sobre bullying escolar
"""

import os
import shutil
from pathlib import Path

def create_download_package():
    """Cria um pacote de download com todas as cartilhas"""
    
    # Cria pasta de download
    download_dir = Path("download_cartilhas")
    download_dir.mkdir(exist_ok=True)
    
    # Arquivos para incluir no download
    files_to_copy = [
        "Cartilha_Bullying_Escolar.pdf",
        "Cartilha_Bullying_Melhorada.pdf",
        "README.md",
        "requirements.txt"
    ]
    
    print("📦 Criando pacote de download...")
    
    # Copia os arquivos
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, download_dir)
            print(f"✅ Copiado: {file}")
        else:
            print(f"❌ Arquivo não encontrado: {file}")
    
    # Cria arquivo de instruções
    instructions = """# 📚 Instruções de Download - Cartilhas sobre Bullying Escolar

## 📄 Arquivos Incluídos

1. **Cartilha_Bullying_Escolar.pdf** - Versão básica (5.9 KB)
2. **Cartilha_Bullying_Melhorada.pdf** - Versão melhorada (7.3 KB)
3. **README.md** - Documentação completa
4. **requirements.txt** - Dependências Python (se quiser executar os scripts)

## 🖨️ Como Usar

1. **Para impressão:** Abra qualquer um dos PDFs e imprima
2. **Recomendação:** Use a versão "Melhorada" para distribuição
3. **Formato:** A4, orientação retrato
4. **Qualidade:** Alta resolução para impressão

## 📱 Para Dispositivos Móveis

- Os PDFs podem ser visualizados em tablets e smartphones
- Recomendado para leitura: Adobe Reader, Google PDF Viewer
- Para impressão: Use aplicativos de impressão móvel

## 🎯 Público-Alvo

- Crianças em idade escolar
- Pais e educadores
- Escolas e instituições educacionais
- Projetos de conscientização sobre bullying

## 📞 Suporte

Para dúvidas sobre o conteúdo ou uso das cartilhas, consulte o README.md

---
**Feito com ❤️ para ajudar crianças a entenderem e combaterem o bullying escolar**
"""
    
    with open(download_dir / "INSTRUÇÕES.txt", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print(f"✅ Pacote de download criado em: {download_dir.absolute()}")
    
    # Lista arquivos no pacote
    print("\n📁 Arquivos no pacote de download:")
    for file in download_dir.iterdir():
        size = file.stat().st_size
        size_kb = size / 1024
        print(f"  📄 {file.name} ({size_kb:.1f} KB)")
    
    return download_dir

def create_zip_package():
    """Cria um arquivo ZIP com as cartilhas"""
    import zipfile
    
    zip_filename = "Cartilhas_Bullying_Escolar.zip"
    
    print(f"\n📦 Criando arquivo ZIP: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Adiciona as cartilhas
        cartilhas = [
            "Cartilha_Bullying_Escolar.pdf",
            "Cartilha_Bullying_Melhorada.pdf"
        ]
        
        for cartilha in cartilhas:
            if os.path.exists(cartilha):
                zipf.write(cartilha)
                print(f"✅ Adicionado ao ZIP: {cartilha}")
        
        # Adiciona README
        if os.path.exists("README.md"):
            zipf.write("README.md")
            print(f"✅ Adicionado ao ZIP: README.md")
    
    zip_size = os.path.getsize(zip_filename) / 1024
    print(f"✅ Arquivo ZIP criado: {zip_filename} ({zip_size:.1f} KB)")
    
    return zip_filename

def main():
    """Função principal"""
    print("="*60)
    print("📚 CARTILHAS SOBRE BULLYING ESCOLAR - DOWNLOAD")
    print("="*60)
    
    # Verifica se as cartilhas existem
    cartilhas = [
        "Cartilha_Bullying_Escolar.pdf",
        "Cartilha_Bullying_Melhorada.pdf"
    ]
    
    missing_files = []
    for cartilha in cartilhas:
        if not os.path.exists(cartilha):
            missing_files.append(cartilha)
    
    if missing_files:
        print("❌ Arquivos não encontrados:")
        for file in missing_files:
            print(f"  - {file}")
        print("\nExecute primeiro o script de criação das cartilhas.")
        return False
    
    print("✅ Todas as cartilhas encontradas!")
    print("\n📄 Cartilhas disponíveis:")
    for cartilha in cartilhas:
        size = os.path.getsize(cartilha) / 1024
        print(f"  📖 {cartilha} ({size:.1f} KB)")
    
    # Cria pacote de download
    download_dir = create_download_package()
    
    # Cria arquivo ZIP
    zip_file = create_zip_package()
    
    print("\n" + "="*60)
    print("🎉 DOWNLOAD PREPARADO COM SUCESSO!")
    print("="*60)
    print(f"📁 Pasta de download: {download_dir.absolute()}")
    print(f"📦 Arquivo ZIP: {zip_file}")
    print("\n📋 Opções de download:")
    print("1. 📁 Pasta completa com todos os arquivos")
    print("2. 📦 Arquivo ZIP compactado")
    print("3. 📄 Download individual dos PDFs")
    
    print("\n🌐 Para compartilhar:")
    print("• Faça upload da pasta ou ZIP para um serviço de nuvem")
    print("• Use GitHub para hospedar o projeto")
    print("• Compartilhe os PDFs diretamente")
    
    return True

if __name__ == "__main__":
    main()