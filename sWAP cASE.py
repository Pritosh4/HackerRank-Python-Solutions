def swap_case(s):
    answer = ''
    for letter in s:
        if letter == letter.upper():
            answer+=letter.lower()
        else:
            answer+=letter.upper()
            
    return answer

if __name__ == '__main__':
