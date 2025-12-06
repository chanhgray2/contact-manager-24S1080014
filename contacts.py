# Khai báo biến danh sách toàn cục
phonebook = []

# Hàm main hiển thị menu
def main():
    print("=== QUẢN LÝ DANH BẠ ===")
    print("1. Thêm liên hệ")
    print("2. Xem danh bạ")
    print("3. Tìm kiếm")
    print("0. Thoát")

# Gọi hàm main
main()
# Danh sách toàn cục
phonebook = []

# Hàm thêm liên hệ
def add_contact(name, phone):
    contact = {
        "name": name,
        "phone": phone
    }
    phonebook.append(contact)

# Hàm main (menu đơn giản)
def main():
    print("1. Thêm liên hệ")
    choice = input("Chọn: ")

    if choice == "1":
        name = input("Nhập tên: ")
        phone = input("Nhập số điện thoại: ")
        add_contact(name, phone)
        print("Đã thêm liên hệ")

main()
