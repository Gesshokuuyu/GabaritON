from pathlib import Path

dirBase = "./storage"

def _get_gabarito(file:str):
    nomeArquivo = Path(dirBase) / f"{file}.txt"

    arquivo = Path(nomeArquivo)
    if(not arquivo.exists()):
        print(f"Gabarito não encontrado no caminho {arquivo}.")
        return False
    
    gabaritoBase = arquivo.read_text(encoding="utf-8").strip()

    gabaritoList = gabaritoBase.split(',')

    if(len(gabaritoList) < 20):
        print("O gabarito deve ter ao menos 20 questões para ser considerado válido.")
        return False

    return gabaritoList
    

