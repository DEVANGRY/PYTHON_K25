# Để xây dựng một đối tượng cụ thể thì trước tiên phải xây dựng class 

#  class : Bản thiết kế về tài khoản ngân hàng 
#  Thuộc tính : id , ten_nguoi_dung , mat_khau , so_du , dia_chi
class BankAccount :
    # cách khai báo các state : các thuộc tính 
    def __init__(self , id_nguoi_dung , ten_nguoi_dung , mat_khau , so_du , dia_chi = "Hà Nội"):
        self.id = id_nguoi_dung
        self.ten_nguoi_dung = ten_nguoi_dung 
        self.mat_khau = mat_khau
        self.__so_du = so_du
        self.dia_chi = dia_chi

    def hien_thi_thong_tin_the (self):
        print(f"ID : {self.id} | Tên Thẻ : {self.ten_nguoi_dung}")

    @staticmethod
    def kiem_tra_tinh_hop_le(type_money): 
        list_type = ["VND" , "ERUP" , "Yên"]
        if type_money in list_type : 
            print("Hợp lệ có thể chuyển tiền")
        else :
            print("Ngân hàng không dùng tiền tệ này quy đổi")

    # Tính đóng gói : Để lấy các thuộc tính private 
    # get : lấy  , set : chỉnh sửa 
    @property
    def so_du (self):
        return self.__so_du
    
    # thuoctinh.setter
    @so_du.setter
    def so_du (self , tien_thanh_toan):
        if (self.__so_du < tien_thanh_toan) :
            print("Số dư không đủ thanh toán")
        else:
            self.__so_du -=  tien_thanh_toan
            print("Đã thanh toán hóa đơn")
    
# Tạo đối tượng từ class 
account_01 = BankAccount(1,"Tuấn","12345",123456)

print(account_01.id,account_01.ten_nguoi_dung)

account_01.hien_thi_thong_tin_the()
account_01.hien_thi_thong_tin_the()

BankAccount.kiem_tra_tinh_hop_le("USD")
# Tạo một hàm để kiểm tra đơn vị tiền tệ có được hỗ trợ trong class BankAccount không 

print(account_01.so_du)
account_01.so_du = 100_000