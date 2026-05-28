# Khởi tạo một list danh sách 3 tên sinh viên có trong lớp mình 
students = ["Phú Tài" , "Gia Huy" , "Hữu Quốc" , "Văn Thi"]

# Cách để lấy giá trị trong list
name_user_01 = students[1]

print(name_user_01)

# cập nhật giá trị trong mảng 
students[0] = "Anh Dương"

# Xóa phần tử cuối cùng trong mảng 
# Cách 1 : Xóa dựa theo giá trị : .remove()
students.remove("Văn Thi")

# Thêm vào cuối list dùng append
students.append("Văn Thi")
print(students)

# Thêm vào vị trí bất kỳ 
students.insert(1,"Hồng Minh")

# Cách 2 : Xóa dựa theo index 
remove_student = students.pop(3)
print(remove_student)

# Dùng clear : xóa hết tất cả ký ức về người ấy

# Dùng for để duyệt qua danh sách 

for index in range(len(students)):
    print(f"{index + 1}.{students[index]}")


# Cách 2  : Thuần Python 
for index, name in enumerate(students,start=0):
    print(f"Cách 2 : {index + 1}:{name}")

# Cho một list [100,200,300, 101 ,103] 
# tạo một list khác chỉ chứa các số lẻ

list_number =  [100,200,300, 101 ,103] 
new_list = list()
for index,number in enumerate(list_number,start=1):
    if number % 2 != 0:
        new_list.append(number)
print(new_list)