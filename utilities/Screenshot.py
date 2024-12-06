import os
from datetime import datetime


class ScreenShot:
    @staticmethod
    def capturescreen(self, driver, pagename, path):
        timestamp = datetime.now().strftime("%H%M%S")
        screenshotname = timestamp + "_" + pagename
        out = open(os.path.join(path, screenshotname + ".png"), "wb")
        out.write(driver.get_screenshot_as_png(self))
        out.close()
        getpath = path.split("\\Screenshots")
        return "..\\Screenshots" + getpath[1] + "\\" + screenshotname + ".jpg"