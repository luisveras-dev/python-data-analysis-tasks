def criar_pessoa(nome: str, idade: int, id: int) -> dict:
  return {
      "id": id,
      "nome": nome,
      "idade": idade
  }

def adicionar_gostos(pessoas: list, gostos: list) -> list:
  gostos_map = {gosto['id']: gosto['gostos'] for gosto in gostos}
  
  pessoas_processadas = []
  
  for pessoa in pessoas[:5]:
    pessoa_id = pessoa['id']
    if pessoa_id in gostos_map:
      pessoa['gostos'] = gostos_map[pessoa_id]
      pessoas_processadas.append(pessoa)
      
  return pessoas_processadas

pessoas = [
    criar_pessoa("Luis", 28, 1),
    criar_pessoa("Henrique", 24, 2),
    criar_pessoa("Veras", 30, 3),
    criar_pessoa("Araújo", 22, 4),
    criar_pessoa("Maria", 27, 5),
    criar_pessoa("Fátima", 26, 6)
]

gostos = [
    {"id": 1, "gostos": ["Cubo mágico", "Futebol"]},
    {"id": 2, "gostos": ["Academia", "Cinema"]},
    {"id": 3, "gostos": ["Viagem", "Namorar"]},
    {"id": 4, "gostos": ["Estudar", "Esportes"]},
    {"id": 5, "gostos": ["Maquiagem", "Comer"]},
    {"id": 6, "gostos": ["Moda"]}
]

resultado = adicionar_gostos(pessoas, gostos)

print(resultado)