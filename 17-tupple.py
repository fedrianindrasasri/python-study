# tupple = collection which is ordered and unchangeable
# digunakan untuk menggrupkan data yang terkait

student = ("Fedrian", 21, "male")

print(student.count("Fedrian"))

print(student.index("male"))

print(student[0])

for x in student:
    print(x)

if "Fedrian" in student:
    print("Fedrian is here")
