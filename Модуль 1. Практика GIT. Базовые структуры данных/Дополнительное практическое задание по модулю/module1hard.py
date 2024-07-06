grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list_2 = sorted(students_list)
first_grades = (sum(grades[0]) / len(grades[0]))
second_grades = (sum(grades[1]) / len(grades[1]))
third_grades = sum(grades[2]) / len(grades[2])
fourth_grades = sum(grades[3]) / len(grades[3])
fifth_grades = sum(grades[4]) / len(grades[4])
total_grades = [first_grades, second_grades, third_grades, fourth_grades, fifth_grades]
total = dict(zip(students_list_2, total_grades))
print(total)
