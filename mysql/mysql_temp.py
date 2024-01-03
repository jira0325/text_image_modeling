import mysql.connector 



cnx = mysql.connector.connect(user='root', 
                              host='localhost',
                              use_pure=False)

mycursor= cnx.cursor()

mycursor.execute("CREATE DATABASE img_txt_project")