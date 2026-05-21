# # # Nếu tuổi lớn hơn 18 thì "đi tù" còn ko thì "không phải đi tù"


# # # age = int(input("Mời người dùng nhập tuổi :"))
# # # if age >= 18 :
# # #     print("Đi tù")
# # # else :
# # #     print("Không đi tù")

# # # Nếu là số 0 thì in ra thứ hai , số 1 thì in ra thứ 3 , số 2 thì in ra thứ 4
# # day = int(input("Mời bạn nhập số"))
# # match day:
# #     case 0:
# #         print("Thứ hai")
# #     case 1:
# #         print("Thứ ba")
# #     case 2:
# #         print("Thứ tư")

# # # Đóng tiền nhà : Tiền : 2 -> 4 : nhà cấp 1 
# # #  Tiền : 4 -> 6 : nhà cấp 2 
# # #  Tiền : lớn hơn 6 : pen houser 

# # money = int(input("Mời bạn nhập tiền phòng :"))
# # if money >= 2 and money <= 4:
# #     print("Nhà cấp 1")
# # elif money > 4 and money <=6:
# #     print("Nhà cấp 2")
# # elif :
# #     print("pen house")

# # Vòng lặp For 
# # in từ 1 đến 10 


# # range (start , end , step)
# # start : Điểm bắt đầu : 0
# # end : Điểm kết thúc 
# # step : bước nhảy nếu không truyền : step = 1

# # i in range(0,2,1) => : 
# # lần 1 : i :  0 ; i < 2 ; chạy code body ;  i = 1
# # lần 2 : i = 1 ; i < 2 ; chạy code body ; i = 2
# # lần 3 : i = 2 ; i < 2 => kết thúc 

# # i in range(3) => range(0,3,1)

# # i in range(1,2) => start = 1 , end = 2

# # i in range(1,11) => 1 ,2 ,3,4,5,.... ,9

# # while : Vòng lặp không biết trước số lần lặp 

# # Tạo một trò chơi pingo nếu người dùng nhập đúng số 9 thì in ra bạn trúng thưởng 
# # còn ko thì in ra số bạn nhọ và cho người dùng nhập khi nào đúng thì thôi
# # number_user = 0

# # while number_user != 9 :
# #    number_user = int(input("Bạn đen lắm , nhập lại nữa đi :"))
# # print("Bạn đã nhập đúng rồi")

# number_user = 0

# while not (number_user == 9) :
#    number_user = int(input("Bạn đen lắm , nhập lại nữa đi :"))
# print("Bạn đã nhập đúng rồi")

# while True:
#     number_user = int(input("Nhập số đi :"))
#     if number_user == 9 :
#         print("Tìm đúng số rồi")
#         break
#     else :
#         print("Nhập lại đi!")

#  Tính tổng từ 1 đến 10 
sum = 0
for i in range(1,11): 
    sum += i
print(f"Tổng là : {sum}")