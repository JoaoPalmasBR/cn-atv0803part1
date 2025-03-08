import subprocess
import time
from datetime import datetime

def executar_script(nome_arquivo):
    """Executa um script Python e mede seu tempo de execução"""
    hora_inicio = datetime.now()
    print(f"\n📌 Iniciando {nome_arquivo} às {hora_inicio.strftime('%H:%M:%S.%f')}")

    inicio = time.time()
    resultado = subprocess.run(["python", nome_arquivo], capture_output=True, text=True)
    fim = time.time()

    hora_fim = datetime.now()
    duracao = fim - inicio

    print(f"\n✅ Finalizado {nome_arquivo} às {hora_fim.strftime('%H:%M:%S.%f')}")
    print(f"⏳ Duração total: {duracao:.4f} segundos\n")
    
    return duracao, resultado.stdout

# Executando os dois scripts e medindo o tempo
tempo_uma, saida_uma = executar_script("uma.py")
tempo_multi, saida_multi = executar_script("multi.py")

# Exibindo o comparativo de desempenho
print("📊 Comparação de Desempenho:")
print(f"🟢 Execução única (uma thread): {tempo_uma:.4f} segundos")
print(f"🔴 Execução multi-thread (10 threads): {tempo_multi:.4f} segundos")

# Mostra o resultado dos dois scripts (opcional)
# print("\n🔹 Saída do script 'uma.py':\n", saida_uma)
# print("\n🔹 Saída do script 'multi.py':\n", saida_multi)

aluno1 = "João Antonio"
aluno2 = "Emmanuel Peralta"
print(f"⏳ Atividade Aula 08/03/2025: {aluno1} e {aluno2}")
print(f"-----------------------------------------------")
