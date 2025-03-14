from translate import Translator
import os
from PyPDF2 import PdfReader

   # Configura o tradutor
translator = Translator(to_lang="pt")

def traduzir_texto(texto, idioma_origem='en', idioma_destino='pt'):
       try:
           traducao = translator.translate(texto)
           return traducao
       except Exception as e:
           print(f"Erro ao traduzir: {e}")
           return texto

def traduzir_arquivo(caminho_arquivo, idioma_origem='en', idioma_destino='pt'):
       try:
           # Verifica o tipo de arquivo
           if caminho_arquivo.endswith('.txt'):
               with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                   texto = arquivo.read()
           elif caminho_arquivo.endswith('.pdf'):
               leitor = PdfReader(caminho_arquivo)
               texto = ''.join([pagina.extract_text() for pagina in leitor.pages])
           elif caminho_arquivo.endswith('.docx'):
               from docx import Document
               documento = Document(caminho_arquivo)
               texto = '\n'.join([paragrafo.text for paragrafo in documento.paragraphs])
           else:
               print("Formato de arquivo não suportado.")
               return

           # Traduz o texto
           texto_traduzido = traduzir_texto(texto, idioma_origem, idioma_destino)

           # Salva o texto traduzido em um novo arquivo
           nome_arquivo, extensao = os.path.splitext(caminho_arquivo)
           caminho_saida = f"{nome_arquivo}_traduzido{extensao}"
           with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
               arquivo_saida.write(texto_traduzido)

           print(f"Tradução concluída! Arquivo salvo em: {caminho_saida}")
       except Exception as e:
           print(f"Erro ao processar o arquivo: {e}")

   # Caminho do arquivo PDF
caminho_do_livro = r'C:\Users\laiane.pereira\Desktop\pag23.pdf'

   # Traduzir o arquivo
traduzir_arquivo(caminho_do_livro)