from Src.fileHelper import (_get_gabarito, _get_candidatos)
from Src.classification import (_classificator)

gabarito = _get_gabarito("gabarito")
candidatos, excecoes = _get_candidatos("candidatos")

print("\n=== GABARITO ===")

for i, questao in enumerate(gabarito, start=1):
    print(f"Questão {i:02d}: {questao}")

print("=" * 16)

print("=" * 21)
print("...📃Processando📃...")
print("=" * 21)

classificados = _classificator(candidatos, gabarito)
print("Classificação finalizada, deseja consultar as notas? [s/n]")
resposta = input("> ").strip()

if(resposta.lower() == 's'):
    for candidato in classificados:
        print("=" * 5)
        print(f"ID: {candidato[0]} \n Nome candidato: {candidato[1]} \n Nota Final: {candidato[2]}")
        print("=" * 5)

