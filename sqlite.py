import sqlite3

# Connect to SQLite database (creates if not exists)
connection = sqlite3.connect("registration.db")
cursor = connection.cursor()

# Drop the table if it already exists (for repeatable runs)
cursor.execute("DROP TABLE IF EXISTS REGISTRATION_DATA")

# Create the table
table_info = """
CREATE TABLE REGISTRATION_DATA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    dob TEXT NOT NULL,
    address TEXT NOT NULL
)
"""
cursor.execute(table_info)

# Sample data (15-20 records)
records = [
    ("Alice Johnson", "alice.johnson@example.com", "9876543210", "1990-04-12", "123 Maple Street, NY"),
    ("Bob Smith", "bob.smith@example.com", "9123456780", "1985-09-23", "456 Oak Avenue, CA"),
    ("Carol White", "carol.white@example.com", "9988776655", "1992-07-19", "789 Pine Road, TX"),
    ("David Brown", "david.brown@example.com", "9090909090", "1988-11-05", "321 Birch Blvd, FL"),
    ("Emma Davis", "emma.davis@example.com", "8080808080", "1995-01-22", "654 Cedar St, WA"),
    ("Frank Miller", "frank.miller@example.com", "7070707070", "1991-03-17", "987 Spruce Ln, IL"),
    ("Grace Lee", "grace.lee@example.com", "6060606060", "1993-12-30", "222 Elm Dr, AZ"),
    ("Henry Wilson", "henry.wilson@example.com", "5050505050", "1987-08-09", "333 Fir Ct, NV"),
    ("Ivy Thomas", "ivy.thomas@example.com", "4040404040", "1996-06-15", "444 Willow Pkwy, GA"),
    ("Jack Garcia", "jack.garcia@example.com", "3030303030", "1994-02-10", "555 Redwood Way, CO"),
    ("Kara Martinez", "kara.martinez@example.com", "2020202020", "1997-10-01", "666 Ash Ave, OR"),
    ("Leo Robinson", "leo.robinson@example.com", "1122334455", "1989-05-08", "777 Sequoia St, MI"),
    ("Mia Clark", "mia.clark@example.com", "2233445566", "1990-07-20", "888 Cypress Rd, MO"),
    ("Nathan Lewis", "nathan.lewis@example.com", "3344556677", "1986-04-14", "999 Alder Blvd, TN"),
    ("Olivia Hall", "olivia.hall@example.com", "4455667788", "1998-09-03", "101 Poplar Cir, NC"),
    ("Paul Young", "paul.young@example.com", "5566778899", "1983-03-26", "202 Beech Ln, MA"),
    ("Quincy Allen", "quincy.allen@example.com", "6677889900", "1991-12-11", "303 Dogwood Pl, OH"),
    ("Rachel Scott", "rachel.scott@example.com", "7788990011", "1993-06-06", "404 Magnolia Dr, NJ"),
    ("Steve Adams", "steve.adams@example.com", "8899001122", "1984-02-18", "505 Chestnut Ave, IN"),
    ("Tina Baker", "tina.baker@example.com", "9900112233", "1992-11-29", "606 Walnut Blvd, PA")
]

# Insert data into the table
cursor.executemany("""
INSERT INTO REGISTRATION_DATA (full_name, email, phone, dob, address)
VALUES (?, ?, ?, ?, ?)
""", records)

# Commit and close connection
connection.commit()
connection.close()
print(" Table created and 20 records inserted successfully.")
