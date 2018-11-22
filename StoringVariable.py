"""
Stores variables in a database
"""
import sqlite3
from sqlite3 import Error
import os.path



def create_connection(DateTime_Database):
    #create a database connection to the SQLite database
    try:
        conn = sqlite3.connect(DateTime_Database)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")


def select_task_by_priority(conn, ticks, hour, minute, second, DateTime_Database, is_DateTime, day, month, year, pm):
    cur = conn.cursor()
    if (is_DateTime):
        cur.execute("Create Table data (ticks, hour, minute, second, day, month, year, pm)")
        cur.execute("INSERT INTO data VALUES (%u, %u, %u, %u, %u, %u, %u, %u) " %(ticks, hour, minute, second, day, month, year, pm))
    else:
        cur.execute("UPDATE data SET ticks=%u, hour=%u, minute=%u, second=%u, day=%u, month=%u, year=%u, pm=%u"%(
            ticks, hour, minute, second, day, month, year, pm))



def main(ticks, minute, second, hour, hourclock, pm, day, month, year):
    DateTime_Database = "DATABASE/TimeDate.db"
    # create a database connection
    is_DateTime = not os.path.isfile(DateTime_Database)
    conn = create_connection(DateTime_Database)
    with conn:
        select_task_by_priority(conn, ticks, hour, minute, second,DateTime_Database, is_DateTime, day, month, year, pm)
        select_all_tasks(conn)


if __name__ == '__main__':
    main()

def Data_get():
    #gets Data from Database
    DateTime_Database = "DATABASE/TimeDate.db"
    conn = create_connection(DateTime_Database)
    cur = conn.cursor()
    cur.execute("Select * From data")
    row = cur.fetchone()
    ticks = int(row[0])
    hour = int(row[1])
    minute = int(row[2])
    second = int(row[3])
    day = int(row[4])
    month = int(row[5])
    year = int(row[6])
    pm = bool(row[7])
    
    return ticks, hour, minute, second, day, month, year, pm
