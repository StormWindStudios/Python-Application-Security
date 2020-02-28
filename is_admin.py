import sqlite3

connection = sqlite3.connect('local.db')

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, username TEXT NOT NULL, admin BOOLEAN);")
cursor.execute("INSERT INTO users (username, admin) VALUES ('zac', True);")
cursor.execute("INSERT INTO users (username, admin) VALUES ('Matt', False);")


def is_admin(username):
    cursor.execute("""
        SELECT admin 
        FROM users 
        WHERE username = '%s'
        """ % username
    )
    result = cursor.fetchone()

    if result is None:
        return False

    admin, = result
    return admin


print(is_admin("zac"))
print(is_admin("matt"))

print(is_admin("'; select true; --"))

