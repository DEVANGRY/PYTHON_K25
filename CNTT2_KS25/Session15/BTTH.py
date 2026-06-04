blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]
new_list_user = []
for value in blood_inventory :
    list_split = value.split("-")
    if "" in list_split:
        find_index_empty = list_split.index("")
        list_split[find_index_empty - 1] = list_split[find_index_empty - 1] + "-"
        list_split.pop(find_index_empty)
    new_format_user = ",".join(list_split)
    new_list_user.append(new_format_user)
        # print(find_index_empty)
    print(value.split("-"))
print(new_list_user)