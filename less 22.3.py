with open('3.txt') as f:
    students = f.readline().split()
    students_winner = int(students[0])
    min_mark_win = int(students[1])
    marks = [int(i) for i in f]
    marks.sort(reverse=True)
    print(marks[9])


