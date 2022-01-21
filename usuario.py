class Usuario:
    # Atributos de clase - Definidos en clase
    bank_name = "Banco Dojo"
    # Metodo"__init__"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0 
    # Metodo "hacer deposito"
    def hacer_deposito(self, amount):
        self.account_balance += amount
    # Metodo "hacer retiro"
    def hacer_retiro(self, amount):
        self.account_balance -= amount
    # Metodo "mostrar el balance de usuario"
    def mostrar_balance_usuario(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transferir_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)

#Crear 3 instancias de la clase Usuario
vizcarra = Usuario("Martin Vizcarra", "martin@python.com")
toledo = Usuario("Alejandro Toledo", "alejandro@python.com")
fujimori = Usuario("Keiko Fujimori", "keiko@python.com")

vizcarra.hacer_deposito(8000)
vizcarra.hacer_deposito(4400)
vizcarra.hacer_deposito(5500)
vizcarra.hacer_retiro(1800)
vizcarra.mostrar_balance_usuario()

toledo.hacer_deposito(50000)
toledo.hacer_deposito(1000)
toledo.hacer_retiro(100)
toledo.hacer_retiro(1800)
toledo.mostrar_balance_usuario()

fujimori.hacer_deposito(10500)
fujimori.hacer_retiro(1200)
fujimori.hacer_retiro(3000)
fujimori.hacer_retiro(185)
fujimori.mostrar_balance_usuario()

# BONUS - Transferir dinero
vizcarra.transferir_dinero(fujimori, 1100)
vizcarra.mostrar_balance_usuario()
fujimori.mostrar_balance_usuario()
