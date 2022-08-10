def maximum_number(list, output_to_terminal = False):
    max_num = list[0]
    for value in list:
        if value > max_num:
            max_num = value
    if output_to_terminal == True:
        print(max_num)
    else:
        return max_num
