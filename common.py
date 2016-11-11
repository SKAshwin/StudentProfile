#!/usr/bin/env python3
import sqlite3
from nushgrading import *

def load_modules(db='database/grading.db',table='Module'):
    conn = sqlite3.connect(db)
    query = "SELECT code,credits from {}".format(table)
    modules = dict()
    for row in conn.execute(query):
        code = row[0]
        credits = row[1]
        modules[code] = Module(code,int(credits))
    return modules

"""
Function: Used to verify that inputs are of a particular type, effectively introduce
          static typing where its useful.
Usage: Both tuple and dictionary arguments accepted. If a variable can be of multiple
       different types, then a tuple must be used to list all types
       For example, verify_input((num, int, float), (cb, Module)) checks if num is an int
       or a float, and if cb is a Module.
       verify_input({x: int, y:int, z:str, gpa:CAP}) is the shorthand equivalent of
       verify_input((x,int),(y,int),(z,str),(gpa,CAP)): checks if x and y are ints,
       z is a string and gpa is a CAP object.
       Dictionary arguments can be used alongside tuples
       verify_input({x:int,y:str}, (z, int, float)) checks if x is an int, y is a str and
       z is an int or a float
Encouraged stye: Use a dictionary for values that need a single type; use tuple for values
                 that can have multiple types.
Output: Throws a TypeError if a condition fails (and states the failed condition). Otherwise
        returns None.
"""
def verify_input(*class_input_pairs):
    for elem in class_input_pairs:
        is_instance = False
        try:
            val = elem[0]
            classes = elem[1:]
        except:
            for key,value in elem.items():
                if not isinstance(key,value):
                    raise TypeError('Expected type {} got: {}'.format(value,key))
            continue
        for p_class in classes:
            if isinstance(val,p_class):
                is_instance = True
                break;
        if not is_instance:
            raise TypeError('Expected one of {} but got {}'
                    .format(str(classes),val))

