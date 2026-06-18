from Src.fileHelper import (_get_gabarito)

gabarito = _get_gabarito("gabarito")

print("\n=== GABARITO ===")

for i, questao in enumerate(gabarito, start=1):
    print(f"Questão {i:02d}: {questao}")

print("=" * 16)

print("=" * 21)
print("...📃Processando📃...")
print("=" * 21)




