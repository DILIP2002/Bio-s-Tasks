students = []
sec_name = []
second_low =[]
n = int(input(" number : "))
for _ in range(n):
    s_name = input("Name:")
    score = float(input("Grade Score:"))
    students.append([s_name,score])
print("\n Names and Grade of all students:")
print(students)
order = sorted(students, key = lambda x: int(x[1]))
for i in range(n):
    if order[i][1] != order[0][1]:
        second_low = order[i][1]
        break
print("\n second lowest grade:", second =_low)
