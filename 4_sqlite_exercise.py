#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Accenture Big Data Academy - November 2017
#  File: 4_sqlite_exercise.py <Python 2.7.13>
#  Developer: Grecia María Cortés Espinosa <ecragi@gmail.com>
#  Description: Script lo list students information from a SQLite database.
#
#Create a Function to add a new student.
import sqlite3
import sys

class dbStudent:
    'Class to conect and manage an SQLite database for students'

    def __init__(self, in_db):
        self.db_student = in_db
        self.db_connection = None
        try:
            self.db_connection = sqlite3.connect(self.db_student)
            db_cursor = self.db_connection.cursor()
            db_cursor.execute('SELECT SQLITE_VERSION()')
            db_data = db_cursor.fetchone()
            #print "SQLite version: %s" % db_data
        except sqlite3.Error, e:
            #print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if self.db_connection:
                self.db_connection.close()

    def db_read_query(self, in_query):
        self.db_connection = sqlite3.connect(self.db_student)
        self.db_connection.text_factory = str
        with self.db_connection:
            db_cursor = self.db_connection.cursor()
            db_cursor.execute(in_query)
            return db_cursor.fetchall()

    def db_read_one_query(self, in_query):
        self.db_connection = sqlite3.connect(self.db_student)
        self.db_connection.text_factory = str
        with self.db_connection:
            db_cursor = self.db_connection.cursor()
            db_cursor.execute(in_query)
            return db_cursor.fetchone()

    def db_add_student(self, in_student_values):
        db_s_count = self.db_read_one_query("SELECT COUNT(S.id) FROM students as S")
        i_id = int(db_s_count[0]) + 1
        #print("{0}".format(i_id))
        #if self.db_connection:
        #    self.db_connection.close()
        self.db_close()
        #t_values = (i_id, in_student_values[0], in_student_values[1], in_student_values[2], in_student_values[3])
        #print(t_values)
        s_insert = "INSERT INTO students VALUES (" + str(i_id) + ", '" + in_student_values[0] + "', '" + in_student_values[1] + "', '" + in_student_values[2] + "', " + str(in_student_values[3]) + ")"
        #s_insert = "INSERT INTO students VALUES (?, ?, ?, ?, ?)"
        ##
        self.db_connection = sqlite3.connect(self.db_student)
        self.db_connection.text_factory = str
        with self.db_connection:
            db_cursor = self.db_connection.cursor()
            #db_cursor.execute(s_insert, t_values)
            db_cursor.execute(s_insert)
            #return db_cursor.fetchone()
            #return db_cursor.fetchall()
            ##print("The last Id of the inserted row is {0}".format(db_cursor.lastrowid))
            return db_cursor.lastrowid

    def db_close(self):
        if self.db_connection:
            self.db_connection.close()



## - Main script - ##
in_answer = "Y"
while (in_answer == 'y' or in_answer == 'Y'):
    print "Accenture Big Data Academy - November 2017"
    print "4. Script lo list students information from a SQLite database."

    myStudentBD = dbStudent('school.db')
    # - Students and their subjects - #
    s_q_students = "SELECT S.id, S.first_name, S.last_name, C.id as course_id, C.description as course FROM students as S LEFT JOIN student_courses as SC on S.id = SC.student_id LEFT JOIN courses as C on SC.course_id = C.id ORDER BY S.first_name, S.last_name, C.description"
    s_q_result = myStudentBD.db_read_query(s_q_students)
    if s_q_result:
        print("\n --- Student Full name --- --- Subject ---")
        for s_q_rom in s_q_result:
            print("{0:<20} - {1:<16}".format(("[" + str(s_q_rom[0]) + "] " + s_q_rom[1] + " " + s_q_rom[2]), ("[" + str(s_q_rom[3]) + "] - " + str(s_q_rom[4]))))
    # - Students' names and their teachers - #
    s_q_students = "SELECT S.first_name, T.id, T.Name as teacher FROM students as S LEFT JOIN teachers as T on S.teacher_id = T.id ORDER BY S.first_name, T.Name"
    s_q_result = myStudentBD.db_read_query(s_q_students)
    if s_q_result:
        print("\n --- Student --- --- Teacher ---")
        for s_q_rom in s_q_result:
            print("{0:<12} - {1:<12}".format(s_q_rom[0], (str(s_q_rom[1]) + " - " + s_q_rom[2])))

    #s_q_students = "SELECT COUNT(S.id) FROM students as S"

    #t_values = ()
    in_n_student = raw_input("Do you want to add a new student (Y/N)?: ")
    if in_n_student == 'y' or in_n_student == 'Y':
        in_s_name = raw_input("Student's name: ")
        in_s_lname = raw_input("Student's last name: ")
        in_s_bday = raw_input("Student's birthday [YYYY-MM-DD]: ")
        in_s_t_id = raw_input("Teacher's ID: ")
        l_s_values = [in_s_name, in_s_lname, in_s_bday, int(in_s_t_id)]
        #s_q_result = myStudentBD.db_add_student(l_s_values)
        myStudentBD.db_add_student(l_s_values)
#        if s_q_result:
#            print(s_q_result)


    in_answer = raw_input("Do you want to read again from the Students' database (Y/N)?: ")
