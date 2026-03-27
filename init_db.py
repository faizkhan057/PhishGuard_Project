import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'phishguard.db')

def init_db():
    # Delete Old Files
    if os.path.exists(db_path):
        os.remove(db_path)
        print("Deleted Old files.")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Creating Tables
    cursor.execute('CREATE TABLE blacklisted_urls (id INTEGER PRIMARY KEY, domain_name TEXT UNIQUE, threat_type TEXT)')
    cursor.execute('CREATE TABLE scan_logs (scan_id INTEGER PRIMARY KEY, scanned_url TEXT, result_status TEXT, scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')

    # Data insertion
    test_data = [
        ('paypa1-support.co', 'Credential Theft'),
        ('secure-login-bank.xyz', 'Phishing'),
        ('update-your-password-now.net', 'Malware')
    ]
    
    cursor.executemany('INSERT INTO blacklisted_urls (domain_name, threat_type) VALUES (?, ?)', test_data)
    
    conn.commit()
    conn.close()
    print("New Database 'phishguard.db' Created!")

if __name__ == "__main__":
    init_db()
    
