import auth_service as auth
import student_service
from student_service import handle_add_student as add_student
import datetime
from comman.service import handle_format_text

from tabulate import tabulate

list_student = [
    {"id":1 , "name":"Quang Minh" ,"age" : 18},
    {"id":2 , "name":"Quang Minh V2" ,"age" : 19},
    {"id":3 , "name":"Quang Minh V3" ,"age" : 20}
]

list_nameuser = [
    ["Tuấn" , "20" , "Nam" ,"Hà Nội"],
    ["Tuấn" , "20" , "Nam" ,"Hà Nội"],
    ["Tuấn" , "20" , "Nam" ,"Hà Nội"],
]

while True:
    choice = int(input("Mời bạn nhập chức năng :"))
    match choice:
        case 1 :
            auth.handle_login("Quốc Tuấn","12345")
        case 2 : # in ra điểm trung bình sinh viên
            print(student_service.handle_score_avg())
        case 3 : # in ra giờ hiện tại 
            print(datetime.datetime.now())
        case 4 : #in danh sách dưới dạng bảng đẹp
            print(tabulate(list_student,headers="keys",tablefmt="grid"))
        case 5 :
            print(tabulate(list_nameuser,headers=["Tên","Tuổi","Giới Tính","Địa chỉ"],tablefmt="github"))
        case 6 :
            print(handle_format_text("tuấn"))