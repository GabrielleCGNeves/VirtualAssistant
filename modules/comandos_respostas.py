"""
Módulo comandos_respostas
Define comandos e respostas usados pela assistente virtual.
"""

# Comandos definidos por categoria
COMANDOS = {
    "funcoes": [
        "o que você pode fazer", "o que você faz", "funcionalidades",
        "o que você sabe fazer", "o que mais você sabe fazer"
    ],
    "horas": [
        "que horas são", "hora", "hora agora", 
        "que horas são agora", "qual é a hora"
    ],
    "data": [
        "que dia é hoje", "que dia é", "que dia hoje"
    ],
    "teste": [
        "xablau", "aoba", "como vai"
    ],
    "adicionar_lista_compras": [
        "adicionar na lista de compras ", "adicionar à lista de compras ", 
        "colocar na lista de compras ", "incluir na lista de compras "
    ]
}

# Respostas da assistente organizadas por contexto
RESPOSTAS = {
    "funcionalidades": (
        "falar as horas, falar a data, falar testes, criar lista de compras, criar lista de lembretes"
    ),
    "conclusao": [
        "Ok!", "Feito!", "Concluído!", 
        "Tudo certo!", "Terminado!"
    ],
    "perguntas": [
        "Como posso ajudar?", "Ok, vamos lá!", 
        "Certo, é só falar!"
    ],
    "agradecimento": [
        "Se precisar é só chamar!", "Qualquer coisa estou aqui!"
    ],
    "despedida": [
        "Até mais!", "Até breve!", 
        "Até logo!", "Até a próxima"
    ]
}

# Acessos diretos para comandos e frases específicos
FUNCOES = COMANDOS["funcoes"]
HORAS = COMANDOS["horas"]
DATA = COMANDOS["data"]
TESTE = COMANDOS["teste"]
ADICIONAR_LISTA_COMPRAS = COMANDOS["adicionar_lista_compras"]

FUNCIONALIDADES = RESPOSTAS["funcionalidades"]
RESPOSTAS_CONCLUSAO = RESPOSTAS["conclusao"]
PERGUNTAS = RESPOSTAS["perguntas"]
RESPOSTAS_AGRADECIMENTO = RESPOSTAS["agradecimento"]
DESPEDIDA = RESPOSTAS["despedida"]
