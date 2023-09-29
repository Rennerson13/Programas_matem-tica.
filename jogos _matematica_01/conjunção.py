# Criação da tabela verdade, teoria de boole
tabela_verdade = []

for p in [True, False]:
    for q in [True, False]:
        resultado = p and q
        tabela_verdade.append((p, q, resultado))

print("P | Q | P ∧ Q")
print("--|---|------")
for linha in tabela_verdade:
    p, q, resultado = linha
    print(f"{int(p)} | {int(q)} | {int(resultado)}")
