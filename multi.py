import threading
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Mutex para sincronizar a saída
mutex = threading.Lock()

def processar_linha(linha, numero_linha):
    """Processa a linha contando palavras e caracteres"""
    num_palavras = len(linha.split())
    num_caracteres = len(linha)
    
    # Bloqueia a exibição para evitar conflitos
    with mutex:
        print(f"Linha {numero_linha}: {num_palavras} palavras, {num_caracteres} caracteres")

def processar_arquivo(nome_arquivo):
    """Lê e processa o arquivo linha por linha usando múltiplas threads"""
    hora_inicio = datetime.now()
    print(f"\n📌 Início da leitura: {hora_inicio.strftime('%H:%M:%S.%f')}")

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()  # Carrega todas as linhas na memória

    # Criar um pool de 10 threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        for numero_linha, linha in enumerate(linhas, start=1):
            executor.submit(processar_linha, linha.strip(), numero_linha)

    hora_fim = datetime.now()
    duracao = hora_fim - hora_inicio

    print(f"\n✅ Fim da leitura: {hora_fim.strftime('%H:%M:%S.%f')}")
    print(f"⏳ Duração total: {duracao}")

# Executar o processamento
aluno1 = "João Antonio"
aluno2 = "Emmanuel Peralta"
arquivo_teste = "HAMLET.txt"  # Substitua pelo seu arquivo de entrada
processar_arquivo(arquivo_teste)


print(f"⏳ Atividade Aula 08/03/2025: {aluno1} e {aluno2}")
print(f"📂 Arquivo de entrada: {arquivo_teste}")
print(f"-----------------------------------------------")
