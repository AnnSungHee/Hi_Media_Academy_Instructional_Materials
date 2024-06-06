
# else 문
# 정상적으로 모든 루프가 종료된 후 else 안에 있는 내용이 실행된다.

for x in [1,2,3] :
    print(x)
else:   # 모든 루프가 끝난 뒤에 실행할 명령문
    print("끝")



# continue 문
# 반복문 안에서 continue 를 만나면 다음 실행문은 실행되지 않고 다음 반복으로 넘어간다.
# 특정 순간을 생략하고 진행하기 위해 사용된다.
for i in range(3) :
    if i == 1:
        continue
    print(i)

print("break 문")
# break 문
# 반복문을 종료할 때 사용한다.
# break를 만나면 남은 과정은 모두 취소된다.
for x in [1,2,3] :
    if x == 2 :
        print("끝")
        break
    else:
        print(x)