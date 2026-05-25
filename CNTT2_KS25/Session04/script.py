# # Nếu 0 : Thứ 2 
# #  1 : Thứ 3 
# #  2 : Thứ 4
# day = 0
# match day:
#     case 0 :
#         print("THứ 2")
#     case 1 : 
#         print("Thứ 3")
#     case 2 :
#         print("Thứ 4")


# # Break : Dùng để kết thúc vòng lặp 
# # Tìm số lẻ đầu tiên từ 10 về 1
# for number in range(10,0,-1):
#     if not (number % 2 == 0) :
#         print(number)
#         break
# #  In ra tất cả số chẵn từ 1 đến 100 và phải áp dụng continue 
# for number in range(1,101):
#     print("Xin chào cả lớp")
#     continue
#     print("Tôi là Hiếu 6")

# #  Vòng lặp lồng 

# # in số giờ phút từ 1 h cho đến 2h 
# # 1:01 , 1:02 , 1:03 ,.... 1:59
# for i in range(1,3) :
#     for j in range(1,60):
#         print(f"{i}:{j}")
#         break
    

# # Lần 1 : i  = 1 : 
#     # Lần 1 : j = 1 => in ra : 1 : 1
#     # Lần 59 : j = 59 => in ra 1 : 59

# #   chỉ lấy 2 số chẵn từ 1 cho đến 100 
# flag = 0
# for i in range(1,100):
#     if i % 2 == 0:
#         print(i)
#         flag += 1
#     if flag == 2:
#         break
# # lần i = 1 
# # Lần 2 : i =2 ; in ra 2 ,flag = 1
# # Lần 3 : i = 3 
# # lần 4 : i = 4 in ra 4 , flag = 2

# # BTTH

# # B1 : Nhập số lượng nhân viên input => int
# # B2 : Nhập thông tin nhân viên : input => 2 biến 
# # B3 : Kiểm tra dữ liệu hợp lệ (toán tử logic ngày làm việc : or)

# # 4.5. Hiển thị biểu đồ ngày làm việc
# # Sau khi nhập hợp lệ, chương trình hiển thị số ngày làm việc bằng dấu *.
# # Áp dụng for (ngay_lam_viec) => print(* , end = "")
