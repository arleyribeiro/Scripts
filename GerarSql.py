#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#OBSERVACAO o primeiro atributo deve ser a chave primaria da tabela para ser usado como identificador para atualização
#Formato do arquivo de entrada
#Nome da tabela
#atributo1 valor1
#atributo2 valor2
#atributo3 valor3
#quebra de linha
#Nome da tabela
#atributo1 valor1
#atributo2 valor2
#quebra de linha

def Insert(table, atributos, valores):    
    query = "INSERT INTO "+ table +" (\n\t\t" + ',\n\t\t'.join(atributos) + ")\nVALUES (\n\t\t@" + ',\n\t\t@'.join(valores) + ");\nSELECT SCOPE_IDENTITY();"    
    print(query)

def Select(table, atributos, valores):    
    query = "SELECT\n"
    tamanho = len(atributos)
    for i in range(0, tamanho):
        query = query +"\t"+ atributos[i] + " as " + valores[i]
        if(i <= (tamanho-2)):
            query = query + ",\n"    
    query = query + "\nFROM " + table + ";"
    print(query)

def Update(table, atributos, valores):    
    query = "UPDATE " + table + " SET\n"
    tamanho = len(atributos)
    for i in range(0, tamanho):
        query = query +"\t"+ atributos[i] + " = @" + valores[i]
        if(i <= (tamanho-2)):
            query = query + ",\n"    
    query = query + "\nWHERE " + atributos[0] + " = @" + valores[0]  +";"
    print(query)

table = ""
atributos = []
valores = []
_valores = []

with open("C:\\Users\\Dell\\Desktop\\"+ sys.argv[1], "r") as openfileobject:
    for line in openfileobject:
        table = line[:-1]
        atributos = []
        valores = []
        _valores = []
        for line2 in openfileobject:
            if(line2 == '\n'):
                break
            palavras = line2.split(" ")
            atributos.append(palavras[0])
            valores.append(palavras[1][:-1])
        Select(table, atributos, valores)
        print()
        Insert(table, atributos, valores)
        print()
        Update(table, atributos, valores)


