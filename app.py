import os
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'phishguard.db')

def check_url_security(user_url):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        user_url = user_url.lower().strip()
        
        # 1. Database Check
        cursor.execute("SELECT threat_type FROM blacklisted_urls WHERE domain_name = ? OR ? LIKE '%' || domain_name || '%'", (user_url, user_url))
        result = cursor.fetchone()
        
        status = "Safe"
        if result:
            status = "Malicious"
        else:
            # 2. Heuristic Pattern Check (50 character limit REMOVED)
            suspicious_tlds = ['.top', '.xyz', '.club', '.info', '.site', '.tk']
            suspicious_keywords = ['login', 'secure', 'verify', 'update', 'banking', 'account', '00', '1inkdin']
            
            score = 0
            # Agar TLD suspicious hai (Score 2)
            if any(user_url.endswith(tld) for tld in suspicious_tlds): 
                score += 2
            
            # Agar Keyword suspicious hai (Score 1)
            if any(key in user_url for key in suspicious_keywords): 
                score += 1
            
            # Logic: 
            # 3 points = Malicious (TLD + Keyword dono hain)
            # 2 points = Suspicious (Sirf TLD hai)
            # 1 point = Caution/Suspicious (Sirf Keyword hai)
            if score >= 3: 
                status = "Malicious"
            elif score >= 1: 
                status = "Suspicious"
            else:
                status = "Safe"

        # 3. Log into SQLite
        cursor.execute("INSERT INTO scan_logs (scanned_url, result_status) VALUES (?, ?)", (user_url, status))
        conn.commit()
        conn.close()
        return status
    except Exception as e:
        print(f"Error: {e}")
        return "Safe"

@app.route('/', methods=['GET', 'POST'])
def index():
    report = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            status = check_url_security(url)
            report = {"url": url, "status": status}
    return render_template('index.html', report=report)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
