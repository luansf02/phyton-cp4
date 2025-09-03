# Projeto Easy Bike
# Integrantes:


# - João Pedro Morra lopes - 565737
# - Luan Shiba Felix - 565541
# - Leandro de Freitas Farias Filho - 566488

# Estruturas de Dados
usuarios = []
bicicletas = []
vistorias = []

# Funções Auxiliares
def buscar(lista: list, chave: str, valor):
   return next((i for i in lista if i[chave] == valor), None)

# Requisitos Funcionais
def cadastrar_usuario(nome: str, email: str):
   if nome.strip() == "":
       print("Nome inválido. Não pode ficar vazio."); return
   for c in nome:
       if c.isdigit():
           print("Nome inválido. Não pode conter números."); return
   if "@" not in email:
       print("Email inválido."); return
   if buscar(usuarios, "email", email):
       print("Email já cadastrado."); return
   usuarios.append({"id": len(usuarios)+1, "nome": nome, "email": email})
   print("Usuário cadastrado!")

def listar_usuarios():
   if not usuarios:
       print("Nenhum usuário foi encontrado."); return
   for u in usuarios:
       print(f"ID:{u['id']} | Nome:{u['nome']} | Email:{u['email']}")

def cadastrar_bicicleta(modelo: str, dono_email: str):
   dono = buscar(usuarios, "email", dono_email)
   if not dono:
       print("O Usuário não foi encontrado."); return
   bicicletas.append({
       "id": len(bicicletas)+1,
       "modelo": modelo,
       "dono": dono_email,
       "status": "Disponível"
   })
   print("A Bicicleta foi cadastrada!")

def listar_bicicletas():
   if not bicicletas:
       print("Nenhuma bicicleta."); return
   for b in bicicletas:
       print(f"ID: {b['id']} | Modelo: {b['modelo']} | Dono: {b['dono']} | Status: {b['status']}")

def acionar_sinistro(bid: int):
   b = buscar(bicicletas, "id", bid)
   if not b: return print("A Bicicleta não foi encontrada.")
   b["status"] = "Sinistro acionado."
   print(f"O Sinistro foi acionado para a Bicicleta: {b['modelo']}")
   return None

def acionar_reparo(bid: int):
   b = buscar(bicicletas, "id", bid)
   if not b: return print("A Bicicleta não foi encontrada.")
   b["status"] = "Em reparo"
   print(f"O Reparo foi acionado para a Bicicleta: {b['modelo']}")
   return None

def validar_foto(bid: int, foto: str):
   b = buscar(bicicletas, "id", bid)
   if not b: return print("A Bicicleta não foi encontrada.")
   if "foto" in foto.lower():
       print(f"A Foto da bicicleta: {b['modelo']} foi validada com sucesso.")
       return None
   else:
       print("Foto inválida.")
       return None

def emitir_relatorio():
   print("\n Relatório Geral.")
   print(f"Usuários: {len(usuarios)} | Bicicletas: {len(bicicletas)} | Vistorias: {len(vistorias)}")
   for b in bicicletas:
       print(f"Bicicleta {b['id']} | Modelo: {b['modelo']} | Dono: {b['dono']} | Status: {b['status']}")

def consultar_status(bid: int):
   b = buscar(bicicletas, "id", bid)
   if not b: return print("Bicicleta não encontrada.")
   print(f"Status da Bicicleta: {b['modelo']}: {b['status']}")
   return None

def feedback_vistoria(bid: int, feedback: str):
   b = buscar(bicicletas, "id", bid)
   if not b: return print("Bicicleta não encontrada.")
   vistorias.append({"bicicleta": bid, "feedback": feedback})
   print(f"Feedback registrado para a Bicicleta: {b['modelo']}: {feedback}")
   return None

# Menu Principal
def menu():
   while True:
       print("""
          - - EASY  BIKE - -          
|        1. Cadastrar Usuário        |
|         2. Listar Usuários         |
|       3. Cadastrar Bicicleta       |
|        4. Listar Bicicletas        |
|        5. Acionar Sinistro         |
|         6. Acionar Reparo          |
|          7. Validar Foto           |
|        8. Emitir Relatório         |
|  9. Consultar Status da Bicicleta  |
| 10. Registrar Feedback de Vistoria |
|              0. Sair               |

""")
       op = input("Opção: ")
       if op == "1": cadastrar_usuario(input("Nome: "), input("Email: "))
       elif op == "2": listar_usuarios()
       elif op == "3": cadastrar_bicicleta(input("Modelo: "), input("Email do dono: "))
       elif op == "4": listar_bicicletas()
       elif op == "5": acionar_sinistro(int(input("ID bicicleta: ")))
       elif op == "6": acionar_reparo(int(input("ID bicicleta: ")))
       elif op == "7": validar_foto(int(input("ID bicicleta: ")), input("Nome da foto: "))
       elif op == "8": emitir_relatorio()
       elif op == "9": consultar_status(int(input("ID bicicleta: ")))
       elif op == "10": feedback_vistoria(int(input("ID bicicleta: ")), input("Feedback: "))
       elif op == "0": break
       else: print("Inválido")

if __name__ == "__main__":
   menu()