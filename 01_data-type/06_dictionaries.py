
# Dictionaries

# 키와 값 의 쌍으로 것오딘 데이터 구조로,키를 통해 값을 찾을 수 있으므로 매우 빠른 조회 성능을
# 보여준다.












# in 키워드
print('name' in teacher)


# 1. get()
# 매개변수로 전달받은 key에 해당하는 값을 반환한다.
print(teacher.get('name'))


# 2. keys()
print(teacher.keys())


# 3. values()
print(teacher.values())


# 4. items()
print(teacher.items())
print(teacher)


# 5. pop(키)
print(teacher.pop('age'))
print(teacher)

# 6. clear()
teacher.clear()
print(teacher)