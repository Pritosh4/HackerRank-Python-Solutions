english = int(input())
english_roll = set(input().split())
french = int(input())
french_roll = set(input().split())
either = english_roll^french_roll
print(len(either))