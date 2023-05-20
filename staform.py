#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import mysql.connector
import cgi
from datetime import datetime

f = cgi.FieldStorage()
pid = f.getvalue("id")
conn = mysql.connector.connect(host="localhost", user="root", password="", database="studyworld")
cur = conn.cursor()
q1 = """select staff_id from staff where id= %s """ % (pid)
cur.execute(q1)
r = cur.fetchone()
q = """select max(id) from staffleave"""
cur.execute(q)
max = cur.fetchone()
if max[0] != None:
    n = max[0]
else:
    n = 0
if n <= 9:
    z = "000"
elif n >= 10 and n <= 99:
    z = "00"
elif n >= 100 and n <= 999:
    z = "0"
id1 = "LID" + z + str(n + 1)

print("""
 <!DOCTYPE html>
<html>
<head>
   <link rel="stylesheet" href="common.css">
       <link rel="stylesheet" href="nav.css">
<style>
form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color:rgba(255,255,255,0.5);
    border-radius: 10px;
  }

  h2 {
    text-align: center;
    margin-bottom: 20px;
  }

  .form-group {
    margin-bottom: 15px;
  }

  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }

  input[type="text"],
  input[type="email"],
  input[type="tel"],
  input[type="password"],
  select {
    width: 100px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }

  input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    float: right;
  }

  input[type="submit"]:hover {
    background-color: #45a049;
  }

</style>
</head>
<body style="background-color:aliceblue">
  <div class="header">
        <img src="images/logo.jpg" alt="logo"/><h1 style= "background-color: rgb(255, 255, 255);font-family: 'Times New Roman';font-size:50px;text-align: center;font-variant: small-caps;font-weight: bold;text-decoration-thickness: 50px;color: rgb(0, 2, 121);">Study World College of Engineering</h1>
    </div>
      <nav class="navbar">
<ul class="nav-links">
<div class="menu">

<li><a href=index.html>Home</a></li>



<li><a href=stadash.py>Dashboard</a></li>



</div>

</ul>

</nav>
<form method="post">
    <h2>Staff Leave Form</h2>

    <div class="form-group">
      <label>leave_id</label>
      <input type="text" id="leave_id" name="leave_id" value="%s" required>
    </div>
    <div class="form-group">
      <label>staff_id</label>
      <input type="text" id="staff_id" name="staff_id" value="%s" placeholder="Enter Staff Name" required>
    </div>
    <div class="form-group">
    <label>name</label>
    <input type=text name=name required>
    </div>

    <div class="form-group">
      <label>Reason</label>
      <textarea name="reason"></textarea>

    </div>
    <div class="form-group">
      <label>From date</label>
      <input type="date" id="fromdate" name="from_date" placeholder="Enter From date" required>
    </div>
    <div class="form-group">
      <label>To date</label>
      <input type="date" id="todate" name="to_date" placeholder="Enter To date" required>
    </div>

    <div class="form-group">
      <input type="submit" value="Register" name="submit">
    </div>  </form>
          <div class="footer">
        <h6>© 2023 All Rights Reserved By Study World Education Holding Group's.</h6>
    </div>

</body>
</html>

""" % (id1, r[0]))

pleave_id = f.getvalue("leave_id")
pstaff_id = f.getvalue("staff_id")
pstaff_name=f.getvalue("name")
preason = f.getvalue("reason")
pfrom_date = f.getvalue("from_date")
pto_date = f.getvalue("to_date")
psubmit = f.getvalue("submit")
d1 = datetime.strptime(pfrom_date, "%Y-%m-%d")
d2 = datetime.strptime(pto_date, "%Y-%m-%d")
total_days = d2 - d1
total = total_days.days
if psubmit != None:
    q2 = """insert into staffleave(leave_id,staff_id,name,reason,from_date,to_date,total_days,status)values('%s','%s','%s','%s','%s','%s','%s','PENDING')""" % (
        pleave_id, pstaff_id,pstaff_name, preason, pfrom_date, pto_date, total)
    cur.execute(q2)
    conn.commit()
    print("""
        <script>
        alert("data inserted successfully");
        </script>

        """)
    conn.close()
