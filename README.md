# OCR Text Extractor

Script Python para extrair texto de imagens usando OCR (Optical Character Recognition) com suporte a múltiplos idiomas e pré-processamento de imagens.

## Instalação

### 1. Instalar dependências Python
```bash
pip install -r requirements.txt
```

### 2. Instalar Tesseract OCR

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por
```

#### Windows:
- Baixe o instalador do Tesseract em: https://github.com/UB-Mannheim/tesseract/wiki
- Instale e adicione ao PATH do sistema

#### macOS:
```bash
brew install tesseract tesseract-lang
```

## Uso

### Uso básico:
```bash
python ocr_extractor.py imagem1.jpg imagem2.png imagem3.jpg
```

### Salvar resultado em arquivo:
```bash
python ocr_extractor.py imagem1.jpg -o texto_extraido.txt
```

### Usar idioma específico:
```bash
python ocr_extractor.py imagem1.jpg -l eng  # Inglês
python ocr_extractor.py imagem1.jpg -l spa  # Espanhol
python ocr_extractor.py imagem1.jpg -l fra  # Francês
```

### Desabilitar pré-processamento:
```bash
python ocr_extractor.py imagem1.jpg --no-preprocess
```

### Modo verbose (mostra detalhes):
```bash
python ocr_extractor.py imagem1.jpg -v
```

## Exemplos

### Processar múltiplas imagens:
```bash
python ocr_extractor.py *.jpg *.png -o todas_as_imagens.txt
```

### Processar com verbose:
```bash
python ocr_extractor.py documento.pdf -v -o texto_do_documento.txt
```

## Funcionalidades

- ✅ Suporte a múltiplos formatos de imagem (JPG, PNG, TIFF, BMP, etc.)
- ✅ Pré-processamento automático para melhor precisão
- ✅ Suporte a múltiplos idiomas
- ✅ Processamento em lote de múltiplas imagens
- ✅ Modo verbose para debug
- ✅ Salvamento automático em arquivo
- ✅ Tratamento de erros robusto

## Idiomas Suportados

- `por` - Português (padrão)
- `eng` - Inglês
- `spa` - Espanhol
- `fra` - Francês
- `deu` - Alemão
- `ita` - Italiano
- E muitos outros...

## Troubleshooting

### Erro "tesseract not found":
- Certifique-se de que o Tesseract está instalado e no PATH
- No Windows, pode ser necessário reiniciar o terminal após instalar

### Baixa precisão do OCR:
- Tente usar `--no-preprocess` para desabilitar pré-processamento
- Verifique se a imagem tem boa qualidade e resolução
- Certifique-se de usar o idioma correto com `-l`

### Imagem não carrega:
- Verifique se o arquivo existe e não está corrompido
- Certifique-se de que o formato é suportado