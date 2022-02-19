import time, win32con, win32api, win32gui
from pywinauto import clipboard

talk_name = '이해강'
chat_command = '야스'

def open_chatroom(name):
    hwndKakao = win32gui.FindWindow(None,'카카오톡')
    hwndKakao_edit1 = win32gui.FindWindowEx(hwndKakao,None,"EVA_ChildWindow",None)
    hwndKakao_edit2_1 = win32gui.FindWindowEx(hwndKakao_edit1,None,"EVA_Window",None)
    hwndKakao_edit2_2 = win32gui.FindWindowEx(hwndKakao_edit1, hwndKakao_edit2_1,"EVA_Window",None)
    hwndKakao_edit3 = win32gui.FindWindowEx(hwndKakao_edit2_2,None,"Edit",None)

    win32api.SendMessage(hwndKakao_edit3, win32con.WM_SETTEXT,0,name)
    time.sleep(1)
    SendReturn(hwndKakao_edit3)
    time.sleep(1)

def kakao_sendtext(name,text):
    #캡션(이름)이 talk_name인 창을 찾아서 핸들을 저장
    hwndMain = win32gui.FindWindow(None,name)

    #hwndMain의 자식인 RichEdit20W(텍스트 박스)의 핸들을 저장
    hwndEdit = win32gui.FindWindowEx(hwndMain,None,"RICHEDIT50W",None)

    win32api.SendMessage(hwndEdit,win32con.WM_SETTEXT,0,text)
    SendReturn(hwndEdit)

#엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd,win32con.WM_KEYDOWN,win32con.VK_RETURN,0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd,win32con.WM_KEYUP, win32con.VK_RETURN,0)



#글이 올라오는 대화창의 핸들, 채팅 내용 인식할 때 필요
#hwndListControl = win32gui.FindWindowEx(hwndMain,None,"EVA_VH_ListControl_Dblclk",None)


def main():
    
    open_chatroom(talk_name)
    text = "test"
    kakao_sendtext(talk_name,text)

if __name__ == '__main__':
    main()