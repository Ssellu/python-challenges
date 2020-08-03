"""

    Employee 클래스가 있습니다.
    필드 : 직원 이름(name), 부서(department), 연봉(salary), 이메일(email)
        ** 부서는 '경영부', '마케팅부', '영업부', '개발부' 가 있습니다.
        ** 전체 직원 수를 세는 total_employees 변수를 선언하세요.
            직원이 추가 될 때마다 (객체가 생성될 때마다) 1씩 증가되도록 합니다.
            => 클래스변수로 선언해도 되는지 판단하세요.

    생성자 : 자유롭게 정의

    메서드 :
        set_data(kwargs**)
            => set_data(name='홍길동', email='user01@gmail.com')
            => set_data(email='user02@gmail.com', salary=100000000, name='고길동')
            모두 가능 하게끔 키워드 매개변수를 활용하여 각 필드에 올바른 데이터가 저장될 수 있도록 하세요
            리턴값은 없습니다.
            => staticmethod 로 선언해도 되는지 판단하세요.

        check_email()
            => 객체의 email 이 naver.com, gmail.com, nate.com 중 1개로 끝나는지 확인하세요.
                문자열.endswith() 를 활용하세요.
                    e.endswith('@naver.com') 을 예로들면
                    endswith()는 e가  '@naver.com' 로 끝난다면 True 를 ,아니면 False 를 return 합니다.
            => 셋 중 하나로 끝난다면 True 를, 아니면 False 를 return 하세요.
            => staticmethod 로 선언해도 되는지 판단하세요.

        raise_salary()
            => 현재 연봉의 2%를 추가하세요.
            => staticmethod 로 선언해도 되는지 판단하세요.

        add_department()
            => 인자로 들어온 부서를 추가하세요.
            => 부서 리스트의 초기값은 다음과 같습니다.
                '경영부', '마케팅부', '영업부', '개발부'
            => 만약 add_department('생산부') 을 하게되면
              부서 리스트의 값은 다음과 같습니다.
              '경영부', '마케팅부', '영업부', '개발부', '생산부'
            => 부서 리스트를 클래스변수로 선언해도 되는지 판단하세요.
            => add_department() 를 staticmethod 로 선언해도 되는지 판단하세요.


"""
