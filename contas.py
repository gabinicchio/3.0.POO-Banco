import abc #importando método abstrato por causa do decorador


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None: # função inicializar com tipagem
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod   # decorador
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float: # type: ignore
        self.saldo += valor  #manipulando o saldo
        self.detalhes(f'(DEPÓSITO {valor})')  #criando 'msg' para aparecer em detalhes

    def detalhes(self, msg: str = '') -> None: #função para exibir na tela a atualização do saldo
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor  # Serve para checar o valor depois do saque

        if valor_pos_saque >= 0:  # Verificando se o valor de saque é maior ou igual a 0, limitando.
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})') #criando 'msg' de detalhes de Conta
            return self.saldo

        print('Não foi possível sacar o valor desejado') #Mostrando que o saque não pode ser feito
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int,
        saldo: float = 0, limite: float = 0
    ): #adiciona o limite
        super().__init__(agencia, conta, saldo) # vai herdar da superclasse
        self.limite = limite #foi criado por causa da ContaCorrente

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo: #Ele permite sacar mesmo estando negativo
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':  # Uso isso para testar o código dentro desse módulo e quando o módulo for importado o código não será executado
    cp1 = ContaPoupanca(111, 222) #cp = conta poupanca
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(12)
    print('##')