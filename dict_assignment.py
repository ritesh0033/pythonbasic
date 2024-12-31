
# student = {
#         1:{
#                 "name":"ram",
#                 "marks":{
#                         "math": 30,
#                         "science": 40,
#                         "englist": 502

#                 },
#         },
#         2:{
#                 "name":"shyam",
#                 "marks":{
#                         "math": 40,
#                         "science": 40,
#                         "englist": 50
#                 }
#         },
#         3:{
#                 "name":"hari",
#                 "marks":{
#                         "math": 30,
#                         "science": 60,
#                         "englist": 50
#                 }
#         }
# }




# student={
#     1: {'name': 'Spiderman',
#     'age': 16,
#     'marks': {
#         'maths': 90,
#         'science': 95,
#         'history': 85
#     }},

#           2 : { 'name': 'Tony stark',
#     'age': 22,
#     'marks': {
#         'maths': 99,
#         'science': 95,
#         'history': 98
#     }},
#        3 : { 'name': 'Captain America',
#     'age': 80,
#     'marks': {
#         'maths': 97,
#         'science': 91,
#         'history': 92
#     }}   
         
# }
# stud_number= int(input("enter student number"))
# if stud_number ==1:
#   print(student[1])
# elif stud_number ==2:
#   print(student[2])
# elif stud_number ==3:
#   print(student[3])
# else:
#   print("invalid student number")

#to calculate the total marks of each student

# student= {
#     1: {'name': 'Spiderman',
#     'age': 16,
#     'marks': {
#         'maths': 90,
#         'science': 95,
#         'history': 85
#     }},

#           2 : { 'name': 'Tony stark',
#     'age': 22,
#     'marks': {
#         'maths': 99,
#         'science': 95,
#         'history': 98
#     }},
#        3 : { 'name': 'Captain America',
#     'age': 80,
#     'marks': {
#         'maths': 97,
#         'science': 91,
#         'history': 92
#     }}   
# }


# for student_id, details in student.items():
#     name = details["name"]
#     marks = details["marks"]
#     total_marks = sum(marks.values())  # Total of all marks
#     avg_marks = total_marks / len(marks)  # Calculate average marks
#     print(f"Student: {name}, Total Marks: {total_marks}, Average Marks: {avg_marks:}")



    #to calculate threshold value
student = {
    1: {
        'name': 'Spiderman',
        'age': 16,
        'marks': {
            'maths': 90,
            'science': 95,
            'history': 85
        }
    },
    2: {
        'name': 'Tony Stark',
        'age': 22,
        'marks': {
            'maths': 99,
            'science': 95,
            'history': 98
        }
    },
    3: {
        'name': 'Captain America',
        'age': 80,
        'marks': {
            'maths': 97,
            'science': 91,
            'history': 92
        }
    }
}


threshold = int(input("Enter the marks threshold: "))
print(f"\nStudents who scored more than {threshold} in all subjects:")
for student_id, details in student.items():
    name = details["name"]
    marks = details["marks"]
    if all(score > threshold for score in marks.values()):
        print(f"- {name}")
