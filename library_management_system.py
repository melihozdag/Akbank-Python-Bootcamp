class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        
    def __del__(self):
        self.file.close()
        
    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("Kütüphanenizde kitap bulunmamaktadır...")
        else:
            print("Kütüphanenizdeki kitaplar:")
            for index, book_info in enumerate(books):
                book_details = book_info.split(',')
                if len(book_details) == 4:
                    book_title, author, _, _ = book_details
                    print(f"{index+1}: {book_title.capitalize()}, {author.capitalize()}")

                
    def add_book(self):
        book_title = input("Kitap adı: ")
        book_author = input("Yazar adı: ")
        
        while True:
            try:
                first_release_year = int(input("Yayınlanma yılı: "))
                break
            except ValueError:
                print("Geçersiz giriş. Yıl bir tam sayı olmalıdır.")

        while True:
            try:
                page_number = int(input("Sayfa sayısı: "))
                break
            except ValueError:
                print("Geçersiz giriş. Sayfa sayısı bir tam sayı olmalıdır.")
                
        book = f"{book_title},{book_author},{page_number},{first_release_year}\n"
        self.file.write(book)
        
    def remove_book(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("Kütüphanenizde kitap bulunmamaktadır...")
        else:
            book_title_to_remove = input("Kaldırılacak kitap adı: ").capitalize()
            updated_books = []
            
            found = False
            for book_info in books:
                book_details = book_info.split(',')
                if len(book_details) == 4 and book_details[0].capitalize() == book_title_to_remove:
                    print(book_title_to_remove + " kütüphaneden kaldırıldı...")
                    found = True
                else:
                    updated_books.append(book_info)
                    
            if not found:
                print("Kütüphanenizde '" + book_title_to_remove + "' adlı kitap bulunmamaktadır.")
                    
            self.file.seek(0)
            self.file.truncate()
            
            for updated_book in updated_books:
                self.file.write(updated_book + '\n')

            
lib = Library()

while True:
    print("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Exit")
    user_choice = input("Yapmak istediğiniz işlemi seçiniz (1-4): ")
    
    if user_choice == "1":
        lib.list_books()
    elif user_choice == "2":
        lib.add_book()
    elif user_choice == "3":
        lib.remove_book()
    elif user_choice == "4":
        print("Menuden çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek. Lütfen 1 ile 4 arasında bir sayı giriniz.")
