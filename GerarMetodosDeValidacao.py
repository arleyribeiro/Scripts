#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

#OBSERVACAO o primeiro atributo deve ser a chave primaria da tabela para ser usado como identificador para atualização
#Formato do arquivo de entrada
#Nome da tabela
#atributo1 tipo valor1
#atributo2 tipo valor2


#"public void ValidarTamanhoDosCampos(StringBuilder parametrosInvalidos, StringBuilder parametrosValores)\n{"

def IfAtributoNuloObrigatorio(atributo):    
    return "\tif (String.IsNullOrEmpty("+ atributo +") || String.IsNullOrWhiteSpace(" + atributo +"))\n\t\tAdicionarParametro(\"" + atributo +"\", " + atributo + ", parametrosInvalidos, parametrosValores);\n\n"

def IfTamanhoInvalido(atributo, tamanho):    
    return "\tif (!String.IsNullOrEmpty("+ atributo +") && !String.IsNullOrWhiteSpace(" + atributo +") && " + atributo +".Length > " + tamanho +")\n\t\tAdicionarParametro(\"" + atributo +"\", " + atributo + ", parametrosInvalidos, parametrosValores);\n\n"

def IfCodigoInvalido(atributo, tamanho):    
    return "\tif (" + atributo +" <= "+ tamanho + ")\n\t\tAdicionarParametro(\"" + atributo +"\", " + atributo + ", parametrosInvalidos, parametrosValores);\n\n"

def IfDateTimeInvalido(atributo):    
    return "\tif (" + atributo +" == default(DateTime))\n\t\tAdicionarParametro(\"" + atributo +"\", " + atributo + ", parametrosInvalidos, parametrosValores);\n\n"

table = ""
atributos = []
valores = []
_valores = []

ValidarTamanhoDosCampos = "public void ValidarTamanhoDosCampos(StringBuilder parametrosInvalidos, StringBuilder parametrosValores)\n{\n"
CamposObrigatorios = "public void ValidarCamposObrigatorios(StringBuilder parametrosInvalidos, StringBuilder parametrosValores){\n"

with open("C:\\Users\\Dell\\Desktop\\"+ sys.argv[1], "r") as openfileobject:
    for line in openfileobject:
        if(line == '\n'):
            break
        palavras = line.split(" ")
        if palavras[1] == "string":
            ValidarTamanhoDosCampos = ValidarTamanhoDosCampos + IfTamanhoInvalido(palavras[0], palavras[2][:-1])
        else:           
            CamposObrigatorios = CamposObrigatorios + IfCodigoInvalido(palavras[0], palavras[2][:-1])
            CamposObrigatorios = CamposObrigatorios + IfAtributoNuloObrigatorio(palavras[0])
    CamposObrigatorios = CamposObrigatorios +"\t}"
    ValidarTamanhoDosCampos = ValidarTamanhoDosCampos +"\t}"
        
print(CamposObrigatorios)
print()
print(ValidarTamanhoDosCampos)


