class Student : #클래스 이름 대문자
    #student를 초기화하는 생성자
    def __init__(self, name="", korean=0, math=0, eng=0):
        self.name = name
        self.korean = korean
        self.math = math
        self.eng = eng

    def get_average(self) : #get_avg 메서드 선언
        avg = (self.korean + self.math + self.eng) / 3 #국영수 평균점수 계산
        return avg #인스턴스가 갖는 국어,수학,영어 점수의 평균 반환
    
def load_data(file_name) :
    student_list=[]
    fp = open("week12/students.csv", "r", encoding="utf-8") #학생 정보가 저장된 파일 열기
    lines = fp.readlines() #불러온 파일을 줄 별로 읽기
    for line in lines[1:] : #첫번째 줄 제외하고 학생들 정보가 담긴 줄에 대해서만 처리
        data = line.strip().split(',') #파일의 각 줄을 쉼표로 분리->학생의 이름과 성적 얻음
        #인스턴스
        #불러온 파일의 한줄한줄이 하나의 인스턴스(=학생)가 되는 것
        student_instance = Student()
        student_instance.name = data[0] #학생 이름을 학생 인스턴스 name에 저장
        student_instance.korean = float(data[1]) #국어 점수를 학생 인스턴스 korean에 저장
        student_instance.math = float(data[2]) #수학 점수를 학생 인스턴스 math에 저장
        student_instance.eng = float(data[3]) #영어 점수를 학생 인스턴스 english에 저장
        student_list.append(student_instance) #리스트에 학생 인스턴스 추가
    return student_list #각각의 학생 정보가 담긴 리스트 반환