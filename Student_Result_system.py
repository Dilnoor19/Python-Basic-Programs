Student_name = input("Enter Your Name--> ")

subjects = []
marks = []

print("--- 5 Subjects aur Unke Marks Enter Karo ---")


for i in range(1, 6):
    sub_name = input(f"\nSubject {i} ka naam: ")
    sub_mark = float(input(f"{sub_name} ke marks (out of 100): "))
    
    subjects.append(sub_name)
    marks.append(sub_mark)

total_obtained = sum(marks)
max_marks = 500
percentage = (total_obtained / max_marks) * 100

print("\n" + "="*35)
print(f"          {Student_name} RESULT")
print("="*35)

for i in range(5):
    print(f"{subjects[i]} : {marks[i]} / 100")

print("-" * 35)
print(f"Total Marks Obtained : {total_obtained} / {max_marks}")
print(f"Percentage           : {percentage:.2f}%")
print("="*35)