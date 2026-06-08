from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/complaints')
def complaints():

    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM complaints')
    all_complaints = cursor.fetchall()

    total_issues = len(all_complaints)

    pending_issues = sum(
        1 for complaint in all_complaints
        if complaint[4] == "Pending"
    )

    resolved_issues = sum(
        1 for complaint in all_complaints
        if complaint[4] == "Resolved"
    )

    conn.close()

    return render_template(
        'complaints.html',
        complaints=all_complaints,
        total_issues=total_issues,
        pending_issues=pending_issues,
        resolved_issues=resolved_issues
    )


@app.route('/submit', methods=['POST'])
def submit():
    title = request.form['title']
    description = request.form['description']
    category = request.form['category']

    status = "Pending"

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO complaints
        (title, description, category, status)
        VALUES (?, ?, ?, ?)
        ''',
        (title, description, category, status)
    )

    conn.commit()
    conn.close()

    return f"""
    <h1>Issue Submitted Successfully</h1>
    <p><strong>Title:</strong> {title}</p>
    <p><strong>Description:</strong> {description}</p>
    """


if __name__ == '__main__':
    init_db()
    app.run(debug=True)