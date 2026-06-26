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
    

def _get_candidatos(file: str):
    nomeArquivo = Path(dirBase) / f"{file}.txt"

    if not nomeArquivo.exists():
        print(f"Candidatos não encontrados no arquivo: [{nomeArquivo}].")
        return False
    
    candidatos = []
    excecoes = []
    TOTAL_QUESTOES = 20 

    with open(nomeArquivo, "r", encoding='utf-8') as file:
        for num_linha, linha in enumerate(file, 1):
            linha = linha.strip()
            if not linha:
                continue

            partes = linha.split(',')

            # precisa ter ao menos id e nome
            if len(partes) < 2:
                print(f"Linha {num_linha} inválida (formato incorreto): {linha}")
                excecoes.append(linha)
                continue

            candidato_id = partes[0].strip()
            nome = partes[1].strip()
            
            respostas_brutas = partes[2:]

            respostas_validadas = []
            for i in range(TOTAL_QUESTOES):
                if i < len(respostas_brutas):
                    resposta = respostas_brutas[i].strip()
                    # Se o caractere for vazio, salva como "X" (ou None)
                    respostas_validadas.append(resposta if resposta != "" else "X")
                else:
                    # Se a linha terminou antes das 20 questões, preenche o restante com "X"
                    respostas_validadas.append("X")

            if len(respostas_brutas) != TOTAL_QUESTOES or "X" in respostas_validadas:
                print(f"Aviso: Candidato {nome} (ID: {candidato_id}) possui respostas ausentes ou desalinhadas.")

            candidatos.append([candidato_id, nome, respostas_validadas])

    return candidatos, excecoes

    