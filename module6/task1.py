student_marks={
    "anmol":92,
    "Rohan": 76,
    "Priya": 85,
    "Sneha": 90,
    "jenny":99,
    "khushi":92
}

string=input("Enter the Student's name: ")

if string in student_marks:
    print(f"{string}'s marks: {student_marks[string]}" )
else:
    print(f"Student not found")