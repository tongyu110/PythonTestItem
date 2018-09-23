import MySQLdb

host = 'localhost';
user = 'root';
password = '';
database = 'db_product';

conn = MySQLdb.connect(host,user,password,database);
cursor = conn.cursor();

cursor.execute("""select * from site_category where id=%s""", (332,));
values = cursor.fetchall();
print(values);
cursor.close();
