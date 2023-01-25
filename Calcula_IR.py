def calculadora_ir(salario_bruto):
    # Tabela de alíquotas e faixas do imposto de renda
    tabela_ir = [
        {"faixa": (0, 1903.98), "aliquota": 0, "deducao": 0},
        {"faixa": (1903.99, 2826.65), "aliquota": 7.5, "deducao": 142.80},
        {"faixa": (2826.66, 3751.05), "aliquota": 15, "deducao": 354.80},
        {"faixa": (3751.06, 4664.68), "aliquota": 22.5, "deducao": 636.13},
        {"faixa": (4664.69, float("inf")), "aliquota": 27.5, "deducao": 869.36},
    ]
    # Calcular o imposto de renda
    imposto = 0
    for faixa in tabela_ir:
        if salario_bruto > faixa["faixa"][0] and salario_bruto <= faixa["faixa"][1]:
            imposto = (salario_bruto * faixa["aliquota"]) / 100 - faixa["deducao"]
            break
    return imposto

# Testando a função
salario_bruto = float(input("Informe o seu salário bruto: "))
imposto = calculadora_ir(salario_bruto)
print(f"O imposto de renda devido é de R$ {imposto:.2f}")
