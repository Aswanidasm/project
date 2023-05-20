#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
import cgi
f = cgi.FieldStorage()
pid = f.getvalue("id")
conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q = """select * from staff where id=%s"""%(pid)
cur.execute(q)
a = cur.fetchall()

print("""
<head>
  <link rel="stylesheet" href="common.css">
     <link rel="stylesheet" href="nav.css">
<style>
table {
        margin-left: auto;
        margin-right: auto;
         }
</style>
</head>
   <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
      <nav class="navbar">
<ul class="nav-links">
<div class="menu">

<li><a href=index.html>Home</a></li>



<li><a href=dashboard.py>Dashboard</a></li>



</div>

</ul>

</nav>
    <table border="1">
    <tr>
    <th>staff_id</th>
    <th>name</th>
    <th>email</th>
     <th>dob</th>
    <th>password</th>
    <th>profile</th>

    </tr>""")
for i in a:
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
    <td><img src='%s' height="60px" width="60px"></td>


    </tr>
    """ % (i[1], i[2], i[3], i[4], i[5], "images/" + i[6]))
print("""
    </table>
          <div class="footer">
        <h6>© 2023 All Rights Reserved By Study World Education Holding Group's.</h6>
    </div>

    """)