from datetime import datetime

print(datetime.now().year)

# Tuổi lớn hơn 18 , tiền lớn hơn 10 triệu 
# thì in ra là True còn một trong hai sai thì in ra là False
tuoi = 19
tien = 2_000_000
print(tuoi > 19 and tien > 10_000_000)  # False
print(tuoi > 19 or tien > 10_000_000) # False 
print(tuoi <= 19 or tien > 10_000_000) # True
print(tuoi <= 19 or tien < 10_000_000) #True
print(not tuoi <= 19) # False
print(not (tuoi <= 19 or tien > 10_000_000)) # False

# Câu điều kiện 
age_user = 19

if age_user > 18 :
    print("Tôi lớn rồi") # đoạn code nằm trong if
else :
    print("Tôi còn nhỏ")

a = 10 # đoạn code này ngoài câu điều kiện if

# Điểm từ 8 -> 10 thì in ra sinh viên xuất sắc
# Điểm từ 6->8 thì sinh viên vừa vừa 
# Điểm còn lại thì sinh viên cần nỗ lực
diem = float(input("Mời bạn nhập điểm"))

if diem > 8 and diem <= 10 :
    print("Sinh viên cưng của thầy")
elif diem > 6 and diem <= 8 :
    print("sinh viên vừa vừa ")
else :
    print("sinh viên cần nỗ lực")

