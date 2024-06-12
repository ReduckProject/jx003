import time

import WindowsUtils
from WyKeybord import WyKeybord

wyk=WyKeybord()
for i in range(10000):
    if(WindowsUtils.isJx003()):
       WindowsUtils.clickIconRetry('icon/chou.png', 100)
    else:
        time.sleep(1)