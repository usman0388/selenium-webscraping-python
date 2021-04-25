from selenium import webdriver
from urllib.error import HTTPError
from urllib.error import URLError
import urllib.request as urllib
import os
from selenium.webdriver.chrome.options import Options

MetaList = []

def getMeta(path_link,save_path):        
    try:
        option = Options()
        option.headless = True
        driver = webdriver.Chrome(options=option,executable_path='driver/chromedriver.exe')
        driver.get(path_link)
        title = driver.find_element_by_xpath("/html/body/div[3]/h1")
        sypnosis ="" 
        for i in range(1,6):
            sypnosis = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div["+str(i)+"]/p")
            if len(sypnosis.text) > 0:
                break

        print(title.text)
        print(sypnosis.text)
        MetaList.append([title.text,sypnosis.text])
        posters = driver.find_elements_by_css_selector('.row:nth-child(15) .img-responsive')
        if len(posters) == 0:
            posters = driver.find_elements_by_css_selector('.row:nth-child(16) .img-responsive')
        if len(posters) == 0:
            posters = driver.find_elements_by_css_selector('.row:nth-child(17) .img-responsive')

        if not os.path.exists(os.path.dirname(save_path)):
            try:
                os.makedirs(os.path.dirname(save_path))
            except Exception as e:
                print(e)
        count = 0
        for i in posters:
            try:
                src = i.get_attribute('src')
                urllib.urlretrieve(src,save_path+str(count)+".png")
                count=count+1
            except:
                count = count +1
        driver.close()
    except HTTPError as e:
        print(e)
    except URLError as e:
        print(e)
    except Exception as e:
        print(e)
        print(main_link)    



def generate_link(name,path):
    name = name.lower()
    name = name.replace(" ","-")
    new_path = path+name
    return new_path

show_path = "D:/Anime"
show_list = os.listdir(show_path)
save_path = "media/Anime/"
main_link ="https://www.thetvdb.com/series/"
for i in show_list:
    getMeta(generate_link(i,main_link),save_path+i+"/")

for i in MetaList:
    print(i)
    print("\n")