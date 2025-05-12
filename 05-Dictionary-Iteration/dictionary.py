def reverse_dict(ascii_dict):
    return {value:key for key,value in ascii_dict.items()}

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
reversed_ascii_dict = reverse_dict(ascii_dict)
print(reversed_ascii_dict)