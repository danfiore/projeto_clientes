from validate_docbr import CPF
import re

def nome_valido(nome):
    return nome.isalpha()

def cpf_valido(nmr_cpf):
    cpf = CPF()
    return cpf.validate(nmr_cpf)

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o celular é validado (XX XXXXX-XXXX)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta