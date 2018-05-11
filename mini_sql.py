#python script.py arg1 arg2 arg3....
from sys import argv,exit
import MySQLdb as db
from tabulate import tabulate
import time

try:
    connection = db.connect('127.0.0.1',argv[1],argv[2],argv[3])
    cursor = connection.cursor()
except db.OperationalError as e:
    print('Error on connect {}'.format(e))
    
while True: 
    _sql = input('mini_sql>>>')
    if _sql.lower() == 'quit':
        exit()
    try:
        start = int(time.time() * 1000)
        cursor.execute(_sql)
        _exec_time = int(time.time() * 1000) - start
    except db.Error as e:
        print('Error in sql execute {}'.format(e))
        continue
    #print(cursor.description)
    result = cursor.fetchall()
    headers = []
    if not cursor.description is None:
        for head in cursor.description:
            headers.append(head[0])
    print(tabulate(result,headers=headers))
    print('Rows affected {} ' .format(cursor.rowcount))
    print('Query time {} ms' .format(_exec_time))