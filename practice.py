def find_single(num_list):
    num = 0
    for x in num_list:
        num ^= x
    return num
