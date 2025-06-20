#6개의 리스트 선언
First = ["기후 예측", "친환경 교통 수단", "기후 정책"]
Second = ["기후 모델링", "기후 데이터 분석", "충전 인프라 확충", "대중 교통 개선", "탄소 배출 규제", "재생 가능 에너지 자원", "기후 협약 참여"]
Third = ["에너지 효율", "환경 규제", "지속 가능한 도시", "생태계 보전", "농업 혁신", "전기 자동차", "전기 버스", "버스요금 인상", "도시 자전거 공유 시스템", "온실 가스 감축 정책", "친환경 산업 지원", "재생 가능 에너지", "국제 환경 협력"]
Forth = ["경제 성장", "에너지 자립", "경제 활동 유연성", "기업 규제 완화", "도시 개발 확장", "개인 차량 우선", "보험료 절감", "생물 다양성 보전", "유기농 농업 확대", "지역 농업 지원", "국가 전기차 보조금", "탄소 중립", "대중교통 노조", "공공 건강", "기술 개발", "에너지 제로 하우스", "확대 필요성", "필요한 이유"]
Fifth = ["재생 가능 에너지", "환경 지속 가능성", "오염 물질 제한", "지속 가능한 자원 권리", "도시 녹지 공간 확대", "대중 교통 개선", "보건 교육 실시", "그린벨트 반대", "농업 기술 촉진", "경제적 농업 지원", "전기차 사고율", "중국산 전기버스", "버스요금 인상 반대", "디지털 약자 소외", "목표량 달성 실패", "그린워싱 광고", "비리 의혹", "구속력 없음"]
Arctics = []

#웹크롤링(추가예정)

#1개의 리스트에 5개의 리스트 통합
Arctics = First + Second + Third + Forth + Fifth

#점수 리스트 생성, 상위 3개의 키워드가 들어갈 변수 생성
Scores = []
Relative = [3, 4, 0], [5, 6, 0], [7, 9, 8], [10, 12, 11], [13, 14, 0], [15, 16, 0], [17, 18, 0], [19, 20, 0], [21, 0, 0], [22, 0, 0], [41, 24, 0], [43, 26, 0], [45, 28, 0], [48, 30, 0], [49, 32, 0], [33, 51, 0], [52, 34, 0], [53, 35, 0], [36, 54, 0], [55, 37, 0], [38, 56, 0], [57, 39, 0], [40, 58, 0], [41, 0, 0], [42, 0, 0], [43, 0, 0], [44, 0, 0], [45, 0, 0], [46, 0, 0], [0, 0, 0], [48, 0, 0], [49, 0, 0], [50, 0, 0], [51, 0, 0], [52, 0, 0], [53, 0, 0], [54, 0, 0], [55, 0, 0], [56, 0, 0], [57, 0, 0], [58, 0, 0], [23, 0, 0], [24, 0, 0], [25, 0, 0], [26, 0, 0], [27, 0, 0], [28, 0, 0], [29, 0, 0], [30, 0, 0], [31, 0, 0], [32, 0, 0], [33, 0, 0], [34, 0, 0], [35, 0, 0], [36, 0, 0], [37, 0, 0], [38, 0, 0], [39, 0, 0], [40, 0, 0]
Ceiling, Wall, Floor = " ", " ", " "

#기사 리스트의 개수만큼 점수 항목 추가
for i in range(len(Arctics)):
    Scores.append(0)
#텍스트 출력
print("\n# Anti-Algorithm\n\n//환경 오염에 관한 기사//\n\n")
#0번, 1번, 2번 기사 항목에 권위 점수 100점 추가
Scores[0] = 152
Scores[1] = 151
Scores[2] = 150
print(Scores) #디버깅용
#새로운 리스트 4개, 변수 1개 추가
Bdict = {}
Flist, ranks, index, sorted_indices = [], [], [], []
ans = ""
#함수 선언 시작
def ranksys():
    #함수에 변수, 리스트 불러오기
    global Scores, Arctics, Bdict, ranks, ans, Flist, index, Relative
    #리스트 3개 초기화
    Bdict = {}
    Flist, index = [], []
    #점수에 따라 순위 부여 후 리스트화
    ranks = [sorted(Scores, reverse=True).index(ele) for ele in Scores]
    print(Arctics)
    print(Scores)
    print(ranks)

    #순위에 해당하는 키워드와 등급을 리스트에 삽입
    for i in range(len(ranks)):
        if ranks[i] == 0:
            Bdict[i] = Arctics[i] + "a"
            #print(BList)
        elif ranks[i] == 1:
            Bdict[i] = Arctics[i] + "b"
            #print(BList)
        elif ranks[i] == 2:
            Bdict[i] = Arctics[i] + "c"
            #print(BList)
        else:
            pass

    print(Bdict) #디버깅용
    #등급을 제거하여 새로운 리스트에 추가
    for i in range(59):
        if i in Bdict:
            if "a" in Bdict[i]:
                Flist.append(Bdict[i].strip("a"))
                index.append(i)
                #print(Flist)
    if len(Flist) < 4:
        for i in range(59):
            if i in Bdict:
                if "b" in Bdict[i]:
                    Flist.append(Bdict[i].strip("b"))
                    index.append(i)
                #print(Flist)
    if len(Flist) < 4:
        for i in range(59):
            if i in Bdict:
                if "c" in Bdict[i]:
                    Flist.append(Bdict[i].strip("c"))
                    index.append(i)
                #print(Flist)
    print(Flist)
    print(len(Bdict))
    print(index)
    #3개 각각의 변수에 상위 점수를 가진 키워드 할당 
    Ceiling, Wall, Floor = Flist[0], Flist[1], Flist[2]
    ans = int(input(f"""1. {Ceiling}
                
2. {Wall}

3. {Floor}

Clicked>>>"""))
    
    
    return ranks, ans, Flist, index
#함수 끝

def find_list_containing_item(item):
    if item in First:
        return 1
    elif item in Second:
        return 2
    elif item in Third:
        return 3
    elif item in Forth:
        return 4
    elif item in Fifth:
        return 5

while max(Scores) > -999:
    ranksys()
    finclu = find_list_containing_item(Arctics[index[0]])
    senclu = find_list_containing_item(Arctics[index[1]])
    thnclu = find_list_containing_item(Arctics[index[2]])
    if ans == 1:
        if finclu > 3:
            if senclu != finclu:
                Scores[index[1]] -= 50
            if thnclu != finclu:
                Scores[index[2]] -= 50
        for i in range(3):
            if Relative[index[0]][i] != 0:
                Scores[Relative[index[0]][i]] += 200 - 48 * i
        print(Arctics[index[0]])
        Scores[index[0]] = -999
        for i in range(3):
            Scores[index[i]] -= 50
    if ans == 2:
        if senclu > 3:
            if finclu != senclu:
                Scores[index[0]] -= 50
            if thnclu != finclu:
                Scores[index[2]] -= 50
        for i in range(3):
             if Relative[index[1]][i] != 0:
                Scores[Relative[index[1]][i]] += 200 - 48 * i
        Scores[index[1]] = -999
        for i in range(3):
            Scores[index[i]] -= 50
    if ans == 3:
        if thnclu > 3:
            if finclu != thnclu:
                Scores[index[0]] -= 50
            if senclu != thnclu:
                Scores[index[1]] -= 50
        for i in range(3):
             if Relative[index[2]][i] != 0:
                Scores[Relative[index[2]][i]] += 200 - 48 * i
        print(Arctics[index[2]])
        Scores[index[2]] = -999
        for i in range(3):
            Scores[index[i]] -= 50
