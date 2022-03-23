K = int(input())
room_number = list(input().split())
single_room = set()
multi_room = set()
for i in room_number:
    if i not in single_room:
        single_room.add(i)
    else:
        multi_room.add(i)

answer = single_room.difference(multi_room)
print(answer.pop())