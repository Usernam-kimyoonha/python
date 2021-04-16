# 1
x = [3,2,4,1]

for n in x:           # 리스트 x 를 n에 3,2,4,1
    print(n)          # 하나씩 출력
    
# 2
x = [3,2,4,1]
y = ["Hello", "There"]
for c in y:           # 리스트 y를 c에 차례로
    print(c)          # 출력된다.
    
# 3    
# 엘레먼트 위치 찾기
x = [3,2,4,1]
    #0,1,2,3
y = ["Hello", "There"]

print(x.index(4))        # 변수 x의 리스트 0, 1, 2에서 2에 있다.  없는 숫자를 넣으면 에러
print(y.index("Hello"))  # 변수 y에서 Hello는 0번에 있다.


# # 4
x = [3,2,4,1]
    #0,1,2,3
y = ["Hello", "There", "bye"]

print("bye" in y)    # y에 bye가 있는지 True or False로 확인
print("Hello" in y)  # y에 Hello가 있는 True or False로 확인

if "Hello" in y:
    print("Hello가 있어요.")
    
if "bye" in y:
    print("bye")
#print("bye는 없어요.")