import sqlite3

def get_user_data(email):
    conn = sqlite3.connect('users.sqlite')
    cur = conn.cursor()

    #cur.execute('INSERT INTO Profiles (name, email, goal) VALUES (?,?,?)',('Dewashish Mehta','dewashish3590@gmail.com','GATE CSE'))
    #cur.execute('INSERT INTO Profiles (name, email, goal) VALUES (?,?,?)',('Kartik Bhatt','kartikbhatt@gmail.com','GATE CSE'))
    #conn.commit()

    query = "SELECT * FROM Profiles WHERE email = '"+ email + "'"

    cur.execute(query)
    for row in cur:
        obj = {
            "name" : row[0],
            "email" : row[1],
            "goal" : row[2]
        }
        print(obj)
    cur.close()
    conn.close()
    return obj

def put_user_details(name,email,goal):
    conn = sqlite3.connect('users.sqlite')
    cur = conn.cursor()

    query = "'INSERT INTO Profiles (name, email, goal) VALUES (?,?,?)',(name,email,goal)"
    cur.execute(query)
    conn.commit()

