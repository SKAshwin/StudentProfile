#!/usr/bin/python3
import sys
import sqlite3
import getopt

VERSION = "0.1"
skip=1
args = sys.argv[1:]
db = "grading.db"       
table = "Module"
datasource = "moduleData.txt"
IGNORE = ""
opts, vals = getopt.getopt(args, 's:d:t:h', ['skip=','db=','database=','table=','help','ignore='])

for opt, arg in opts:
    if opt in ('-s','--skip'):
        skip = arg
    elif opt in ('-d','--db','--database'):
        db = arg
    elif opt in ('-t','--table'):
        table = arg
    elif opt=="--ignore":
        IGNORE = arg
    elif opt in ('-h','--help'):
        print("""\
VERSION: {}
Usage: populateDatabase.py [h] <datasource> [-d <database>] [-t <table>] [-s <skipcount>]
<datasource>    File containing module data formatted with each line as <Code> <credits>
-h              Help
--help          See -h
-d <database>   Use the specified databse. DEFAULT: {}
--database      See -d
--db            See -d
-t              Specified the table to fetch module data. DEFAULT: {}
--table         See -t
-s              Specifies the number of lines to be skipped before reading module
                data. Useful to ignore headers. DEFAULT: {}
--skip          See -s
--ignore        Sets the script to ignore all lines beginning with the provided
                string. Used to ignore comments
""".format(VERSION,db,table,skip))
        sys.exit(0)
if len(vals)!=0:
    datasource = vals[0]

conn = sqlite3.connect(db)
for line in open(datasource):
    if skip>0:
        skip-=1
        continue
    if len(IGNORE)!=0 and line[:len(IGNORE)]==IGNORE:
        continue
    if line!='\n':
        line = line[:-1]
        code, mc = line.split(' ')[0], line.split(' ')[-1]
        query = "INSERT OR IGNORE INTO {} VALUES({},{})".format(table,code,mc)
        print(query)
        conn.execute("INSERT OR IGNORE INTO {} VALUES(?,?)".format(table), (code,mc))
conn.commit()       
