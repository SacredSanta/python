'''
# 참고한 코드 원본 링크 #

검색어 : python 윈도우 창 옮기기   https://goodthings4me.tistory.com/491   
마우스 클릭     https://blog.naver.com/PostView.naver?blogId=heennavi1004&logNo=222053488845&parentCategoryNo=&categoryNo=82&viewDate=&isShowPopularPosts=true&from=search
+ https://m.blog.naver.com/jsk6824/221765884364

사용자 이름 변경으로 인해 PATH 오류 -> 대부분 바로가기의 속성 문제일 확률이 높다.
visual code의 파일위치찾기 -> 속성 -> 바로가기 경로를 수정해주면된다.    응 안돼~
<!-- --> https://enjoytools.net/xe/board_PZRP31/4816#google_vignette 여기 참고...
'''

import pyautogui
import pywinauto
import os
import time
import tkinter as tk




# https://picory.com/entry/Python-%ED%8A%B9%EC%A0%95-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4-%EC%A2%85%EB%A3%8C-%EC%8B%9C%ED%82%A4%EA%B8%B0
import psutil

for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processID = proc.pid

        print(processName[:6])

        # if processName[:6] == "python": # 윈도우는 python.exe로 올라옴
        #     commandLine = proc.cmdline()

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


print('동일 프로세스 확인 완료....')









# -------------------------  DEBUG ZONE  -------------------------------- 

check_win = ['Chrome', '내 일정 관리', 'Microsoft Teams']

def check_curwin():
    curwinlist = []
    fwAll = pyautogui.getAllWindows()
    for windows in fwAll:
        curwinlist.append(windows.title)
    
    for check in check_win:
        if check not in curwinlist:
            return check
        else:
            if check != 'Microsoft Teams':
                continue
            else:
                return 0
        

os.startfile('Chrome.exe')
os.startfile('Microsoft Teams.lnk')


# pyautogui.click(x=1051, y=1057)  #완전 하드코딩;
# os.startfile("C:\\Users\\서동휘\\AppData\\Local\\Programs\\Notion\\Notion.exe")
# 원래 노션을 이렇게 실행시키려고 했으나 오류로 인한 실패

fwAll = pyautogui.getAllWindows()   # 모든 윈도우 창 가져오기
curwinlist = []
for windows in fwAll:
    curwinlist.append(windows.title)
flag = 1
i = 0
justonce = 2

# 창 3개 다 열렸는지 확인
while(flag):
    A = check_curwin()
    if A == 0:
        flag = 0
    else:
        if justonce != 0:
            justonce = justonce - 1
            continue
        print(A,"가 실행이 되지않음")
        needW = str(A)
        pyautogui.typewrite(['win'])
        pyautogui.typewrite('notion')
        pyautogui.typewrite(['enter'])  # 걍 하드하게 불러오기..
        flag = 1
    time.sleep(5)
    i = i+1

w1 = pyautogui.getWindowsWithTitle('Chrome')
w1[0].left=-1542
w1[0].top=-122
w1[0].width=1037
w1[0].height=1118
# <Win32Window left="-1542", top="-122", width="1037", height="1118", title="Chrome">

w2 = pyautogui.getWindowsWithTitle('내 일정 관리')
w2[0].left=-2566
w2[0].top=503
w2[0].width=1037
w2[0].height=494
# <Win32Window left="-2566", top="503", width="1037", height="494", title="내 일정 관리">

w3 = pyautogui.getWindowsWithTitle('Microsoft Teams')
w3[0].left=-2560
w3[0].top=-122
w3[0].width=1024
w3[0].height=627
# <Win32Window left="-2560", top="-122", width="1024", height="627", title="Microsoft Teams">





'''
참고 코드
'''
# mpos_x, mpos_y = pyautogui.position()   #마우스 위치 나타내기
# print(mpos_x, mpos_y) # 1151, 1057


# fw = pyautogui.getActiveWindow()   # 켜진 창 정보보기
# print(fw.title)
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 25, fw.top + 20)

# fwAll = pyautogui.getAllWindows()   # 모든 윈도우 창 가져오기
# for w in fwAll:
#     print(w)

# w = pyautogui.getWindowsWithTitle('Notion')  #특정 제목을 가지는 윈도우창 정보 가져오기(list로 가져오기 때문에 개별 선택이 필요하다)
# for chr in w:
#     print(chr)


# m = pyautogui.getWindowsWithTitle('메모장')[0]
# print(m)
# if w.isActive == False:
#     pywinauto.application.Application().connect(handle=w._hWnd).top_window().set_focus()
#     w.activate()


'''
ERROR_CODE
'''
# C:\Users\서동휘\Desktop\pratice> c: && cd c:\Users\서동휘\Desktop\pratice && cmd /C "C:\Users\서동휘\AppData\Local\Programs\Python\Python310\python.exe c:\Users\서동휘\.vscode\extensions\ms-python.python-2022.14.0\pythonFiles\lib\python\debugpy\adapter/../..\debugpy\launcher 62798 -- c:\Users\서동휘\Desktop\pratice\windowmove.py "

