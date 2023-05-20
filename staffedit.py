#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb

cgitb.enable()
f = cgi.FieldStorage()
pid = f.getvalue("id")
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()

q = """select * from staff where id=%s""" % (pid)
cur.execute(q)
a = cur.fetchall()

print("""
<head>
    <link rel="stylesheet" href="common.css">
    <style>
    .footer{
             background-color:#808080;
             padding: 9px;
             text-align: center;
             position:absolute;
             width: 100%;
              bottom:0;

          }
    </style>
</head>
    <table border="1" align="center">
    <tr>
    <th>staff_id</th>
    <th>name</th>
    </tr>""")
for i in a:
    print("""
        <tr>
        <td>%s</td>
        <td>%s</td>
        </tr>""" % (i[1], i[2]))
    print("""
    <head>
        <link rel="stylesheet" type="text/css" href="css/common.css">
    </head>
    <body >
   <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
        </table>
            <form method="post" align="center">
            <input type ="email" value="%s" name="email"><br>
            <input type="Date" value="%s" name="dob"<br>
            <input type="password" value="%s" name="pass"><br>
            <input type="submit"  value="sub" name="sub">
            </form>
      <div class="footer">
        <h6>© 2023 All Rights Reserved By Study World Education Holding Group's.</h6>
    </div>""" % (i[3], i[4], i[5]))
    pnewemail = f.getvalue("email")
    pdob = f.getvalue("dob")

    pnewpass = f.getvalue("pass")
    psub = f.getvalue("sub")
    if psub != None:
        q2 = """update staff set email='%s',dob='%s',password='%s' where id='%s' """ % (
        pnewemail, pdob, pnewpass, i[0])
        cur.execute(q2)
        conn.commit()
        print("""
                    <script>
                    location.href="staffview.py"
                    </script>
                    """)