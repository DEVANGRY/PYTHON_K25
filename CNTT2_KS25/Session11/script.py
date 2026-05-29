# list
list_user = ["an" , "nam" , "hùng"]
list_user[1] = "Tuấn"

# tuple ()
list_user_fix = (1,2,3,4,5)

list_user_fix_v2 = 1,2,3
print(type(list_user_fix_v2))
# Bất biến 
# list_user_fix_v2[1] = 3

list_user_fix_v2 = (2,3,4)

tuple_age = (1,)
print(type(tuple_age))

# dict {}

info_user = {
    "id_user" : 1,
    "name" : "Đối Tượng Cao Nguyễn Anh Dương",
    "age" : 16,
    "address" : {
        "address_id" : 1,
        "address_name" : "Hà Lội 2"
    },
    "is_status" : True,
    "year_exc" : (1,1,2040)
}
# Cách truy cập value trong dict
# .get("key",giá trị mặc định) 
print(f"Quê của đối tượng ở {info_user.get("address").get("address_name")}")

# dict["key"]
print(f"Tuổi của đối tượng {info_user['age']}")

# dict["key"] : Trường hợp không có key thỏa mãn => keyError
# print(f"Tuổi của đối tượng {info_user['tuan']}")

# .get("key",giá trị mặc định) : trường hợp không cóc key thỏa mãn 
print(f"Quê của đối tượng ở {info_user.get("tuan","Hà lội 1")}")

# Update 
info_user["is_status"] = False

info_user.update({"is_status" : True})

print(info_user.get("is_status" , False))

# Create 
info_user["sex"] = "Nữ"
print(info_user)

# Delete .pop("Key")
sex_info = info_user.pop("sex")
print(sex_info)

# duyệt qua key 
for key in info_user.keys():
    print(f"Các key : {key}")

# duyệt qua value
for value in info_user.values():
    print(f"Các value {value}")

# duyệt qua key : value
for key,value in info_user.items():
    print(f"Key : {key} , value : {value}")




