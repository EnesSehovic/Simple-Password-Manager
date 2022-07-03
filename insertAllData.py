# File dbConn.py, wordDB.db and this one need to be in the same folder (current working directory)
def insertData(dataDict):
    from dbConn import conn, checkIfExistsDB, createTableDB    
    #conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    if checkIfExistsDB('person') != []:
        pass
    else:
        createTableDB()
    conn.commit()

    c.execute('INSERT INTO person(first, last, username, email, website, password) VALUES(?, ?, ?, ?, ?, ?)',
            (dataDict['first'], dataDict['last'], dataDict['username'], dataDict['email'], dataDict['website'], dataDict['password']))
    
    conn.commit()

# To enter more data, add as many dictionary copies in the list as you want
# Don't forget to change the values 
contactListDict = [{'first': 'Chris', 'last': 'Mackleine', 'username': 'chrismckk', 'email': 'kleine91@hotmail.com', 'website': 'f95', 'password': 'vibracijass'},
                    {'first': 'Enter your first name', 'last': 'Last name', 'username': 'User name', 'email': 'Email', 'website': 'Website', 'password': 'Password'},]

for i in range(len(contactListDict)):
    insertData(contactListDict[i])