#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb

cgitb.enable()
f = cgi.FieldStorage()
pid = f.getvalue("id")
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()

q = """select * from student where id=%s""" % (pid)
cur.execute(q)
a = cur.fetchall()

print("""
<head>
    <link rel="stylesheet" href="common.css">
 
<style>

    body {

  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</head>
</style>
   <body style="background-image:url('images/stl.jpg');">
   <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
    <table border="1" align="center">
    <tr>
    <th>student_id</th>
    <th>name</th>
    </tr>""")
for i in a:
    print("""
        <tr>
        <td>%s</td>
        <td>%s</td>
        </tr>""" % (i[1], i[2]))
    print("""
   
  
        </table>
            <form method="post" align="center" >
            <input type ="email" value="%s" name="email"><br><br>
            <input type="Date" value="%s" name="dob"<br><br><br>
            <input type="password" value="%s" name="pass"><br><br>
            <input type="submit"  value="EDIT" name="sub"><br>
            </form>

         
""" % (i[3], i[4], i[5]))
    pnewemail = f.getvalue("email")
    pdob = f.getvalue("dob")

    pnewpass = f.getvalue("pass")
    psub = f.getvalue("sub")
    if psub != None:
        q2 = """update student set email='%s',dob='%s',password='%s' where id='%s' """ % (
        pnewemail, pdob, pnewpass, i[0])
        cur.execute(q2)
        conn.commit()
        print("""
                    <script>
                    location.href="studentview.py"
                    </script>
                    """)