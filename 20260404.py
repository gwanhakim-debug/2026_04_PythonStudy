number='0'
kor=0
eng=0
math=0

prompt = """
    1. 국어 점수 입력
    2. 영어 점수 입력
    3. 수학 점수 입력
    4. 총점 및 평균 출력
    5. 종료

    번호선택>>"""

while number != "5":
    print(prompt)
    number = input("번호>>")

    if number == "1":
        kor=int(input("국어 점수:"))
    elif number == "2":
        eng=int(input("영어 점수:"))
    elif number == "3":
        math=int(input("수학 점수:"))
    elif number == "4":
        total = kor + eng + math
        average = total / 3
        print(f"국:{kor}, 영:{eng}, 수:{math}, 총점: {total}, 평균: {average}")
    elif number == "5":
        print("프로그램을 종료합니다.")
    else:
        print("잘못된 번호입니다. 다시 선택해주세요.")