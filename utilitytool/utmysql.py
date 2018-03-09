import MySQLdb
import CV

def queryFirstRow(strsql, args=None):
    return queryMany(strsql, args, rows=1)

def queryAll(strsql, args=None):
    return queryMany(strsql, args)
    
def queryMany(strsql, args=None, rows=0):
    conn = __connection()
    cur = conn.cursor()
    cur.execute(strsql, args)
    if rows == 0:
        rows = cur.rowcount
    res = cur.fetchmany(rows)
    __close(conn)
    return res

def __connection():
    conn = MySQLdb.connect(host=CV.MYSQL_CONN_HOST,
        port = CV.MYSQL_CONN_POST,
        user=CV.MYSQL_CONN_USERNAME,
        passwd=CV.MYSQL_CONN_PWD,
        db=CV.MYSQL_CONN_DBNAME,
        charset=CV.MYSQL_CONN_CHARSET)
    return conn

def __close(conn):
    conn.commit()
    conn.close()