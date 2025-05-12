# Exercise Name:
# 	04-List-Occurence-Counter
# Description:
# 	Display all duplicate items from a list
# Given:
# 	sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
# Return:
# 	[20, 60, 30]
# Hint: 
# 	Count occurence of each item in the list and print items occuring more than once.

def find_duplicates(sample_list):
    duplicates = []
    for item in sample_list:
        if sample_list.count(item)>1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicate_items = find_duplicates(sample_list)
print(duplicate_items)