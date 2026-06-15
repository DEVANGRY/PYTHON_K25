import auth.auth_service as auth_service
import product.product_service as product_service
from datetime import datetime


from product.product_service import handle_add_product as add_product
# Làm một trang web quản lý bán hàng 
# Đăng ký đăng nhập , đổi tk , mk , quên mk : auth
# CRUD : hàng hóa 
list_product = [
    {"id":1,"name" : "Búp bê" , "price" : 1_000_000},
    {"id":2,"name" : "Búp bê V2" , "price" : 2_000_000},
    {"id":3,"name" : "Búp bê V3" , "price" : 3_000_000}
]

while True:
    choice = int(input("Mới bạn nhập chức năng của trang quản lý đặt hàng :"))
    match choice:
        case 1 : #chức năng đăng nhập 
            auth_service.handle_login()
        case 2 : # danh sách sản phẩm
            product_service.handle_display_list_product(list_product)
        case 3 :
            print(datetime.now())
        case 4: 
            add_product()