# Comparacao de Desempenho: Processamento de Arquivo com Threads

Este projeto implementa duas abordagens para processar um arquivo linha por linha e comparar o desempenho entre uma execucao **single-thread** e **multi-thread**.

📌 **Arquivos do projeto**:

- `uma.py`: Processamento **sequencial** (apenas uma thread).
- `multi.py`: Processamento **paralelo** com **10 threads**.
- `comparador.py`: Executa ambos os scripts e compara o tempo de execucao.

---

## 👥 Requisitos

- **Python 3.8+** instalado
- **Arquivo de texto (`texto.txt`)** para processamento

Caso precise instalar dependencias, rode:

```sh
pip install -r requirements.txt
```

_(Este projeto nao possui bibliotecas externas, mas essa etapa e util para projetos futuros.)_

---

## 🚀 Como Executar

### 1️⃣ **Rodar os scripts separadamente**

Para testar cada abordagem, execute:

```sh
python uma.py
```

```sh
python multi.py
```

### 2️⃣ **Comparar desempenho**

Para rodar ambos e comparar a performance:

```sh
python comparador.py
```

Isso exibira:

- **Hora de inicio e fim** de cada execucao.
- **Tempo total de processamento** para cada abordagem.

---

## 📊 Exemplo de Saida

```
📌 Iniciando uma.py as 10:35:22.525833
👌 Finalizado uma.py as 10:35:22.670286
⏳ Duracao total: 0.1425 segundos

📌 Iniciando multi.py as 10:35:22.672288
👌 Finalizado multi.py as 10:35:22.834911
⏳ Duracao total: 0.1626 segundos

📊 Comparacao de Desempenho:
🟢 Execucao unica (uma thread): 0.1425 segundos
🔴 Execucao multi-thread (10 threads): 0.1626 segundos
```

⚠️ **Observacao**:  
O multi-thread pode ser **mais lento devido ao GIL do Python** e ao **overhead das threads**. Para melhor desempenho, pode-se usar **multiprocessing** ao inves de threads.

---

## 🔧 Possiveis Melhorias

💪 **Implementar `multiprocessing` para bypassar o GIL**  
💪 **Testar com diferentes numeros de threads** (`max_workers=5, 20, etc.`)  
💪 **Usar leitura por chunks para arquivos muito grandes**

---

## 🏆 Conclusao

Este projeto ajuda a entender como **multi-threading pode nao ser sempre mais rapido** no Python, especialmente em tarefas **CPU-bound** (como contagem de palavras). A experimentacao pode levar a uma abordagem mais eficiente dependendo do caso de uso.

🚀 **Divirta-se testando e otimizando!**

---

## 👨‍💻 Autor

Desenvolvido por [João](https://github.com/joaopalmasbr) e .[Peralta](https://github.com/Emmanuelperalta8)
