def Relatorio_Incidentes():
    erro = 0
    erro_critical = 0
    erro_totais = erro + erro_critical
    
    try:
        with open ('server_logs.txt', 'r') as arquivo:
            for linha in arquivo:
                if '[ERROR]' in linha:
                    erro += 1
                elif '[CRITICAL]' in linha:
                    erro_critical += 1
    except FileNotFoundError:
            print("Erro: O arquivo de logs não foi encontrado")
            return
    erro_totais = erro + erro_critical
    with open ('resumo.txt', 'w') as arquivo_saida:
        texto_relatorio = (f"""Relatório de Incidentes
                                    Erros encontrados: {erro}
                                    Críticos encontrados: {erro_critical}
                                    Total de de problemas : {erro_totais}""")
        arquivo_saida.write(texto_relatorio)

Relatorio_Incidentes()   

            
