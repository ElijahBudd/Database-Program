# Abraham Anderson + Elijah Budd
# 5/15/2025
# Students Database Program

import sqlite3

def main():

    conn = sqlite3.connect('students.db')

    cur = conn.cursor()

    add_student_table(cur)

    add_students(cur)

    conn.commit()

    display_students(cur)

    conn.close()

# Create the create table function
def add_student_table(cur):

    cur.execute("DROP TABLE IF EXISTS Students")

    # Create table
    cur.execute('''CREATE TABLE Students (
    FirstName TEXT PRIMARY KEY NOT NULL,
    LastName TEXT,
    IdNumber TEXT,
    DOB TEXT,
    Major TEXT,
    GPA INTEGER,
    Email TEXT)
    ''')

#Create the add students function
def add_students(cur):

    # Add data
    students_pop = [('John', 'Doe', '1389403-01', '1/24/1971', 'Economics', 3.73, 'jjdoe@students.ucw.edu'),
                    ('Mary', 'Jane', '1389403-02', '12/6/1969', 'History', 3.82, 'mjjane@students.ucw.edu'),
                    ('Bill', 'Forbes', '1389403-03', '3/3/1970', 'Areal Photography', 2.21, 'bxforbes@students.ucw.edu'),
                    ('Phin', 'Whignberger', '1389403-04', '2/19/1971', 'English', 2.89, 'plwhignberger@students.ucw.edu'),
                    ('Whit', 'Quiering', '1389403-05', '8/24/1970', 'Physics', 2.44, 'wequiering@students.ucw.edu'),
                    ('Jars', 'Govner', '1389403-06', '11/29/1969', 'Art', 4.00, 'jnGovner@students.ucw.edu'),
                    ('Norma', 'Kinota', '1389403-07', '7/21/1969', 'German', 3.62, 'nhkinota@students.ucw.edu'),
                    ('Mooney', 'Houston', '1389403-08', '7/16/1969', 'Astronomy', 1.20, 'mtxhouston@students.ucw.edu'),
                    ('Caleb', 'Dalten', '1389403-09', '6/4/1972', 'Civil Engineering', 3.25, 'cadalten@students.ucw.edu'),
                    ('Israel', 'Achman', '1389403-10', '10/23/1971', 'Math', 3.84, 'iowachman@students.ucw.edu'),]

    # Insert information into the database
    for row in students_pop:
        cur.execute('''INSERT INTO Students (FirstName, LastName, IdNumber, DOB, Major, GPA, Email)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# Display Data
def display_students(cur):
    cur.execute("SELECT * FROM Students")
    results = cur.fetchall()
    for row in results:
        print(row)

# Call main function
if __name__ == '__main__':
    main()
