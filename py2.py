Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> def k():
	a=input("servername:")
	b=input("dbname:")
	c=input("username:")
	d=input("passward:")
	return"server=%s;dbname=%s;username=%s;passward=%s",a,b,c,d

>>> k()
servername:servername
dbname:dbname
username:username
passward:passward
('server=%s;dbname=%s;username=%s;passward=%s', 'servername', 'dbname', 'username', 'passward')
>>> 
def k():
	a=input("servername:")
	b=input("dbname:")
	c=input("username:")
	d=input("passward:")
	return"server=%s;dbname=%s;username=%s;passward=%s"%(a,b,c,d)

>>> k()
servername:servername
dbname:dbname
username:username
passward:passward
'server=servername;dbname=dbname;username=username;passward=passward'
>>> 
