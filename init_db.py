import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'phishguard.db')

def init_db():
    
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Purani database delete kar di gayi.")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create Tables
    cursor.execute('CREATE TABLE blacklisted_urls (id INTEGER PRIMARY KEY, domain_name TEXT UNIQUE, threat_type TEXT)')
    cursor.execute('CREATE TABLE scan_logs (scan_id INTEGER PRIMARY KEY, scanned_url TEXT, result_status TEXT, scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')

    # Insert Data
    test_data = [
        ('paypa1-support.co', 'Credential Theft'),
        ('secure-login-bank.xyz', 'Phishing'),
        ('update-your-password-now.net', 'Malware')
    ]
    
    cursor.executemany('INSERT INTO blacklisted_urls (domain_name, threat_type) VALUES (?, ?)', test_data)
    
    conn.commit()
    conn.close()
    print("Nayi database 'phishguard.db' taiyaar hai!")

if __name__ == "__main__":
    init_db()
