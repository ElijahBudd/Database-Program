# Abraham Andersen + Elijah Budd
# 5/15/2025
# Students Database Program Interactions

import sqlite3

def connect_to_database(db_name='students.db'):

    try:
        conn = sqlite3.connect(db_name)
        return conn
        
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def get_cursor(conn):

    try:
        cur = conn.cursor()
        return cur
        
    except sqlite3.Error as e:
        print(f"Error getting cursor: {e}")
        return None


def get_student_by_id(cur, id_number):

    try:
        cur.execute("SELECT * FROM Students WHERE IdNumber=?", (id_number,))
        student = cur.fetchone()
        return student
        
    except sqlite3.Error as e:
        print(f"Error retrieving student: {e}")
        return None

def update_student_email(conn, cur, id_number, new_email):

    try:
        cur.execute("UPDATE Students SET Email=? WHERE IdNumber=?", (new_email, id_number))
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"Email for student with ID {id_number} updated successfully.")
            return True
            
        else:
            print(f"Student with ID {id_number} not found.")
            return False
            
    except sqlite3.Error as e:
        print(f"Error updating email: {e}")
        conn.rollback()
        return False

def display_all_students(cur):

    try:
        cur.execute("SELECT * FROM Students")
        students = cur.fetchall()
        
        if not students:
            print("No students found in the database.")
            return
            
        print("\n--- All Students ---")
        
        for student in students:
            print(student)
            
    except sqlite3.Error as e:
        print(f"Error displaying students: {e}")
        
def main():

    conn = connect_to_database()
    if conn is None:
        return

    cur = get_cursor(conn)
    if cur is None:
        conn.close()
        return

    while True:
        print("\n<<<( Student Database Menu )>>>")
        print("1. Get Student by ID")
        print("2. Update Student Email")
        print("3. Display All Students")
        print("4. Exit")
        print("Enter the corresponding number to use each option")

        choice = input("Enter your choice: ")

        if choice == '1':
            id_number = input("Enter student ID number: ")
            student = get_student_by_id(cur, id_number)
            if student:
                print("--- Student Details: ---")
                print(student)
            else:
                print("Student not found.")
                
        elif choice == '2':
            id_number = input("Enter student ID number: ")
            new_email = input("Enter new email: ")
            update_student_email(conn, cur, id_number, new_email)
            
        elif choice == '3':
            display_all_students(cur)
            
        elif choice == '4':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")
            
    conn.close()
    
if __name__ == '__main__':
    main()
