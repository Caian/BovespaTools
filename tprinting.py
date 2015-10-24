#!/usr/bin/python3
# -*- coding: utf-8 -*-

#  tprinting.py
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

import scipy.io as sio
import numpy as np
import sys

###############################################################################
# Alguma definições
###############################################################################

tablesep = '\t'

###############################################################################
# Escreve a tabela em modo texto para um arquivo
###############################################################################

def writeTable(file, header, table):

    if file == '':
        file = sys.stdout
        closefile = False
    else:
        file = open(file, 'wt')
        closefile = True

    colszs = [len(title) for title in header]
    for i in range(0, len(colszs)):
        colszs[i] = max([colszs[i]]+[len(row[i]) for row in table])

    file.write(
        tablesep.join([i[1].ljust(i[0]) for i in zip(colszs, header)]) + '\n'
    )

    for row in table:
        file.write(
            tablesep.join([i[1].ljust(i[0]) for i in zip(colszs, row)]) + '\n'
        )

###############################################################################
# Salva a tabela como arquivo .mat do matlab
###############################################################################

def writeMat(filename, header, table):

    # Cria uma matriz de células para guardar os elementos
    a = np.empty((len(table),len(header)),dtype=object)

    # Salva a tabela nas células
    for i in range(len(table)):
        for j in range(len(header)):
            a[i,j] = table[i][j]

    # Escreve a tabela
    sio.savemat(filename, {'header' : header, 'data' : a})
