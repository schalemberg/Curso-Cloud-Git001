def sacar(self, valor: float) -> None:  # inicio do bloco de código

    if self.saldo >= valor:  # inicio do bloco de código if
        self.saldo -= valor
        self.extrato.append(f'Saque: {valor}')

    # fim do bloco de código if

# fim do bloco de código
