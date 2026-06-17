from abc import ABC , abstractmethod
# Game Liên Quân 
# 4 tính chất OOP : 
# Tính đóng gói , Tính kế thừa , tính đa hình , tính trừ tượng

# TÍnh đóng gói : 
class Tuong(ABC):
    def __init__(self,ten_tuong : str, hp: float ,mana : float, sat_thuong_co_ban : int ):
        self.ten_tuong = ten_tuong
        self.hp = hp
        self.mana = mana
        self.sat_thuong_co_ban = sat_thuong_co_ban
    def hanh_dong_di_chuyen(self):
        print(f"Tôi là {self.ten_tuong} , tôi đang di chuyển")
    @abstractmethod
    def danh_thuong(self):
        print("Đanh nhau loạn xạ")

# Nhân vật 1 
# ngo_khong = Tuong("Ngộ Văn" , 3_400 , 3_600 , 200)
# nak = Tuong("nak Hiếu" , 2_400 , 1_600 , 0)
# natalya = Tuong("nataly Tùng" , 1_400 , 6_600 , -1)
# krixi = Tuong("cờ ri Chi" , 1_400 , 6_600 , 36)

# Tính kế thừa
# Để xử lý xây dựng tướng theo các vai trò 
# super() : kế thừa toàn bộ tài sản của lớp cha 
class TuongSatThu(Tuong):
    def __init__(self, ten_tuong, hp, mana, sat_thuong_co_ban,ti_le_chi_mang = 100):
        super().__init__(ten_tuong, hp, mana, sat_thuong_co_ban)
        self.ti_le_chi_mang = ti_le_chi_mang
    
    def combat(self):
        print("Ta dùng dẹp chém người")

    def danh_thuong(self):
        print("Ta cầm kiếm chém nhau")

    def __add__(self, other):
        if isinstance(other , TrangBi):
            self.hp += other.chi_so_tang_hp
            self.mana += other.chi_so_tang_mana
        print("Đã mua đồ thành công")
    def __str__(self):
        return f"Ta là {self.ten_tuong} , Ta có chỉ số máu là : {self.hp} , Ta có chỉ số năng luongwj là : {self.mana}"

class TuongPhapSu(Tuong):
    def __init__(self, ten_tuong, hp, mana, sat_thuong_co_ban, chi_so_danh_xa = 80):
        super().__init__(ten_tuong, hp, mana, sat_thuong_co_ban)
        self.chi_so_danh_xa = chi_so_danh_xa
    
    def combat(self):
        print("Ta dùng dẹp chém người")

    def danh_thuong(self):
        print("Ta dùng sự cute đánh ngươi")

class TuongGiangHoMang(Tuong):
    def __init__(self, ten_tuong, hp, mana, sat_thuong_co_ban, chi_so_boc_phet = 100):
        super().__init__(ten_tuong, hp, mana, sat_thuong_co_ban)
        self.chi_so_boc_phet = chi_so_boc_phet
    
    def combat(self):
        print("Ta dùng dẹp chém người")
    def danh_thuong(self):
        print("Ta lời nói để đánh ngươi")

dang_lop_truong = TuongSatThu("Đăng bé bóng",2_000 , 2_000 , 150 , 24)
dang_lop_truong.combat()

print(dang_lop_truong)

# tính đa hình 
# Một hành vi có thể định 

# Làm chức năng trong LQ : Khi trang bị thêm đồ thì chỉ số nhân vật tăng 
# class : NhanVat + TrangBi
class TrangBi:
    def __init__(self,ten_trang_bi,gia_tien , chi_so_tang_hp , chi_so_tang_mana):
        self.ten_trang_bi = ten_trang_bi
        self.gia_tien = gia_tien
        self.chi_so_tang_hp = chi_so_tang_hp
        self.chi_so_tang_mana = chi_so_tang_mana

trang_bi_01 = TrangBi("Sách Thánh" , 2_980 ,  999 , 1_000)

mua_do = dang_lop_truong + trang_bi_01
print(mua_do)
print(dang_lop_truong)

# Tính trừu tượng

thuy_giang_ho = TuongGiangHoMang("Thuy" , -1 , 0 , 0 , 100)
thuy_giang_ho.danh_thuong()