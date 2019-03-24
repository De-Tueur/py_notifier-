import sqlite3
conn = sqlite3.connect('msg.db')
cur = conn.cursor()
cmd="CREATE TABLE msgs(id integer primary key autoincrement,msg text not null)"
cur.execute(cmd)
conn.commit()
cur.close()
