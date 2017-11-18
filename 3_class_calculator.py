#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Accenture Big Data Academy - November 2017
#  File: 3_class_calculator.py <Python 2.7.13>
#  Developer: Grecia María Cortés Espinosa <ecragi@gmail.com>
#  Description: Script that creates a calculator class for the aritmetic operations: +, -, *, /. With one value being 15.
#

class MyCalculator:
    'Class to create calculators for basic aritmetic operations'

    def my_sum(self, in_value_a, in_value_b = 15):
        return in_value_a + in_value_b

    def my_sub(self, in_value_a, in_value_b = 15):
        return in_value_a - in_value_b

    def my_mul(self, in_value_a, in_value_b = 15):
        return in_value_a * in_value_b

    def my_div(self, in_value_a, in_value_b = 15):
        if in_value_b == 0:
            i_answer = 0
        else:
            i_answer = in_value_a / in_value_b

        return i_answer


## - Main script - ##
in_answer = "Y"
while (in_answer == 'y' or in_answer == 'Y'):
    print "Accenture Big Data Academy - November 2017"
    print "3. Script that creates a calculator class for the aritmetic operations: +, -, *, /. With one value being 15."
    aCalculator = MyCalculator()
    in_operation = '0'
    while (in_operation <= '0' or in_operation >= '5'):
        print("Operation to execute: ")
        print("1. Sum")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        in_operation = raw_input("Option?: ")

    if in_operation == '1':
        print("=> Sum:")
        in_value_a = raw_input("Value A: ")
        in_value_b = raw_input("Value B: ")
        f_result = aCalculator.my_sum(float(in_value_a), float(in_value_b))
        f_result15 = aCalculator.my_sum(float(in_value_a))
    elif in_operation == '2':
        print("=> Substraction:")
        in_value_a = raw_input("Value A: ")
        in_value_b = raw_input("Value B: ")
        f_result = aCalculator.my_sub(float(in_value_a), float(in_value_b))
        f_result15 = aCalculator.my_sub(float(in_value_a))
    elif in_operation == '3':
        print("=> Multiplication:")
        in_value_a = raw_input("Value A: ")
        in_value_b = raw_input("Value B: ")
        f_result = aCalculator.my_mul(float(in_value_a), float(in_value_b))
        f_result15 = aCalculator.my_mul(float(in_value_a))
    elif in_operation == '4':
        print("=> Division:")
        in_value_a = raw_input("Value A: ")
        in_value_b = raw_input("Value B: ")
        f_result = aCalculator.my_div(float(in_value_a), float(in_value_b))
        f_result15 = aCalculator.my_div(float(in_value_a))

    print("=-= Results:")
    print("Result = {0:.3f}".format(f_result))
    print("Result w/15 ({1:.2f} and 15) = {0:.3f}".format(f_result15, float(in_value_a)))
    in_answer = raw_input("Do you want to make other operation (Y/N)?: ")
