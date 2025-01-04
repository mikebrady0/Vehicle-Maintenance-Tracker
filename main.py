import sqlite3

def create_connection(db_file):
    """Create a database connection to SQLite"""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

def create_tables(conn):
    """Create the Vehicles and Maintenance_Tasks tables if they don't exist"""
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Vehicles (
                id INTEGER PRIMARY KEY,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                license_plate TEXT UNIQUE
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Maintenance_Tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                description TEXT,
                frequency INTEGER
            );
        """)
        conn.commit()
        print("Tables created and verified.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def list_tables(conn):
    """List all tables"""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    print("Tables in database: ", tables)

def check_plate(conn, license_plate):
    """Check if a vehicle with the given license plate exists"""
    sql = "SELECT id FROM Vehicles WHERE license_plate = ?"
    cur = conn.cursor()
    cur.execute(sql, (license_plate,))  # Wrap in a tuple
    return cur.fetchone() is not None

def add_vehicle(conn, vehicle):
    """Add a new vehicle to the Vehicles table"""
    make, model, year, license_plate = vehicle
    if check_plate(conn, license_plate):  # Pass only the license plate
        print(f"Vehicle with license plate {license_plate} already exists.")
        return None
    
    sql = """INSERT INTO Vehicles (make, model, year, license_plate)
             VALUES (?, ?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, vehicle)
    conn.commit()
    return cur.lastrowid

def add_task(conn, task):
    """Add a new maintenance task to the Maintenance_Tasks table"""
    sql = """INSERT INTO Maintenance_Tasks (task_name, description, frequency)
             VALUES (?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

if __name__ == "__main__":
    database = "vehicle.db"
    conn = create_connection(database)
    
    if conn:
        create_tables(conn)
        list_tables(conn)
    
    with conn:
        year = int(input('Enter year: '))
        make = input('Enter make: ')
        model = input('Enter model: ')
        plate = input('Enter license plate: ')
        
        new_vehicle = (make, model, year, plate)
        vehicle_id = add_vehicle(conn, new_vehicle)
        print("Vehicle ID:", vehicle_id)
        
        task = input('Enter maintenance task: ')
        task_desc = input('Enter description: ')
        frequency = int(input("Enter frequency in miles: "))
        
        new_task = (task, task_desc, frequency)
        task_id = add_task(conn, new_task)
        print("Task ID: ", task_id)
