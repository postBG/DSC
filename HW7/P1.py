def swap(i, j, num_list):
    tmp = num_list[i]
    num_list[i] = num_list[j]
    num_list[j] = tmp


def P1(num_list: list) -> int:
    cnt = 0
    for i in range(len(num_list) - 1, 0, -1):
        for j in range(i):
            if num_list[j + 1] < num_list[j]:
                swap(j, j + 1, num_list)
                cnt += 1
    return cnt
