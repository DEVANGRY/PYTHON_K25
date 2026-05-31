# list
list_user = ["trí hùng" , "Thiện Nhân" , "Thành long"]
list_user[0] = "tên mới"

# tuple ()
tuple_user = ("Việt Dũng bé bỏng" , "Gia bảo đáng yêu" , "Đức Thuy")
# tuple_user[0] = "Dũng chưa có người yêu"

tuple_user = ("Tuấn" , "An" , "DeV")
print(tuple_user)

# Bỏ ngoặc tròn luôn 
tuple_user = "Tuấn" , "An" , "DeV"

tuple_ages = 18,
print(type(tuple_ages))

# Làm việc với DICT 
# init
info_user = {
    "id_user" : "01",
    "name_user" : "Vũ Văn Hiếu",
    "age" : 20,
    "sex" : "other",
    "address" : {
        "id_address" : 1,
        "name_address" : "Hai phong khong long vong"
    },
    "is_status" : True,
    "year_exc" : [1,1,2080],
    "res" : "Chui thay"
} 

# Read 
# Vũ Văn Hiếu đi bệnh viện vì chui thay
# 2 cách để lấy value :

# Cách 1 : disc["key"]
print(f"{info_user['name_user']} đi bệnh viện vì {info_user['res']}")

# Cách 2 : .get("key")
print(f"{info_user.get("name_user_","Thuy Bé Bỏng")} {info_user.get("age")} tuổi")


# Create 
# Thêm thuộc tính số điện thoại vào trong dict info_user

info_user["phone"] = "08888888888"

print(info_user)

# Update 

info_user["phone"] = "099999999"

print(info_user)

# Delete 
res = info_user.pop("res")

print(res)


# Duyệt key 
for key in info_user.keys():
    print(f"Key : {key}")

# Duyệt value 
for value in info_user.values():
    print(f"Value : {value}")

# Duyệt qua key : value
for key, value in info_user.items():
    print(f"key :{key} , value : {value}")

list = [1,2,3,4,5]

find_number = 2

if find_number in list :
    print("Đã tìm ra sản phẩm")
else :
    print("Không tìm thấy sản phẩm")