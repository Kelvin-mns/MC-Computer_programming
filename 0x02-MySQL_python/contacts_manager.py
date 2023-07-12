import mysql.connector
import os

DATABASE_USR = os.environ.get("DATABASE_USER")
DATABASE_PWD = os.environ.get("DATABASE_PWD")

database_connection = mysql.connector.connect(
    host="localhost",
    user=DATABASE_USR,
    password=DATABASE_PWD,
    database="contact"
)

def create_contact(name, email, phone):
    cursor = database_connection.cursor()
    query = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

create_contact("kelvin", "kelvinmunsaka38@gmail.com", "+260975222141")

def get_all_contacts():
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts"
    cursor.execute(query)
    contacts = []
    for row in cursor.fetchall():
        contact = {
            "name": row[1],
            "email": row[2],
            "phone": row[3],
        }
        contacts.append(contact)
    # print(type(roes))
    cursor.close() 
    return contacts

contacts = get_all_contacts()
for contact in contacts:
    print(contact)

#updata the contacts
def update_contact(contact_id, name, email, phone):
    cursor = database_connection.cursor()
    query = "UPDATE contacts SET name=%s, email=%s, phone=%s WHERE id=%s"
    values = (name, email, phone, contact_id)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()


update_contact(1, "kelvin", "kelvinatro@.com", "+260975222141")

#Deletes a user
def delete_contacts(contact_id):
    cursor = database_connection.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    values = (contact_id),
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

delete_contacts(1)

# Gets a single User
def get_single_user(contact_id):
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts WHERE id%s"
    values = (contact_id)
    cursor.execute(query, values)
    rows = cursor.fetchone()
    cursor.close()
    return rows

# usage exampie
create_contact("", "john@example.com", "1234567890")
create_contact("john Doe", "john@example.com", "1234567890")

contacts = get_all_contacts()
for contact in contacts:
    print(contact)

update_contact(1, "", "john.doe@example.com", "1234567890")
update_contact(1, "john Doe", "john.doe@example.com", "9876543210")
delete_contacts(1)

database_connection.close()
