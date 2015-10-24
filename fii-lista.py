#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  fii-lista.py
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

baseurl = "http://www.bmfbovespa.com.br/fundos-listados/fundoslistados.aspx"
queryurl = baseurl + "?Idioma=pt-br&tipoFundo=imobiliario"

matext = '.mat'

clicktimeout = 10
timeoutsleep = 1

headerxpath = "//*[@class='tabela tabFundos']//table//thead//tr//th"
tablexpath = "//*[@class='tabela tabFundos']//table//tr//td"

asserttitle = 'Fundos Imobiliários'
assertheader = (
    'Razão Social',
    'Fundo',
    'Segmento',
    'Código'
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

    # Lê o cabeçalho da tabela e o conteúdo
    
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

    # Fecha a janela

    driver.close()

    # Valida os cabeçalhos, dados da tabela e links

    assert len(header) >= len(assertheader)

    for i in range(len(assertheader)):
        assert header[i] == assertheader[i]

    assert len(table) % len(header) == 0
    
    # Divide a tabela

    table2 = [table[k:k+len(header)] for 
              k in 
              range(0,len(table),len(header))]

    # Imprime a tabela

    if outfile.endswith(matext):
        tprinting.writeMat(outfile, header, table2)
    else:
        tprinting.writeTable(outfile, header, table2)

###############################################################################
# Ponto de entrada do script
###############################################################################

if __name__ == '__main__':

    # Parsing dos argumentos de entrada
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=str, default='', help='arquivo de saida')
    args = parser.parse_args()

    main(args.out)
