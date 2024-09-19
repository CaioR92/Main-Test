class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco): #atributos
        self.nome = nome
        self.__cpf = cpf #atributos privados são acessados apenas dentro da própria classe (outros métodos da classe podem acessá-lo)
        self.data_nascimento = data_nascimento
        self.endereco = endereco
    
    def criar_conta(self): #ações #métodos privados são acessados apenas dentro da própria classe (outros métodos da classe podem acessá-lo)
        self.nro_conta
        self.agencia
        self.usuario[cpf]
        if self.__validar_usuario()
        
    def __validar_usuario(self, usuario, cpf):
        
    def sacar(self, conta):
        
    def ver_extrato(self, conta):
        
    def depositar(self, conta):
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
        
# objeto #classe -> #instanciamos um objeto 
u1 = Usuario(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)

# setter
# getter
# @property - usa método como atributo
# Solid = 1 responsabilidade por função

