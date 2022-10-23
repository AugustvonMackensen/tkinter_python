from tkinter import *

def processOK():
    print('OK 버튼이 클릭되었습니다.')

def processCancel():
    print('cancel 버튼이 클릭되었습니다.')

window = Tk() # 창 생성
btOK = Button(window, text='OK', fg='red', command=processOK)
btCancel = Button(window, text='Cancel', fg='yellow', command=processCancel)

btOK.pack() # ok버튼 배치
btCancel.pack() # Cancel 버튼 창 내부 배치

window.mainloop() # 이벤트 루프 생성.
