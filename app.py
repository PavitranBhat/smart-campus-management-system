from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API Running!"

@app.route("/student/<name>")
def student(name):
    data = {
        "student_name": name,
        "course": "Computer Science",
        "status": "Active"
    }
    return jsonify(data)

@app.route("/api/student/<int:id>")
def get_student(id):
    student = {
        "id": id,
        "name": "Pavitra",
        "department": "AI & Data Science"
    }
    return jsonify(student)


if __name__ == "__main__":
    app.run(debug=True)
