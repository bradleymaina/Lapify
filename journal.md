#2026-05-18
sqlite3 is a database , more like POSTGRE and MongoDb
SQL is the language 

After calling the sqlite3 library , you need to create an object and a cursor.
An object acts as a bridge, tells the database which file to open.
A cursor is the worker , executes the sql commands , it is like the worker that gets stuff from the door (the bridge) and retrives data.
The naming convention for the object is db and the cursor is csr. 
when inserting the values to the table , it is important to not feed the values directly to avoid sql injection like so :

`self.cursor.execute("INSERT INTO Students VALUES (?,?,?,?)", name, (regNo, laptopModel, serialNumber))`


it is good practise to close the database .( end the call)
`db.close()`

