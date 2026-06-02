list_users = []

# Dạng bài tập với menu -> while 
# {'id': int, 'name': str, 'salary': float}.
while True:
    choice = int(input("""
    QUẢN LÝ NHÂN SỰ - STAFF MANAGER
        1. Thêm nhan viên mới
        2. Danh sách nhân viên
        3. Tìm kiêm nhân viên (theo mã)
        4. Xóa nhân viên khỏi hệ thông
        5. Thoat chương trình
    """))
    match choice:
        case 5:
            print("Bạn đã thoát chương trình")
            break
        case 1:
            new_user = {}
            if len(list_users) == 0:
                new_user["id"] = 101
            else :
                new_user["id"] = list_users[-1]["id"] + 1
                
            while True:
                new_user["name_user"] = input("Mời bạn nhập tên :")
                if new_user["name_user"] == "" :
                    print("Tên không được để trống")
                    continue
                break
            
            while True:
                new_user["salary_user"] = float(input("Mời bạn nhập lương :"))

                if new_user["salary_user"] == "" or new_user["salary_user"] < 0 :
                    print("Lương không được để trống")
                    continue
                break
            
            list_users.append(new_user)
            print(f"Thêm nhân viên thành công! ID :{new_user["id"]}")

        case 2 : 
            if len(list_users) == 0:
                print("Chưa có dữ liệu nhân sự!")
            else:
                print(f"ID   | Tên Nhân Viên  | Lương")
                for user in list_users:
                    print(f"{user["id"]} | {user["name_user"]} | {user["salary_user"]}")
        
        case 3 :
            id_find_user = int(input("Mời bạn nhập ID nhân viên :"))
            flag_user = False
            for user in list_users:
                if user["id"] == id_find_user :
                    print(user)
                    flag_user = True
                    break
            if not flag_user :
                print("Không tìm thấy user")
        case 4 :
            id_find_user = int(input("Mời bạn nhập ID nhân viên muốn xóa:"))
            flag_user = False
            for index,user in enumerate(list_users):
                if user["id"] == id_find_user :
                    list_users.pop(index)
                    flag_user = True
                    break
            if not flag_user :
                print("Không tìm thấy user")
            