# # Tính tích từ 1 đến 20
# # result = 1
# # for i in range(1,21):
# #     result = result * i
# # print(result)

# # in ra các số chẵn từ 1 đến 100
# for i in range(1,101):
#     if i % 2 == 0 :
#         print(i)


# In ra số chia hết cho 3 đầu tiên từ 100 về 1 

# In cac số từ 100 về 1 
#  TÌm số đầu tiên trong dãy số đó chia hết cho 3

# break : dừng vòng lặp ngay lập tức khi thỏa mãn một điều
# kiện gì đó

for i in range(100,0,-1):
    if i % 3 == 0:
        print(i)
        break

# continue : Nhảy sang lần lắp tiếp theo 
# In ra các số chẵn từ 1 đến 100 dùng continue 
for i in range(1,101):
    if(i % 2 != 0) :
        continue
    print(i)

# Vòng lặp lồng nhau 
#  IN ra bảng cửu chương từ 2 cho đến 5 
#  2 vòng lặp : lặp cha : chạy từ 2 -> 5
#  Lặp con : 1 -> 10 
# for i in range(2,6):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")

for i in range(3):
    for j in range(5):
        print("x",end ="")
    print()