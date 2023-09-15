#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""


if __name__ == "__main__":
    """
    When imported it will not be executed.
    """
    from sys import argv
    import MySQLdb

    username = argv[1]
    password = argv[2]
    database = argv[3]
    server = 'localhost'
    port = 3306

    db = MySQLdb.connect(host=server, user=username, passwd=password,
                            db=database, port=port, charset="utf8")

    cur = db.cursor()
    sql = """
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        INNER JOIN
            states ON
                cities.state_id=states.id"""
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
