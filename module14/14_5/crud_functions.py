import sqlite3

def initiate_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    # cursor.execute('DELETE FROM Products')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INT NOT NULL
    );
    ''')
    # for i in range(1, 5):
    #     cursor.execute(
    #         'INSERT INTO Products (title, description, price) VALUES (?,?,?)', (
    #             (f'Продукт {i}', f'Описание {i}', i * 100)
    #         )
    #     )
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
    connection.commit()

def is_included(username):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    check_user = cursor.execute('SELECT * FROM Users WHERE username =?', (username,))
    
    if check_user.fetchone() is not None:
        return True
    else:
        return False

def get_all_products():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, title, description, price FROM Products')
    db = cursor.fetchall()

    connection.commit()
    connection.close()
    return list(db)
