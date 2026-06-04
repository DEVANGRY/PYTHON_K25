from functools import reduce

infor_user = " Chu Gia Huy - 18 - other - Phú Thọ - Có chồng"

# .strip() : Bỏ khoảng trắng thừa ở hai đầu 

# .split : Tách một chuỗi thành một danh sách 
list_info_user = infor_user.strip().split("-")
# print(list_info_user)

# Tạo một hàm : có chức năng nhận vào một chuỗi và nhận vào ký tự muốn cắt
#  => cắt chuỗi thành list mong muốn 
def split_string (info_string , string_spl):
    return info_string.strip().split(string_spl)

print(split_string(infor_user,"-"))

new_infor = split_string(infor_user,"-")

# .join()
info_user_new_format = " , ".join(new_infor)
print(info_user_new_format)

# .replace(x, y) : Thay thế chuỗi 
new_infor_replace = infor_user.replace("other", "Nam")
print(f"Replace : {new_infor_replace}")

# .format_map() : thay thế giá trị trong chuỗi + dict
info_player = {
    "name" : "Dương",
    "age" : 18,
    "sex" : "Other"
}

text_info = "Tên tôi là : {name}, Tuổi tôi là {age}, Giới tình của tôi là : {sex}"

print(text_info.format_map(info_player))

# lambda 
# Tạo một hàm có mục đích tính tổng 2 đối số truyền vào 
def calc_sum (a,b):
    return a + b

calc_sum_v2 = lambda a,b : a + b

print(calc_sum_v2(1,2))

# map : thao tác với danh sách (list) => Thay đổi các giá trị trong danh sách 
list_money = [1,2,3,4,5,6]

# Lấy một danh sách chứa giá gấp đôi danh sách cũ 
# [2,4,6,]

# map(, iterables)
list_new = list(map(lambda number : number * 2 , list_money))
print(list_new)

list_user = [
    {"id" : 1 , "name" : "Tuấn" , "age" : 20},
    {"id" : 2 , "name" : "An" , "age" : 18},
    {"id" : 3 , "name" : "Dương" , "age" : 16},
    {"id" : 4 , "name" : "Dev" , "age" : 30}
]

# Tạo một hàm để lọc những nhân viên có tuổi lớn hơn 18 

# filter(function, iterable)
new_list_filter = list(filter(lambda user : user["age"] > 18 , list_user))
print(new_list_filter)


list_money = [1,2,3,4,5,6]
new_list_money = list(filter(lambda x : x % 2 != 0  , list_money))
print(new_list_money)

# reduce() : Tích lũy giá trị 
list_money = [1,2,3,4,5,6]
total = reduce(lambda tong , value_hien_tai : tong + value_hien_tai , list_money)
print(total)

# sort : Sắp xếp thay đổi trực tiếp danh sách 
# sorted(iterable, key=key, reverse=reverse) : tạo một danh sách mới đã được xắp sếp 

list_money = [1,2,3,4,5,6,21,-1,20,2,4]
print(sorted(list_money))


list_user = [
    {"id" : 1 , "name" : "Tuấn" , "age" : 20},
    {"id" : 2 , "name" : "An" , "age" : 18},
    {"id" : 3 , "name" : "Dương" , "age" : 16},
    {"id" : 4 , "name" : "Dev" , "age" : 30}
]
# Tạo hàm để in ra danh sách nhân viên tăng dần theo tuổi 
def sort_user_by_age (list):
    print(sorted(list,key=lambda user : user["age"]))
    
sort_user_by_age(list_user)

