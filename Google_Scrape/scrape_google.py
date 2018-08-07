from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import time
from urllib.request import urlopen, Request
import socket
import matplotlib.pyplot as plt
from PIL import Image


header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

# ### 1- Art
# search_list =  ['painting','paintings','art','arts','arts surreal','drawing','drawings','sculpting','sculpture','artists']
# ### 2- Film & tv
# search_list =  ['movie theater','cinema','theater movie','tv rooms','tv room']
# ### 3- Finance & retail
# search_list =  ['finance','finances','money','dollar','savings','moneys']
# ### 4- Food
# search_list =  ['dishes','preparing food','gourmet','dinner','drinks', 'drinks']
# ### 5- Music
# search_list =  ['instrument','music','concert','instruments','music festival','music festivals','rock band','show','shows']
# ### 6- Politics
# search_list =  ['trump', 'theresa may','donnald trump','political people','obama','barack obama','presidents']
# ### 7- Religion
# search_list =  ['religion','god','church','churches','religion christian','christianity']
# ### 8- Science
# search_list =  ['experiments','chemistry','space','physics','industrial equipment','spaceship','science fiction','robot']
# ### 9- Sport
# search_list =  ['soccer','gym','sport','basketball','golf','tennis','bowling','sports','american football']
# ### 10- Travel
# search_list =  ['vacation','vacations','trip','holidays','travel','travels','sightseeing', 'famous places', 'places', 'place', 'tour', 'tourism', 'adventure','attractions','nature','amusement','famous place']

### London Touristic places
search_list =  [
                # "Palace of Westminster",
                # "The Royal Albert Hall",
                # "Kensington Gardens",
                # "Millennium Bridge, London",
                # "Hampton Court Palace",
                # "Borough Market",
                # "London King's Cross railway station",
                # "St James's Park",
                # "Tate Modern, London",
                # "Natural History Museum, London",
                # "Regent's Park",
                # "Camden Town",
                # "Victoria and Albert Museum",
                # "Soho",
                # "The Shard",
                # "Westminster Abbey",
                # "National Gallery, London",
                # "Covent Garden",
                # "St Paul's Cathedral",
                # "trafalgar square",
                # "hyde park",
                # "tower bridge",
                # "british museum",
                # "big ben",
                # "London Eye",
                # "Tower of London",
                # "buckingham palace",
                # "Canary Wharf",
                # "Shoreditch",
                # "Monument to the Great Fire of London",
                # "BFI",
                # "Piccadilly Circus",
                # "Leicester Square",
                # "Oxford Street",
                # "Leicester Square"
                ]

for searchterm in search_list:
    # searchterm = search_list[5] ### will also be the name of the folder

    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    # NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
    browser = webdriver.Chrome(r'C:/Users/Aimore/Downloads/chromedriver_win32/chromedriver.exe')
    browser.get(url)

    root = r'D:\ImageRecognition\DataSets\DataSet_Scraped\Google_Images/'
    root_path = root + searchterm
    if not os.path.exists(root_path):
        os.mkdir(root_path)

    counter = 0
    succounter = 0
    for _ in range(5):
        browser.execute_script("window.scrollBy(0,5000)")
        time.sleep(0.3)  # bot id protection


    for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
        counter += 1
        print("Total Count:", counter)
        print("Succsessful Count:", succounter)
        ### Scroll down page:
        # scroll_index = "window.scrollTo(0," + str(counter * 300) + ")"
        # time.sleep(0.3)  # bot id protection
        # browser.execute_script(scroll_index)

        try:
            # timeout = 2
            # socket.setdefaulttimeout(timeout)

            url = json.loads(x.get_attribute('innerHTML'))["ou"]
            print("URL:", url)

            req = Request(url, headers=header)
            resp = urlopen(req)
            raw_img = resp.read()
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]

            save_path = os.path.join(root_path, searchterm + "_" + str(counter) + "." + imgtype)
            # print(url[-4:])
            if url[-4:] == '.jpg' and save_path[-4:] == '.jpg':
                File = open(save_path, "wb")
                print('File : ', File)
                File.write(raw_img)
                succounter += 1
                File.close()

        except:
            print("Couldn't get img!")

    print('\n')
    print(succounter, "pictures successfully downloaded")
    browser.close()