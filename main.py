import mysql.connector

cnx=mysql.connector.connect(user='root',  password='niloofar', host='127.0.0.1',
                            database='clerk_info')

cursor=cnx.cursor()
quary='SELECT * FROM information ORDER BY Height DESC,Weight; '

cursor.execute(quary)

for (name,Weight,Height) in cursor:

    print(name,Height,Weight)
cnx.close()