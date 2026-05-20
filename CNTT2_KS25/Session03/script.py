# Dùng vòng lặp for 
# range (start , end , step) => start <= number < end
# start : Giá trị khởi tạo ban đầu cho biến 
# end : kết thúc 
# step : bước nhẩy
for i in range(1 , 5 , 2):
    print(i)

for index in range(5): # đối số duy nhất : end , step : 1 , start : 0
    print(f"Vòng lặp thứ 2 : {index}")


# Tính tổng từ 0 -> 10 
sum = 0
for number in range(11) :
    sum += number
print(f"Tổng = {sum}")

# in danh sách từ 10 -> 1 
for number in range(10, 0 , -1):
    print(number)


# while : Vòng lặp không biết trước số lần lặp 

# Người dùng nhập số đến khi nào = 9 thì mới dừng chương trình 
choice = 0 
while choice != 9 :
   choice = int(input("Mời bạn nhập giá trị :"))
print("Thoát chương trình")

while True:
    choice = int(input("Mời bạn nhập giá trị :"))
    if choice == 9 :
        print("Bạn đã nhập đúng , thoát khỏi chương trình")
        break