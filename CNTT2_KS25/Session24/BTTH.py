class Drink: 
    def __init__(self, code, name, price):
        self.code = code 
        self.name = name
        self.__price = price
        self.is_available = True
    
    def toggle_available(self):
        pass
    
menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

def display_list_drink (list_menu) :
    """Chức năng in danh sách"""

while True:
    choice = input("""
        === HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===

        1. Xem danh sách đồ uống
        2. Thêm đồ uống mới
        3. Cập nhật trạng thái kinh doanh
        4. Thoát chương trình

        ==============================================
        Chọn chức năng (1-4):
""")
    
