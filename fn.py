Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> def a:
	
SyntaxError: invalid syntax
>>> def a():
	servername=input("enter the server name:")
	dbname=input("\n Enter the data base name:")
	username=input("\n Enter the username:")
	x=input("\n Enter the passward:")
	print(servername+dbname+username+x)

	
>>> def a():
	servername=input("enter the server name:")
	dbname=input("\n Enter the data base name:")
	username=input("\n Enter the username:")
	x=input("\n Enter the passward:")
	print(a.servername+a.dbname+a.username+a.x)

	
>>> def a(*args,sep="/"):
	servername=input("enter the server name:")
	dbname=input("\n Enter the data base name:")
	username=input("\n Enter the username:")
	x=input("\n Enter the passward:")

	
>>> a(servername,dbname,username,x)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a(servername,dbname,username,x)
NameError: name 'servername' is not defined
>>> def a(*args,sep="/"):
...	return sep.join(args)
	servername=input("enter the server name:")
	dbname=input("\n Enter the data base name:")
	username=input("\n Enter the username:")
	x=input("\n Enter the passward:")
	
SyntaxError: expected an indented block
>>> def a(*args,sep="/"):
	return sep.join(args)
	servername=input("enter the server name:")
	dbname=input("\n Enter the data base name:")
	username=input("\n Enter the username:")
	x=input("\n Enter the passward:")

	
>>> a("sename","dbname","username","passward")
'sename/dbname/username/passward'
>>> 
