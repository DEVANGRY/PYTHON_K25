name = "Hiếu 6 đẹp trai"

print(f"Chữ cái đầu tiên trong biến name : {name[0]}")

for i in range(0,5,1) :
    print(name[i],end="")

# slicing  : Cắt chuỗi 
print(f"\nCách 2 : Lấy chuỗi : {name[0:5:2]}")

#  Đảo ngược chuỗi 
print(name[::-1])

# Nối chuỗi 
status_user = "Lười học"

full_status_user = name + " " + status_user
print(full_status_user)

# Nhân bản chuỗi dùng toán tử *
print((status_user + " ") * 3)

#  Toán tử in : kiểm tra có tồn tại chuỗi trong chuỗi hay không 
full_name = "Hiếu đẳng cấp"
validate = "Cấp"
is_true = validate not in full_name
print(is_true)


# Tìm xem full_name có chữ cấp hay không 
# TÌm chỉ số index của chữ cấp trong full_name
find_index = full_name.find("Cấp")
print(find_index)

# Thay thế trong chuỗi
full_name_new = full_name.replace("đẳng cấp", "không đẳng cấp")
print(full_name_new)

print("-".join(full_name.split(" ")))