# 20:41:11.498 > Checking for update
# 20:41:11.761 > App ready with version 2.0.29
# 20:41:11.999 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'latestVersionPath',
#   data: {
#     message: 'latestVersion.json path C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\latestVersion.json'
#   }
# }
# 20:41:12.030 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'currentVersionLoaded',
#   data: { version: '23.10.26.19', hash: '8c4aeb4516aef9a956135e1206402f88' }
# }
# 20:41:12.032 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'syncVersions',
#   data: {
#     message: 'Sync versions: assets.json path C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets.json headers.json path C:\\Users\\?쒕 
# 룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\headers.json'       
#   }
# }
# 20:41:12.062 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'currentSyncedAssetsJson',
#   data: { version: '23.10.26.19' }
# }
# (node:7560) electron: The default of nativeWindowOpen is deprecated and will be changing from false to true in Electron 15.  See https://github.com/electron/electron/issues/28511 for more information.
# (Use `Notion --trace-warnings ...` to show where the warning was created)
# (node:7560) electron: The default of nativeWindowOpen is deprecated and will be changing from false to true in Electron 15.  See https://github.com/electron/electron/issues/28511 for more information.
# (node:7560) electron: The default of nativeWindowOpen is deprecated and will be changing from false to true in Electron 15.  See https://github.com/electron/electron/issues/28511 for more information.
# 20:41:12.470 > Showing window with id 1
# 20:41:12.536 > Update for version 2.0.29 is not available (latest version: 2.0.29, downgrade is disallowed).
# 20:41:12.716 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'syncVersionSameSkippingSync'
# }
# 20:41:12.719 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest2',
#   data: {
#     message: 'Performing file request: /, abs path C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\index-ko-KR-fa52605a6bea9d848044.html'
#   }
# }
# 20:41:12.846 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\644-2a7873b6cc2d434334f4.js',
#     url: '/644-2a7873b6cc2d434334f4.js'
#   }
# }
# 20:41:12.850 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\app-8b7241513d03a329ddcc.js',
#     url: '/app-8b7241513d03a329ddcc.js'
#   }
# }
# 20:41:12.853 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\app-b80ae593881436f4ef02.css',
#     url: '/app-b80ae593881436f4ef02.css'
#   }
# }
# 20:41:12.856 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\print.b31f28aa.css',
#     url: '/print.b31f28aa.css'
#   }
# }
# 20:41:13.867 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\primusV8-6a439f5c292567d52ed9.js',
#     url: '/primusV8-6a439f5c292567d52ed9.js'
#   }
# }
# 20:41:14.453 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\analytics-amplitude-3c68b6ff07d238a40a08.js',
#     url: '/analytics-amplitude-3c68b6ff07d238a40a08.js'
#   }
# }
# 20:41:14.706 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\emoji-english-babb41ba67ca1079aadd.js',
#     url: '/emoji-english-babb41ba67ca1079aadd.js'
#   }
# }
# 20:41:14.713 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\markdown-linkify-it-de6de0a7cf56f508e657.js',
#     url: '/markdown-linkify-it-de6de0a7cf56f508e657.js'
#   }
# }
# 20:41:14.717 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\tinymce-word-paste-filter-f53fbfab3c962ddda1d0.js',
#     url: '/tinymce-word-paste-filter-f53fbfab3c962ddda1d0.js'
#   }
# }
# 20:41:14.761 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\381-bf64900dff49169faead.js',
#     url: '/381-bf64900dff49169faead.js'
#   }
# }
# 20:41:14.764 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\585-2f89b49cc69b512c359a.js',
#     url: '/585-2f89b49cc69b512c359a.js'
#   }
# }
# 20:41:14.767 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\414-493a9a89932ae7972f1d.js',
#     url: '/414-493a9a89932ae7972f1d.js'
#   }
# }
# 20:41:14.770 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\383-9bf0167e56a6557de816.js',
#     url: '/383-9bf0167e56a6557de816.js'
#   }
# }
# 20:41:14.772 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\827-269212c2ce8e9d601b16.js',
#     url: '/827-269212c2ce8e9d601b16.js'
#   }
# }
# 20:41:14.775 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\postRender-d4c4d910b4650dfcaf97.js',
#     url: '/postRender-d4c4d910b4650dfcaf97.js'
#   }
# }
# 20:41:14.905 > {
#   level: 'info',
#   from: 'AssetCache',
#   type: 'performingFileRequest',
#   data: {
#     absolutePath: 'C:\\Users\\?쒕룞??\AppData\\Roaming\\Notion\\notionAssetCache-v2\\23.10.26.19\\assets\\emoji-korean-c1f9db6ac4877188a12b.js',
#     url: '/emoji-korean-c1f9db6ac4877188a12b.js'
#   }
# }