import os
import zipfile
import tempfile
import glob
from PyPDF2 import PdfMerger

# Local do ZIP
zip_files = glob.glob('zip/*.zip')

if not zip_files:
    print("Nenhum arquivo .zip encontrado na pasta zip/")
    exit(1)

# Pega o primeiro ZIP encontrado
zip_path = zip_files[0]
print(f"Usando ZIP: {zip_path}")

# Nome do PDF de saída
output_pdf = 'output/saida_unificada.pdf'

# Cria um diretório temporário
with tempfile.TemporaryDirectory() as tmpdirname:
    print(f"Extraindo para {tmpdirname}...")

    # Extrai o ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(tmpdirname)

    # Localiza todos os PDFs
    pdfs_encontrados = []
    for root, dirs, files in os.walk(tmpdirname):
        for file in files:
            if file.lower().endswith('.pdf'):
                full_path = os.path.join(root, file)
                pdfs_encontrados.append(full_path)

    print(f"{len(pdfs_encontrados)} PDFs encontrados.")

    # Ordena os PDFs (opcional: ordem alfabética)
    pdfs_encontrados.sort()

    # Une os PDFs
    merger = PdfMerger()
    for pdf in pdfs_encontrados:
        print(f"Adicionando: {pdf}")
        merger.append(pdf)

    # Cria pasta de saída se não existir
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

    merger.write(output_pdf)
    merger.close()

    print(f"\nPDF unificado gerado: {output_pdf}")

    # Kelvin Kauan Melo Mattos 