def solution(phone_book):
    # 1. 해시 맵 생성
    phone_dict = {p: True for p in phone_book}

    # 2. 모든 번호를 하나씩 꺼내서
    for p in phone_book:
        temp = ""
        # 글자를 하나씩 붙여가며 접두어인지 확인
        for num in p[:-1]:  # 마지막 글자 전까지만 (자기 자신 제외)
            temp += num
            if temp in phone_dict:  # 딕셔너리에 있으면 바로 False 반환
                return False

    return True
