list_employee = [{'id': 101, 'name_employee': 'Tuấn', 'salary_employee': 1000000.0}]
# {'id': int, 'name': str, 'salary': float}.
while True :
    choice = int(input("""
        QUẢN LÝ NHAN SỰ - STAFF MANAGER
        1. Thêm nhân viên mới
        2. Danh sach nhan viên
        3. Tìm kiêm nhân viên (theo mã)
        4. Xóa nhân viên khỏi hệ thông
        5. Thoat chưong trinh
    """))

    match choice:
        case 5:
            print("Thoát chương trình")
            break
        case 1:
            new_employee = {}
            if len(list_employee) == 0:
                new_employee["id"] = 101
            else :
                new_employee["id"] = list_employee[-1]["id"] + 1 
            
            while True:
                new_employee["name_employee"] = input("Mời bạn nhập tên nhân viên:")
                if not new_employee["name_employee"]:
                    print("Tên không được để trống")
                else :
                    break

            while True:
                new_employee["salary_employee"] = float(input("Mời bạn nhập lương nhân viên:"))
                if not new_employee["salary_employee"] or new_employee["salary_employee"] < 0:
                    print("Không hợp lệ")
                else :
                    break

            list_employee.append(new_employee)
            print(f"Thêm Nhân Viên thành công ! {new_employee["id"]}")
            print(list_employee)
        case 2 :
            if not list_employee :
                print("Chưa có dữ liệu nhân sự")
            else :
                print(f"{"ID" :<20} | {"Tên Nhân Viên" :<20} | {"Mức Lương" :<20}")
                for employee in list_employee:
                    print(f"{employee['id'] :<20} {employee['name_employee'] :<20} {employee['salary_employee'] :<20}")
        case 3 : 
            id_input = int(input("Mời bạn nhập ID:"))
            is_found = False

            for index,employee in enumerate(list_employee):
                if employee["id"] == id_input:
                    is_found = True
                    print(employee)
            if not is_found :
                print("Không tìm thấy mã nhân viên")

        case 4 : 
            id_input = int(input("Mời bạn nhập ID:"))
            is_found = False

            for index,employee in enumerate(list_employee):
                if employee["id"] == id_input:
                    is_found = True
                    list_employee.pop(index)
                    print("Đã xóa thành công")
            if not is_found :
                print("Không tìm thấy mã nhân viên")    