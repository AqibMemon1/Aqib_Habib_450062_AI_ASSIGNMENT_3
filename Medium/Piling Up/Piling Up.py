
Cube = int(input())
ANS = []
for _ in range(Cube):
    n = int(input())
    cube_list = list(map(int, input().split()))

    for _ in range(n-1):
        if cube_list[0] >= cube_list[len(cube_list)-1]:
            a = cube_list[0]
            cube_list.pop(0)
        elif cube_list[0] < cube_list[len(cube_list)-1]:
            a = cube_list[len(cube_list)-1]
            cube_list.pop(len(cube_list)-1)
        else:
            pass

        if len(cube_list) == 1:
            ANS.append("Yes")

        if((cube_list[0] > a) or (cube_list[len(cube_list)-1] > a)):
            ANS.append("No")
            break

print("\n".join(ANS))