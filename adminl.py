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
      <form method="post" action="#">
     <label for="staff_id">Staff id</label>
           <input type ="text" value="%s" name="staff_id" readonly><br>
         <label for="staff_name">Staff name</label>
           <input type ="text" value="%s" name="staff_name" readonly><br>
          <label for="dob">Dob</label>

           <input type ="dob" value="%s" name="dob"><br>
          <label for="email">Email</label>
           <input type ="email" value="%s" name="email"><br>
         <label for="Mobile no"></label>
           <input type="number" value="%s" name="mobile_no"><br>

        <label for="password">Password</label>
           <input type="password" value="%s" name="pass"><br>
         <label for="file">Profile</label>
           <input type ="file" value="%s" name="profile" readonly><br>

       <input type="submit"  value="sub" name="sub">


     </form>
     """ % (i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

pnewemail = f.getvalue("email")
pnewnumber = f.getvalue("mobile_no")
pnewpass = f.getvalue("pass")
psub = f.getvalue("sub")
if psub != None:
    q2 = """update staff set email='%s', mobile_no='%s',password='%s' where id='%s' """ % (
        pnewemail, pnewnumber, pnewpass, i[0])
    cur.execute(q2)
    conn.commit()

    print("""
                    <script>
                    location.href="staffview.py"
                    </script>
                    """)