from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import wget
from subprocess import Popen, PIPE

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    return soup

def find_mp4(link):
    infos = urllib2.urlopen(link).geturl()
    infos = infos.split("&")
    for info in infos:
        if info.endswith(".mp4"):
            info = info.replace("file=","")
            return info
            break
    return 0

def upload_youtube(link,title,desc,keyword):
    os.chdir('/home/hadn/')
    wget.download(link)
    file_mp4 = link.split("/")[-1]
    cmd = '/home/hadn/python/bin/python /home/hadn/upload_youtube.py --file "%s" --title "%s" --description "%s" --keywords "%s" --category=25' % (file_mp4, title, desc, keyword)
    cmd = shlex.split(cmd.encode('utf8'))
    print cmd
    try:
        up = Popen(cmd, stdout=PIPE)
        print up.communicate()
    #: remove file which uploaded to youtube
        os.remove(file_mp4)
    except Exception as e:
        print str(e)
        pass


soup = mysoup("http://vtv.vn/truyen-hinh-truc-tuyen.htm")
videos_new = soup.find("div",{"class":"video-news-box"}).find("ul",{"class":"list-item"}).find_all("li")

links = []

for video in videos_new:
    link = "http://vtv.vn"+video.find("a").get("href")
    links.append(link)

if not links:
    sys.exit(0)

with open('/home/hadn/vtv.txt') as f:
    link_traced = f.readlines()[0].split(',')

index = 0
for link in links:
    if link in link_traced:
        break
    index += 1

if index > 0:
    with open('/home/hadn/vtv.txt', 'w') as f:
        f.write(','.join(links[:index]))

for link in links[:index]:
    soup = mysoup(link)
    getinfos = soup.find("div",{"class":"inner"})
    title = getinfos.find("h1",{"class":"news-title"}).string.replace("''","'").replace('"','\'')
    try:
        desc = getinfos.find("h2",{"class":"news-sapo"}).string.replace("''","'").replace('"','\'').replace("VTV.vn -","")
    except:
        desc = title
    try:
        link_key = soup.find("div",{"class":"clearfix inner"}).find("param",{"name":"movie"}).get("value")
    except:
        link_key = 0
    if link_key:
        link_mp4 = find_mp4(link_key)
	print link_mp4
        keyw = ""

        try:
            tags = soup.find("div",{"class":"tag"}).find_all("li")
        except:
            tags = ['tintuc, vtv']

        for tag in tags:
            if len(tag.string) < 30:
                keyw += ","+ tag.string
        print title.encode('utf-8'), link_mp4
        print keyw.encode('utf-8'), desc.encode('utf-8')
        upload_youtube(link_mp4,title,desc,keyw)
