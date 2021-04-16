def chat(name1, name2):      
    print("%s: 안녕? 넌 몇살이니?" %name1)
    print("%s: 나? 나는 20살이야!" %name2)
chat("정수", "태희")
chat("은지", "가연")
def chat(name1, name2, age): 
    print("%s: 안녕? 넌 몇살이니?" % name1)
    print("%s: 나? 나는 %d" % (name2, age) + "살이야!")
chat("정수", "태희", 20)
chat("은지", "가연", 19)