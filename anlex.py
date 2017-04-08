# coding:utf-8
import sys
import re


def converte_simbolos():
    """Substitui simbolos por números"""
    pass

def exibe_tokens(lista):
    for i in lista:
        print i
try:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
except Exception as e:
    arquivo = open("teste2.c", "r")


token = ""
numerico = ""
estado = 0
separadores = [';', '[', ']', ')', '(', ')', '{', '}', ',', '=', '.']
sep_num = [';',',', '=']
operadores = ['-', '+', '/', '*']
op_log = ['&&', '||', '>', '<', '>=', '<=', '==', '!=']
lista_erros = []
token_geral = []
linha = 0
final = ""
for i in arquivo:
    linha = linha + 1
    final = ""
    for k in i:

        if estado is 0:
            """Define o estado inicial"""
            if re.match(r"([A-Za-z_])", k):
                estado = 1  # Identificador
            if re.match(r"[0-9]", k):

                estado = 2  # Constante Numerica
            if k in operadores:
                token = token + k + "|"
                estado = 0

        if estado is 1:
            """Valida Identificador"""
            if re.match(r"([A-za-z0-9])", k):
                token = token + k
            if k in separadores or re.match(r"(\s)", k):
                """Lista com separadores"""
                estado = 0
                #print "Valor presente em k:" , k
                token_geral.append(["Iden ",token,"l: "+str(linha)])
                token_geral.append(["Sep ",k,"l:"+str(linha)])
                #token = "|Iden, " + token + ", L:" + \
                #str(linha) + gera_marcador(k) + ", L:" + str(linha) + "|"
                token = ""

        if estado is 2:
            """Estado de indentificacao de constante numerica"""
            if re.match(r"[\w.]", k):
                numerico = numerico + k
            if k in sep_num or k in operadores:

                if(re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)):
                    valor = re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)
                    #print "numerico ",numerico
                    if valor is not None:
                        #token = token + "Num, " + valor.group() + ",L:" + str(linha) + gera_marcador(k)
                        token_geral.append(["Num",valor.group(),"l:"+str(linha)])
                        token_geral.append(["Sep",k,"l:"+str(linha)])
                        estado = 0
                        numerico = ""
                else:
                    lista_erros.append([numerico, linha])
                    numerico = ""
            else:
                if k in sep_num:
                    "Armazena token de separadores"
                    token_geral.append(["Sep",k,"l:"+str(linha)])


#formata_tokens(token)
print "Identificadores ",token_geral
exibe_tokens(token_geral)
print "Erros ",lista_erros
# print "Erro", lista_erros
