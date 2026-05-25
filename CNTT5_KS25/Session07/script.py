full_name = "Phạm Việt Dũng bé bỏng , đẳng cấp bé bỏng"

print(full_name[0])
# Lấy số lượng ký tự len()
print(len(full_name))

print(full_name[-2])

# full_name[9] = "t"

# slicing : Cắt chuỗi

# biến[start:end:step]
name = full_name[:4]

print(name)


print(full_name[::-1])

status = "Đáng Yêu"

full_name_vip = full_name + " " + status
print(full_name_vip)


# Nhân bản (*)
full_name_vip_v2 = full_name_vip + (status * 3)
print(full_name_vip_v2)

# Toán tử in và not in 
if "đáng yêu".upper() in full_name_vip_v2.lower() :
    print("Dũng đẳng cấp")
else :
    print("Dũng không có người yêu")

find_index = full_name.find("b")
count_b = full_name.count("b")
print(count_b)

last_name = "   demo 123  a   "
print(last_name.strip())

# replace 
new_user = full_name.replace("bé bỏng", "Không bé bỏng")
print(new_user)

list_user = full_name.split(" ")
print("x".join(list_user))


print(str(1) + "khánh")