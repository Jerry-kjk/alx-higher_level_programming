#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, but  is safe from
MySQL injections!
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    When imported it will not be executed.
    """
    host = 'localhost'
    port = 3306
    username = argv[1]
    password = argv[2]
    name = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host=host,
                         user=username,
                         passwd=password,
                         db=name,
                         port=port,
                         charset="utf8"
                         )

    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(sql, (state,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
