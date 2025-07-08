# https://stepik.org/lesson/1376612/step/13?unit=1393065


# def get_student_stat(student_dict):
    
#     student_stat_dict = {
#         name: round(sum(subjects.values()) / len(subjects), 2)
#         for name, subjects in student_dict.items()
#     }
            
#     return student_stat_dict


# def get_best_subject(sub_dict):
    
#     if not sub_dict:
#         return None
    
#     subject_avg = {
#         subject: round(sum(marks) / len(marks), 2)
#         for subject, marks in sub_dict.items()
#     }
            
#     return max(subject_avg.items(), key=lambda x: x[1])[0]

# n = int(input())
# student_dict = {}
# subject_dict = {}

# for _ in range(n):
#     line = input().split()
#     name = line[0]
#     subjects_count = line[1]
    
#     student_marks = {}
    
#     for i in range(2, len(line), 2):
#         subject = line[i]
#         mark = int(line[i + 1])
#         student_marks[subject] = mark
#         subject_dict.setdefault(subject, []).append(mark)
        
#     student_dict[name] = student_marks
    
# student_stat_dict = get_student_stat(student_dict)
# best_student = max(student_stat_dict.items(), key=lambda x: x[1])[0]
# best_sub = get_best_subject(subject_dict)
 
# print(f'Средние оценки студентов: {student_stat_dict}')
# print(f'Студент с самой высокой средней оценкой: {best_student}')
# print(f'Предмет с самой высокой средней оценкой: {best_sub}')


avg, classes = {}, []
for line in (input().split() for _ in range(int(input()))):
    name, n, *marks = line
    marks[1::2] = map(int, marks[1::2])
    avg[name] = round(sum(marks[1::2]) / int(n), 2)
    classes += [*zip(*[iter(marks)] * 2)]
print(f'''Средние оценки студентов: {avg}
Студент с самой высокой средней оценкой: {max(avg, key=avg.get)}
Предмет с самой высокой средней оценкой: {max(classes, key=lambda x: x[1])[0]}''')