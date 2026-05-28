branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]
target_achieved = [True, True, False, True, False]

while True:
    choice = int(input("""
    ===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====
        1. Hiển thị báo cáo doanh thu tổng hợp
        2. Thống kê chi nhánh Cao nhất / Thấp nhất
        3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)
        4. Thoát chương trình
        ================================================
        Nhập lựa chọn của bạn (1-4): _
"""))
    match choice :
        case 4 :
            print("Kết thúc chương trình")
        case 1:
            for i in range(len(branch_names)):
                status_name = "Đạt" if target_achieved[i] else "Không Đạt"
                print(f"Tên cơ sở : {branch_names[i]} , Doanh Thu : {daily_revenues[i]} , Trạng Thái :{status_name}")
