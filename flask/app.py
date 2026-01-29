from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    return sqlite3.connect("database.db")

# Create tables
conn = get_db()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS doctor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS patient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS appointment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doctor TEXT,
    patient TEXT
)
""")

conn.commit()
conn.close()

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/doctor')
def doctor():
    return render_template("doctor.html")

@app.route('/patient')
def patient():
    return render_template("patient.html")

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form['name']
    specialization = request.form['specialization']

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO doctor(name, specialization) VALUES (?,?)",
                (name, specialization))
    conn.commit()
    conn.close()

    return redirect('/admin')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    doctor = request.form['doctor']
    patient = request.form['patient']

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO appointment(doctor, patient) VALUES (?,?)",
                (doctor, patient))
    conn.commit()
    conn.close()

    return "Appointment Booked Successfully!"

if __name__ == "__main__":
    app.run(debug=True)