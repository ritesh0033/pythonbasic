university_data = {
    "Computer Science": {
        "CS101": {
            "professor": "Dr. Smith",
            "students": [
                {"name": "Alice", "grade": 85, "attendance": 90},
                {"name": "Bob", "grade": 78, "attendance": 75},
                {"name": "Charlie", "grade": 92, "attendance": 88},
            ],
        },
        "CS102": {
            "professor": "Dr. Johnson",
            "students": [
                {"name": "David", "grade": 89, "attendance": 95},
                {"name": "Eve", "grade": 74, "attendance": 80},
            ],
        },
    },
    "Mathematics": {
        "MATH201": {
            "professor": "Dr. Taylor",
            "students": [
                {"name": "Frank", "grade": 93, "attendance": 85},
                {"name": "Grace", "grade": 88, "attendance": 92},
            ],
        },
        "MATH202": {
            "professor": "Dr. White",
            "students": [
                {"name": "Hannah", "grade": 79, "attendance": 70},
                {"name": "Ian", "grade": 95, "attendance": 98},
            ],
        },
    },
}


# for department, courses in university_data.items():
#       for courses, details in courses.items():
#         students = details["students"]
#         #print(students)
#         #students = students.get("grades")
#         gardes = [student.get("grade") for student in students]
#         #print(gardes)
#         averages_gardes = sum(gardes) / len(gardes)
#         print(averages_gardes)        

#to identifystudent with the higest performer


# higest_garde = 0
# top_performers = dict()

# for department, courses in university_data.items():
#     higest_garde = 0  
#     for course_name, details in courses.items(): 
#         students = details["students"]
#         for student in students:
#             name = student.get("name")
#             grade = student.get("grade")
#             attendance = student.get("attendance")

#             if grade > higest_garde: 
#                 higest_garde = grade
#                 top_performers[department] = {  
#                     "name": name,
#                     "grade": grade,
#                     "attendance": attendance,
#                 }

# print(top_performers)


# for department, courses in university_data.items():
#     for course_name, details in courses.items(): 
#         students = details["students"]
#         total_attendance = sum(student["attendance"] for student in students)  # Sum attendance for the course
#         avg_attendance = total_attendance / len(students)  # Calculate average attendance

#         print(f"Course: {course_name}, Average Attendance: {avg_attendance:.2f}%")

#         if avg_attendance > 85:
#             print(f"The course {course_name} has an average attendance above 85%.")
#         else:
#             print(f"The course {course_name} has an average attendance below 85%.")
