# Porcentagens de erros
# Foram contabilizados os erros no código de alunos iniciando em programação com o objetivo de identificar quais são as maiores dificuldades. Os resultados desse estudo foram armazenados em um dicionário, como o mostrado a seguir (atenção: este é apenas um exemplo):
#     {
#         'Erro de indentação': 493,
#         'Erro de parênteses': 1102,
#         'Variável inexistente': 405,
#     }
# Faça uma função que recebe um dicionário de resultados, como o mostrado acima, e devolve um novo dicionário com as porcentagens de cada erro.
# A saída esperada para o exemplo acima é o dicionário:
#     {
#         'Erro de indentação': 24.65,
#         'Erro de parênteses': 55.1,
#         'Variável inexistente': 20.25,
#     }
# O nome da sua função deve ser 'calcula_porcentagens'.

def calcula_porcentagens (issues):
    # Conta o total de ocorrências
    total_occurreces = sum(issues.values())
    
    # Dicionário de ocorrências em porcentagem
    occurrence_percentage = {}
    
    # Contabiliza para o dicionário as ocorrências em porcentagem
    for issue, occurrence in issues.items():
        occurrence_percentage[issue] = occurrence / total_occurreces * 100
        
    return occurrence_percentage

# Feedback do professor:
# "muito bom"
