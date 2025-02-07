from flask import Flask, render_template, request, jsonify
import sqlite3
from fuzzywuzzy import process

app = Flask(__name__)

# Connect to SQLite Database
def get_db_connection():
    conn = sqlite3.connect("company.db")
    conn.row_factory = sqlite3.Row  # Return results as dictionaries
    return conn

# Function to process user queries
def process_query(user_query):
    queries = {
        "employees in the Sales department": "SELECT * FROM Employees WHERE Department = 'Sales';",
        "manager of the Engineering department": "SELECT Manager FROM Departments WHERE Name = 'Engineering';",
        "all employees hired after 2021-01-01": "SELECT * FROM Employees WHERE Hire_Date > '2021-01-01';"
    }

    # Find the best match for the query
    best_match = process.extractOne(user_query, queries.keys(), score_cutoff=80)

    if best_match:
        query = queries[best_match[0]]
        conn = get_db_connection()
        result = conn.execute(query).fetchall()
        conn.close()

        # If no results, return a message
        if not result:
            return "<p>No records found.</p>"

        # Convert results to a styled HTML table
        table_html = "<table><tr>"
        table_html += "".join(f"<th>{col}</th>" for col in result[0].keys())  # Table headers
        table_html += "</tr>"

        for row in result:
            table_html += "<tr>" + "".join(f"<td>{row[col]}</td>" for col in row.keys()) + "</tr>"

        table_html += "</table>"

        return table_html
    else:
        return "<p>Sorry, I didn't understand that. Please try again.</p>"

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    user_question = data.get("question", "")
    response = process_query(user_question)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
