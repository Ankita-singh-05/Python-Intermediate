def merge_sort(num_list):
    low = ()
    high = len(num_list) - 1
    if (low == high):
        return num_list
    else:
        mid = (low + high)
        left_list = num_list[:(mid + 1)] 
        right_list = num_list[(mid + 1):]
        s_left_list = merge_sort(left_list)
        s_right_list = merge_sort(right_list)
        sorted_list = merge(s_left_list, s_right_list)
    return sorted_list
def merge(left_list, right_list):
    i = 0
    j = 0
    sorted_list = []
    while (i < len(left_list) and j <len(right_list)):
        if(left_list[i] <= right_list[j]):
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1
    while(i < len(left_list)):
        sorted_list.append(left_list[i])
        i += 1
    while(j < len(right_list)):
        sorted_list.append(right_list[j])
        j += 1
    return sorted_list

