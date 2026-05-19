from datetime import datetime

print(datetime.now().year)

age = 18
is_done = True

print(age < 17 and is_done) #False 

print(age == 17 or is_done) #True 

print(not (age < 17 and is_done or not is_done))

if age > 18 :
    print("An đủ tuổi đi tù")
else :
    print("Chưa đủ tuổi") 
a = 10
print(a)

# số bàn phản lưới lớn hơn 10 thì "bán độ"
# từ 5 -> 9 thì "hên"
# nhỏ hơn 5 thì "không cố tình "
score_goal = int(input("Mời bạn nhập bàn thắng"))

if score_goal >= 10 :
    print("bán độ")
elif score_goal > 5 and score_goal <= 9 :
    print("Hên")
else :
    print("Không cố tình")

name_user == ""
year_user = 2000

# if year_user > 1900 and year_user < 2026