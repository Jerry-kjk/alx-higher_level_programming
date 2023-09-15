#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    When imported it will not be executed.
    """
    host = 'localhost'
    port = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state = str(sys.argv[4])
    
    db = MySQLdb.connect(host=host, user=username, passwd=password,
                            db=name, port=port, charset="utf8")

    cur = db.cursor()
    sql = """SELECT * FROM states WHERE name LIKE BINARY '{}'
          ORDER BY id ASC""".format(state)
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
