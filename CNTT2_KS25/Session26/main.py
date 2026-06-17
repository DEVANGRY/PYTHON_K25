from abc import ABC , abstractmethod
# Role play game 

# Thuộc tính : tên , hp , mana , ky_nang
class NhanVat(ABC) :
    def __init__(self,id : int,ten : str,hp : float,mana : float, sat_thuong_gay_ra : float):
        self.__id = id
        self.ten = ten 
        self.hp = hp 
        self.mana = mana
        self.sat_thuong_gay_ra = sat_thuong_gay_ra

    def __str__(self):
        return f"Đây là nhân vật trong game"

    def gioi_thieu_nhan_vat(self):
        print(f"Ta là {self.ten} : , Ta có lực tấn công la : {self.sat_thuong_gay_ra}")
    
    @abstractmethod
    def hanh_dong_chien_dau(self):
        pass

# Tính kế thừa : trong game thì sẽ dùng để có thể chia các bang phái cụ thể
# BangKim : lớp con , NhanVat : lớp cha 
# BangPhai Kim : Sát thương  vật lý 
class BangPhaiKim(NhanVat):
    def __init__(self, id, ten, hp, mana, sat_thuong_gay_ra, sat_thuong_chuan = 100):
        super().__init__(id, ten, hp, mana, sat_thuong_gay_ra)
        self.sat_thuong_chuan = sat_thuong_chuan

    def thuc_hien_an_chay(self):
        print(f"Tôi là {self.ten} : Hôm nay tôi sẽ ăn chay")

    def hanh_dong_chien_dau(self):
        print(f"Ta là {self.ten} ta sẽ chém người bằng kỹ năng đẳng cấp của ta")
    def __add__(self, other):
        if isinstance(other , TrangBi):
            self.hp += other.hp_tang
            self.mana += other.mana_tang
        print(f"Đã trang bị đồ thành công chỉ số mới của bạn là {self.hp} , {self.mana}")

class BangPhaiMoc(NhanVat):
    def __init__(self, id, ten, hp, mana, sat_thuong_gay_ra,chi_so_danh_bay = 200):
        super().__init__(id, ten, hp, mana, sat_thuong_gay_ra) 
        self.chi_so_danh_bay = chi_so_danh_bay
    
    def hanh_vi_chat_cay(self):
        print(f"Ta là {self.ten} , bây giờ ta sẽ chặt cây")

    def hanh_dong_chien_dau(self):
        print(f"Ta là {self.ten} sẽ đấm người bằng sức mạnh của ta")


class BangPhaiCuTe(NhanVat):
    def __init__(self, id, ten, hp, mana, sat_thuong_gay_ra,chi_so_dang_yeu = -200):
        super().__init__(id, ten, hp, mana, sat_thuong_gay_ra) 
        self.chi_so_dang_yeu = chi_so_dang_yeu
    
    def hanh_vi_chat_cay(self):
        print(f"Ta là {self.ten} , bây giờ ta sẽ chặt cây")
    
    # def hanh_dong_chien_dau(self):
    #     print(f"Ta là {self.ten} sẽ đánh người bằng sự đáng yêu của ta")
    


duc_lop_truong = BangPhaiMoc(2 , "Chiến binh bé bỏng" , 1_000 , 100_000 , 0 , -1)
thi_lop_pho = BangPhaiKim(3 , "Thi cute" , 2_000 , 500 , -1 , 0)
duong_bi_thu_lop = BangPhaiCuTe(4 , "Dương ngủ gật" , 1, 1 , 100)

print(duc_lop_truong)
duc_lop_truong.gioi_thieu_nhan_vat()
duc_lop_truong.hanh_vi_chat_cay()
duc_lop_truong.hanh_dong_chien_dau()

print(duong_bi_thu_lop)
duong_bi_thu_lop.hanh_dong_chien_dau()

thi_lop_pho.hanh_dong_chien_dau()

# Tính đa hình 
# Nhân vật thì đều phải đánh nhau 
# Bang mộc : đấm tay 
# Bang Kim : chém 


# Khi lắp đồ cho nhân vật thì phải tăng chỉ số nhân vật 
class TrangBi:
    def __init__(self,ten_trang_bi,hp_tang,mana_tang):
        self.ten_trang_bi = ten_trang_bi
        self.hp_tang = hp_tang
        self.mana_tang = mana_tang

vu_khi_co_ban = TrangBi("Dép lào", 1_000 , 2_000)

mac_do_cho_nhan_vat = thi_lop_pho + vu_khi_co_ban

# Tính trừ tượng