import MySQLdb

# open connection

db = MySQLdb.connect(
    host="localhost",
    user='Adm-User',
    passwd='222',
    db='services_db',
    charset="utf8",
    use_unicode=True
)

cursr = db.cursor()

cursr.execute('INSERT INTO User (name, age) VALUES (%s, %s);', ('Рылёва', int(20)))
db.commit()

cursr.execute('SELECT * FROM User ')
entries = cursr.fetchall()

for e in entries:
    print(e)

cursr.execute('DELETE FROM User')
db.commit()

cursr.execute('SELECT * FROM User')
entries = cursr.fetchall()


for e in entries:
    print(e)

cursr.close()
db.close()
