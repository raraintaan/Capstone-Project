# Data bisnis dalam Yellow Pages
yellow_pages_contacts = [
    {"id": 1, "business_name": "Toko Buku", "phone": 62878555060, "email": "tokobuku@gmail.com", "address": "Jalan Buntu No.1", "category": "Bookstore"},
    {"id": 2, "business_name": "Apotek Farma", "phone": 62838555350, "email": "apotekfarma@gmail.com", "address": "Jalan Kayu No.21", "category": "Pharmacy"},
    {"id": 3, "business_name": "Restoran", "phone": 62897555112, "email": "restoran@gmail.com", "address": "Jalan Batu No.55", "category": "Restaurant"},
    {"id": 4, "business_name": "Salon Ratu", "phone": 62899555347, "email": "salonratu@gmail.com", "address": "Jalan Bahagia No.23", "category": "Salon"},
    {"id": 5, "business_name": "Bengkel Motor", "phone": 62818555761, "email": "bengkelmotor@gmail.com", "address": "Jalan Makmur No.50", "category": "Workshop"},
    {"id": 6, "business_name": "Hotel Indonesia", "phone": 62838555233, "email": "hotelindonesia@gmail.com", "address": "Jalan Indonesia No.9", "category": "Hotel"},
    {"id": 7, "business_name": "Supermarket", "phone": 62899555186, "email": "supermarket@gmail.com", "address": "Jalan Britaya No.43", "category": "Supermarket"},
    {"id": 8, "business_name": "Klinik Medita", "phone": 62838555195, "email": "klinikmedita@gmail.com", "address": "Jalan Temanggung No.8", "category": "Clinic"},
    {"id": 9, "business_name": "Sekolah Harap Bangsa", "phone": 62857555963, "email": "sekolahharapbangsa@egmail.com", "address": "Jalan Panti No.12", "category": "School"},
    {"id": 10, "business_name": "Universitas Marajaya", "phone": 62878555998, "email": "universitasmarajaya@gmail.com", "address": "Jalan Dago No.15", "category": "University"},
]

# Menginisialisasi Yellow Pages dengan kontak bisnis
yellow_pages = yellow_pages_contacts

next_id = len(yellow_pages) + 1  # Inisialisasi ID yang akan di-generate secara otomatis

# Fungsi untuk memvalidasi email
def validate_email(email):
    at_index = email.find('@')
    dot_index = email.rfind('.')
    return at_index > 0 and dot_index > at_index

# Fungsi untuk menambahkan kontak
def create_contact():
    global next_id

    # Validasi input nama bisnis
    while True:
        business_name = input("Enter business name: ")
        if business_name:
            business_name = str(business_name)
            break
        else:
            print("Business name cannot be empty!")

    # Validasi input phone
    while True:
        phone = input("Enter phone: ")
        if phone.isdigit():
            phone = int(phone)
            break
        else:
            print("Phone must be an integer!")

    # Validasi input email
    while True:
        email = input("Enter email: ")
        if validate_email(email):
            email = str(email)
            break
        else:
            print("Invalid email format!")

    # Validasi input address
    while True:
        address = input("Enter address: ")
        if address:
            address = str(address)
            break
        else:
            print("Address cannot be empty!")

    # Validasi input category
    while True:
        category = input("Enter category: ")
        if category:
            category = str(category)
            break
        else:
            print("Category cannot be empty!")

    contact = {
        "id": next_id,
        "business_name": business_name,
        "phone": phone,
        "email": email,
        "address": address,
        "category": category
    }
    yellow_pages.append(contact)
    next_id += 1
    print("Contact added successfully!")

# Fungsi untuk menampilkan seluruh kontak dalam format tabel
def read_contacts():
    if yellow_pages:
        print(f" {'ID':<6} | {'Business Name':<25} | {'Phone':<15} | {'Email':<30} | {'Address':<25} | {'Category':<15}")
        print("-" * 140)
        for contact in yellow_pages:
            print(f" {contact['id']:<6} | {contact['business_name']:<25} | {contact['phone']:<15} | {contact['email']:<30} | {contact['address']:<25} | {contact['category']:<15}")
    else:
        print("Yellow Pages is empty.")

# Fungsi untuk memperbarui kontak berdasarkan ID
def update_contact(contact_id, business_name=None, phone=None, email=None, address=None, category=None):
    contact_found = False
    for contact in yellow_pages:
        if contact["id"] == contact_id:
            if business_name is not None:
                business_name = business_name.strip()  # Menghapus spasi ekstra
                if not business_name:
                    print("Business name cannot be empty!")
                    return False
            if phone is not None:
                phone = phone.strip()  # Menghapus spasi ekstra
                if not phone.isdigit():
                    print("Phone must be a numeric value!")
                    return False
            if email is not None:
                email = email.strip()  # Menghapus spasi ekstra
                if not validate_email(email):
                    print("Invalid email format!")
                    return False
            if address is not None:
                address = address.strip()  # Menghapus spasi ekstra
                if not address:
                    print("Address cannot be empty!")
                    return False
            if category is not None:
                category = category.strip()  # Menghapus spasi ekstra
                if not category:
                    print("Category cannot be empty!")
                    return False
            
            # Jika semua validasi berhasil, update kontak
            if business_name is not None:
                contact["business_name"] = business_name
            if phone is not None:
                contact["phone"] = int(phone)
            if email is not None:
                contact["email"] = email
            if address is not None:
                contact["address"] = address
            if category is not None:
                contact["category"] = category
            
            print("Contact updated successfully!")
            contact_found = True
            break
    
    if not contact_found:
        print("Contact not found.")
    return contact_found

# Fungsi untuk menghapus kontak berdasarkan ID
def delete_contact(contact_id):
    for contact in yellow_pages:
        if contact["id"] == contact_id:
            yellow_pages.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main menu (tetap sama seperti sebelumnya)
def main_menu():
    while True:
        print("\nYellow Pages Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            read_contacts()
        elif choice == "3":
            contact_id = input("Enter ID of the contact to update: ")
            if contact_id.isdigit() and any(contact["id"] == int(contact_id) for contact in yellow_pages):
                while True:  # Loop untuk memastikan input valid
                    business_name = input("Enter new business name (leave blank if no change): ")
                    phone = input("Enter new phone (leave blank if no change): ")
                    email = input("Enter new email (leave blank if no change): ")
                    address = input("Enter new address (leave blank if no change): ")
                    category = input("Enter new category (leave blank if no change): ")
                    
                    # Memanggil update_contact dengan parameter yang valid
                    if update_contact(int(contact_id),
                                      business_name if business_name else None,
                                      phone if phone else None,
                                      email if email else None,
                                      address if address else None,
                                      category if category else None):
                        read_contacts()  # Menampilkan ulang tabel kontak setelah update berhasil
                        break  # Keluar dari loop jika update berhasil
                    else:
                        print("Please correct the input errors.")

            else:
                print("Invalid input for ID or contact not found.")
        elif choice == "4":
            contact_id = input("Enter ID of the contact to delete: ")
            if contact_id.isdigit() and any(contact["id"] == int(contact_id) for contact in yellow_pages):
                delete_contact(int(contact_id))
            else:
                print("Invalid input for ID or contact not found.")
        elif choice == "5":
            print("Exiting Yellow Pages...")
            break
        else:
            print("Invalid choice, please try again.")

# Menjalankan main menu
main_menu()