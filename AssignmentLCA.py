# Q1 Part1
my_dict = {"name": "Shubham","rollno.": 26,"age": 18,"course": "B.Tech", "marks": 95
}

print("Student information:")
print(my_dict)

# Q1 Part2

# Add info
my_dict["city"] = "Pune"
print("After adding city:")
print(my_dict)

# Delete info
del my_dict["age"]
print("After deleting age:")
print(my_dict)

# Q2
list1 = ["name", "class", "rollno"]
list2 = ["Jack", "B", 34]

my_dict = dict(zip(list1, list2))

print(my_dict)


# Q3
my_dict = {"name": "Sam","class": "B","rollno": 26,"marks": [65, 87, 67, 94]}

print(sorted(my_dict))

# Q4
my_dict = {"name": "Sam","class": "B","rollno": 27}

keys = list(my_dict.keys())
values = list(my_dict.values())

print("Keys:", keys)
print("Values:", values)


# Q5
mydict = {"marks1": 23,
    "marks2": 123,
    "marks3": 43,
    "marks4": 13,
     "marks5": 39}

values = mydict.values()

mean = sum(values) / len(values)

print("Mean =", mean)


# Q6
my_dict = {"name": ["Yash", "Neel", "Dev"],"rollno": [11, 12, 13],"marks": [78, 56, 98]}

print("a) Name:", my_dict["name"][2])

print("b) Roll no:", my_dict["rollno"][1])

print("c) Greatest marks:", max(my_dict["marks"]))


# Q7
string = input("Enter a string: ")
frequency = {}

for ch in string:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Frequency:", frequency)


# Q8
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

quotient = numerator // denominator
remainder = numerator % denominator

result = (quotient, remainder)

print(result)


# Q9
from datetime import date

d1 = int(input("Enter day of first date: "))
m1 = int(input("Enter month of first date: "))
y1 = int(input("Enter year of first date: "))

d2 = int(input("Enter day of second date: "))
m2 = int(input("Enter month of second date: "))
y2 = int(input("Enter year of second date: "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

difference = abs((date2 - date1).days)

print("Number of days between dates:", difference)