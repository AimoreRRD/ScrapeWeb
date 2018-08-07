import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import time

# from urllib.request import Request, urlopen

# req = Request('https://www.pexels.com/search/religion/', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()
# print(webpage)

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soup = BeautifulSoup(thepage, "html.parser")
    return soup

total_start_time = time.time()

save_path_base = r'D:\ImageRecognition\DataSets\DataSet_Scraped\Pixabay_Images/'
# type_of_images_list = ["music","sport","film","religion","finance","politics","science","art","food"]
type_of_images_list = ["film & tv", "religion", "finance & retail", "politics", "science", "art", "food", "travel", "music", "sport"]
total_num_pages = 2


for type_of_image in type_of_images_list:
    ### Create Folder if does not exits
    save_path = save_path_base + type_of_image

    website = "https://pixabay.com/en/photos/?q=cat_type&image_type=photo&cat=&min_height=3&min_width=&order=popular&pagi="
    website_core = ('/').join(website.split("/")[0:3])
    print(website_core)

    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print('Created folder: \n', save_path)
    save_path = save_path + "/"

    print('type_of_image: ', type_of_image)
    website = website.replace("cat_type", type_of_image)
    i = 0

    for num_pages in range(1,total_num_pages):
        start_time = time.time()
        print('----------------------------------------------------------------------------------')
        print('\nnum_pages: ',num_pages)
        if num_pages % 2 == 0:
            print("PAGE EVEN", num_pages)
            website = website.replace("?min_height=3&image_type=photo&cat=&q="+type_of_image, "?q="+type_of_image+"&image_type=photo&cat=&min_height=3")  # Se for par

        website_page = website + str(num_pages)
        print('website_page',website_page)
        soup = make_soup(website_page)

        for img in soup.find_all('img'):
            i += 1
            try:
                temp = img.get('data-lazy')
                # print(temp)
                if temp[:1] == "/":
                    image = website_core + temp
                else:
                    image = temp
            except:
                temp = img.get('src')
                # print(temp)
                if temp[:1] == "/":
                    image = website_core + temp
                else:
                    image = temp

            nametemp = img.get('alt')
            filename = str(i) + '-' + nametemp
            print(filename)
            imagefile = open(save_path + filename + ".jpeg", 'wb')
            imagefile.write(urllib.request.urlopen(image).read())
            imagefile.close()

        final_time = time.time() - start_time
        print(final_time)

total_final_time = time.time() - total_start_time
print(total_final_time)