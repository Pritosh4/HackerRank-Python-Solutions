if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg = student_marks[query_name]
    average = float((avg[0] + avg[1] + avg[2])/3)
    print("{:.2f}".format(average))