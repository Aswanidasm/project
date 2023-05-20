#!C:/Users/HP/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi
f=cgi.FieldStorage()
id=f.getvalue("id")
otp=f.getvalue("genarate_otp")
print(otp)
print("""
<html>

<body>
<form method="post">
<label>Enter your otp</label>
<input type="text" name="otp">
<input type="submit" name="sub" value="enter">
</form>
</body>
</html>
""")

potp=f.getvalue("genarate_otp")
psub=f.getvalue("sub")
if psub != None:

    print(potp)
    if potp == otp:
        print("""
            <script>
                    alert("great! your otp is correct");
                    location.href="changepassword.py?id=%s";
            </script>"""%(id))
    else:
        print("""
                    <script>
                            alert("great! your otp is  incorrect");
                    </script>""")