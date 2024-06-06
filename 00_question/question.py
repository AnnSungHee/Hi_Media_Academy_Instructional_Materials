# ### **문제 2: 학생 성적 관리 프로그램**

# 학생들의 성적을 관리하는 프로그램을 작성하세요. 프로그램은 다음 기능을 포함해야 합니다:

# 1. 학생의 이름과 성적을 입력 받아 저장합니다.
# 2. 특정 학생의 성적을 조회합니다.
# 3. 모든 학생의 평균 성적을 계산하여 출력합니다.
# 4. 성적이 특정 점수 이상인 학생들의 이름을 출력합니다.

student_score = { }

cnt = 0

# 1. 학생의 이름과 성적을 입력 받아 저장
while(cnt <= 3) :
    print("이름 ")
    name = input()
    print("성적 ")
    score = input()
    student_score[name] = int(score)
    cnt = cnt + 1

# 2. 성적을 조회할 학생의 이름을 매개변수로 받고 해당 학생의 점수를 return
def browse_student(x) : 
    return student_score[x]

# 3. 모든 학생의 평균 성적을 계산하여 출력
def average_score() :
    scores = 0
    cnt = 0
    for x in student_score.values() :
        scores = scores + int(x)
        cnt = cnt + 1
    return scores / cnt

# 4. 특정 점수를 매개변수로 받아서 해당 점수 이상의 학생을 출력
def search_score(sco) :
    for x,y in student_score.items() :
        if (y >= sco):
            print(x)

print("성적을 조회할 학생의 이름을 입력하시오.")

specific_name = input()

print(browse_student(specific_name))

print("평균 성적 " + str(average_score()))

print("특정 점수의 학생을 찾읍시다.")
specific_sco = input()
search_score(int(specific_sco))


# print()

