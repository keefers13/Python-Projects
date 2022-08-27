


import sqlite3

conn = sqlite3.connect('db_assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('db_assignment.db')

#tuple of files
filelist = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loop through each object in the tuple to find the names that end in y.
for x in filelist:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
# The value for each row will be one name out of the tuple therefore (x,)
# will denote a one element tuple for each name ending with .txt
            cur. execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (x,))
            print(x)

  
conn.close()



