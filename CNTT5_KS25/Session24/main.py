# OOP : Lập trình hướng đối tượng : Sẽ cố gắng biến mọi thứ thành đối tượng 

# class và object 
# class : là một bản thiết kế (Khuôn mẫu)
# Thuộc tính (state) - Phương thức (method)
# __init__ : hàm khởi tạo của class 
# tham số self : đại diện cho đối tượng cụ thể áp dụng class đấy 
# Thuộc tính : Tên , tuổi , giới tính , chiều cao , cân nặng , tài chính
# Method : hành vi 
class NguoiYeu :
    def __init__(self, ten , tuoi , gioi_tinh , chieu_cao ,can_nang,tai_chinh, diem_xau = "Men lì"):
        self.ten = ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.tai_chinh = tai_chinh
        self.__diem_xau = diem_xau
    
    def noi_de_thuong(self):
         print(f"Em là {self.ten} : Em yêu anh Huân lắm")

    @staticmethod
    def hom_nay_em_muon_an_gi():
        print("Em ăn gì cũng được")

    def nap_tien_cho_em_nguoi_yeu(self,so_tien_nap):
        self.tai_chinh += so_tien_nap
        print(f"Tiền mới là {self.tai_chinh}")
    # Thuộc tính không muốn người khác ở bên ngoài xem : private 
    # Get : lấy dữ liệu và setter : chỉnh sửa 
    # Get
    @property
    def diem_xau(self):
        return self.__diem_xau
    
    # Setter 
    @diem_xau.setter
    def diem_xau(self , diem_xau_moi):
        self.__diem_xau = diem_xau_moi

# object : đối tượng cụ thể  
nguoi_yeu_01 = NguoiYeu("Phượng",20,"nữ","1M60",50 ,2_000_000_000)
nguoi_yeu_02 = NguoiYeu("Linh", 40 ,"Nữ","1M60",50 ,10_000_000_000)
nguoi_yeu_03 = NguoiYeu("Nam", 18, "Nam","1M80", 40 ,100_000_000_000)

print(nguoi_yeu_01.ten)
print(nguoi_yeu_01.tuoi)

print(nguoi_yeu_01.gioi_tinh)

nguoi_yeu_03.noi_de_thuong()

# Xây một method : nhận vào tiền muốn nạp cho người yêu : thuộc tính tiền tăng lên đúng bằng tiền cũ + với tiền muốn nạp
nguoi_yeu_03.nap_tien_cho_em_nguoi_yeu(1_000_000)

NguoiYeu.hom_nay_em_muon_an_gi()

# print(nguoi_yeu_03.__diem_xau)
print(nguoi_yeu_03.diem_xau)

nguoi_yeu_03.__diem_xau = "sad girl"

print(nguoi_yeu_03.__diem_xau)

