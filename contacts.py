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
# Danh sách toàn cục
phonebook = []

def add_contact(name, phone):
    phonebook.append({
        "name": name,
        "phone": phone
    })

# Hiển thị danh bạ
def view_contacts():
    if len(phonebook) == 0:
        print("Danh bạ trống")
        return

    for contact in phonebook:
        print("Tên:", contact["name"], "- SĐT:", contact["phone"])
# Danh sách toàn cục
phonebook = []

def add_contact(name, phone):
    phonebook.append({
        "name": name,
        "phone": phone
    })

def view_contacts():
    for contact in phonebook:
        print("Tên:", contact["name"], "- SĐT:", contact["phone"])

# Tìm kiếm liên hệ theo tên
def search_contact(name):
    found = False
    for contact in phonebook:
        if contact["name"] == name:
            print("Số điện thoại:", contact["phone"])
            found = True

    if not found:
        print("Không tìm thấy")
