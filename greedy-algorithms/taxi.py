# https://informatics.msk.ru/mod/statements/view.php?id=77798&chapterid=734#1

def get_best_taxi(distance_list, tariff_list):
    
    ''' 
    Идея решения - смэтчить наименьшее с наибольшим без потери индексов (нужны для вывода).
    В этих целях используем кортеж: (расстояние/тариф, номер в порядке ввода) 
    '''
    # Создаем список сотрудников с их номерами и сортируем по расстоянию
    employees = sorted(((dist, i) for i, dist in enumerate(distance_list, 1)), key=lambda x: x[0])
    
    # Создаем список такси с их номерами и сортируем по тарифу (по убыванию)
    taxis = sorted(((rate, i) for i, rate in enumerate(tariff_list, 1)), key=lambda x: -x[0])
    
    # Сопоставляем сотрудников и такси
    assignments = [(emp[1], taxi[1]) for emp, taxi in zip(employees, taxis)]
    
    # Сортируем по номерам сотрудников и извлекаем номера такси  
    assignments.sort(key=lambda x: x[0])
        
    return [assign[1] for assign in assignments]
        
        

n = int(input())
distance_list = list(map(int, input().split()))
tariff_list = list(map(int, input().split()))

print(' '.join(map(str, get_best_taxi(distance_list, tariff_list))))