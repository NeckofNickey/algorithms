# https://informatics.msk.ru/mod/statements/view.php?id=86290&chapterid=3755#1

def guess_number(n, questions, answers):
    
    possible_numbers = set(range(1, n + 1))
    
    for question, answer in zip(questions, answers):
        question_set = set(question)
        if answer == 'YES':
            possible_numbers &= question_set
        if answer == 'NO':
            possible_numbers -= question_set
            
    return ' '.join(map(str, sorted(possible_numbers)))
        
    
n = int(input())

questions = []
answers = []

while True:
    
    line = input().strip()
    
    if line == 'HELP':
        break
    
    questions.append(list(map(int, line.split())))
    
    answer = input().strip()
    
    while answer not in ('YES', 'NO'):
        answer = input().strip()
    answers.append(answer)
    
    
print(guess_number(n, questions, answers))
    



