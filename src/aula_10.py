from datetime import date,time,datetime
def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%y'))

def trabalhando_com_time():
    horario = time(hour=15,minute=18,second=30)
    horario_str = horario.strftime('%H:%M:%S')

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y  %H:%M:%S'))
    print(data_atual.strftime('%c'))



if __name__ == "__main__":
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()