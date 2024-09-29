from datetime import datetime
import utils

class Historico: #init + adicionar transaçoes em self.transacoes + atributo transacoes retorna transacoes
    def __init__(self):
        self.__transacoes = []  #Lista vazia; armazena instância criadas da classe
    
    @property #getter    
    def transacoes(self):
        return self.__transacoes
        
    def adicionar_transacao(self, transacao): #precisa de um append para __transacoes; dict
        self.__transacoes.append({'Tipo de Transação': transacao.__class__.__name__, #retorna a o nome da classe a qual o objeto transacao pertence com string
                    'Valor da Transação': transacao.valor,
                    'Data da Transação': utils.gerar_data_atual()})
