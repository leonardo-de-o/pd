# Definindo as variáveis
saldo = 500.00
juros = 0.01

# Calculando o saldo após três meses de juros
saldo += saldo * juros
saldo += saldo * juros
saldo += saldo * juros

# Imprimindo o saldo final
print("Saldo após três meses: ", saldo)