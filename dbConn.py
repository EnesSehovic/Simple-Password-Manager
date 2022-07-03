import sqlite3

conn = sqlite3.connect('workDB.db')# IF THE DB DOESN'T EXIST IT'LL CREATE A BLANK

c = conn.cursor()

def checkIfExistsDB(nameOfYourTable):
    s = c.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nameOfYourTable}'").fetchall()
    conn.commit()
    return(s)

def createTableDB():
    c.execute('''CREATE TABLE person(
                id INTEGER PRIMARY KEY,
                first TEXT NOT NULL,
                last TEXT NOT NULL,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                website TEXT NOT NULL,
                password TEXT NOT NULL)''')
    conn.commit()

checkIfExistsDB('person')
if checkIfExistsDB != []:
    pass
else:
    createTableDB()

def getOneWebsiteInfo(webpage):
    s = []
    s = c.execute('SELECT * FROM person WHERE website = ?', (webpage, ))
    try:
        return(s.fetchall()[0])
    except IndexError:
        pass

def addNewContact(contactDict):
    c.execute('INSERT INTO person(first, last, username, email, website, password) VALUES (?, ?, ?, ?, ?, ?)', (contactDict['first'], contactDict['last'], contactDict['username'], contactDict['email'], contactDict['website'], contactDict['password']))
    conn.commit()

def getAllInfo():
    s = c.execute('SELECT first, last, username, email, website, password FROM person')
    return(s.fetchall())
    
