# tính tổng các số chẵn từ 1 đến 100 
sum = 0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(sum)

# Người dùng nhập nếu đúng là 10 thì in ra trúng thưởng còn 
# không thì in ra không trúng thưởng 
# , nhập đến khi nào trúng thì thôi

trung_thuong = 0

while trung_thuong != 10:
    trung_thuong = int(input("Nhập số trúng thưởng :"))
    
print("Đã trúng thưởng")