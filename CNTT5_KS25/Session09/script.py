# Tạo một danh sách gồm 3 cái tên em ghét nhất trong lớp 
list_user_quan_ap = ["Quân", "Quang Huy" , "Bảo Lâm" , "Giang Long"]

# In ra cái tên mà QUân ghét thứ 3 trong lớp 
print(list_user_quan_ap[2])

# Sửa top 1 thành : Thuy 
list_user_quan_ap[0] = "Thuy"

# Thêm Dũng bé bỏng vào cuối danh sách 
# append() : Thêm vào cuối danh sách 
# name = input("Mời bạn nhập tên")

# list_user_quan_ap.append(name)

# Thêm Minh 2 vào tại vị trí thứ 3 ?
list_user_quan_ap.insert(2,"Minh 2 hắt tê mờ lờ")
print(f"Danh Sách ban đầu : {list_user_quan_ap}")

# Xóa tên cuối cùng trong danh sách 
# pop() : Nếu không truyền đối số : Thì xóa cuối 
#       : Nếu truyền đối số - Xóa theo index
delete_user = list_user_quan_ap.pop()
print(delete_user)

try:
    list_user_quan_ap.remove("Giang Long")
    print(list_user_quan_ap)
except:
  print('An exception occurred')

print(list_user_quan_ap)

# 1:Thuy
# 2: Quang Huy
# ...
# Cách 1 
count = 0 
for name in list_user_quan_ap:
   count += 1
   print(f"{count} : {name}")

# Cách 2
for index in range(len(list_user_quan_ap)):
   print(f"{index} : {list_user_quan_ap[index]}")

for index,name in enumerate(list_user_quan_ap,start=1):
   print(f"{index}: {name}")

# Danh sách [100,101,102,103]
# Tạo ra một danh sách mới chỉ có các số lẻ 

list_number = [100,101,102,103]
new_list_number = list()

for number in list_number:
   if number % 2 != 0 :
      new_list_number.append(number)
print(new_list_number)


branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]


index_max = 1
index_min = 2

print(f"{branch_names[index_max]} : {daily_revenues[index_max]} VND")

