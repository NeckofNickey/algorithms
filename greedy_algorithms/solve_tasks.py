# https://informatics.msk.ru/mod/statements/view.php?id=77798&chapterid=2826#1

def get_solve_problems(tasks_list, a):
    
    sorted_tasks_list = sorted(tasks_list, key=lambda x: x[0])
    
    max_solved_tasks = 0
    
    for task in sorted_tasks_list:
        if task[0] <= a:
            a += task[1]
            max_solved_tasks += 1
    
    return max_solved_tasks

n, a = list(map(int, input().split()))

tasks_list = []

for i in range(n):
    tasks_list.append(list(map(int, input().split())))
    
print(get_solve_problems(tasks_list, a))