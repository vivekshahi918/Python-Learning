# #### List ####
# # List is an ordered collection of items which can be of different types,
# # and it is mutable, meaning that we can change its content after creation.

# numbers = [10, 20, 30, 40, 50]
# names = ["Alice", "Bob", "Charlie", "David"]

# # print(numbers)
# # print(names)

# # Modify an element in the list
# numbers[2] = 35
# numbers.append(60)  # Add a new element to the end of the list
# numbers.insert(1, 15)  # Insert an element at a specific index
# # print(numbers)
# print(numbers[1:4])
# print(60 in numbers)  # Check if 60 is in the list
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))


# a = [1, 2, 3]
# b = [4, 5, 6]

# a.extend(b)  # Extend list a by appending elements from list b
# # print(a)  # Output: [1, 2, 3, 4, 5, 6]

# ===> TUPLE
# # Tuple is an ordered collection of items which IMMUTABLE, meaning that once it is created, its content cannot be changed.
# numbers = (3, 5, 6, 8, 10)
# print(numbers)
# # numbers[2] = 7  # This will raise an error because tuples are immutable

# print(len(numbers), max(numbers), min(numbers), sum(numbers))


# # ===> SET
# # # Set is an unordered collection of unique items. It is mutable, meaning that we can add or remove elements from it.

# numbers = {2, 4, 6, 8, 10}
# num = {1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 10}
# print(numbers)
# print(num)  # Duplicates will be removed in the set
# print(len(num) == 10)


# ===> SET OPERATION

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# print(A.union(B))  # Union of sets A and B
# print(A.intersection(B))  # Intersection of sets A and B
# print(A.difference(B))  # Difference of sets A and B
# print(A | B)  # Union using the | operator
# print(A & B)  # Intersection using the & operator
# print(A - B)  # Difference using the - operator
# print(A ^ B)  # Symmetric difference using the ^ operator

# ===> DICTIONARY
# # Dictionary is an unordered collection of key-value pairs. It is mutable, meaning that we can change its content after creation.

student = {
    "name": "Alice",
    "age": 20,
    "marks": [85, 90, 95]
}
print(student.get("name"))  # Accessing value using key
print(student["age"])  # Accessing value using key  
student["age"] = 21  # Modifying value using key
student["marks"].append(100)  # Modifying value using key
student["city"] = "New York"  # Adding a new key-value pair
# print(student)

# iteration 

for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(key, ":", value)    
    
# --> Dictonary methods
# student.keys()
# student.values()
# student.items()    


# | Operation       | List           | Tuple | Set   | Dictionary    |
# | --------------- | -------------- | ----- | ----  | -------------|
# | Access by index | O(1)           | O(1)  | No   | No            |
# | Search (`in`)   | O(n)           | O(n)  | O(1) | O(1) for keys |
# | Insert at end   | O(1) amortized | NO    | O(1) | O(1)          |
# | Delete          | O(n)           | NO    | O(1) | O(1)          |
# | Update          | O(1)           | NO    | O(1)| O(1)           |
