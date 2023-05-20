#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q = """create table staffleave(id int(100)auto_increment primary key,
                              leave_id varchar (70),
                              staff_id varchar(70),
                              name varchar(50),
                              reason varchar(100),from_date varchar(60),
                              to_date varchar(60),
                              total_days int(60),
                              status text(1000)  )"""
cur.execute(q)
conn.commit()
print("""
 <script>
    alert("table created successfully..!");
 </script>
 """)
conn.close()