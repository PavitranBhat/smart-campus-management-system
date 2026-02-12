from flask import Flask, request, jsonify
from services.campus_service import CampusService

app = Flask(__name__)

campus_service = CampusService()


@app.route("/")
def home():
    return "Smart Campus Management System API Running", 200


# -----------------------------
# STUDENT ROUTES
# -----------------------------

@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    student = campus_service.add_student(
        data.get("id"),
        data.get("name"),
        data.get("department"),
        data.get("year")
    )

    if not student:
        return jsonify({"error": "Student already exists"}), 400

    return jsonify(student.display_info()), 201


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(campus_service.get_all_students()), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = campus_service.get_student(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.display_info()), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()

    student = campus_service.update_student(student_id, data)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(student.display_info()), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = campus_service.delete_student(student_id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"}), 200


# -----------------------------
# FACULTY ROUTES
# -----------------------------

@app.route("/faculties", methods=["POST"])
def create_faculty():
    data = request.get_json()

    faculty = campus_service.add_faculty(
        data.get("id"),
        data.get("name"),
        data.get("specialization")
    )

    if not faculty:
        return jsonify({"error": "Faculty already exists"}), 400

    return jsonify(faculty.display_info()), 201


@app.route("/faculties", methods=["GET"])
def get_faculties():
    return jsonify(campus_service.get_all_faculties()), 200


# -----------------------------
# COURSE ROUTES
# -----------------------------

@app.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()

    course = campus_service.add_course(
        data.get("id"),
        data.get("title")
    )

    if not course:
        return jsonify({"error": "Course already exists"}), 400

    return jsonify({"message": "Course created successfully"}), 201


@app.route("/courses/<int:course_id>/enroll/<int:student_id>", methods=["POST"])
def enroll_student(course_id, student_id):
    course = campus_service.enroll_student_to_course(course_id, student_id)

    if not course:
        return jsonify({"error": "Course or Student not found"}), 404

    return jsonify(course.get_course_info()), 200

@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    required_fields = ["id", "name", "department", "year"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    student = campus_service.add_student(
        data["id"],
        data["name"],
        data["department"],
        data["year"]
    )

    if not student:
        return jsonify({"error": "Student already exists"}), 400

    return jsonify(student.display_info()), 201



if __name__ == "__main__":
    app.run(debug=True)
