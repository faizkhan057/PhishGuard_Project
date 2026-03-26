🛡️ PhishGuard: Intelligent Phishing Detection System
PhishGuard is a lightweight, real-time URL security scanner built to protect users from phishing attacks and "Typosquatting" (fake domains like faceb00k or 1inkdin). It combines a local SQL blacklist with a powerful heuristic engine to categorize links as Safe, Suspicious, or Malicious.

🚀 Key Features

 * Typosquatting Detection: Automatically identifies character substitutions (e.g., 0 for o, 1 for l) used by hackers to mimic popular brands.
   
 * Heuristic Scoring Engine: Analyzes URL structures, suspicious keywords (login, verify, bank), and high-risk TLDs (.xyz, .top, .tk).
   
 * Hybrid Security Logic: Cross-references URLs against a local SQLite blacklist while simultaneously running pattern analysis for "Zero-Day" threats.
   
 * Responsive Web UI: A clean, modern interface designed for both desktop and mobile users.
   
 * Audit Logging: Every scan is timestamped and logged into a database for security monitoring.
   
🛠️ Tech Stack

 * Backend: Python 3 (Flask Framework)
 * Database: SQLite3
 * Frontend: HTML5, CSS3 (Inter & Space Grotesk Fonts)
 * Deployment: Render / GitHub
   
📂 Project Structure

PhishGuard/
├── app.py              # Core logic & Flask server
├── init_db.py          # Database schema initialization
├── phishguard.db       # SQLite database file
├── requirements.txt    # Project dependencies
└── templates/
    └── index.html      # Frontend user interface

⚙️ Installation & Setup

 * Clone the Repository:
   git clone https://github.com/your-username/PhishGuard.git

 * Install Dependencies:
   pip install flask gunicorn

 * Initialize Database:
   python init_db.py

 * Run the Application:
   python app.py

🔍 How it Works
The system follows a three-step verification process:
 * Pattern Check: Scans for "looks-alike" characters (e.g., vv instead of w).
 * Keyword Analysis: Looks for high-pressure words like update-account or secure-login.
 * Blacklist Lookup: Checks if the domain exists in the known malicious database.
Developed by: MD Faiz Khan
Cyber Security Capstone Project 2026

💡 Final Tip for your PDF:
Since you are submitting this for a Capstone Project, make sure to mention in your "Methodology" section that you chose the Heuristic Engine approach to keep the app fast and efficient on mobile devices (Pydroid).
Mubarak ho Faiz! Your GitHub is now ready for submission. Would you like me to draft the final Project Conclusion for your PDF report?
