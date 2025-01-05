### README for Vehicle Maintenance Tracker

---

## **Vehicle Maintenance Tracker**

The **Vehicle Maintenance Tracker** is a Python-based application that uses SQLite to manage and store data about vehicles and their maintenance tasks. It allows users to record vehicle details and schedule maintenance tasks efficiently.

---

## **Features**

- **Vehicle Management**:  
  Add vehicles with details like make, model, year, and license plate. Duplicate license plates are not allowed, ensuring data integrity.
  
- **Maintenance Tasks**:  
  Create and store maintenance tasks, including task name, description, and frequency (in miles).

- **Database Tables**:  
  - **Vehicles Table**: Stores vehicle details with unique license plates.  
  - **Maintenance_Tasks Table**: Keeps track of maintenance task information.

- **Table Listing**:  
  View all tables in the SQLite database for debugging or verification purposes.

---

## **Technologies Used**

- **Programming Language**: Python 3  
- **Database**: SQLite  
- **Modules**:  
  - `sqlite3`: For database management.  

---

## **Getting Started**

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of Python and SQLite.

---

### Installation

1. Clone this repository or download the source code:
    ```bash
    git clone <repository-url>
    cd Vehicle-Maintenance-Tracker
    ```
2. Ensure Python is installed. You can verify this by running:
    ```bash
    python --version
    ```
3. Install any required libraries (if not already installed):
    ```bash
    pip install sqlite3
    ```
   *(Note: `sqlite3` is included in Python’s standard library, so installation might not be necessary.)*

---

### How to Run

1. Run the Python script:
    ```bash
    python main.py
    ```
2. Follow the prompts to:
   - Add a new vehicle by entering its **year**, **make**, **model**, and **license plate**.
   - Add a maintenance task by providing its **name**, **description**, and **frequency (in miles)**.

---

## **Database Structure**

### **1. Vehicles Table**
Stores details about vehicles:
| Column           | Data Type   | Constraints               |
|-------------------|-------------|---------------------------|
| `id`             | INTEGER     | PRIMARY KEY               |
| `make`           | TEXT        | NOT NULL                  |
| `model`          | TEXT        | NOT NULL                  |
| `year`           | INTEGER     | NOT NULL                  |
| `license_plate`  | TEXT        | UNIQUE                    |

### **2. Maintenance_Tasks Table**
Keeps track of maintenance tasks:
| Column           | Data Type   | Constraints               |
|-------------------|-------------|---------------------------|
| `id`             | INTEGER     | PRIMARY KEY, AUTOINCREMENT|
| `task_name`      | TEXT        | NOT NULL                  |
| `description`    | TEXT        |                           |
| `frequency`      | INTEGER     |                           |

---

## **Usage Examples**

### Adding a Vehicle:
Input values for:
- **Year**: `2023`  
- **Make**: `Toyota`  
- **Model**: `Camry`  
- **License Plate**: `ABC123`

The application will save this information to the `Vehicles` table.

---

### Adding a Maintenance Task:
Input values for:
- **Task Name**: `Oil Change`  
- **Description**: `Replace engine oil`  
- **Frequency**: `5000` miles  

The application will save this information to the `Maintenance_Tasks` table.

---

## **Known Issues**

- Ensure the SQLite database file (`vehicle.db`) is in the same directory as the script to avoid connection errors.
- License plates must be unique. Duplicate entries will be rejected.

---

## **Contributors**

- **Michael Brady**  
---

## **License**

This project is licensed under the MIT License. Feel free to use and modify it as needed. 

---

Feel free to let me know if you'd like further modifications!
