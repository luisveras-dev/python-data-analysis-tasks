import pandas as pd

def exportar_csv(pessoas: list, nome_arquivo: str):
  df = pd.DataFrame(pessoas)
  df.to_csv(nome_arquivo, index=False, encoding='utf-8')

resultado_q2 = [
    {'id': 1, 'nome': 'Marcos', 'idade': 28, 'gostos': ['Música', 'Futebol']},
    {'id': 2, 'nome': 'Ana', 'idade': 24, 'gostos': ['Leitura', 'Cinema']},
    {'id': 3, 'nome': 'Carlos', 'idade': 30, 'gostos': ['Viagem']},
    {'id': 4, 'nome': 'Julia', 'idade': 22, 'gostos': ['Dança', 'Esportes']},
    {'id': 5, 'nome': 'Pedro', 'idade': 27, 'gostos': ['Tecnologia', 'Culinária']}
]

nome_do_arquivo_csv = "pessoas.csv"

exportar_csv(resultado_q2, nome_do_arquivo_csv)

print(f"Arquivo '{nome_do_arquivo_csv}' foi criado com sucesso.")