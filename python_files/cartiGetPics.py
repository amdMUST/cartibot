import requests #lets u send requests to sites
from bs4 import BeautifulSoup as bs #used for taking data out of html files
import os #lets u create the folder

url = 'https://www.google.com/search?q=playboi+carti&rlz=1C1CHBF_enUS766US766&sxsrf=ACYBGNRQWEQQzdsr_Wkz4f5Wyx32_pLyNg:1568767528948&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj_8bC6ktnkAhUHEqwKHQ--ABMQ_AUIEygC&biw=958&bih=927'

# new picture in imgs folder
# os.chdir('cartiPics')
# for model_image in os.listdir('.'):
#    api.update_with_media(model_image)
#    time.sleep(3)

# this where we download the page to parse through it
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# find all the elements that have the img tag
image_tags = soup.findAll('img')

# this creates directory for the carti images
if not os.path.exists('cartiPics'):
    os.makedirs('cartiPics')

# this moves to the new directory
os.chdir('cartiPics')

# initialize image file count
count = 0

# write the images
# for image in image_tags:
 #   try:
  #      url = image['src']
   #     source = requests.get(url)
    #    if source.status_code == 200:
    #        with open('cartiPics-'+ str(count)+'.jpg','wb') as f:
     #           f.write(requests.get(url).content)
    #            f.close()
    #            count +=1
 #   except:
 #       pass