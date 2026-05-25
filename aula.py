nota = float(input("Digite a nota: "))

if nota >= 6.0:
    print("Aprovado")

elif nota >= 4.0 and nota < 6.0:
    print("Recuperação")

else:
    print("Reprovado")