#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi
f=cgi.FieldStorage()
pid=f.getvalue("id")
print(pid)
print("""
<html>
  <body>
     <form method="post">
        <input type="password" placeholder="Enter new password"name="password">
        <input type="submit" name="sub" value="submit">
     </form>
  </body>
</html>
""")
ppass=f.getvalue("password")
psub=f.getvalue("sub")
if psub != None:
    import mysql.connector

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
    cur = conn.cursor()
    q="""update student set password='%s' where id=%s"""%(ppass,pid)
    cur.execute(q)
    conn.commit()
    print("""
       <script>
                alert("password changed successfully..!");
                location.href="studentl.py?id=%s";
            </script>
    """%(pid))