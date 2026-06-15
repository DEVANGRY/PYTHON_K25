# Tất cả chức năng , hàm liên quan đến : Thông tin người dùng 

def handle_login():
    user_name = input("Nhập tài khoản người dùng :")
    password = input("Nhập mật khẩu người dùng :")
    if user_name == "tuan" and password == "12345":
        print("Đăng nhập thành công")
    else :
        print("Tài khoản mật khẩu sai")