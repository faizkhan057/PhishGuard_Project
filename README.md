🛡️ PhishGuard: Neural Link Detection System
PhishGuard ek lightweight aur modern web application hai jo users ko malicious phishing links se bachane ke liye banaya gaya hai. Yeh tool real-time mein URLs ko scan karta hai aur unhe Safe, Suspicious, ya Malicious categorize karta hai.
🚀 Key Features
 * Real-time Heuristic Analysis: Bina kisi external API ke link ke structure (TLDs aur Keywords) ko analyze karta hai.
 * Blacklist Database: SQLite3 ka use karke known phishing domains ko turant detect karta hai.
 * Activity Logging: Har ek scan ka record backend database mein save hota hai (Audit Trail).
 * Modern UI/UX: Clean, responsive aur dark-themed interface jo use karne mein bohot asaan hai.
 * Zero-False Positive Logic: Optimized algorithms taaki lambe legitimate URLs (jaise Google Drive) ko galti se block na kare.
🛠️ Tech Stack
 * Backend: Python (Flask Framework)
 * Database: SQLite3 (Serverless SQL)
 * Frontend: HTML5, CSS3 (Modern Inter & Space Grotesk Fonts)
 * Tools: Pydroid 3 / VS Code, Git
📂 Project Structure
PhishGuard/
├── app.py              # Main Flask Backend Logic
├── init_db.py          # Database Initialization Script
├── phishguard.db       # SQLite Database File
├── requirements.txt    # Python Dependencies
└── templates/
    └── index.html      # Modern UI Design

⚙️ How to Run
 * Dependencies Install Karein:
   pip install flask

 * Database Initialize Karein:
   python init_db.py

 * Application Start Karein:
   python app.py

 * Browser Mein Open Karein:
   http://localhost:5000 ya http://0.0.0.0:5000
🛡️ Security Logic
System do layers par kaam karta hai:
 * SQL Layer: Database se domain_name match karta hai.
 * Pattern Layer: Suspicious TLDs (jaise .xyz, .top) aur Keywords (jaise login, verify) ko scan karke risk score calculate karta hai.
Developed by: MD Faiz Khan
Cyber Security Capstone Project 2026
💡 Ek Chhoti Si Tip:
Jab aap GitHub par file upload karein, toh ek achha sa Screenshot bhi README mein add kar dena (Optionally). Isse aapka project file bahut impressive lagega.
Kya aapko GitHub par files upload karne mein koi dikkat aa rahi hai? I can guide you through the mobile browser upload process if needed!
