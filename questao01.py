def criar_pessoa(nome: str, idade: int, id: int) -> dict:
  return {
      "id": id,
      "nome": nome,
      "idade": idade
  }

p1 = criar_pessoa("Luis", 28, 1)
p2 = criar_pessoa("Henrique", 24, 2)
p3 = criar_pessoa("Veras", 30, 3)

print(p1)
print(p2)
print(p3)