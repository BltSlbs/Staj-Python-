from db import save_data, load_data

def add_customer(customers, name, company):
    customers.append({"name": name, "company": company})
    save_data(customers)

def add_interns(interns, name, university):
    interns.append({"name": name, "university": university})
    save_data(interns)

def main():
    customers = load_data()
    interns = load_data()

    while True:
        print("\n*** Staj Defteri ERP Programı ***")
        print("1. Müşteri Ekle")
        print("2. Stajyer Ekle")
        print("3. Çıkış")

        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == '1':
            name = input("Müşteri adı: ")
            company = input("Şirket adı: ")
            add_customer(customers, name, company)
            print("Müşteri başarıyla eklendi!")
        elif choice == '2':
            name = input("Stajyer adı: ")
            university = input("Üniversite adı: ")
            add_interns(interns, name, university)
            print("Stajyer başarıyla eklendi!")
        elif choice == '3':
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()