import sqlite3
import os

DB_PATH = "C:/Users/kaytn/cable_fault_predictor/data/snmp_poll_data.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS snmp_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            device TEXT,
            interface TEXT,
            in_octets INTEGER,
            out_octets INTEGER,
            in_errors INTEGER,
            out_errors INTEGER,
            speed INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(records):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    for r in records:
        c.execute('''
            INSERT INTO snmp_stats (
                timestamp, device, interface,
                in_octets, out_octets, in_errors, out_errors, speed
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            r['timestamp'], r['device'], r['interface'],
            r['in_octets'], r['out_octets'],
            r['in_errors'], r['out_errors'], r['speed']
        ))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_db()
