from tabulate import tabulate
# tất cả chức năng , hàm của quản lý sản phầm : CRUD


def handle_display_list_product(list_product) :
    print("Danh sách sản phẩm :")
    print(tabulate(list_product,headers="keys",tablefmt="grid"))

def handle_add_product():
    print("Thêm hàng thành công")