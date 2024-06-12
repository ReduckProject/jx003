import time

import WindowsUtils
import WyhkmClients
from WyKeybord import WyKeybord

while not WindowsUtils.isJx003():
    time.sleep(1)

WyhkmClients.press('N')

WindowsUtils.clickIconRetry('icon/lankeshan/go_lankeshan.png', 100)
WindowsUtils.clickIconRetry('icon/lankeshan/lankeshan_eren.png', 100)
WindowsUtils.clickIconRetry('icon/lankeshan/lankeshan_jinruditu.png', 100)
WindowsUtils.clickIconRetry('icon/lankeshan/lankeshan_shenxing.png', 100)
