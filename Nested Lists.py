if __name__ == '__main__':
    rec = []
    records = []
    score_list = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in score_list:
            score_list.append(score)
        rec = [name, score]
        records.append(rec)
        rec = []
    score_list.sort()
    for i in range(0, len(records)):
        if records[i][1] == score_list[1]:
            names.append(records[i][0])
    for ele in sorted(names):
        print(ele)
