
book1={"title": "Гарри Поттер и философский камень", "author":"Джоан Роулинг","year":"1997"}
book2={"title":"Гарри Поттер и Тайная комната","author":"Джоан Роулинг","year":"1998"}
book3={"title":"Гарри Поттер и узник Азкабана","author":"Джоан Роулинг","year":"1999"}
book4={"title":"Гарри Поттер и Кубок огня","author":"Джоан Роулинг","year":"2000"}
book5={"title":"Гарри Поттер и Орден Феникса","author":"Джоан Роулинг","year":"2003"}
books=[ book1,book2,book3,book4,book5]
count=1
for i in books:
    
    for key, value in i.items():
       
      
       if key =='title':
           print(f"--------------------------Книга {count}-----------------------")
           print(f"Название:{value}",end =', ')
           count+=1

       elif key =='author':
           print(f"Автор:{value}")
    print(f"----------------------------{value}------------------------")
    print()
       
    # print(f"-----------{value}--------")
    # print()
    # if key =='title':
    #        print(f"-----------{count}----------")
    #        print(f"Название:{value}")
    #        count+=1

    #    elif key =='author':
    #        print(f"Автор:{value}")