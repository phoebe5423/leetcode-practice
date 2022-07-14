def two_sum(unordered_list, sum):
    need_to_check = []
    for i in unordered_list:
        if i in need_to_check:
            return True
        else:
            need_to_check.append(sum - i)
    return False


a = [1, 2, 3, 4]
b = [4, 1, 2, 4]

print(two_sum(a, 7))
print(two_sum(b, 8))
