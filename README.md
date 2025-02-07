📚 SQLite Chat Assistant
A Python-based chat assistant that processes natural language queries, converts them into SQL, fetches data from an SQLite database, and provides structured responses.

🚀 Features
✅ Supports natural language queries related to employees and departments
✅ Converts user input into SQL queries automatically
✅ Fetches data from an SQLite database and returns formatted results
✅ Handles errors (invalid queries, missing data, etc.) gracefully
✅ Built with Flask and uses NLTK & FuzzyWuzzy for text processing

🏗️ Project Structure
bash
Copy
Edit
/ChatAssistant
│── /static                 # Folder for static assets (images, CSS)
│── /templates              # Folder for HTML templates (if using Flask web UI)
│── chat_assistant.db       # SQLite database file
│── app.py                  # Flask application
│── requirements.txt        # List of dependencies
│── README.md               # Documentation
│── setup.sql               # SQL script to create tables & insert data
🔧 Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/your-repo/chat-assistant.git  
cd chat-assistant  
2️⃣ Create a Virtual Environment (Recommended)
sh
Copy
Edit
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up the Database
sh
Copy
Edit
python setup.py
🏃 Running the Application
1️⃣ Run Flask Server
sh
Copy
Edit
python app.py
2️⃣ Access the Chat Assistant
Open your browser and go to:
📌 http://127.0.0.1:5000/

💬 Example Queries
✅ "Show me all employees in the Sales department."
✅ "Who is the manager of the Engineering department?"
✅ "List all employees hired after 2021-01-01."
✅ "What is the total salary expense for the Sales department?"
✅ "How many employees are in the Marketing department?"

🛠️ Troubleshooting
❌ ModuleNotFoundError: No module named 'fuzzywuzzy'
🔹 Solution: Run pip install fuzzywuzzy python-Levenshtein

❌ Database file missing?
🔹 Solution: Re-run python setup.py to recreate the database


🎯 Future Improvements
🔹 Add more NLP processing for better query understanding
🔹 Improve UI with a chatbot-style interface
🔹 Expand database schema for additional use cases