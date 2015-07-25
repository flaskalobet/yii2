from bs4 import BeautifulSoup
import urllib2
import shlex
import os
import wget
from subprocess import Popen, PIPE
from sys import argv
import re

def mysoup(link):
    url = urllib2.Request(link, headers={ 'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0' })
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    return soup

def getMP4Link(temp_link):
    '''
        <div id="video-embeb">
        <div allowfullscreen="" frameborder="0" height="355" mozallowfullscreen="" msallowfullscreen="" oallowfullscreen="" scrolling="no" src="http://vcplayer.vcmedia.vn/1.1/?_site=vtv&amp;vid=vtv/ijz-bet8rewrytvvmh5s1vc2x6zbjm/2015/07/25/be-1437826646289-41b33.mp4&amp;_videoId=85846" webkitallowfullscreen="" width="650"></div>
        </div>
    '''
    temp_link = temp.div.get('src')
    pattern = re.compile('=vtv/(.*)mp4')
    link_key = 'https://hls.vcmedia.vn/%s' % re.search(pattern, temp_link).group().replace('=vtv', 'vtv')
    return link_key

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


soup = mysoup(argv[1])
getinfos = soup.find("div",{"class":"inner"})
title = getinfos.find("h1",{"class":"news-title"}).string.replace("''","'").replace('"','\'')
try:
    desc = getinfos.find("h2",{"class":"news-sapo"}).string.replace("''","'").replace('"','\'').replace("VTV.vn -","")
except:
    desc = title
try:
    temp = soup.find("div",{"id":"video-embeb"})
    link_mp4 = getMP4Link(temp)
    print link_mp4
except Exception as e:
    print str(e)
    link_mp4 = 0
if link_mp4:
    keyw = ""

    try:
        tags = soup.find("div",{"class":"tag"}).find_all("li")
    except:
        tags = ['tintuc, vtv']

    for tag in tags:
        if len(tag.string) < 30:
            keyw += ","+ tag.string
    #print title.encode('utf-8'), link_mp4
    #print keyw.encode('utf-8'), desc.encode('utf-8')
    upload_youtube(link_mp4,title,desc,keyw)
