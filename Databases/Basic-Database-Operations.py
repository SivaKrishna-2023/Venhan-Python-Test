import sqlite3

# Function to insert a new student into the database
def insert_student(name: str, grade: float):
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        grade REAL
                    )''')
    
    # Insert the new student into the table
    cursor.execute('''INSERT INTO students (name, grade)
                      VALUES (?, ?)''', (name, grade))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

# Example usage
insert_student('John Doe', 85.5)