book1={"title": "Гарри Поттер и философский камень", "author":"Джоан Роулинг","year":"1997"} #создание словаря 
book2={"title":"Гарри Поттер и Тайная комната","author":"Джоан Роулинг","year":"1998"}  #создание словаря 
book3={"title":"Гарри Поттер и узник Азкабана","author":"Джоан Роулинг","year":"1999"}  #создание словаря 
book4={"title":"Гарри Поттер и Кубок огня","author":"Джоан Роулинг","year":"2000"}  #создание словаря 
book5={"title":"Гарри Поттер и Орден Феникса","author":"Джоан Роулинг","year":"2003"}  #создание словаря 
books=[ book1,book2,book3,book4,book5] #из предыдущих словарей создаём список 
count=1 #переменная для подсчёта наших книг 
for i in books: #цикл для перебора словарей в списке 
    
    for key, value in i.items(): # цикл переберающий ключи и значения в каждом словаре 
       
       if key =='title': #если ключ равен "title"
           print(f"Книга {count}".center(58,"-")) #вывод на консоль 
           print(f"Название:{value}",end =', ') #вывод на консоль названия нашей книги 
           count+=1

       elif key =='author': #если ключ равен "author"
           print(f"Автор:{value}") #вывод на консоль автора нашей книги 
    print(f"{value}".center(58,"-")) #вывод на консоль даты выхода книги
    print() #выводим пустую строку
