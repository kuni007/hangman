import sys

input_list = sys.argv[1:]

new_dict = {}

dict_key = 0
dict_value = 0

for val in input_list:
    dict_key = val
    dict_value = len(val)
    new_dict[dict_key]=dict_value

print(new_dict)
