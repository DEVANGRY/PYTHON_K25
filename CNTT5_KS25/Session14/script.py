# Hàm trong python 

# input , code trong thân hàm , output

# Tạo hàm trong python : 
# cú pháp : def
def hello_an():
    print("Xin chào An Bé BỎNG") 

hello_an()
hello_an()
hello_an()
hello_an()

# Khi làm việc với hàm : Tham số : là các biến định nghĩa , 
# đối số : là biến truyền vào

# Tạo một hàm để tính tổng 2 số bất kỳ 
def calc_sum(a,b=20):
    sum = a + b
    print(sum)

calc_sum(10,11)
calc_sum(10)
calc_sum(b=11,a=20)

# Tạo một hàm để tính điểm trung bình của Thuy học kỳ 1 
def calc_avg(a,b,c,d,e , *list_mon_hoc):
    print(type(list_mon_hoc))
    sum = (a+b+c+d+e)
    for value in list_mon_hoc:
        sum += value
    print(f"{sum/(len(list_mon_hoc) + 5)}")

calc_avg(0,1,0,20,0)
calc_avg(0,1,0,20,0,11,12,13,14,15,123) 
# list_mon_hoc = (11,12,13,14,15,123)
# Tính toán điểm trung bình tất cả các kỳ của Thuy 

def print_name_user (name_01 , *ten_danh_sach_nguoi_dung):
    print(name_01)
    print(ten_danh_sach_nguoi_dung)
    return 10
    print("log")

print_name_user("Tuấn","An","Thuy","Dev")


print(print_name_user("Tuấn","An","Thuy","Dev"))

# Kiểu dữ liệu toàn cục là int , float , string thì mới phải áp dụng gloab
count = 0 
# Tạo một hàm khi gọi hàm đó  thì count tăng 1 đơn vị 
def handle_increment_count ():
    global count
    count += 1
    
handle_increment_count()
print(count)

list_user = [{"id":1 , "name" : "Tuấn"}]
# Tạo hàm để thêm nhân viên vào list user 
def handle_add_user() :
    """
        Hàm để thêm nhân viên 

        Args :

        Return :        
    """
    new_user = {}
    if len(list_user) == 0 :
        new_user["id"] = 1
    else :
        new_user["id"] = list_user[-1]["id"] + 1
    new_user["name"] = "Thuy"
    list_user.append(new_user)

handle_add_user()
print(list_user)