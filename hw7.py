import sqlite3

db = sqlite3.connect('student.db')

c = db.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user (
name text,
surname text,
hobby text,
birthday text,
mark int
)''')
db.commit()

# c.execute('INSERT INTO user VALUES ("Aza","Azamatov","reading","1 January",10)')
# c.execute('INSERT INTO user VALUES ("Aqa","Aramzanov","seating","1 April",4)')
# c.execute('INSERT INTO user VALUES ("Awa","Afirjanov","runing","8 Mart",10)')
# c.execute('INSERT INTO user VALUES ("Aea","Abdulmanapov","talking","9 May",9)')
# c.execute('INSERT INTO user VALUES ("Ara","Abdyrakhmanov","chewing","7 July",1)')
# c.execute('INSERT INTO user VALUES ("Ata","Batrudinov","hiding","8 June",8)')
# c.execute('INSERT INTO user VALUES ("Aya","Grigoriev","shooting","31 August",10)')
# c.execute('INSERT INTO user VALUES ("Aua","Minov","screeming","1 Sep",2)')
# c.execute('INSERT INTO user VALUES ("Aia","Zabludinov","jumping","21 October",9)')
# c.execute('INSERT INTO user VALUES ("Aoa","Paycharmov","walking","13 November",5)')
# c.execute('INSERT INTO user VALUES ("Apa","Paytanov","boxing","31 December",1)')

c.execute("UPDATE user SET name = 'genius' WHERE mark = 10")
c.execute("SELECT rowid, surname, name FROM user ")

items = c.fetchall()

print(items)

for i in items:
    surname = i[1]
    if len(surname) > 10:
        print(surname)
    else:
        ...

c.execute("SELECT rowid, name FROM user WHERE name = 'genius'")
c.execute("DELETE FROM user WHERE rowid % 2 = 0")




db.commit()
db.close()