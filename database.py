import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="forensic_investigation"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS evidences_duplicate(hair_colour TEXT, complexion TEXT, blood_group TEXT, eye_colour TEXT, DNA TEXT)')


def add_data(hair_colour, complexion, blood_group, eye_colour, DNA):
    c.execute('INSERT INTO evidences(hair_colour, complexion, blood_group, eye_colour, DNA) VALUES (%s,%s,%s,%s,%s)',
              (hair_colour, complexion, blood_group, eye_colour, DNA))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM evidences')
    data = c.fetchall()
    return data


def view_only_DNA():
    c.execute('SELECT DNA FROM evidences')
    data = c.fetchall()
    return data


def get_DNA(DNA):
    c.execute('SELECT * FROM evidences WHERE DNA="{}"'.format(DNA))
    data = c.fetchall()
    return data

def edit_DNA(new_hair_colour, new_complexion, new_blood_group, new_eye_colour, new_DNA, hair_colour, complexion, blood_group, eye_colour, DNA):
    c.execute("SET FOREIGN_KEY_CHECKS=0 ")
    c.execute("UPDATE evidences SET hair_colour=%s, complexion=%s, blood_group=%s, eye_colour=%s, DNA=%s WHERE hair_colour=%s AND complexion=%s AND blood_group=%s AND eye_colour=%s AND DNA=%s", (new_hair_colour, new_complexion, new_blood_group, new_eye_colour, new_DNA, hair_colour, complexion, blood_group, eye_colour, DNA)) 
    mydb.commit()


def delete_DNA(DNA):
    c.execute('DELETE FROM evidences WHERE DNA="{}"'.format(DNA))
    mydb.commit()