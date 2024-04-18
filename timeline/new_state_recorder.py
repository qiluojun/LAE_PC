import sqlite3







def write_state(basic_state):
        
    # Create a connection to the database file
    conn = sqlite3.connect('basic_state.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS basic_state (
            time TEXT,
            tiredness TEXT,
            exhaustion TEXT,
            anxiety TEXT,
            vitality TEXT,
            activeness TEXT
        )
    ''')

    # Insert the values into the database
    cursor.execute('''
        INSERT INTO basic_state (time, tiredness, exhaustion, anxiety, vitality, activeness)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (basic_state['time'], basic_state['tiredness'], basic_state['exhaustion'], basic_state['anxiety'], basic_state['vitality'], basic_state['activeness']))
    # Commit the changes to the database
    conn.commit()
    # Close the database connection
    conn.close()        
    

