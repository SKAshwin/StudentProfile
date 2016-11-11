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

d = load_modules()
print(d['FR4202'])
print(d['FR4202'].is_elective())
print(d['FR4202'].module_type())
