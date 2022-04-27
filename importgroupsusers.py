import csv
import os
from sql import check, inserir, remove

rootpath = os.getcwd()
csvfile = os.path.join(rootpath,'csv/usuariosxgrupos.csv')

cont = 1

with open(csvfile, 'r') as file:
    reader = csv.reader(file, delimiter = ';')
    for linha in reader:
        login = linha[0]
        area = linha[1]
        gerente = linha[2]
        delegar= linha[3]
        campos = (login, area, gerente, delegar,)
        nome = (login, )
        if cont != 1:
            resultcheck = check(nome)
            if resultcheck:
                users_id = resultcheck[0]
                remove(users_id)
            inserir(campos)
        cont = cont+1