#! /Users/shaunjayaraj/.pyenv/shims/python

def main():
    list = [7, 2, 1, 33, 5, 22, 8]
    final_list = sort(list)

    print("Final sorted List is : {}".format(final_list))

def sort(list):
    splitting_idx = int(len(list)/2)
    print("splitting index is: {}".format(splitting_idx))
    left_list = list[:splitting_idx]
    right_list = list[splitting_idx:]
    if(splitting_idx > 0):
        print("list 1: {}".format(left_list))
        print("list 2: {}".format(right_list))
        result_left_list = sort(left_list)
        result_right_list = sort(right_list)
        return get_single_list_in_sorted_order(result_left_list,result_right_list)
    else: 
        print("returning list: {}".format(list))
        return list
    


def get_single_list_in_sorted_order(left_list,right_list):
    
    if left_list and right_list:
        print("Merging 1: {}".format(left_list))
        print("Merging 2: {}".format(right_list))
        left_list.extend(right_list)
        sorted_list = sorted(left_list)
        print("sorted List: {}".format(sorted_list))
        return sorted_list
    else:
        return None

if __name__ == '__main__':
    main()