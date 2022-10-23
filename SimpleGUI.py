# tkinter 정의 임포트
# Tkinter는 객체지향 프로그래밍을 학습하기 위한 중요한 교육 도구이기도 함
from tkinter import * # * : 모든 정의를 프로그램에 임포트한다는 뜻.

# Tkinter에서 GUI 기반 프로그램 생성시, tkinter 모듈 임포트 후 Tk 클래스 생성해 창 생성함
# Tk() : 창의 인스턴스를 생성함
# Label과 Button은 레이블과 버튼을 생성하기 위한 파이썬 Tkinter 위젯 클래스(widget class)임.
# 위젯 클래스의 첫 번째 인자는 항상 부모 컨테이너가 됨
# Tkinter GUI 프로그래밍은 이벤트 구동(event-driven) 방식.


window = Tk() # 창 생성

label = Label(window, text='파이썬에 오신 것을 환영합니다.') # 레이블 생성
button = Button(window, text='저를 클릭해주세요.') # 버튼 생성
label.pack() # 창 내부에 레이블 배치
button.pack() # 창 내부에 버튼 배치

window.mainloop() #이벤트 루프 생성.
