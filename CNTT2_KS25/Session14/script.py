# Khai báo hàm : Từ khóa def 
# Tham số 
def hello_hieu(name):
    print(f"Xin chào {name} bé bỏng")

hello_hieu("Dương")
hello_hieu("Phong")
hello_hieu("Hiếu")
hello_hieu("Dũng")

# Tạo một hàm tính tổng 2 số bất kỳ mà người dùng nhập 
def calc_sum(a, b=10):
    sum = a + b
    print(sum)

calc_sum(1,2)
calc_sum(1)
calc_sum(1,12)

def info_user (name,address) :
    print(f"Tôi tên là {name} , Quê tôi : {address}")

info_user(address="Hà lội",name="Tuấn")

def calc_point (*danh_sach_diem) :
    sum = 0
    for value in danh_sach_diem:
        sum += value
    print(sum)

calc_point(10,1,0,1,12,14,15,16)

list_number = [1,2,3,4,5]
# Tạo một hàm để trả về danh sách các số lẻ 

def filter_number(list) :
    new_list = []
    for value in list:
        if not value % 2 == 0:
            new_list.append(value)
    return new_list
    

print(filter_number(list_number))
print(calc_point(1,2,3))


number_01 = "Tuấn" 
# Khi gọi chương trình thì biến number_01 sẽ tự tăng 1 giá trị 

def handle_increment():
    global number_01
    name_01 = "Dev"
    number_01 = "An"

handle_increment()
print(number_01)
#bai1 

def tinh_bmi (a,b):
    if b == 0:
        print ("chiều cao không được là 0!!!")
        return 
    else:
        bmi = a/(b*b)
        print (bmi)

tinh_bmi(68,0)

list_user = [{"id" : 1 , "name" : "Tuấn"}]

def add_user (list) : 
    list.append({"id":2 , "name" : "Dev"})

add_user(list_user)

print(list_user)