# need NppExec
# click Follow $(FULL_CURRENT_PATH)
# C:\Users\willy\Anaconda3\python.exe "$(FULL_CURRENT_PATH)"
import threading, os, time, sys
from pytube import YouTube
from selenium import webdriver

def getPackage(entity, num):
    xpath='//*[@id="entities"]/div[contains(text(),"{}")]'.format(entity)
    driver=webdriver.Chrome('C:/LinuxShare/dataset/chromedriver.exe')
    web=driver.get('https://research.google.com/youtube8m/explore.html')
    driver.minimize_window()
    driver.maximize_window()
    count=0
    sys.stdout.write("Select target package...\n")
    sys.stdout.flush()
    driver.find_element_by_xpath(xpath).click()
    time.sleep(5)
    for i in range(0,1+int(num/10)):
        sys.stdout.write('scrolling..'+str(i)+'\n')
        sys.stdout.flush()
        driver.execute_script('outerthumbs.style.overflowY="scroll"')
        driver.execute_script('outerthumbs.scrollTo(0,outerthumbs.scrollHeight)')
        time.sleep(3)
    thumbs_all_a = driver.find_elements_by_css_selector('#thumbs a')
    lst=[i.get_attribute('href') for i in thumbs_all_a]
    driver.close()
    return lst

lst=getPackage("Violin", 800)


class BathDownloadThread(threading.Thread):
    def __init__(self, urlList, outputpath):
        super(BathDownloadThread, self).__init__()
        self.urlList=urlList
        self.outputpath=outputpath
    
    def run(self):
        if not os.path.exists(self.outputpath):
            os.mkdir(self.outputpath)
        for i in range(len(self.urlList)):
            sys.stdout.write('Downloading url '+str(i+1)+" : "+self.urlList[i]+'\n')
            sys.stdout.flush()
            yt=YouTube(url=self.urlList[i])
            yt.streams.first().download(output_path=self.outputpath)
            time.sleep(10)

BathDownloadThread(lst[500:600],'Dragon_Ball').start()
BathDownloadThread(lst[600:700],'Dragon_Ball').start()
BathDownloadThread(lst[700:800],'Dragon_Ball').start()
