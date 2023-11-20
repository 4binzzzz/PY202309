import Student #Student.py 불러오기


#메인 프로그램
student_list = Student.load_data("students.csv") #Student 파일 불러와서 함수 호출
print('-----학생들의 평균 점수-----')
for student_instance in student_list: #학생 정보가 담긴 리스트에서 각각의 인스턴스에 대해 반복
    print(student_instance.name,'의 평균 점수는 ',student_instance.get_average(),'입니다.')


# 평균 점수를 파일에 저장
with open('average.txt', 'w', encoding='utf-8') as output_file: #average.txt파일 쓰기모드로 열기
    output_file.write("------학생들의 평균 점수------\n") #처음 한줄만 작성되면 되기 때문에 반복문에 넣지 않음
    for student_instance in student_list: #학생 정보가 담긴 리스트에서 각각의 인스턴스에 대해 반복
        output_file.write(f"{student_instance.name}의 평균 점수는 {student_instance.get_average()}입니다.\n") #학생 평균 점수 한줄씩 입력


