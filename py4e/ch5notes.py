largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9,13,27,44,2,99,3]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)