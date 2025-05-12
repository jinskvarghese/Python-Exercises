# Exercise Name:
# 	03-List-Manipulation
# Description:
# 	Remove items greater than 50 from a list while iterating but without creating a different copy of a list.
# Given:
# 	number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Return:
# 	[10, 20, 30, 40, 50]
# Note:
# 	ID of input and output list should match

def manip(number_list):
    number_list[:]= [num for num in number_list if num<=50]
    return number_list


number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
manip_list = manip(number_list)
print(manip_list)