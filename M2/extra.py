print('---Zadanie 1---')

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


print('---Zadanie 2---')
names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}
for name in names:
  first_letter = name[0]

  if first_letter in name_dict:
    if name not in name_dict[first_letter]:
      name_dict[first_letter].append(name)
  else:
    name_dict[first_letter] = [name]

print("Name Dict: {}" .format(name_dict))


print('---Zadanie 3---')

i = 1
num = 30
fibonacci = [1]
while True:
  if i == num:
    break
  fibonacci.append(sum(fibonacci[-2:]))
  i+=1

print(fibonacci)


print('---Zadanie 4--')

a = 1
b = -2
c = -5

def equation(a,b,c):
  delta = (b**2) -4*a*c
  if delta > 0:
    x1 = b*(-1) - delta**(0.5)/2*a
    x2 = b*(-1) + delta**(0.5)/2*a
    return x1, x2
  elif delta == 0:
    return -b/(2*a)
  else:
    return 'Brak rozwiązań'


print(equation(a, b, c))
