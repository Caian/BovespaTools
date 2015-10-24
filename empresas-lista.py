#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  empresas-lista.py
#
#  Copyright (C) 2015 Caian Benedicto <caianbene@gmail.com>
#
#  This file is part of bovespa-tools
#
#  bovespa-tools is free software; you can redistribute it and/or modify 
#  it under the terms of the GNU General Public License as published by 
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  Asparagus is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import tprinting

import time
import argparse

###############################################################################
# Alguma definições
###############################################################################

baseurl = "http://www.bmfbovespa.com.br/cias-listadas/empresas-listadas/BuscaEmpresaListada.aspx"
queryurl = baseurl + "?idioma=pt-br"

matext = '.mat'

allbtnid = 'ctl00$contentPlaceHolderConteudo$BuscaNomeEmpresa1$btnTodas'

clicktimeout = 10
timeoutsleep = 1

cvmFrag = 'codigoCvm='
cvmHeader = 'Código CVM'

headerxpath = "//*[@class='tabela']//thead//tr//*"
tablexpath = "//*[@class='tabela']//tr//td"
linkxpath = "//*[@class='tabela']//tr//td//a"

asserttitle = 'Empresas Listadas | BM&FBOVESPA'
assertheader = (
    'Razão Social',
    'Nome de Pregão',
    'Segmento'
)

###############################################################################
# Rotina principal
###############################################################################

def main(outfile):

    # Cria um driver do Firefox (mude pro seu navegador), abre a 
    # página de query e verifica se está na página certa

    driver = webdriver.Firefox()
    driver.get(queryurl)

    assert driver.title == asserttitle

    # Procura pelo botão da página que exibe todas as empresas,
    # se assegura que ele exista e envia um clique

    allbtn = driver.find_element_by_name(allbtnid)

    assert allbtn is not None

    allbtn.click()

    # Lê o cabeçalho da tabela, o conteúdo e salva os links com o código CVM
    
    for i in range(clicktimeout):

        header = [elem.text for 
                  elem in 
                  driver.find_elements_by_xpath((headerxpath))]
        
        if len(header) != 0:
            break
        
        time.sleep(timeoutsleep)

    table = [elem.text for 
             elem in 
             driver.find_elements_by_xpath((tablexpath))]

    links = [elem.get_attribute("href") for 
             elem in 
             driver.find_elements_by_xpath((linkxpath))]

    # Fecha a janela

    driver.close()

    # Valida os cabeçalhos, dados da tabela e links

    assert len(header) >= len(assertheader)

    for i in range(len(assertheader)):
        assert header[i] == assertheader[i]

    assert len(table) % len(header) == 0
    assert len(table) / 3 == len(links) / 2

    # Combina os links na tabela

    header2 = header + [cvmHeader]

    links2 = [int(link[len(cvmFrag) + link.find(cvmFrag):]) for 
              link in 
              links[::2]]

    table2 = [table[k:k+len(header)] for 
              k in 
              range(0,len(table),len(header))]

    assert len(links2) == len(table2)

    table2 = [i[0]+[str(i[1])] for 
              i in 
              zip(table2, links2)]

    # Imprime a tabela

    if outfile.endswith(matext):
        tprinting.writeMat(outfile, header2, table2)
    else:
        tprinting.writeTable(outfile, header2, table2)

###############################################################################
# Ponto de entrada do script
###############################################################################

if __name__ == '__main__':

    # Parsing dos argumentos de entrada
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=str, default='', help='arquivo de saida')
    args = parser.parse_args()

    main(args.out)
