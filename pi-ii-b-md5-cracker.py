#IMPORTACAO DAS BIBLIOTECAS
import time
import string
import hashlib
import threading
import itertools
from pytz import timezone
from datetime import datetime

##########################################################################################################################

def getString(length):
    array = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*()_-+=[]{}?/\|><ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Produto cartesiano do alfabeto ​​de entrada.
    # O elemento mais a direita avanca a cada iteracao.
    for senha in itertools.product(array, repeat = length):
        # Devemos utilizar o yield quando ha uma lista muito grande com a qual queremos lidar, 
        # O método .join() pega todos os itens em uma interacao e os une em uma string.
        # O 'return' interrompe a execução, mas 'yield' pausa a execução e continua no mesmo ponto.
        yield "".join(senha)

##########################################################################################################################

def compara(senha, hash2):
    hash1 = open('Arquivo-Hashes.txt', 'r')
    for linha in hash1:
        # O rstrip() remove os caracteres da direita com base no argumento 
        # (uma string que especifica o conjunto de caracteres a ser removido).
        linha = linha.rstrip()
        if hash2 in linha:
            #DATA E HORA FINAIS
            data_e_hora_atuais2 = datetime.now()
            fuso_horario2 = timezone('America/Sao_Paulo')
            data_e_hora_sao_paulo2 = data_e_hora_atuais2.astimezone(fuso_horario2)
            data2 = data_e_hora_sao_paulo2.strftime('%d-%m-%Y')
            hora2 = data_e_hora_sao_paulo2.strftime('%H:%M:%S')
            arq = open('Arquivo-Senhas.txt', 'a')
            arq.write("Hash: " + str(hash2) + "     Senha: " + str(senha) + "\n" +
                      "Data e Hora de Inicio: " + str(data) + "  " + str(hora) +
                      "     Data e Hora de Termino: " + str(data2) + "  " + str(hora2) + "\n\n")
            print("Hash: " + str(hash2) + "     Senha: " + str(senha))
            arq.close()
    hash1.close()

##########################################################################################################################

def quebra_md5(length):
    for senha in getString(length):
        hash2 = (hashlib.md5(senha.encode()).hexdigest())
#        print(str(hash2) + " <-------------> " + str(senha))
        compara(senha, hash2)

##########################################################################################################################

if __name__ == "__main__":

    #DATA E HORA INICIAIS
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data = data_e_hora_sao_paulo.strftime('%d-%m-%Y')
    hora = data_e_hora_sao_paulo.strftime('%H:%M:%S')

    threading.Thread(target=quebra_md5, args=(2, )).start()
    threading.Thread(target=quebra_md5, args=(3, )).start()
#    threading.Thread(target=quebra_md5, args=(4, )).start()
##########################################################################################################################
#FIM
