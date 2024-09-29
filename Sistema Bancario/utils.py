from datetime import datetime

def gerar_data_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M")
