#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Accenture Big Data Academy - November 2017
#  File: 1_perimeter_and_area.py <Python 2.7.13>
#  Developer: Grecia María Cortés Espinosa <ecragi@gmail.com>
#  Description: Script that calculates the perimeter and area of an unkown polygon based on the user’s input.
#  Reference: "Área y perímetro de los polígonos" (https://www.geoka.net/geometria/area.html)

## - Functions - ##
# Perimeter of an Equilateral Triangle #
def p_e_triangle(in_side):
    return (3 * in_side)

# Area of an Equilateral Triangle #
def a_e_triangle(in_base, in_height):
    return ((in_base * in_height) / 2)

# Perimeter of a Square and a Diamond #
def p_square(in_side):
    return (4 * in_side)

# Area of a Square #
def a_square(in_side):
    return (in_side * in_side)

# Perimeter of a Rectangle and a Rhomboid #
def p_rectangle(in_base, in_height):
    return (2 * (in_base + in_height))

# Area of a Rectangle and a Rhomboid #
def a_rectangle(in_base, in_height):
    return (in_base * in_height)

# Area of a Diamond #
def a_diamond(in_l_dimension, in_s_dimension):
    return ((in_l_dimension * in_s_dimension) / 2)

# Perimeter of a Trapeze #
def p_trapeze(in_mi_base, in_ma_base, in_side):
    return (in_mi_base + in_ma_base + (2 * in_side))

# Area of a Trapeze #
def a_trapeze(in_mi_base, in_ma_base, in_height):
    return (((in_mi_base + in_ma_base) * in_height) / 2)

## - Main script - ##
s_answer = "Y"
while (s_answer == 'y' or s_answer == 'Y'):
    print "Accenture Big Data Academy - November 2017"
    print "1. Script that calculates the perimeter and area of an unkown regular polygon based on the user’s input."
    i_poligon = '0'
    while (i_poligon <= '0' or i_poligon >= '7'):
        print("For which type of regular polygon do you want to calculat its perimeter and area: ")
        print("1. Equilateral Triangle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Diamond")
        print("5. Rhomboid")
        print("6. Trapeze")
        i_poligon = raw_input("Option?: ")

    if i_poligon == '1':
        print("=> Equilateral Triangle's...")
        i_side_a = raw_input("Side: ")
        i_height = raw_input("Height: ")
        f_perimeter = p_e_triangle(float(i_side_a))
        f_area = a_e_triangle(float(i_side_a), float(i_height))
    elif i_poligon == '2':
        print("=> Square's...")
        i_side_a = raw_input("Side: ")
        f_perimeter = p_square(float(i_side_a))
        f_area = a_square(float(i_side_a))
    elif i_poligon == '3':
        print("=> Rectangle's...")
        i_base = raw_input("Base: ")
        i_height = raw_input("Height: ")
        f_perimeter = p_rectangle(float(i_base), float(i_height))
        f_area = a_rectangle(float(i_base), float(i_height))
    elif i_poligon == '4':
        print("=> Diamond's...")
        i_side_a = raw_input("Side: ")
        i_side_b = raw_input("Large dimension: ")
        i_side_c = raw_input("Short dimension: ")
        f_perimeter = p_square(float(i_side_a))
        f_area = a_diamond(float(i_side_b), float(i_side_c))
    elif i_poligon == '5':
        print("=> Rhomboid's...")
        i_side_a = raw_input("Side: ")
        i_base = raw_input("Base: ")
        i_height = raw_input("Height: ")
        f_perimeter = p_rectangle(float(i_side_a), float(i_base))
        f_area = a_rectangle(float(i_base), float(i_height))
    elif i_poligon == '6':
        print("=> Trapeze's...")
        i_base = raw_input("Minor Base: ")
        i_base_ma = raw_input("Mayor Base: ")
        i_side_a = raw_input("Side: ")
        i_height = raw_input("Height: ")
        f_perimeter = p_trapeze(float(i_base), float(i_base_ma), float(i_side_a))
        f_area = a_trapeze(float(i_base), float(i_base_ma), float(i_height))

    print("=-= Results:")
    print("Perimeter = {0:.2f}".format(f_perimeter))
    print("Area = {0:.4f}".format(f_area))
    s_answer = raw_input("Do you want to calculate the perimeter and area of another polygon (Y/N)?: ")
