# In ra màn hình console log 
print("Xin chào tôi bị trừ lương vì dạy CNTT5")

# Khai báo biến và kiểu dữ liệu 
name_user = "CNTT5"



# Kiểu dữ liệu 
# Chuỗi , số nguyên , số thức , bool 
age_user = 18
age_user = 18.5
age_user = "Mười tám"
is_done = True
is_done = False
money = 1_00.10_000

print(type(age_user))
print(type(is_done))
print(type(money))

# Lấy dữ liệu từ người dùng nhập => Kiểu dữ liệu luôn là string
money_sal = input("Mời bạn nhập lương của bạn :")
# Cách 1 : 
print(f"Tôi đẳng cấp Lương tôi : {int(money_sal)}")
# Cách 2 : 
print("Tôi đẳng cấp Lương tôi : ",money_sal,"")

# 
print(bool(0)) #false 
print(bool(1))   #true
print(bool("Tuan"))