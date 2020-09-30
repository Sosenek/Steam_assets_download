import requests
import os
import time
import os.path
import json,urllib.request
from PIL import ImageFile
from PIL import Image

STEAM_KEY = "" #STEAM API Key https://steamcommunity.com/dev/apikey
STEAM_ID = "" # steamID64 https://steamidfinder.com/

data = urllib.request.urlopen(str("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="+STEAM_KEY+"&steamid="+STEAM_ID+"&include_appinfo=true&format=json"), timeout=1).read()
output = json.loads(data)
game_count = output['response']['game_count']

# xxx = [Done, Downloaded, Missing]
Capsule = [0,0,0]
Header = [0,0,0]
Logo = [0,0,0]
Background = [0,0,0]
Cover = [0,0,0]
Icon = [0,0,0]

try: os.makedirs("./steam_img/backgrounds/") 
except: ()
try:  os.makedirs("./steam_img/covers/")
except: ()
try: os.makedirs("./steam_img/headers/")
except: ()
try: os.makedirs("./steam_img/icons/")
except: ()
try: os.makedirs("./steam_img/logos/")
except: ()
    
print("\033[1;33;40m       | Game ID |                                                    Game Name |       Done | Downloaded |    Missing |")

for x in range(game_count):
    done = 0
    downloaded = 0
    missing = 0
    
    Game_id = output['response']['games'][x]['appid']
    Game_name = output['response']['games'][x]['name']
    Icon_hash = output['response']['games'][x]['img_icon_url']

    if os.path.isfile(str("./steam_img/"+str(Game_id)+".jpg")):
        done += 1
        Capsule[0] += 1
    else:
        url = str("https://steamcdn-a.akamaihd.net/steam/apps/"+str(Game_id)+"/capsule_231x87.jpg")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            missing += 1
            Capsule[2] += 1
        else:
            with open(str("./steam_img/"+str(Game_id)+".jpg"), "wb") as f:
                f.write(r.content)
            downloaded += 1
            Capsule[1] += 1

    if os.path.isfile(str("./steam_img/headers/"+str(Game_id)+".jpg")):
        done += 1
        Header[0] += 1
    else:
        url = str("https://steamcdn-a.akamaihd.net/steam/apps/"+str(Game_id)+"/header.jpg")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            missing += 1
            Header[2] += 1
        else:    
            with open(str("./steam_img/headers/"+str(Game_id)+".jpg"), "wb") as f:
                f.write(r.content)
            downloaded += 1
            Header[1] += 1

    if os.path.isfile(str("./steam_img/logos/"+str(Game_id)+".png")):
        done += 1
        Logo[0] += 1
    else:
        url = str("https://steamcdn-a.akamaihd.net/steam/apps/"+str(Game_id)+"/logo.png")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            missing += 1
            Logo[2] += 1
        else:
            with open(str("./steam_img/logos/"+str(Game_id)+".png"), "wb") as f:
                f.write(r.content)
            downloaded += 1
            Logo[1] += 1
    
    if os.path.isfile(str("./steam_img/backgrounds/"+str(Game_id)+".jpg")):
        done += 1  
        Background[0] += 1
    else:
        url = str("https://steamcdn-a.akamaihd.net/steam/apps/"+str(Game_id)+"/library_hero.jpg")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            missing += 1
            Background[2] += 1
        else:    
            with open(str("./steam_img/backgrounds/"+str(Game_id)+".jpg"), "wb") as f:
                f.write(r.content)
            downloaded += 1
            Background[1] += 1
  
    if os.path.isfile(str("./steam_img/covers/"+str(Game_id)+".jpg")):  
        done += 1
        Cover[0] += 1
    else:
        url = str("https://steamcdn-a.akamaihd.net/steam/apps/"+str(Game_id)+"/library_600x900.jpg")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            missing += 1
            Cover[2] += 1
        else:    
            with open(str("./steam_img/covers/"+str(Game_id)+".jpg"), "wb") as f:
                f.write(r.content)
            downloaded += 1
            Cover[1] += 1
            
    if os.path.isfile(str("./steam_img/icons/"+str(Game_id)+".jpg")):
        done += 1
        Icon[0] += 1
    else:
        url = str("https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/apps/"+str(Game_id)+"/"+str(Icon_hash)+".jpg")
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            missing += 1
            Header[2] += 1
        else:    
            with open(str("./steam_img/icons/"+str(Game_id)+".jpg"), "wb") as f:
                f.write(r.content)
            downloaded += 1
            Icon[1] += 1
    if missing > 0:
        print(f"\033[1;31;40m{x:6} | {Game_id:7} | {Game_name:>60} | {done:10} | {downloaded:10} | {missing:10} |")
    if missing == 0 and downloaded > 0 :
        print(f"\033[1;34;40m{x:6} | {Game_id:7} | {Game_name:>60} | {done:10} | {downloaded:10} | {missing:10} |")
    if missing == 0 and downloaded == 0:
        print(f"\033[1;32;40m{x:6} | {Game_id:7} | {Game_name:>60} | {done:10} | {downloaded:10} | {missing:10} |")
    
print("\033[1;37;40m")
print("             Already: | Downloaded | Missing |")
print("----------------------+------------+---------|")
print(f"\033[1;37;40mBackgrounds: \033[1;32;40m{Background[0]:8} | \033[1;34;40m{Background[1]:10} | \033[1;31;40m{Background[2]:7} |")
print(f"\033[1;37;40mCapsule:     \033[1;32;40m{Capsule[0]:8} | \033[1;34;40m{Capsule[1]:10} | \033[1;31;40m{Capsule[2]:7} |")
print(f"\033[1;37;40mCover:       \033[1;32;40m{Cover[0]:8} | \033[1;34;40m{Cover[1]:10} | \033[1;31;40m{Cover[2]:7} |")
print(f"\033[1;37;40mHeader:      \033[1;32;40m{Header[0]:8} | \033[1;34;40m{Header[1]:10} | \033[1;31;40m{Header[2]:7} |")
print(f"\033[1;37;40mIcons:       \033[1;32;40m{Icon[0]:8} | \033[1;34;40m{Icon[1]:10} | \033[1;31;40m{Icon[2]:7} |")
print(f"\033[1;37;40mLogo:        \033[1;32;40m{Logo[0]:8} | \033[1;34;40m{Logo[1]:10} | \033[1;31;40m{Logo[2]:7} |")
print("\033[1;37;40m----------------------+------------+---------|")
print(f"\033[1;37;40mTotal:       \033[1;32;40m{Background[0] + Capsule[0] + Cover[0] + Header[0] + Icon[0] + Logo[0]:8} | \033[1;34;40m{Background[1] + Capsule[1] + Cover[1] + Header[1] + Icon[1] + Logo[1]:10} | \033[1;31;40m{Background[2] + Capsule[2] + Cover[2] + Header[2] + Icon[2] + Logo[2]:7} |")
