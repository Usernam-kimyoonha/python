def sayhello(name,age):
    if age < 10:
        print("안녕." + name +"군")
    elif age <= 20 and age >= 10:
        print("안녕하세요." + name +" 씨")
    else:
        print("안녕하십니까?" + name + " 님")
        
sayhello("철수", 6)
sayhello("태희", 11)
sayhello("정수", 21)
sayhello("병선", 30)