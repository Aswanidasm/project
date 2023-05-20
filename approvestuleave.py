#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb
cgitb.enable()
f=cgi.FieldStorage()
pid=f.getvalue("id")
import mysql.connector
conn=mysql.connector.connect(host="localhost", user="root", password="",database="studyworld")
cur= conn.cursor()
q="""update stuleave set status='APPROVED' where id=%s"""%(pid)
cur.execute(q)
conn.commit()
print("""
                      <script>
                        alert("Approved");
                        location.href="viewstudentleave.py?id=%s";
                      </script>
                      """%(pid))