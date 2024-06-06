### **문제: 은행 관리 프로그램**

# 1. `Account` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행 계좌의 소유주 이름과 초기 잔액을 설정합니다.
#     - `deposit` 메서드를 사용하여 입금을 처리합니다.
#     - `withdraw` 메서드를 사용하여 출금을 처리합니다. 출금할 금액이 잔액보다 크면 출금을 허용하지 않습니다.
#     - `display_balance` 메서드를 사용하여 현재 잔액을 출력합니다.
# 2. `Bank` 클래스를 정의하세요. 이 클래스는 다음과 같은 특징을 가지고 있어야 합니다:
#     - `__init__` 메서드를 사용하여 은행의 이름을 설정합니다.
#     - `create_account` 메서드를 사용하여 새로운 계좌를 생성합니다.
#     - `get_account` 메서드를 사용하여 계좌를 반환합니다.
#     - `display_accounts` 메서드를 사용하여 현재 은행에 있는 모든 계좌 정보를 출력합니다.
# 3. 사용자가 여러 번 계좌를 생성하고 입금, 출금, 잔액 조회 등의 작업을 수행할 수 있도록 하세요. 
# 사용자가 프로그램을 종료하고 싶을 때에는 "종료"를 입력하면 됩니다.


class Account:
    # 이름, 초기잔액
    def __init__(self, name, init_balance):
        self.name = name
        self.init_balance = init_balance

    # 입금 처리
    def deposit(self, inmoney):
        self.init_balance += inmoney
        return str(inmoney) + "원 입금 완료 현재 잔액 " + str(self.init_balance)

    # 출금 처리 
    def withdraw(self, outmoney):
        if(outmoney > self.init_balance):
            return "금액이 너무 많습니다."
        else:
            self.init_balance -= outmoney
            return str(outmoney) + "원 출금 완료 현재 잔액 " + str(self.init_balance)

    # 현재 잔액 출력
    def display_balance(self):
        return self.name + " 계좌 현재 잔액 " + str(self.init_balance)

class Bank: 
    # 은행 이름
    bank_name = ""
    # 총 계좌 수
    now_account_number = 0
    # 마지막 계좌 번호
    last_bank_account_number = 0
    # 계좌 정보들
    accountlist = []

    # 생성자 은행의 이름 설정
    def __init__(self, bank_name):
        Bank.bank_name = bank_name
        
    # 새로운 계좌 생성()
    def create_account(self):
        Bank.accountlist.append([Bank.last_bank_account_number, 0])
        print("계좌 번호 : " + str(Bank.last_bank_account_number))
        Bank.last_bank_account_number += 1

    # 계좌 반환
    def get_account(self, account):
        for x in Bank.accountlist:
            try:
                index = x.index(account)
                print("\n계좌 번호 : " , x[0] , "잔액 : " , x[1])
            except ValueError:
                pass
        
    # 현재 모든 계좌 정보 출력
    def display_accounts(self):
        for x in Bank.accountlist:
            for y in x:
                print(y)
            print()
    
my_account = Account("안성희", 10000)

# print(my_account.display_balance())

# print(my_account.deposit(50000))

# print(my_account.withdraw(50000))

# print(my_account.withdraw(50000))

# print("은행 이름 : ", Bank.bank_name)

# print("은행 이름 : ", Bank.bank_name)
# bank.create_account()
# bank.create_account()
# bank.create_account()
# bank.create_account()
# bank.create_account()
# bank.display_accounts()
# bank.get_account(1)
bank = Bank("하이 미디어")
print("안녕하세요 " + Bank.bank_name + "은행입니다.")

while(True):
    print("\n1. 계좌 생성")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌 확인")
    print("5. 종료")
    print("원하시는 작업을 선택해주세요.")
    
    action_number = input()

    match action_number:
        # 계좌 생성
        case "1":
            bank.create_account()
            pass
        # 입금
        case "2":
            pass
        # 출금
        case "3":
            pass
        # 현재 잔액 출력
        case "4":
            pass
        case "5":
            print("작업을 종료합니다.")
            break



