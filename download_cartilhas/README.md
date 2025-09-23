# 📚 Cartilha sobre Bullying Escolar

Uma cartilha educativa sobre bullying escolar criada baseada em texto manuscrito de uma criança, transformada em material educativo estruturado.

## 📖 Sobre o Projeto

Este projeto foi desenvolvido a partir da análise de texto manuscrito de uma criança sobre bullying escolar. Utilizando técnicas de OCR (Optical Character Recognition), o texto foi extraído e transformado em uma cartilha educativa completa.

## 🎯 Objetivo

Criar material educativo sobre bullying escolar que:
- Mantenha a linguagem e raciocínio infantil
- Seja visualmente atrativo para crianças
- Forneça orientações práticas sobre como lidar com bullying
- Esteja pronto para impressão e distribuição

## 📄 Cartilhas Disponíveis

### 1. Cartilha Básica
- **Arquivo:** `Cartilha_Bullying_Escolar.pdf`
- **Tamanho:** 5.9 KB
- **Características:** Versão simples e direta, formato básico para impressão

### 2. Cartilha Melhorada
- **Arquivo:** `Cartilha_Bullying_Melhorada.pdf`
- **Tamanho:** 7.3 KB
- **Características:** Versão elaborada com elementos visuais, tabelas com emojis e cores

## 📋 Conteúdo da Cartilha

### 🎨 Capa
- Título colorido "CARTILHA BULLYING NA ESCOLA"
- Elementos visuais infantis (coração, círculos coloridos)
- Mensagem "Feito com ❤️ por uma criança"

### 📖 Páginas Internas

**Página 1: O que é Bullying?**
- Definição simples e clara
- Exemplos concretos com emojis:
  - 🚫 Chamar nomes feios
  - 👊 Empurrar ou bater
  - 🚪 Não deixar brincar
  - 💬 Espalhar mentiras
  - 💔 Quebrar coisas

**Página 2: Como identificar o Bullying?**
- Sinais de que a criança está sendo vítima
- O que fazer quando vê bullying acontecer

**Página 3: O que fazer quando acontece Bullying?**
- Para vítimas: Como pedir ajuda
- Para agressores: Como parar e se desculpar
- Para testemunhas: Como ajudar

**Página 4: Vamos fazer da escola um lugar melhor!**
- Ações positivas com emojis
- Contatos para ajuda (pais, professores, Disque 100)

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **OCR:** Tesseract + pytesseract
- **Processamento de Imagem:** OpenCV (headless)
- **Geração de PDF:** ReportLab
- **Manipulação de Imagem:** Pillow
- **Processamento Numérico:** NumPy

## 📁 Estrutura do Projeto

```
/workspaces/bulling/
├── img/                                    # Imagens originais
│   ├── 1.jpeg
│   ├── 2.jpeg
│   ├── 3.jpeg
│   └── 4.jpeg
├── Cartilha_Bullying_Escolar.pdf          # Cartilha básica
├── Cartilha_Bullying_Melhorada.pdf        # Cartilha melhorada
├── ocr_extractor.py                       # Script OCR avançado
├── ocr_simple.py                          # Script OCR simples
├── process_images.py                      # Processamento em lote
├── requirements.txt                       # Dependências Python
├── output.txt                             # Texto extraído das imagens
├── texto_extraido_todas_imagens.txt       # Resultado do processamento
└── README.md                              # Este arquivo
```

## 🚀 Como Usar

### Instalação das Dependências

```bash
# Instalar dependências Python
pip install -r requirements.txt

# Instalar Tesseract OCR (Ubuntu/Debian)
sudo apt update
sudo apt install tesseract-ocr tesseract-ocr-por
```

### Execução dos Scripts

```bash
# Processar uma imagem específica
python ocr_simple.py img/1.jpeg

# Processar múltiplas imagens
python ocr_extractor.py img/*.jpeg -o output.txt

# Processar todas as imagens da pasta
python process_images.py
```

## 📥 Download

### Download Direto dos PDFs

- [Cartilha Básica - Cartilha_Bullying_Escolar.pdf](Cartilha_Bullying_Escolar.pdf)
- [Cartilha Melhorada - Cartilha_Bullying_Melhorada.pdf](Cartilha_Bullying_Melhorada.pdf)

### Clone do Repositório

```bash
git clone https://github.com/seu-usuario/cartilha-bullying-escolar.git
cd cartilha-bullying-escolar
```

## 🖨️ Impressão

As cartilhas estão em formato A4 e prontas para impressão:
- **Formato:** PDF
- **Tamanho:** A4 (210 x 297 mm)
- **Orientação:** Retrato
- **Qualidade:** Alta resolução para impressão

## 📝 Licença

Este projeto é de uso educacional e pode ser distribuído livremente para fins educativos.

## 🤝 Contribuições

Contribuições são bem-vindas! Se você quiser:
- Melhorar o conteúdo da cartilha
- Adicionar novos recursos
- Corrigir problemas
- Sugerir melhorias

Sinta-se à vontade para fazer um fork e enviar um pull request.

## 📞 Contato

Para dúvidas ou sugestões sobre este projeto educacional, entre em contato através das issues do GitHub.

---

**Feito com ❤️ para ajudar crianças a entenderem e combaterem o bullying escolar**

## 📊 Estatísticas do Projeto

- **Imagens processadas:** 4
- **Texto extraído:** ~2.000 caracteres
- **Cartilhas geradas:** 2 versões
- **Páginas por cartilha:** 4 + capa
- **Idioma:** Português (Brasil)
- **Público-alvo:** Crianças em idade escolar