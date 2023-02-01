from . categoria_repository import CategoriaRepository

categoria_repository = CategoriaRepository()

def test_get_categoria():
  id = 1

  categoria = categoria_repository.get_categoria(id)

  print(categoria)