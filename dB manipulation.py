import sqlite3 #Have to import the sqlite3 module
conn = sqlite3.connect('practiceFiles.db') #Database will be titled practiceFiles since I'm dealing mostly with sorting files for this exercise
with conn:
    c = conn.cursor() # c = conn.cursor() is assigning conn.cursor() to a variable that will make it easier and quicker to work with
    #Creating a table for the two required fields
    c.execute ("CREATE TABLE IF NOT EXISTS tbl_FILES (\
                    generated_id INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fileName TEXT)")
    #Since we now have a table called FILES with an autoincremented generated_id column and a text file_Name column, we're ready to
    #actually build the DB by committing it.
    conn.commit() #committing so that we'll actually have a table to play with
conn = sqlite3.connect('practiceFiles.db')

#tuple of fileNames
fileNames_tuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', \
                  'myPhoto.jpg')

#Setting up the conditional statement with which only .txt files will be displayed
for x in fileNames_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value of each row will be one name out of the tuple therefore (x,)
        # will denote a one element tuple for each fileName with a .txt extension
            cur.execute("INSERT INTO tbl_Files (col_fileName) VALUES (?)", (x,))
            print(x)
conn.close()
    

                            
