from functools import reduce

infor_user = "Phạm Việt Dũng - 18 - Dạy đánh tenis - Other - Quảng Ling"

# split : để cắt chuỗi thành list

list_info_user = infor_user.split(" - ")
print(list_info_user)

list_info_user = infor_user.split("Việt")
print(list_info_user)

list_info_user = infor_user.split("Dạy")
print(list_info_user)

# .join() : Nối một danh sách các phần tử thành một chuỗi 

list_info_user_01 = ['Phạm Việt Dũng', '18', 'Dạy đánh tenis', 'Other', 'Quảng Ling']

text_info_user =  (":").join(list_info_user_01)
print(text_info_user)

infor_user = "Phạm Việt Dũng - 18 - Dạy đánh tenis - Other - Quảng Ling"

# trả về một chuỗi là : "Phạm Việt Dũng ; 18 ; Dạy đánh tenis ; Other ; Quảng Ling"
def change_format_user (info_user) :
    list_info_user = info_user.split("-")
    new_infor_user = (";").join(list_info_user)
    return new_infor_user

print(change_format_user(infor_user))

infor_user = "Phạm Việt Dũng - 18 - Dạy đánh tenis - Other - Quảng Ling"
new_infor_format = infor_user.replace("-", "+")
print(new_infor_format)

print(infor_user.replace("Other", "Nữ"))

# str.format_map() - Template Động
# 	Truyền thẳng dict, hỗ trợ key phức tạp, class tùy chỉnh
# 	Cú pháp: template .format_map(dict)

name = "Tôi là Dũng giới tính Other"
print(f"{name}")

info_user = {
    "name" : "Dũng",
    "age" : 16,
    "Address" : "UFO"
}
# print(f"Tôi tên là {info_user['name']} , Tôi {info_user['age']} tuổi")
text = "Tôi tên là {name} , Tôi {age} tuổi"
print(text.format_map(info_user))


# code hàm tính tổng 2 số bất kỳ 
def handle_sum (a,b) :
    return a + b

handle_sum_v1 = lambda a,b : a + b
print(handle_sum_v1(1,2))

# map() : 
list_number = [2,4,6,8]
# Tạo ra một danh sách mới mà giá trị các phần tử tăng gấp đôi 
# list_new_number = [4,8,12,16]
list_new_number = []
for index in range(len(list_number)):
    value = list_number[index] * 2
    list_new_number.append(value)

print(list_new_number)

# map => duyệt qua danh sách 
list_new_number_map = list(map(lambda number : number * 2, list_number))
print(f"Dùng map để nhân đôi tài sản : {list_new_number_map}")

# filter => Lọc 
list_number = [1,2,3,4,6,8]
list_number_filter = list(filter(lambda number : number > 4 , list_number))
print(list_number_filter)

list_user = [
    {"id":1, "name" : "Tuấn", "age" : 18},
    {"id":2, "name" : "Dũng", "age" : 11},
    {"id":3, "name" : "Thuy", "age" : 30}
]

#  Lọc những người dùng lớn hơn hoặc bằng 18 tuổi 
def handle_filter_user (list_empl) :
    new_list_filter = list(filter(lambda user : user["age"] >= 18 ,list_empl))
    return new_list_filter

print(handle_filter_user(list_user))

# .sort()  : Sắp xếp => thay đổi luôn danh sách cũ     
#  sorted(iterable, key=key, reverse=reverse) : Sắp xếp => Không thay đổi danh sách cũ 

list_age = [99,10,20,18,31,5,2]
list_age.sort(reverse=True)
print(list_age)


list_user = [
    {"id":1, "name" : "Tuấn", "age" : 18},
    {"id":2, "name" : "Dũng", "age" : 11},
    {"id":3, "name" : "Thuy", "age" : 30}
]
# Lấy danh sách các nhân viên có tuổi tăng dần 

def handle_sort (list_emp) :
    new_list_user_sort = sorted(list_emp, key=lambda user : user["age"])
    return new_list_user_sort
print(handle_sort(list_user))

# reduce()
list_age = [99,10,20,18,31,5,2]

total = reduce(lambda tong_cong_don , gia_tri_moi_lan_duyet : tong_cong_don + gia_tri_moi_lan_duyet,list_age , 0)

# sum(list_age)
# max(list_age)
# min(list_age)