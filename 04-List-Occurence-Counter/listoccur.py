def find_duplicates(sample_list):
    duplicates = []
    for item in sample_list:
        if sample_list.count(item)>1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
duplicate_items = find_duplicates(sample_list)
print(duplicate_items)