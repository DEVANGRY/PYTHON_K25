raw_input = "   nGuyen vaN aN  ;  2004   "

while True: 
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
        case 1: 
            print(f"'{raw_input}'") 
        case 2:
            name_user = raw_input.strip().split(";")[0].strip().title()
            age_user = 2026 - int(raw_input.strip().split(";")[1].strip())
            print(f"Họ và tên : {name_user}")
            print(f"Tuổi : {age_user}")

        case 4:
            print("Chương trình đã dừng")
            break
