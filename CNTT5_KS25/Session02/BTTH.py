from datetime import datetime


name = input("Nhập tên bệnh nhân:")
nam_sinh = input ("Nhập năm sinh:")
so_ngay_bi_benh= input ("Nhập số ngày bị bệnh:")
Nhiet_do_co_the = float(input("Nhập nhiệt độ cơ thể: "))
chi_phi_kham = input ("Nhập chi phí khám: ")

current_year = datetime.now().year
if(
    name.strip() == " "
    or nam_sinh < 1990 and nam_sinh > current_year
    or so_ngay_bi_benh < 0 
    or Nhiet_do_co_the < 30 and Nhiet_do_co_the > 45 
    or chi_phi_kham <= 0
):
    print("Lỗi vui lòng nhập lại")
else:
    
