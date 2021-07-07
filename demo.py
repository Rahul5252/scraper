# Import neccesary libraries

from selenium import webdriver  # driver to control chrome browser
import pyautogui
from bs4 import BeautifulSoup  # to parse the html code
import threading  # to do multi threding
import time
import pandas as pd  # to store data in csv file
import urllib3
import re
# enter the filename

print("Enter the filename")  # filename to store data
filename = str(input())

# intiate the chrome webdriver instance
browser = webdriver.Chrome("C:\\python\\chromedriver_win32\\chromedriver.exe")
record = []
e = []


def Selenium_extractor():
    time.sleep(2)
    a = browser.find_elements_by_class_name("VkpGBb")
    time.sleep(1)
    for i in range(len(a)):
        a[i].click()
        time.sleep(2)
        source = browser.page_source
        # Beautiful soup for scraping the html source
        soup = BeautifulSoup(source, 'html.parser')
        try:
            Name_Html = soup.findAll('div', {"class": "SPZz6b"})

            name = Name_Html[0].text
            if name not in e:
                e.append(name)
                print(name)
                logo_Html = soup.findAll('img', {"class": "DU330c"})
                logo = logo_Html[0].get('src')
                print(logo)
                Phone_Html = soup.findAll('span', {"class": "LrzXr zdqRlf kno-fv"})
                phone = Phone_Html[0].text
                print(phone)

                Address_Html = soup.findAll('span', {"class": "LrzXr"})

                address = Address_Html[0].text

                timimg1 = soup.findAll('td', {"class": "SKNSIb"})
                d1 = timimg1[0].text
                d2 = timimg1[1].text
                d3 = timimg1[2].text
                d4 = timimg1[3].text
                d5 = timimg1[4].text
                d6 = timimg1[5].text
                d7 = timimg1[6].text

                timimg2 = soup.findAll('table', {"class": "WgFkxc"})
                t1 = timimg2[0].findAll('td')
                time1 = t1[1].text
                print(time1)
                t2 = timimg2[0].findAll('td')
                time2 = t2[3].text
                print(time2)
                t3 = timimg2[0].findAll('td')
                time3 = t3[5].text
                print(time3)
                t4 = timimg2[0].findAll('td')
                time4 = t4[7].text
                print(time4)
                t5 = timimg2[0].findAll('td')
                time5 = t5[9].text
                print(time5)
                t6 = timimg2[0].findAll('td')
                time6 = t6[11].text
                print(time6)
                t7 = timimg2[0].findAll('td')
                time7 = t7[13].text
                print(time7)




            # review name
                r1n = soup.findAll('div', {"class": "TSUbDb"})
                r1 = r1n[0].findAll('a')
                Rname = r1[0].text
            # print(r1n)
            # years ago reviews
                rya = soup.findAll('span', {"class": "dehysf lTi8oc"})
                Rtime = rya[0].text
            # print(rya)
            # review comment
                rcom = soup.findAll('div', {"class": "Jtu6Td"})
                rc = rcom[0].findAll('span')
                Rcomment = rc[0].text
            # print(rcom)

                try:
                    Website_Html = soup.findAll('div', {"class": "QqG1Sd"})
                    web = Website_Html[0].findAll('a')

                    website = web[0].get('href')
                except:
                    website = "Not available"
                # print(website)
                record.append((name, phone, address, website, logo, d1, d2, d3, d4, d5, d6, d7, time1, time2, time3, time4, time5, time6, time7, Rname, Rtime, Rcomment))
                df = pd.DataFrame(record,
                                  columns=['Name', 'Phone number', 'Address', 'Website', 'logo', 'd1','d2', 'd3','d4', 'd5', 'd6', 'd7','time1', 'time2', 'time3', 'time4', 'time5', 'time6', 'time7', 'Rname', 'Rtime', 'Rcomment'])  # writing data to the file
                df.to_csv(filename + '.csv', index=False, encoding='utf-8')

        except:
            print("error")
            continue

    try:
        time.sleep(1)
        next_button = browser.find_element_by_id("pnnext")  # clicking the next button
        next_button.click()
        browser.implicitly_wait(2)
        time.sleep(2)
        Selenium_extractor()
    except:
        print("ERROR occured at clicking net button")


print("Enter the link of the page")
link = input()
browser.get(str(link))
time.sleep(5)  # pausing the program for 10 secs
Selenium_extractor()