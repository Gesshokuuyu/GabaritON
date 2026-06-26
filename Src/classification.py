from pathlib import Path

def _correction(gabarito:list, question:int, answer:str ):
    valorQuestao = 0.5

    if(gabarito[question] == answer):
        return valorQuestao
    else:
        return 0


def _classificator(candidatos:list, gabarito:list):
    processados = []
    for candidato in candidatos:

        questoes = candidato[2]
        notaCandidato = 0

        for questao, resposta in enumerate(questoes):
            notaCandidato += _correction(gabarito, questao, resposta)

        processados.append([candidato[0], candidato[1], notaCandidato ])

    processados.sort(key=lambda x: (-x[2], x[1]))

    diretorio_atual = Path(__file__).parent.resolve()
    diretorio_destino = (diretorio_atual / "../storage").resolve()
    
    try:
        diretorio_destino.mkdir(parents=True, exist_ok=True)
        arquivo_classificacao = diretorio_destino / "classification.txt"

        with open(arquivo_classificacao, "w", encoding="utf-8") as f:
            f.write("CLASSIFICAÇÃO GERAL DOS CANDIDATOS\n")
            f.write("=" * 60 + "\n")
            f.write(f"{'Pos.':<5} | {'ID':<6} | {'Nome do Candidato':<35} | {'Nota':<5}\n")
            f.write("-" * 60 + "\n")
            
            for posicao, item in enumerate(processados, 1):
                id_cand, nome_cand, nota = item
                f.write(f"{posicao:<4}º | {id_cand:<6} | {nome_cand:<35} | {nota:<5}\n")
                
        print(f"Sucesso! Arquivo de classificação gerado em: {arquivo_classificacao}")
    except PermissionError:
        print(f"Erro de Permissão: O Python não tem autorização para gravar em '{diretorio_destino}'. Verifique os privilégios da pasta.")
    except Exception as e:
        print(f"Ocorreu um erro ao gravar o arquivo de classificação: {e}")

    return processados



