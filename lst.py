# fav_fruits = ["apple","banana","oramge"]

# fav_fruits.append("mango")
# fav_fruits.remove("banana")
# fav_fruits[0] = ("cherry")
# print(fav_fruits)

# list = [1,2,3,4,5,6,7]
# x  = (list[1:]) # to print the value except the first the  element
# y = (list[::-1]) # reverse the list
# print(x)
# print(y)


# numbers = [1,2,3,4,5]
# for x in numbers:
#     result = x * 2
#     print(result)






# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for x in list:
#     y = x * x
#     print(f"The square of {x} is {y}")
#     if y % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")


# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]
#           ]

# print("second element of the first list:",matrix[0][1])



# people = {
#     "alice": 22,
#     "bob":23,
#     "ritesh":24,
#     "rubash":25,
#     "bibek":28,
# }
# print("intial dictionary",people)

# people["bibek"] = 28
# print("after adding in dictionary",people)
# removed_person = people.pop("bob","not_found")
# print("dictionary after removal",)


# print("Dictionary after removal:", people)




# people = {
#     "ritesh": 21,
#     "hari":34,
#     "shyam":45,
#     "xya": 34,
# } 
# person_name = "hari"
# age = people.get("person_name")
# print(f"The age of {person_name} is: {age}")



# sample_dict = {
#     "apple": 10,
#     # "banana": 20,
#     "cherry": 30
# }

# for key, value in sample_dict.items():
#     print(f"Key: {key}, Value: {value}")


# sample_dict = {
#     "apple": 10,
#     "banana": 20,
#     "cherry": 30
# }


# target_value  = 10
# key_with_value = [key for key, value in sample_dict.items() if value == target_value]
# print(f"Keys with value {target_value}: {keys_with_value}")


# sample_dict = {
#     "apple": 10,
#     "banana": 20,
#     "cherry": 30
# }


# print("Keys:", sample_dict.keys())
# print("Values:", sample_dict.values())
# print("Items:", sample_dict.items())




# students_scores = {
#     "Alice": {"Math": 85, "Science": 92, "English": 88},
#     "Bob": {"Math": 78, "Science": 80, "English": 85},
#     "Charlie": {"Math": 90, "Science": 85, "English": 91}
# }


# print(students_scores)
# student_name = "Alice"
# subject_name = "Science"
# score = students_scores.get(student_name, {}).get(subject_name, "Score not found")
# print(f"{student_name}'s score in {subject_name}: {score}")

# Given data
product_info = {
    "Product1": {"category": "Electronics", "brand": "BrandA"},
    "Product2": {"category": "Clothing", "brand": "BrandB"}
}

product_sales = {
    "Product1": {"sales": 1500, "price": 200},
    "Product2": {"sales": 500, "price": 50}
}

# Initialize an empty dictionary to store the merged result
merged_dict = {}

# Iterate through the keys in product_info (we can assume the keys are the same in both dictionaries)
for product in product_info:
    # Merge the data: nest product_info under 'details' and add product_sales data
    merged_dict[product] = {
        "details": product_info.get(product, {}),  # Use get to safely retrieve data
        "sales": product_sales.get(product, {}).get("sales", 0),  # Default 0 if not found
        "price": product_sales.get(product, {}).get("price", 0)  # Default 0 if not found
    }

# Print the final merged dictionary
print(merged_dict)
