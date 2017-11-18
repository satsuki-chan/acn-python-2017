#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Accenture Big Data Academy - November 2017
#  File: 2_loop_statements.py <Python 2.7.13>
#  Developer: Grecia María Cortés Espinosa <ecragi@gmail.com>
#  Description: Script that creates a piramid of asterisks based on the user’s number of rows.
#
#

## - Main script - ##
in_answer = "Y"
while (in_answer == 'y' or in_answer == 'Y'):
    print "Accenture Big Data Academy - November 2017"
    print "2. Script that creates a piramid of asterisks based on the user’s number of rows."

    in_n_rows = raw_input("How many rows of asterisks do you want?: ")
    try:
        i_n_rows = int(in_n_rows)
    except ValueError:
        i_n_rows = 0

    if i_n_rows >= 1:
        i_control = 1
        s_row = "*"
        while i_control <= i_n_rows:
            print("{0:>{digits}}".format(s_row, digits=i_n_rows))
            s_row += "*"
            i_control += 1
    else:
        print("\n")

    in_answer = raw_input("Do you want to print more rows of asterisks (Y/N)?: ")
