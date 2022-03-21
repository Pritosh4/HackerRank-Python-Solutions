def count_substring(string, sub_string):
    counter, sum = 0, 0
    for i in range(0, len(string)):
        if (string[counter:(len(sub_string) + counter)] == sub_string):
            sum = sum + 1
        counter = counter + 1
    return sum


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)