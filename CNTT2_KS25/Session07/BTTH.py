raw_input = "   nGuyen vaN aN  ;  2004   "
while True :
    choice = int(input("""
    ===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====
    1. Hiển thị chuỗi dữ liệu gốc
    2. Chuẩn hóa Họ tên và tính Tuổi
    3. Tạo Mã ID và Email tự động
    4. Thoát chương trình
    =====================================
    Nhập lựa chọn của bạn (1-4):
"""))
    match choice:
        case 4 :
            print("Thoát chương trình thành công")
            break
        case 1: 
            print(f"'{raw_input}'")
        case 2:
            new_full_name = raw_input.strip().split(";")
            print(f"Họ tên : {new_full_name[0].strip().title()}")
            print(f"Tuổi: {2026 - int(new_full_name[1].strip())}")
        case 3:
            #  Lấy chữ cái đầu của Họ + 
            # chữ cái đầu của Tên đệm + 
            # Tên chính rồi viết thường toàn bộ, 
            # kết hợp đuôi @company.com. (Ví dụ: nvan@company.com).
            user_name = new_full_name[0].strip().title()
            year_date = new_full_name[1].strip()
            email_user = user_name[0] + user_name[6] + user_name[9:11].lower() + "@company.com"
            print(email_user)
        case _:
            print("Mời bạn nhập lựa chọn khác")
# nGuyen vaN aN 
# list = ["nguyen" , "van" , "an"]
# list[1][0]