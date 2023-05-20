#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb
cgitb.enable()
f=cgi.FieldStorage()
pid=f.getvalue("id")
import mysql.connector
conn=mysql.connector.connect(host="localhost", user="root", password="",database="studyworld")
cur= conn.cursor()
q="""update staffleave set status='REJECTED' where id=%s"""%(pid)
cur.execute(q)
conn.commit()
print("""
                      <script>
                        alert("REJECTED");
                        location.href="viewstaffleave.py?id=%s";
                      </script>
                      """%(pid))