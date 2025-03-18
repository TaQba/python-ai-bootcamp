exam_points = {
  "Mariusz":30,
  "Mateusz":55,
  "Marta":76,
  "Roman":30,
  "Arleta":59,
  "Adrian": 96,
  "Monika":91,
  "Andrzej":22,
  "Krzysztof":83,
  "Krystyna":93,
  "Piotr":44,
  "Dawid":10,
  "Agnieszka":15
}

failed_students = []
top_students = []

max_score = 0
student = None
for name, points in exam_points.items():
    if points >= 91 and points <= 100:
        top_students.append(name)
    elif points >= 0 and points <= 45:
        failed_students.append(name)

    if max_score < points:
        max_score = points
        student = name


print("Failed students: {}" .format(failed_students))
print("Top students: {}" .format(top_students))
best_student = (student, max_score)
print('{}' .format(best_student))
