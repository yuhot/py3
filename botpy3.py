# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse
from gtts import gTTS
import html5lib,shutil
import wikipedia,goslate
import youtube_dl, pafy, asyncio
from multiprocessing import Pool, Process
from googletrans import Translator

#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE("Evc6GIv0PCpHhdVLKk2d.rKoPKTxMCMFwdYmmCA/nVq.l7K4aJ+2Ed8jlAqHw1r3VR/pnUsm2ev4nyBQW6Mqawc=")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

# ki = LINE()
# ki.log("Auth Token : " + str(ki.authToken))
# ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

# kk = LINE()
# kk.log("Auth Token : " + str(kk.authToken))
# kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

# kc = LINE()
# kc.log("Auth Token : " + str(kc.authToken))
# kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

# ke = LINE()
# ke.log("Auth Token : " + str(ke.authToken))
# ke.log("Timeline Token : " + str(ke.tl.channelAccessToken))


print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

# kiMID = ki.profile.mid
# kiProfile = ki.getProfile()
# kiSettings = ki.getSettings()

# kkMID = kk.profile.mid
# kkProfile = kk.getProfile()
# kkSettings = kk.getSettings()

# kcMID = kc.profile.mid
# kcProfile = kc.getProfile()
# kcSettings = kc.getSettings()

# keMID = kc.profile.mid
# keProfile = kc.getProfile()
# keSettings = kc.getSettings()


# oepoll = OEPoll(ke)
# oepoll = OEPoll(kc)
# oepoll = OEPoll(kk)
# oepoll = OEPoll(ki)
oepoll = OEPoll(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
lineMID = line.getProfile().mid
# kiMID = ki.getProfile().mid
# kkMID = kk.getProfile().mid
# kcMID = kc.getProfile().mid
# kcMID = ke.getProfile().mid
# bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["u4643a992d5e67267d60f230c71af8dbd",lineMID]
admin=['u4643a992d5e67267d60f230c71af8dbd',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
settings = {
    "autoAdd": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":5},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": False,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": True,
    "lang":"JP",
    "Sd": True,
    "Nn": True,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "welcome":"馃惗喔⑧复喔權笖喔掂笗喙夃腑喔權福喔编笟喔浮喔侧笝喙夃腑喔煇�",
    "bye":"喔箟喔侧抚喔о抚!! 喔｀傅喔氞箘喔涏箘喔笝喔∴覆喙冟斧喙夃箑喔勦箟喔侧斧喔ム腑喔佮竵喙堗腑喔權笝馃懟",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"喙佮腑喔斷浮喔侧箘喔∴腑喙夃赴喔班浮喔掂箘喔｀竸喔侧笟~",
    "comment":"喔傕腑喔氞竸喔膏笓喔椸傅喙堗箒喔笖喔∴覆喔勦箟喔�",
    "Respontag":"喙佮笚喔勦笚喔赤箘喔� 喔勦复喔斷笘喔多竾喙�喔勦箟喔侧腑喙堗赴喔斷复喙夝煒�",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": False,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":True,
    "copy2":True,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    }

setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))



def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "鈺斺晲鈺怺喔堗赋喔權抚喔權竸喔權笚喔掂箞喙佮笚喙囙竵 {} 喔勦笝]\n鈺� ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "鈺� "
            else:
                try:
                    textx += "鈺氣晲鈺怺喔娻阜喙堗腑喔佮弗喔膏箞喔�   {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#==============================================================================#
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log(" Rakey " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def myhelp():
    myHelp =      " 馃挜喔勦赋喔副喙堗竾  馃挩 喙�喔｀傅喔⑧竵喔斷腹喔勦赋喔副喙堗竾馃樁"+ "  \n" + \
                  " 鉂む竸喔赤釜喔编箞喔囙箒喔涏弗 馃挩 喙�喔｀傅喔⑧竵喔斷腹喔勦赋喔副喙堗竾喙佮笡喔ヰ煒�"+ "  \n" + \
                  " 馃挦喔｀傅喔氞腹喔� 馃挩 喔｀腹喔氞腹喔福喔班笟喔氿煒�"+ "  \n" + \
                  " 馃崄喙�喔娻箛喔勦腑喔笝喙�  馃挩 喙�喔娻箛喔勦箑喔о弗喔侧笚喔赤竾喔侧笝喔氞腑喔楌煂�"+ "  \n" + \
                  " 馃惗喙勦弗喔權箤  馃挩 喙�喔娻箛喔勦競喙夃腑喔∴腹喔ム箘喔ム笝喙岎煇�"+ "  \n" + \
                  " 馃惤喙�喔娻箛喔勦笗喔编箟喔囙竸喙堗覆  馃挩 喙�喔娻箛喔勦福喔班笟喔氞笗喔编箟喔囙竸喙堗覆鈽�"+ "  \n" + \
                  " 鉁ㄠ箘喔笖喔�  馃挩 喔斷腹mid馃帀"+ "  \n" + \
                  " 馃拃喔娻阜喙堗腑  馃挩 喔斷腹喔娻阜喙堗腑喙勦弗喔權箤馃懟"+ "  \n" + \
                  " 馃懞喔｀腹喔�  馃挩 喔斷付喔囙福喔灌笡馃懝"+ "  \n" + \
                  " 馃樇喔｀腹喔涏抚喔脆笖喔掂箓喔�  馃挩 喔斷付喔囙抚喔脆笖喔掂箓喔煒�"+ "  \n" + \
                  " 馃懢喔｀腹喔涏笡喔�  馃挩 喔斷付喔囙笡喔侌煉�"+ "  \n" + \
                  " 馃檲喔勦笚 @  馃挩 喔斷付喔囙竸喔笝喙佮笚喔勷煓�"+ "  \n" + \
                  " 馃惃喔娻阜喙堗腑 @  馃挩 喔斷付喔囙笂喔粪箞喔煇�"+ "  \n" + \
                  " 馃悋喔曕副喔� @  馃挩 喔斷付喔囙笗喔编釜馃惏"+ "  \n" + \
                  " 馃悂喔｀腹喔� @  馃挩 喔斷付喔囙福喔灌笡馃悁"+ "  \n" + \
                  " 馃惒喔｀腹喔涏抚喔脆笖喔掂箓喔� @  馃挩 喔斷付喔囙福喔灌笡喔о复喔斷傅喙傕腑馃悕"+ "  \n" + \
                  " 馃悤喔涏竵 @  馃挩 喔斷付喔囙笡喔侌煇�"+ "  \n" + \
                  " 馃悈喔勦阜喔權福喙堗覆喔�  馃挩 喔佮弗喔编笟喔｀箞喔侧竾喙�喔斷复喔○煇�"+ "  \n" + \
                  " 馃悗喙�喔ム傅喔⑧笝喙佮笟喔� @  馃挩 喙�喔炧复喙堗浮喔炧腹喔斷笗喔侧浮馃惔"+ "  \n" + \
                  " 馃悙喙�喔ム傅喔⑧笝喙佮笟喔氞弗喔� @  馃挩 喔ム笟喔炧腹喔斷笗喔侧浮馃悇"+ "  \n" + \
                  " 馃悧喙�喔娻箛喔勦箑喔ム傅喔⑧笝喙佮笟喔�  馃挩 喙�喔娻箛喔勦笂喔粪箞喔笧喔灌笖喔曕覆喔○煇�"+ "  \n" + \
                  " 馃崌喙�喔娻箛喔勦箒喔笖  馃挩 喙�喔娻箛喔勦箒喔笖喔箟喔竾馃崜"+ "  \n" + \
                  " 馃崓喙勦腑喔斷傅喔佮弗喔膏箞喔�  馃挩 GID 喔佮弗喔膏箞喔○煃�"+ "  \n" + \
                  " 馃崚喔｀腹喔涏竵喔ム父喙堗浮  馃挩 喔斷付喔囙福喔灌笡喔箟喔竾馃崊"+ "  \n" + \
                  " 馃崠喔娻阜喙堗腑喔佮弗喔膏箞喔�  馃挩 喔斷付喔囙笂喔粪箞喔斧喙夃腑喔囸煃�"+ "  \n" + \
                  " 馃崟喔傕腑喔ム复喙夃竾喔勦箤  馃挩 喙�喔覆喔ム复喙夃竾喔勦箤喔箟喔竾馃嵆"+ "  \n" + \
                  " 馃尳喙�喔涏复喔斷弗喔脆箟喔囙竸喙�  馃挩 喙�喔涏复喔斷弗喔脆箟喔囙竸喙屶斧喙夃腑喔囸煃�"+ "  \n" + \
                  " 馃拵喔涏复喔斷弗喔脆箟喔囙竸喙�  馃挩 喔涏复喔斷弗喔脆箟喔囙竸喙屶斧喙夃腑喔囸煈�"+ "  \n" + \
                  " 馃帗喔傕箟喔浮喔灌弗喔佮弗喔膏箞喔�  馃挩 喙�喔娻箛喔勦福喔侧涪喔ム赴喙�喔傅喔⑧笖喔箟喔竾馃帺"+ "  \n" + \
                  " 馃憻喔浮喔侧笂喔脆竵  馃挩 喔娻阜喙堗腑喔浮喔侧笂喔脆竵馃拲"+ "  \n" + \
                  " 馃憽喔佮弗喔膏箞喔�  馃挩 喙�喔娻箛喔勦福喔侧涪喔娻阜喙堗腑喔佮弗喔膏箞喔○煄�"+ "  \n" + \
                  " 馃憵1喔佮弗喔膏箞喔�  馃挩 喔勦弗喔脆箟喔�1 喙�喔娻箛喔勦福喔侧涪喔娻阜喙堗腑喔佮弗喔膏箞喔○煈�"+ "  \n" + \
                  " 馃憳2喔佮弗喔膏箞喔� 馃挩 喔勦弗喔脆箟喔�2 喙�喔娻箛喔勦福喔侧涪喔娻阜喙堗腑喔佮弗喔膏箞喔○煈�"+ "  \n" + \
                  " 馃憱3喔佮弗喔膏箞喔�  馃挩 喔勦弗喔脆箟喔�3 喙�喔娻箛喔勦福喔侧涪喔娻阜喙堗腑喔佮弗喔膏箞喔○煈�"+ "  \n" + \
                  " 馃憰喙佮笚喙囙竵  馃挩 喔副喙堗竾喙佮笚喙囙竸喔勦笝喔椸副喙夃竾喔浮喔旔煈�"+ "  \n" + \
                  " 馃挘喙�喔娻箛喔勦腑喙堗覆喔�  馃挩 喙�喔涏复喔斷福喔班笟喔氞腑喙堗覆喔欚煉�"+ "  \n" + \
                  " 馃拰喔箞喔侧笝  馃挩 喔斷腹喔｀覆喔⑧笂喔粪箞喔竸喔權腑喙堗覆喔欚煉�"+ "  \n" + \
                  " 馃挱喔勦箟喔權斧喔侧福喔灌笡 馃挩 喔勦箟喔權斧喔侧福喔灌笡喔堗覆喔乬oogle馃挮"+ "  \n" + \
                  " 馃挊喔勦箟喔權斧喔侧腑喔脆笝喔笗喔侧箒喔佮福喔�  馃挩 喔覆喔复喔權釜喔曕覆喙佮竵喔｀浮馃拫"+ "  \n" + \
                  " 馃懀喔｀腹喔涏竵喔侧福喔曕腹喔�  馃挩 喔勦箟喔權斧喔侧福喔灌笡喔堗覆喔乬oogle馃挄"+ "  \n" + \
                  " 馃憖喔勦箟喔權斧喔侧涪喔灌笚喔灌笡  馃挩 喔勦箟喔權斧喔侧涪喔灌笚喔灌笡馃憛"+ "  \n" + \
                  " 馃拝喔｀覆喔⑧竵喔侧福喙�喔炧阜喙堗腑喔�  馃挩 喙�喔娻箛喔勦福喔侧涪喔娻阜喙堗腑喙�喔炧阜喙堗腑喔權箑喔｀覆馃檶"+ "  \n" + \
                  " 馃毝喔｀覆喔⑧竵喔侧福喔氞弗喙囙腑喔�  馃挩 喔｀覆喔⑧竵喔侧福喔佮笖喔氞弗喙囙腑喔勷煆�"+ "  \n" + \
                  " 馃懁喔｀覆喔⑧竵喔侧福mid  馃挩 喔｀覆喔⑧竵喔侧福mid喙�喔炧阜喙堗腑喔權笚喔编箟喔囙斧喔∴笖馃懃"+ "  \n" + \
                  " 馃槂喙�喔娻复喔嵿竵喔�  馃挩 喙�喔娻复喔嵿竸喔權箑喔傕傅喔⑧笝喔氞腑喔楌煒�"+ "  \n" + \
                  " 馃槃喔腑喔�  馃挩 喔副喙堗竾喔曕副喔о箑喔竾喔腑喔佮笀喔侧竵喔箟喔竾馃槅"+ "  \n" + \
                  " 馃樁喔腑喔�1  馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮腑喔竵馃槝"+ "  \n" + \
                  " 馃槏喔ム笟喔｀副喔�  馃挩 喔ム笟喔箟喔竾喔｀副喔欚煒�"+ "  \n" + \
                  " 馃槴喙�喔娻复喔�  馃挩  喙�喔娻复喔嵿笖喙夃抚喔⑧竸喔楌煒�"+ "  \n" + \
                  " 馃槡喙�喔曕赴 @  馃挩 喔ム笟喔勦笝馃槞"+ "  \n" + \
                  " 馃槑喙�喔娻复喔� @ 馃挩 喙�喔娻复喔嵿竸喔欚煒�"+ "  \n" + \
                  " 馃構1喙�喔娻复喔� @  馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮箑喔娻复喔嶐煒�"+ "  \n" + \
                  " 馃槪2喙�喔娻复喔� @  馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮箑喔娻复喔嶐煒�"+ "  \n" + \
                  " 馃彲3喙�喔娻复喔� @  馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮箑喔娻复喔嶐煉�"+ "  \n" + \
                  " 馃彴喙�喔曕赴喔斷赋  馃挩 喙�喔曕赴喔｀覆喔⑧竵喔侧福喔氞笂喔斷赋馃椉"+ "  \n" + \
                  " 馃椌喔ム笟喙佮笂喔�  馃挩 喔副喙堗竾喔ム笟喙佮笂喔椸笚喔编箟喔囙斧喔∴笖馃寢"+ "  \n" + \
                  " 馃巹喔腑喔佮箒喔娻笚喔｀抚喔�  馃挩 喔腑喔佮笀喔侧竵喙佮笂喔椸福喔о浮喔腑喙傕笗喙夝煑�"+ "  \n" + \
                  " 馃巿喔副喔� 喔曕副喔�:   馃挩 喙�喔涏弗喔掂箞喔⑧笝喔曕副喔箑喔｀覆馃帒"+ "  \n" + \
                  " 鈿距腑喔编笧 喔娻阜喙堗腑:   馃挩 喙�喔涏弗喔掂箞喔⑧笝喔娻阜喙堗腑喙�喔｀覆馃弨"+ "  \n" + \
                  "馃幊喔娻阜喙堗腑喔勦弗喔脆箟喔�   馃挩 喙�喔涏弗喔掂箞喔⑧笝喔娻阜喙堗腑喔勦弗喔脆箟喔侌煄�"+ "  \n" + \
                  " 馃幘喔曕副喔竸喔ム复喙夃竵   馃挩 喙�喔涏弗喔掂箞喔⑧笝喔曕副喔煄�"+ "  \n" + \
                  " 鉀�1喔ム笟喔｀副喔�  馃挩 喔ム笟喔｀副喔欚煆�"+ "  \n" + \
                  " 馃張喙�喔娻箛喔勦笖喔�  馃挩 喙�喔娻箛喔勦福喔侧涪喔佮覆喔｀笖喔仇煆�"+ "  \n" + \
                  " 馃幎喔氞弗喙囙腑喔勦箑喔涏复喔�  馃挩 喔腑喙傕笗喙夃笟喔ム箟喔竸喙�喔涏复喔旔煄�"+ "  \n" + \
                  " 馃摨喔氞弗喙囙腑喔勦笡喔脆笖  馃挩 喔腑喙傕笗喙夃笟喔ム箛喔竸喔涏复喔旔煄�"+ "  \n" + \
                  " 馃攲喙�喔傕箟喔侧箑喔涏复喔� 馃挩 喙�喔傕箟喔侧斧喙夃腑喔囙腑喔箓喔曕箟喙�喔涏复喔旔煄�"+ "  \n" + \
                  " 馃摶喙�喔傕箟喔侧笡喔脆笖  馃挩 喙�喔傕箟喔侧斧喙夃腑喔囙腑喔箓喔曕箟喔涏复喔旔煋�"+ "  \n" + \
                  " 馃幏喙佮笂喔椸福喔о浮喙�喔涏复喔�  馃挩 喔佮副喔權笖喔多竾喙佮笂喔椸福喔о浮喙�喔涏复喔旔煄�"+ "  \n" + \
                  " 馃幖喙佮笂喔椸福喔о浮喔涏复喔� 馃挩 喔佮副喔權笖喔多竾喙佮笂喔椸福喔о浮喔涏复喔旔煄�"+ "  \n" + \
                  " 馃摚喔箞喔侧笝喙�喔涏复喔�  馃挩 喙�喔涏复喔斷福喔班笟喔氞腑喙堗覆喔欚煋�"+ "  \n" + \
                  " 馃摓喔箞喔侧笝喔涏复喔�  馃挩 喔涏复喔斷福喔班笟喔氞腑喙堗覆喔欚煍�"+ "  \n" + \
                  "馃攷喙�喔娻箛喔勦笗喔脆箟喔佮箑喔涏复喔�  馃挩 喔｀赴喔氞笟喙�喔娻箛喔勦笗喔脆箟喔佮箑喔涏复喔旔煍�"+ "  \n" + \
                  " 馃搧喙�喔娻箛喔勦笗喔脆箟喔佮笡喔脆笖  馃挩 喔｀赴喔氞笟喙�喔娻箛喔勦笗喔脆箟喔佮笡喔脆笖馃搨"+ "  \n" + \
                  " 馃敀喙�喔涏复喔斷斧喔∴笖  馃挩 喙�喔涏复喔斷福喔班笟喔氞竵喔编笝喔浮喔旔煍�"+ "  \n" + \
                  " 馃敡喔涏复喔斷斧喔∴笖 馃挩 喔涏复喔斷福喔班笟喔氞竵喔编笝喔浮喔旔煍�"+ "  \n" + \
                  " 馃搱喙�喔涏复喔斷竸喔權箑喔傕箟喔�  馃挩 喙�喔涏复喔斷福喔班笟喔氞笗喙夃腑喔權福喔编笟馃搲"+ "  \n" + \
                  " 馃搵喔涏复喔斷竸喔權箑喔傕箟喔�  馃挩 喔涏复喔斷福喔班笟喔氞笗喙夃腑喔權福喔编笟馃搶"+ "  \n" + \
                  " 鈫椸箑喔涏复喔斷竸喔權腑喔竵  馃挩 喙�喔涏复喔斷福喔班笟喔氞笗喙夃腑喔權福喔编笟鈫�"+ "  \n" + \
                  " 猬嗋笡喔脆笖喔勦笝喔腑喔� 馃挩 喔涏复喔斷福喔班笟喔氞笗喙夃腑喔權福喔编笟猬�"+ "  \n" + \
                  " 鉃∴笚喔编竵 喔腑喔�:   馃挩 喔曕副喙夃竾喔傕箟喔竸喔о覆喔∴笚喔编竵喔勦笝喙�喔傕箟喔测瑓"+ "  \n" + \
                  " 鈫斷笚喔编竵 喙�喔傕箟喔�:  馃挩 喔曕副喙夃竾喔傕箟喔竸喔о覆喔∴笚喔编竵喔勦笝喔腑喔佲啎"+ "  \n" + \
                  " 鈫笗喔编箟喔� 喙佮笚喙囙竵:  馃挩 喔曕副喙夃竾喔傕箟喔竸喔о覆喔∴笚喔编竵喔勦笝喙佮笚喙囙竵鈫�"+ "  \n" + \
                  " 鈾堗弗喔氞箑 喔娻复喔峴 馃挩 喔ム笟喔勦箟喔侧竾喙�喔娻复喔嶁檳"+ "  \n" + \
                  " 鈾娻箑喔娻箛喔�  馃挩 喔曕福喔о笀喔堗副喔氞竸喔權腑喙堗覆喔� 鈾�"+ "  \n" + \
                  " 馃敿喔箞喔侧笝  馃挩 喔｀覆喔⑧笂喔粪箞喔竸喔權腑喙堗覆喔欚煍�"+ "  \n" + \
                  " 馃敱urban   馃挩 喔傕覆喔� 馃摏"+ "  \n" + \
                  " 鉁匞cancel: on 馃挩 喙�喔涏复喔斷福喔班笟喔氞涪喔佮箑喔ム复喔佮斧喙夃腑喔団湐"+ "  \n" + \
                  " 馃攦Gcancel: off  馃挩 喔涏复喔斷福喔班笟喔氞涪喔佮箑喔ム复喔佮斧喙夃腑喔囸煍�"+ "  \n" + \
                  " 馃毄Copy @  馃挩 喔勦副喔斷弗喔竵喔勦笝喔阜喙堗笝馃帉"+ "  \n" + \
                  " 鈾漨e  馃挩 喔勦笚喙�喔｀覆鈾�"+ "  \n" + \
                  " 鈾汳E  馃挩 喔勦笚喙�喔｀覆鈾�"+ "  \n" + \
                  " 鈾歁e  馃挩 喔勦笚喙�喔｀覆鈾�"+ "  \n" + \
                  " 鈾瀦t  馃挩 喔斷腹喔勦笝喙勦釜喙堗弗喙堗腑喔囙斧喔欌櫂"+ "  \n" + \
                  " 鈾m  馃挩 喔斷腹喔勦笝喙勦釜喙堗弗喙堗腑喔囙斧喔欌櫑"+ "  \n" + \
                  " 鈾爖c  馃挩 喔斷腹喔勦笝喙勦釜喙堗弗喙堗腑喔囙斧喔欌櫎"+ "  \n" + \
                  " 鈽匒llban 馃挩 喙佮笟喔權斧喔∴笖鈽�"+ "  \n" + \
                  " 鈼哹an @  馃挩 喔氞笂喔斷赋鈼�"+ "  \n" + \
                  " 鈾焨nban @  馃挩 喔氞笂喔傕覆喔р櫃"+ "  \n" + \
                  " 鈻搗ideo @  馃挩 喔斷付喔囙福喔灌笡喔о复喔斷傅喙傕腑鈻�"+ "  \n" + \
                  "鈺� mimic on  馃挩 喙�喔涏复喔斷福喔班笟喔氞笧喔灌笖喔曕覆喔� 鈺�"+ "  \n" + \
                  " 鈻穖imic off  馃挩 喔涏复喔斷福喔班笟喔氞笧喔灌笖喔曕覆喔♀梺"+ "  \n" + \
                  " 鈼圔cvoice  +喔傕箟喔竸喔о覆喔�  馃挩 喔斷付喔噈id鈻�"+ "  \n" + \
                  " 鈻燙bcvoice   馃挩 喔箞喔噈p3喔椸父喔佮斧喙夃腑喔団枴"+ "  \n" + \
                  " 鈻―ow  +喔傕箟喔竸喔о覆喔� 馃挩 喙�喔涏弗喔掂箞喔⑧笝喙勦腑喔斷傅喙勦弗喔權箤鈻�"+ "  \n" + \
                  " 鈻ay  馃挩 喙�喔娻箛喔勦抚喔编笝喙佮弗喔班箑喔斷阜喔笝鈻�"+ "  \n" + \
                  " 鈻pam  on +喙�喔ム競+喔傕箟喔竸喔о覆喔♀枼  鉃� "+ "  \n" + \
                  " 鈩b  馃挩 喔ム箟喔侧竾喔氞笂喔斷赋鈩�"+ "  \n" + \
                  " 鍙圧akey 馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮箑喔傕箟喔茬珛"+ "  \n" + \
                  " 馃帲1-3 @  馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮箑喔曕赴馃幙"+ "  \n" + \
                  " 馃�凜leanse  馃挩 喔副喙堗竾喔勦弗喔脆箟喔佮笟喔脆笝馃幋"+ "  \n" + \
                  " 馃儚喙�喔涏复喔� 喔佮副喔�  馃挩 喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝馃幉"+ "  \n" + \
                  " 馃帇喔涏复喔� 喔佮副喔� 馃挩 喔涏复喔斷笡喙夃腑喔囙竵喔编笝馃帊"+ "  \n" + \
                  " 馃帍喔佮副喔� 喔⑧竵 馃挩 喙�喔涏复喔斷涪喔佮箑喔ム复喔佮笡喙夃腑喔囙竵喔编笝馃帎"+ "  \n" + \
                  " 馃彔喔涏复喔斷竵喔编笝 喔⑧竵 馃挩 喔涏复喔斷涪喔佮箑喔ム复喔佮笡喙夃腑喔囙竵喔编笝馃彙"+ "  \n" + \
                  " 馃審喔佮副喔� 喙�喔娻复喔� 馃挩 喙�喔涏复喔斷箑喔娻复喔嵿笡喙夃腑喔囙竵喔编笝馃寪"+ "  \n" + \
                  " 馃彞喔涏复喔斷竵喔编笝 喙�喔娻复喔�  馃挩 喔涏复喔斷箑喔娻复喔嵿笡喙夃腑喔囙竵喔编笝馃彟"+ "  \n" + \
                  " 馃彣喔佮副喔� 喔ム复喙夃竾 馃挩 喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔勦箤馃彥"+ "  \n" + \
                  " 馃寙喔涏复喔斷竵喔编笝 喔ム复喙夃竾 馃挩 喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔勦箤馃寚"+ "  \n" + \
                  " 馃殑喔佮副喔� 喔浮喔侧笂喔脆竵 馃挩 喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵馃殔"+ "  \n" + \
                  " 鈴赤笡喔脆笖喔佮副喔� 喔浮喔侧笂喔脆竵 馃挩 喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵鈱�"+ "  \n" + \
                  " 馃寷喔佮副喔權竸喔� 喙�喔傕箟喔� 馃挩 喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔拆煂�"+ "  \n" + \
                  " 鈽佮笡喔脆笖喔佮副喔� 喔勦笝喙�喔傕箟喔�  馃挩 喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔测泤"+ "  \n" + \
                  "鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍"
    return myHelp


def helptexttospeech():
    helpTextToSpeech =   "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨敁" + "\n" + \
                         "鈺� af : Afrikaans" + "\n" + \
                         "鈺� sq : Albanian" + "\n" + \
                         "鈺� ar : Arabic" + "\n" + \
                         "鈺� hy : Armenian" + "\n" + \
                         "鈺� bn : Bengali" + "\n" + \
                         "鈺� ca : Catalan" + "\n" + \
                         "鈺� zh : Chinese" + "\n" + \
                         "鈺� zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "鈺� zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "鈺� zh-yue : Chinese (Cantonese)" + "\n" + \
                         "鈺� hr : Croatian" + "\n" + \
                         "鈺� cs : Czech" + "\n" + \
                         "鈺� da : Danish" + "\n" + \
                         "鈺� nl : Dutch" + "\n" + \
                         "鈺� en : English" + "\n" + \
                         "鈺� en-au : English (Australia)" + "\n" + \
                         "鈺� en-uk : English (United Kingdom)" + "\n" + \
                         "鈺� en-us : English (United States)" + "\n" + \
                         "鈺� eo : Esperanto" + "\n" + \
                         "鈺� fi : Finnish" + "\n" + \
                         "鈺� fr : French" + "\n" + \
                         "鈺� de : German" + "\n" + \
                         "鈺� el : Greek" + "\n" + \
                         "鈺� hi : Hindi" + "\n" + \
                         "鈺� hu : Hungarian" + "\n" + \
                         "鈺� is : Icelandic" + "\n" + \
                         "鈺� id : Indonesian" + "\n" + \
                         "鈺� it : Italian" + "\n" + \
                         "鈺� ja : Japanese" + "\n" + \
                         "鈺� km : Khmer (Cambodian)" + "\n" + \
                         "鈺� ko : Korean" + "\n" + \
                         "鈺� la : Latin" + "\n" + \
                         "鈺� lv : Latvian" + "\n" + \
                         "鈺� mk : Macedonian" + "\n" + \
                         "鈺� no : Norwegian" + "\n" + \
                         "鈺� pl : Polish" + "\n" + \
                         "鈺� pt : Portuguese" + "\n" + \
                         "鈺� ro : Romanian" + "\n" + \
                         "鈺� ru : Russian" + "\n" + \
                         "鈺� sr : Serbian" + "\n" + \
                         "鈺� si : Sinhala" + "\n" + \
                         "鈺� sk : Slovak" + "\n" + \
                         "鈺� es : Spanish" + "\n" + \
                         "鈺� es-es : Spanish (Spain)" + "\n" + \
                         "鈺� es-us : Spanish (United States)" + "\n" + \
                         "鈺� sw : Swahili" + "\n" + \
                         "鈺� sv : Swedish" + "\n" + \
                         "鈺� ta : Tamil" + "\n" + \
                         "鈺� th : Thai" + "\n" + \
                         "鈺� tr : Turkish" + "\n" + \
                         "鈺� uk : Ukrainian" + "\n" + \
                         "鈺� vi : Vietnamese" + "\n" + \
                         "鈺� cy : Welsh" + "\n" + \
                         "鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨敍" + "\n" + "\n\n" + \
                          " 鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    "鈺斺晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨敁" + "\n" + \
                       "鈺� af : afrikaans" + "\n" + \
                       "鈺� sq : albanian" + "\n" + \
                       "鈺� am : amharic" + "\n" + \
                       "鈺� ar : arabic" + "\n" + \
                       "鈺� hy : armenian" + "\n" + \
                       "鈺� az : azerbaijani" + "\n" + \
                       "鈺� eu : basque" + "\n" + \
                       "鈺� be : belarusian" + "\n" + \
                       "鈺� bn : bengali" + "\n" + \
                       "鈺� bs : bosnian" + "\n" + \
                       "鈺� bg : bulgarian" + "\n" + \
                       "鈺� ca : catalan" + "\n" + \
                       "鈺� ceb : cebuano" + "\n" + \
                       "鈺� ny : chichewa" + "\n" + \
                       "鈺� zh-cn : chinese (simplified)" + "\n" + \
                       "鈺� zh-tw : chinese (traditional)" + "\n" + \
                       "鈺� co : corsican" + "\n" + \
                       "鈺� hr : croatian" + "\n" + \
                       "鈺� cs : czech" + "\n" + \
                       "鈺� da : danish" + "\n" + \
                       "鈺� nl : dutch" + "\n" + \
                       "鈺� en : english" + "\n" + \
                       "鈺� eo : esperanto" + "\n" + \
                       "鈺� et : estonian" + "\n" + \
                       "鈺� tl : filipino" + "\n" + \
                       "鈺� fi : finnish" + "\n" + \
                       "鈺� fr : french" + "\n" + \
                       "鈺� fy : frisian" + "\n" + \
                       "鈺� gl : galician" + "\n" + \
                       "鈺� ka : georgian" + "\n" + \
                       "鈺� de : german" + "\n" + \
                       "鈺� el : greek" + "\n" + \
                       "鈺� gu : gujarati" + "\n" + \
                       "鈺� ht : haitian creole" + "\n" + \
                       "鈺� ha : hausa" + "\n" + \
                       "鈺� haw : hawaiian" + "\n" + \
                       "鈺� iw : hebrew" + "\n" + \
                       "鈺� hi : hindi" + "\n" + \
                       "鈺� hmn : hmong" + "\n" + \
                       "鈺� hu : hungarian" + "\n" + \
                       "鈺� is : icelandic" + "\n" + \
                       "鈺� ig : igbo" + "\n" + \
                       "鈺� id : indonesian" + "\n" + \
                       "鈺� ga : irish" + "\n" + \
                       "鈺� it : italian" + "\n" + \
                       "鈺� ja : japanese" + "\n" + \
                       "鈺� jw : javanese" + "\n" + \
                       "鈺� kn : kannada" + "\n" + \
                       "鈺� kk : kazakh" + "\n" + \
                       "鈺� km : khmer" + "\n" + \
                       "鈺� ko : korean" + "\n" + \
                       "鈺� ku : kurdish (kurmanji)" + "\n" + \
                       "鈺� ky : kyrgyz" + "\n" + \
                       "鈺� lo : lao" + "\n" + \
                       "鈺� la : latin" + "\n" + \
                       "鈺� lv : latvian" + "\n" + \
                       "鈺� lt : lithuanian" + "\n" + \
                       "鈺� lb : luxembourgish" + "\n" + \
                       "鈺� mk : macedonian" + "\n" + \
                       "鈺� mg : malagasy" + "\n" + \
                       "鈺� ms : malay" + "\n" + \
                       "鈺� ml : malayalam" + "\n" + \
                       "鈺� mt : maltese" + "\n" + \
                       "鈺� mi : maori" + "\n" + \
                       "鈺� mr : marathi" + "\n" + \
                       "鈺� mn : mongolian" + "\n" + \
                       "鈺� my : myanmar (burmese)" + "\n" + \
                       "鈺� ne : nepali" + "\n" + \
                       "鈺� no : norwegian" + "\n" + \
                       "鈺� ps : pashto" + "\n" + \
                       "鈺� fa : persian" + "\n" + \
                       "鈺� pl : polish" + "\n" + \
                       "鈺� pt : portuguese" + "\n" + \
                       "鈺� pa : punjabi" + "\n" + \
                       "鈺� ro : romanian" + "\n" + \
                       "鈺� ru : russian" + "\n" + \
                       "鈺� sm : samoan" + "\n" + \
                       "鈺� gd : scots gaelic" + "\n" + \
                       "鈺� sr : serbian" + "\n" + \
                       "鈺� st : sesotho" + "\n" + \
                       "鈺� sn : shona" + "\n" + \
                       "鈺� sd : sindhi" + "\n" + \
                       "鈺� si : sinhala" + "\n" + \
                       "鈺� sk : slovak" + "\n" + \
                       "鈺� sl : slovenian" + "\n" + \
                       "鈺� so : somali" + "\n" + \
                       "鈺� es : spanish" + "\n" + \
                       "鈺� su : sundanese" + "\n" + \
                       "鈺� sw : swahili" + "\n" + \
                       "鈺� sv : swedish" + "\n" + \
                       "鈺� tg : tajik" + "\n" + \
                       "鈺� ta : tamil" + "\n" + \
                       "鈺� te : telugu" + "\n" + \
                       "鈺� th : thai" + "\n" + \
                       "鈺� tr : turkish" + "\n" + \
                       "鈺� uk : ukrainian" + "\n" + \
                       "鈺� ur : urdu" + "\n" + \
                       "鈺� uz : uzbek" + "\n" + \
                       "鈺� vi : vietnamese" + "\n" + \
                       "鈺� cy : welsh" + "\n" + \
                       "鈺� xh : xhosa" + "\n" + \
                       "鈺� yi : yiddish" + "\n" + \
                       "鈺� yo : yoruba" + "\n" + \
                       "鈺� zu : zulu" + "\n" + \
                       "鈺� fil : Filipino" + "\n" + \
                       "鈺� he : Hebrew" + "\n" + \
                       "鈺氣晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨晲鈺愨敍" + "\n" + "\n\n" + \
                       " 鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				

        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if text.lower() == '喔勦赋喔副喙堗竾':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == '喔勦赋喔副喙堗竾2':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == '喔勦赋喔副喙堗竾3':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == 'Sp':
                    start = time.time()
                    line.sendMessage(to, " 鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 ")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))	
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, " 鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 ")
                    elapsed_time = time.time() - start
                    line.sendMessage(to,format(str(elapsed_time)))						
                elif text.lower() == '喔｀傅喔氞腹喔�':
                    line.sendMessage(to, "鈿旓笍喔佮福喔膏笓喔侧弗喙囙腑喔勦腑喔脆笝喔ム复喙夃竾喔勦箤喙冟斧喔∴箞喔斷箟喔о涪喔權赴喔勦赴鈿旓笍")
#                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == '喙�喔娻箛喔勦腑喔笝喙�':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "喙�喔о弗喔侧竵喔侧福喔椸赋喔囙覆喔權競喔竾喔氞腑喔� {}".format(str(runtime)))
                elif text.lower() == '喙勦弗喔權箤':
                    try:
                        arr = []
                        owner = "u3930826c2f2dbf7b11a27efbcc37add"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = " 鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                        ret_ += "\n喔娻阜喙堗腑 喙勦弗喔權箤喔勦父喔� 鈿旓笍 {}".format(contact.displayName)
                        ret_ += "\n喔｀覆喔⑧竵喔侧福喔佮弗喔膏箞喔� 鈿旓笍  {}".format(str(len(grouplist)))
                        ret_ += "\n喔｀覆喔⑧竵喔侧福喙�喔炧阜喙堗腑喔� 鈿旓笍  {}".format(str(len(contactlist)))
                        ret_ += "\n喔｀覆喔⑧竵喔侧福喔氞弗喙囙腑喔� 鈿旓笍  {}".format(str(len(blockedlist)))
                        ret_ += "\n喔曕副喔� 鈿旓笍  "
                        ret_ += "\n喔溹腹喙夃箑喔傕傅喔⑧笝喔氞腑喔�  鈿旓笍{}".format(creator.displayName)
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == '喙�喔娻箛喔勦笗喔编箟喔囙竸喙堗覆':
                    try:
                        ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "

                        if settings["autoJoin"] == True: ret_ += "\n喙�喔傕箟喔侧斧喙夃腑喔囙腑喔箓喔曕箟 脳 喙�喔涏复喔� "
                        else: ret_ += "\n喙�喔傕箟喔侧斧喙夃腑喔囙腑喔箓喔曕箟 脳 喔涏复喔�"
                        if settings["detectMention"] == True: ret_ += "\n喔傕箟喔竸喔о覆喔∴箒喔椸箛喔� 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔傕箟喔竸喔о覆喔∴箒喔椸箛喔� 脳 喔涏复喔�"						
                        if settings["autoLeave"] == True: ret_ += "\喔腑喔佮箒喔娻笚喔｀抚喔∴腑喔箓喔曕箟 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔腑喔佮箒喔娻笚喔｀抚喔∴腑喔箓喔曕箟 脳 喔涏复喔�"
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喙�喔傕箟喔侧福喔о浮 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喙�喔傕箟喔侧福喔о浮 脳 喔涏复喔�"	
                        if settings["autoRead"] == True: ret_ += "\n喔｀赴喔氞笟喔箞喔侧笝 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔｀赴喔氞笟喔箞喔侧笝 脳 喔涏复喔�"				
                        if settings["checkSticker"] == True: ret_ += "\n喙�喔娻箛喔勦釜喔曕复喙夃竵喙�喔佮腑喔｀箤 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喙�喔娻箛喔勦釜喔曕复喙夃竵喙�喔佮腑喔｀箤 脳 喔涏复喔�"						
                        if RfuProtect["Protectguest"] == True: ret_ += "\n喔涏箟喔竾喔佮副喔� 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔涏箟喔竾喔佮副喔� 脳 喔涏复喔�"		
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喙�喔娻复喔� 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喙�喔娻复喔� 脳 喔涏复喔�"
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喔⑧竵喙�喔ム复喔� 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喔⑧竵喙�喔ム复喔� 脳 喔涏复喔�"
                        if RfuProtect["protect"] == True: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喔ム笟 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔涏箟喔竾喔佮副喔權竵喔侧福喔ム笟 脳 喙�喔涏复喔�"
                        if RfuProtect["linkprotect"] == True: ret_ += "\n喔涏箟喔竾喔佮副喔� QR 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔涏箟喔竾喔佮副喔� QR 喔涏复喔�"
                        if settings["autoCancel"]["on"] == True:ret_+="\n喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮喙�喔∴阜喙堗腑喔∴傅喔浮喔侧笂喔脆竵喔曕箞喔赤竵喔о箞喔�  " + str(settings["autoCancel"]["members"]) + "脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮  脳 喔涏复喔�"
                        if settings["autoAdd"] == True: ret_ += "\n喔腑喙傕笗喙夃笟喔ム箛喔竸 脳 喙�喔涏复喔�"
                        else: ret_ += "\n喔腑喙傕笗喙夃笟喔ム箛喔竸 脳 喔涏复喔�"			
                        ret_ += "\n"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == '喔氞弗喙囙腑喔勦箑喔涏复喔�':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "喔腑喙傕笗喙夃笟喔ム箛喔竸 馃椊 喙�喔涏复喔�")
                elif text.lower() == '喔氞弗喙囙腑喔勦笡喔脆笖':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "喔腑喙傕笗喙夃笟喔ム箛喔竸 馃椊 喔涏复喔�")
                elif text.lower() == '喙�喔傕箟喔侧箑喔涏复喔�':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "喙�喔傕箟喔侧福喔о浮喔佮弗喔膏箞喙堗浮喔腑喙傕笗喙� 馃椊 喙�喔涏复喔�")
                elif text.lower() == '喙�喔傕箟喔侧笡喔脆笖':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "喙�喔傕箟喔侧福喔о浮喔佮弗喔膏箞喔∴腑喔箓喔曕箟 馃椊 喔涏复喔�")			
                elif text.lower() == '喙佮笂喔椸福喔о浮喙�喔涏复喔�':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "喔腑喔佮笀喔侧竵喙佮笂喔椸福喔о浮 喔腑喙傕笗喙� 馃椊 喙�喔涏复喔�")
                elif text.lower() == '喙佮笂喔椸福喔о浮喔涏复喔�':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "喔腑喔佮笀喔侧竵喙佮笂喔椸福喔о浮 喔腑喙傕笗喙� 馃椊 喔涏复喔�")
                elif text.lower() == '喔箞喔侧笝喙�喔涏复喔�':
                    settings["autoRead"] = True
                    line.sendMessage(to, "喔｀赴喔氞笟喔箞喔侧笝喙佮弗喔班笗喔｀抚喔堗笀喔编笟喔腑喙傕笗喙� 馃椊 喙�喔涏复喔�")
                elif text.lower() == '喔箞喔侧笝喔涏复喔�':
                    settings["autoRead"] = False
                    line.sendMessage(to, "喔｀赴喔氞笟喔箞喔侧笝喙佮弗喔班笗喔｀抚喔堗笀喔编笟喔腑喙傕笗喙� 馃椊 喔涏复喔�")
                elif text.lower() == '喙�喔娻箛喔勦笗喔脆箟喔佮箑喔涏复喔�':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "喙�喔涏复喔斷竵喔侧福喙�喔娻箛喔勦福喔班笟喔� 喔曕福喔о笀喔腑喔� 喔笗喔脆箟喔佮箑喔佮腑喔｀箤 馃椊 喙�喔涏复喔�")
                elif text.lower() == '喙�喔娻箛喔勦笗喔脆箟喔佮笡喔脆笖':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "喔涏复喔斷竵喔侧福喙�喔娻箛喔勦福喔班笟喔� 喔曕福喔о笀喔腑喔� 喔笗喔脆箟喔佮箑喔佮腑喔｀箤 馃椊 喔涏复喔�")                   
#==============================================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == '喙勦腑喔斷傅':
                    line.sendMessage(msg.to,"Mid馃帬 " +  lineMID)
                elif text.lower() == '喔娻阜喙堗腑':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"喔娻阜喙堗腑 馃帬 n" + me.displayName)
                elif text.lower() == '喔曕副喔�':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"喔傕箟喔竸喔о覆喔�&喔曕副喔� 馃帬 \n" + me.statusMessage)
                elif text.lower() == '喔｀腹喔�':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == '喔｀腹喔涏抚喔脆笖喔掂箓喔�':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == '喔｀腹喔涏笡喔�':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("喔勦笚 "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("喙勦腑喔斷傅 "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("喔娻阜喙堗腑 "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "鈯�  \n" + contact.displayName)
                elif msg.text.lower().startswith("喔曕副喔� "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "鈯�  \n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("喔｀腹喔� "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("video "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("喔涏竵 "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "喔ム竾喔勦赋喔副喙堗竾喔勦副喔斷弗喔竵喙冟斧喔∴箞")
                        except:
                            line.sendMessage(msg.to, "喔勦副喔斷弗喔竵 鈭� 喙�喔｀傅喔⑧笟喔｀箟喔涪")
                            
                elif text.lower() == '喔勦阜喔權福喙堗覆喔�':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "鈮�")
                    except:
                        line.sendMessage(msg.to, "鈮�")
						
#==============================================================================#
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    line.sendText(msg.to,"鍏充簡閭�璇锋嫆缁濄�傝鏃跺紑璇锋寚瀹氫汉鏁板彂閫�")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,strnum + " 喔浮喔侧笂喔脆竵喙冟笝喔佮弗喔膏箞喔∴笀喔班笡喔忇复喙�喔笜喔勦赋喙�喔娻复喔嵿箓喔斷涪喔副喔曕箓喔權浮喔编笗喔�")
                                else:
                                    line.sendText(msg.to,strnum + "浣夸汉浠ヤ笅鐨勫皬缁勭敤鑷姩閭�璇锋嫆缁�")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,"喔勦箞喔侧箘喔∴箞喔栢腹喔佮笗喙夃腑喔�")
                        else:
                                line.sendText(msg.to,"喔佮覆喔｀笀喔编笖喔副喔權笖喔编笟喔椸傅喙堗箒喔涏弗喔佮笡喔｀赴喔弗喔侧笖")		
                elif msg.text.lower().startswith("喙�喔ム傅喔⑧笝喙佮笟喔� "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"喙�喔ム傅喔⑧笝喙佮笟喔氞笘喔灌竵喙�喔炧复喙堗浮")
                            break
                        except:
                            line.sendMessage(msg.to,"喔ム箟喔∴箑喔弗喔�")
                            break
                elif msg.text.lower().startswith("喙�喔ム傅喔⑧笝喙佮笟喔氞弗喔� "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"喙�喔ム傅喔⑧笟喙佮笟喔氞弗喔�")
                            break
                        except:
                            line.sendMessage(msg.to,"喔ム箟喔∴箑喔弗喔�")
                            break
                elif text.lower() == '喙�喔娻箛喔勦箑喔ム傅喔⑧笝喙佮笟喔�':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n    `~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == '喙�喔娻箛喔勦箒喔笖':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "   `~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻�� ")
                elif text.lower() == '喙勦腑喔斷傅喔佮弗喔膏箞喔�':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "鈫�  鈿旓笍 " + gid.id + " 鈫�")
                elif text.lower() == '喔｀腹喔涏竵喔ム父喙堗浮':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == '喔娻阜喙堗腑喔佮弗喔膏箞喔�':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "鈫� " + gid.name + " 鈫�")
                elif text.lower() == '喔傕腑喔ム复喙夃竾喔勦箤':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "喔權傅喙夃竸喔粪腑 QR 喔傕腑喔囙竵喔ム父喙堗浮喔權傅喙� 喔覆喔∴覆喔｀笘喔權赋喔涏箖喔娻箟喙勦笖喙夃箑喔ム涪 \nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == '喙�喔涏复喔斷弗喔脆箟喔囙竸喙�':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "喙�喔涏复喔斷腑喔⑧腹喙堗竵喔｀父喔撪覆 喔副喙堗竾喔勦赋喔о箞喔� 喔傕腑喔囙弗喔脆箟喔囙竸喙�")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "喙�喔涏复喔擰R喔佮弗喔膏箞喔∴箑喔涏箛喔權腑喔编笝喔椸傅喙堗箑喔｀傅喔⑧笟喔｀箟喔涪")
                elif text.lower() == '喔涏复喔斷弗喔脆箟喔囙竸喙�':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "喔涏复喔斷腑喔⑧父喙堗腑喙堗赴喔堗赴喔涏复喔斷箘喔｀腑喔掂竵喔ム赴")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "OK 锘� QR 喔涏复喔斷弗喔�")
                elif text.lower() == '喔傕箟喔浮喔灌弗喔箟喔竾':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                    ret_ += "\n喔娻阜喙堗腑喔佮弗喔膏箞喔� 鈻�  {}".format(str(group.name))
                    ret_ += "\nGid喔佮弗喔膏箞喔� 鈻�  {}".format(group.id)
                    ret_ += "\n喔溹腹喙夃釜喔｀箟喔侧竾喔佮弗喔膏箞喔� 鈻�  {}".format(str(gCreator))
                    ret_ += "\n喔堗赋喔權抚喔權釜喔∴覆喔娻复喔� 鈻� {}".format(str(len(group.members)))
                    ret_ += "\n喔浮喔侧笂喔脆竵喔勦箟喔侧竾喙�喔娻复喔� 鈻� {}".format(gPending)
                    ret_ += "\nQR 喔傕腑喔囙竵喔ム父喙堗浮 鈻� ".format(gQr)
                    ret_ += "\n   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)

                elif text.lower() == '喔浮喔侧笂喔脆竵':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n鈫� 鈫� {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n   鈫� 喔堗赋喔權抚喔� {}   喔勦笝 鈫� ".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == '喔佮弗喔膏箞喔�':
                        groups = line.groups
                        ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n鉃� {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n 喔堗赋喔權抚喔� {} 喔佮弗喔膏箞喔�  ".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))

                elif text.lower() == '1喔佮弗喔膏箞喔�':
                        groups = ki.groups
                        ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                        no = 0 + 1
                        for gid in groups:
                            group = ki.getGroup(gid)
                            ret_ += "\n鉃� {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n 喔堗赋喔權抚喔� {} 喔佮弗喔膏箞喔� ".format(str(len(groups)))
                        ki.sendMessage(to, str(ret_))

                elif text.lower() == '2喔佮弗喔膏箞喔�':
                        groups = kk.groups
                        ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 "
                        no = 0 + 1
                        for gid in groups:
                            group = kk.getGroup(gid)
                            ret_ += "\n鉃� {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n  喔堗赋喔權抚喔� {} 喔佮弗喔膏箞喔�".format(str(len(groups)))
                        kk.sendMessage(to, str(ret_))

                elif text.lower() == '3喔佮弗喔膏箞喔�':
                        groups = kc.groups
                        ret_ = "鈺斺晲鈺怺 Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = kc.getGroup(gid)
                            ret_ += "\n鉃� {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n 喔堗赋喔權抚喔� {} 喔佮弗喔膏箞喔�".format(str(len(groups)))
                        kc.sendMessage(to, str(ret_))
						
					
#==============================================================================#
#==============================================================================#          
                elif text.lower() == '喙佮笚喙囙竵':
                            if msg.toType == 0:
                                sendMention(to, to, "", "")
                            elif msg.toType == 2:
                                group = line.getGroup(to)
                                contact = [mem.mid for mem in group.members]
                                ct1, ct2, ct3, ct4, ct5, jml = [], [], [], [], [], len(contact)
                                if jml <= 100:
                                    mentionMembers(to, contact)
                                elif jml > 100 and jml <= 200: 
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, jml):
                                        ct2 += [contact[b]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                elif jml > 200 and jml <= 300:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, jml):
                                        ct3 += [contact[c]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                elif jml > 300 and jml <= 400:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, jml):
                                        ct4 += [contact[d]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                elif jml > 400 and jml <= 500:
                                    for a in range(0, 99):
                                        ct1 += [contact[a]]
                                    for b in range(100, 199):
                                        ct2 += [contact[b]]
                                    for c in range(200, 299):
                                        ct3 += [contact[c]]
                                    for d in range(300, 399):
                                        ct4 += [contact[d]]
                                    for e in range(400, jml):
                                        ct4 += [contact[e]]
                                    mentionMembers(to, ct1)
                                    mentionMembers(to, ct2)
                                    mentionMembers(to, ct3)
                                    mentionMembers(to, ct4)
                                    mentionMembers(to, ct5)
#===================================================================#              

                elif text.lower() == '喙�喔娻箛喔�':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["喔о副喔權腑喔侧笚喔脆笗喔⑧箤", "喔о副喔權笀喔编笝喔椸福喙�", "喔о副喔權腑喔编竾喔勦覆喔�", "喔о副喔權笧喔膏笜", "喔о副喔權笧喔む斧喔编釜喔氞笖喔�", "喔о副喔權辅喔膏竵喔｀箤", "喔о副喔權箑喔覆喔｀箤"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n喙�喔о弗喔�  [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "喙�喔｀复喙堗浮喔曕福喔о笀喔堗副喔氞福喔侧涪喔娻阜喙堗腑喔勦笝喔箞喔侧笝喙佮笟喔氞箒喔椸箛喔乗n" + readTime)
                            

                elif text.lower() == '喔箞喔侧笝':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["喔о副喔權腑喔侧笚喔脆笗喔⑧箤", "喔о副喔權笀喔编笝喔椸福喙�", "喔о副喔權腑喔编竾喔勦覆喔�", "喔о副喔權笧喔膏笜", "喔о副喔權笧喔む斧喔编釜喔氞笖喔�", "喔о副喔權辅喔膏竵喔｀箤", "喔о副喔權箑喔覆喔｀箤"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n喙�喔о弗喔�  [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"喔｀覆喔⑧笂喔粪箞喔竸喔權笚喔掂箞喔箞喔侧笝 \nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '喔｀覆喔⑧笂喔粪箞喔竸喔權笚喔掂箞喔箞喔侧笝 \n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n喙�喔о弗喔侧笚喔掂箞喔箞喔侧笝 \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"喔副喙堗竾喙�喔娻箛喔勦箖喔浮喙堗箒喔ム箟喔о釜喔编箞喔囙腑喙堗覆喔權箖喔浮喙堗腑喔掂竵喔｀腑喔� \n   鈿旓笍 艩鈧Ｔ� 喔库湭纽 尾楼.艩伪褩 鈿旓笍 ")

                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)




                elif "Bcvoice " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = ("鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 \n`~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbcvoice " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = ("鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍 \n`~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Dow " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Dow ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="喙�喔佮复喔權競喔掂笖 喔堗赋喔佮副喔� 喔傕箟喔竸喔о覆喔�! 喙傕笡喔｀笖喔勦弗喔脆竵喔ム复喔囙竵喙孿n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))

                elif "喔勦箟喔權斧喔侧斧喔權副喔�" in msg.text:
                    proses = msg.text.split(":")
                    get = msg.text.replace(proses[0] + ":","")
                    getfilm = get.split()
                    title = getfilm[0]
                    tahun = getfilm[1]
                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                    start = time.time()
                    data=r.text
                    data=json.loads(data)
                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                    hasil += "\n\n " +str(data["Plot"])
                    hasil += "\n\nDirector : " +str(data["Director"])
                    hasil += "\nActors   : " +str(data["Actors"])
                    hasil += "\nRelease : " +str(data["Released"])
                    hasil += "\nGenre    : " +str(data["Genre"])
                    hasil += "\nRuntime   : " +str(data["Runtime"])
                    path = data["Poster"]
                    line.sendImageWithURL(msg.to, str(path))
                    line.sendMessage(msg.to,hasil)

                elif text.lower() == 'Day':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 


                
                elif "喔勦箟喔權斧喔侧腑喔脆笝喔笗喔侧箒喔佮福喔�" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = " `~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻�� "
                            ret_ += "\n 喔娻阜喙堗腑   {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n 喔⑧腹喙�喔嬥腑喙�喔權浮 : {}".format(str(data["user"]["username"]))
                            ret_ += "\n 喔曕副喔�  {}".format(str(data["user"]["biography"]))
                            ret_ += "\n 喔溹腹喙夃笗喔脆笖喔曕覆喔�   {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n 喔曕复喔斷笗喔侧浮   {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n 喔佮覆喔｀涪喔粪笝喔⑧副喔�: 喙佮弗喙夃抚"
                            else:
                                ret_ += "\n 喔佮覆喔｀涪喔粪笝喔⑧副喔�: 喔⑧副喔囙箘喔∴箞喙勦笖喙�"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n Akun Pribadi : Iya"
                            else:
                                ret_ += "\n 喔氞副喔嵿笂喔掂釜喙堗抚喔權笟喔膏竸喔勦弗: 喙勦浮喙�"
                            ret_ += "\n Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "喙勦浮喙堗笧喔氞笢喔灌箟喙冟笂喙�")

                    line.sendMessage(to, str(ret_))
                elif "喔勦箟喔權斧喔侧福喔灌笡" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "喔｀腹喔涏竵喔侧福喔曕腹喔�" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "喔勦箟喔權斧喔侧涪喔灌笚喔灌笡" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "喔佮覆喔｀竸喙夃笝喔覆喔∴傅喔｀覆喔⑧弗喔班箑喔傅喔⑧笖喔曕覆喔∴笝喔掂箟"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n鈰� {} ]".format(str(data["title"]))
                            ret_ += "\n鈰� https://www.youtube.com{}".format(str(data["href"]) + "\n")
                        ret_ += "\n\n鈰� 喔椸傅喙堗笧喔� {}  喔勦弗喔脆笡".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["喔箞喔侧笝喔腑喙傕笗喙夃箑喔涏复喔�"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"  `~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��")
                elif msg.text in ["喔箞喔侧笝喔腑喙傕笗喙夃笡喔脆笖"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, " 鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍")



                elif text.lower() == '喔｀覆喔⑧竵喔侧福喙�喔炧阜喙堗腑喔�':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n喔堗赋喔權抚喔�  %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["喔｀覆喔⑧竵喔侧福喔氞弗喙囙腑喔�"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="`~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n喔堗赋喔權抚喔�  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["喔｀覆喔⑧竵喔侧福mid"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="`~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n喔堗赋喔權抚喔�  %i" % len(kontak)
                    line.sendMessage(receiver, msgs)



                elif msg.text.lower() == '喙�喔娻复喔嵿箑喔勦箟喔�':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "喔炧复喔∴笧喙屶竸喔赤箑喔娻复喔嵿竵喔ム父喙堗浮")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "喔溹腹喙夃釜喔｀箟喔侧竾喔佮弗喔膏箞喔∴腑喔⑧腹喙堗箖喔權箒喔ム箟喔�")

                elif msg.text in ["喔腑喔�"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)
                            ki.leaveGroup(receiver)
                            kk.leaveGroup(receiver)
                            kc.leaveGroup(receiver)
                            ke.leaveGroup(receiver)							
                        except:
                            pass


                elif msg.text in ["喙佮笚喙囙竵喙�喔涏复喔�"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"喙�喔涏复喔斷福喔班笟喔氞競喙夃腑喔勦抚喔侧浮喙佮笚喙囙竵")
                
                elif msg.text in ["喙佮笚喙囙竵喔涏复喔�"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"喔涏复喔斷福喔班笟喔氞競喙夃腑喔勦抚喔侧浮喙佮笚喙囙竵")

                elif '喔曕副喙夃竾喙佮笚喙囙竵: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('喔曕副喙夃竾喙佮笚喙囙竵: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "喔曕副喙夃竾喔傕箟喔竸喔о覆喔∴箑喔｀阜喔⑧笟喔｀箟喔涪")
                     else:
                         settings["Respontag"] = spl
                         line.sendMessage(msg.to, "鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍\n\n{}".format(str(spl)))


                elif '喔椸副喔佮腑喔竵: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('喔椸副喔佮腑喔竵: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "喔曕副喙夃竾喔傕箟喔竸喔о覆喔∴竸喔權腑喔竵喙�喔｀傅喔⑧笟喔｀箟喔涪")
                     else:
                          settings["bye"] = spl
                          line.sendMessage(msg.to, "鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍\n\n\n{}".format(str(spl)))

                elif '喔椸副喔佮箑喔傕箟喔�: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('喔椸副喔佮箑喔傕箟喔�: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "喔曕副喙夃竾喔傕箟喔竸喔о覆喔∴竸喔權箑喔傕箟喔侧箑喔｀傅喔⑧笟喔｀箟喔涪喙佮弗喙夃抚")
                     else:
                          settings["welcome"] = spl
                          line.sendMessage(msg.to, "鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍\n\n\n{}".format(str(spl)))

                elif msg.text.lower().startswith("喔犩覆喔� "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif text.lower() == '喔ム笟喔｀副喔�':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "喔ム笟喙佮弗喙夃抚喔堗福喙夃覆喔�")
                    line.sendMessage(to, "喙�喔о弗喔侧笚喔掂箞喙冟竷喙�: %s喔о复喔權覆喔椸傅" % (elapsed_time))						
						
                elif text.lower() == 'zt':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "喔∴箞喔∴傅喔勦笝喙冟釜喙堗福喙堗腑喔囙斧喔權箖喔權竵喔ム父喙堗浮喔權傅喙夝煒�")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == 'zm':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "喙勦浮喙堗浮喔祄id喔勦笝喙冟釜喙堗福喙堗腑喔囙斧喔欚煠�")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == 'zc':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "喙勦浮喙堗浮喔掂竸喔權箖喔箞喔｀箞喔竾喔笝喙冟笝喔佮弗喔膏箞喔∴笝喔掂箟馃槀")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
                            
                elif '喔ム笟喙�喔娻复喔峉' in msg.text.lower():
                   if msg.toType == 2:
                       X = line.getGroup(msg.to)
                       if X.invitee is not None:
                           gInviMids = [contact.mid for contact in X.invitee]
                           line.cancelGroupInvitation(msg.to, gInviMids)
                       else:
                           if settings["lang"] == "JP":
                               line.sendMessage(msg.to,"喙勦浮喙堗浮喔掂竵喔侧福喙�喔娻复喔�")
                           else:
                               line.sendMessage(msg.to,"喔傕腑喔笭喔编涪喙勦浮喙堗浮喔�")
                   else:
                       if settings["lang"] == "JP":
                           line.sendMessage(msg.to,"喙勦浮喙堗釜喔侧浮喔侧福喔栢箖喔娻箟喔權腑喔佮竵喔ム父喙堗浮喙勦笖喙�")
                       else:
                           line.sendMessage(msg.to,"喙勦浮喙堗箖喔娻箟喔囙覆喔權笝喙夃腑喔⑧竵喔о箞喔侧竵喔ム父喙堗浮")

                elif '喔曕副喙夃竾喔勦笝喔腑喔�: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('喔曕副喙夃竾喔勦笝喔腑喔�: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "喔曕副喙夃竾喔勦笝喔腑喔�")
                     else:
                          settings["Nn"] = spl
                          line.sendMessage(msg.to, "{}".format(str(spl)))
                elif '喔曕副喙夃竾喔勦笝喙�喔傕箟喔�: ' in msg.text:
                  if msg._from in admin:
                     spl = msg.text.replace('喔曕副喙夃竾喔勦笝喙�喔傕箟喔�: ','')
                     if spl in [""," ","\n",None]:
                         line.sendMessage(msg.to, "喔曕副喙夃竾喔勦笝喔腑喔�")
                     else:
                          settings["Sd"] = spl
                          line.sendMessage(msg.to, "{}".format(str(spl)))

                elif msg.text in ["喙�喔娻复喔�"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"喔箞喔囙福喔侧涪喔娻阜喙堗腑喙�喔炧阜喙堗腑喙�喔娻复喔�")


                elif msg.text in ["cb"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"喔椸赋喔佮覆喔｀弗喔氞副喔嵿笂喔掂笖喔赤笚喔编箟喔囙斧喔∴笖喙�喔｀傅喔⑧笟喔｀箟喔涪")
                    print ("Clear Ban")

                elif text.lower() == 'Sai':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)                        
                        group.preventedJoinByTicket = True
                        line.updateGroup(group)
                        print ("喔勦弗喔脆箟喔佮箑喔傕箟喔� ")

                elif '喙�喔曕赴' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("喙�喔曕赴喔勦笝")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"喔堗赋喔佮副喔�")

                elif '喙�喔曕赴1' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("喙�喔曕赴喔勦笝1")
                           except:
                               line.sendMessage(msg.to,"喔堗赋喔佮副喔�")                               

                elif '1 ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.kickoutFromGroup(msg.to,[target])           
                               print ("喔勦弗喔脆箟喔�1喙�喔曕赴")
                           except:
                               ki.sendMessage(msg.to,"喔堗赋喔佮副喔�")                               

                elif '2 ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.kickoutFromGroup(msg.to,[target])
                               print ("喔勦弗喔脆箟喔�2喙�喔曕赴")
                           except:
                               kk.sendMessage(msg.to,"喔堗赋喔佮副喔�")                              

                elif '3 ' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kc.kickoutFromGroup(msg.to,[target])
                               print ("喔勦弗喔脆箟喔�3喙�喔曕赴")
                           except:
                               kc.sendMessage(msg.to,"喔堗赋喔佮副喔�")                              


                elif '喙�喔娻复喔�' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "喙�喔娻复喔峯k")
                           except:
                               line.sendMessage(msg.to,"喔堗赋喔佮副喔� 喔佮覆喔｀箑喔娻复喔�")

                elif '1喙�喔娻复喔�' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.inviteIntoGroup(msg.to,[target])
                               ki.sendMessage(receiver, "喙�喔娻复喔峯k")
                               print ("R1 invite User")
                           except:
                               ki.sendMessage(msg.to,"喔堗赋喔佮副喔� 喔佮覆喔｀箑喔娻复喔�")                               

                elif '2喙�喔娻复喔�' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kk.inviteIntoGroup(msg.to,[target])
                               kk.sendMessage(receiver, "喙�喔娻复喔峯k")
                               ("R2 invite User")
                           except:
                               kk.sendMessage(msg.to,"喔堗赋喔佮副喔� 喔佮覆喔｀箑喔娻复喔�")                               

                elif '3喙�喔娻复喔�' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               kc.inviteIntoGroup(msg.to,[target])
                               kc.sendMessage(receiver, "喙�喔娻复喔�")
                               ("R3 invite User")
                           except:
                               kc.sendMessage(msg.to,"喔堗赋喔佮副喔� 喔佮覆喔｀箑喔娻复喔�")                               
                elif "Cleanse" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("Cleanse","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing 么")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line,ki,kk,kc,ke]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["喙�喔曕赴喔斷赋"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"喙勦浮喙堗浮喔掂笟喔编笉喔娻傅喔斷赋")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line,ki,kk,kc,ke]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"喙�喔曕赴喔佮父喙�喔曕赴喔佮弗喔编笟")
                                     print ("喙勦弗喙堗箑喔曕赴喔斷赋")

                elif text.lower() == "喔ム笟喙佮笂喔�":
                        if msg._from in Family:
                            try:
                                line.removeAllMessages(op.param2)
                                kk.removeAllMessages(op.param2)
                                kc.removeAllMessages(op.param2)
                                ke.removeAllMessages(op.param2)                                
                                line.sendMessage(msg.to,"喔ム笟喙佮笂喔椸箑喔｀傅喔⑧笟喔｀箟喔涪")
                            except:
                                pass
                                print ("喔ム笟喙佮笂喔�")

                elif text.lower() == "喔腑喔�1":
                    if msg._from in Family:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)                        
                        print ("Kicker Leave")

                elif text.lower() == "喔腑喔佮箒喔娻笚喔｀抚喔�":
                    if msg._from in Family:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki.leaveGroup(i)
                            kk.leaveGroup(i)
                            kc.leaveGroup(i)
                            ke.leaveGroup(i)                            
                            print ("喔腑喔佮箒喔娻笚")

                elif "喔娻阜喙堗腑: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"ok 喙�喔涏弗喔掂箞喔⑧笝喙佮弗喙夃抚 喙�喔涏弗喔掂箞喔⑧笝喙�喔涏箛喔�  " + string)
                        print ("Update Name")

                elif "喔曕副喔�: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"ok 喔勦父喔撪箘喔斷箟喙�喔涏弗喔掂箞喔⑧笝喙佮弗喙夃抚 喙�喔涏箛喔�  " + string)
                        print ("Update Bio Succes")

                elif "喔勦弗喔脆箟喔�: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki.getProfile()
                        profile_B = kk.getProfile()
                        profile_C = kc.getProfile()
                        profile_D = ke.getProfile()                        
                        profile_A.displayName = string
                        profile_B.displayName = string
                        profile_C.displayName = string
                        profile_D.displayName = string                        
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"喔勦父喔撪箘喔斷箟喙�喔涏弗喔掂箞喔⑧笝喔娻阜喙堗腑喔勦弗喔脆箟喔佮箑喔佮腑喔｀箤 喙�喔涏箛喔�   " + string)
                        print ("Update Name All Kicker")

                elif "喔曕副喔竸喔ム复喙夃竵: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki.getProfile()
                        profile_B = kk.getProfile()
                        profile_C = kc.getProfile()
                        profile_D = kc.getProfile()                        
                        profile_A.statusMessage = string
                        profile_B.statusMessage = string
                        profile_C.statusMessage = string
                        profile_D.statusMessage = string                        
                        ki.updateProfile(profile_A)
                        kk.updateProfile(profile_B)
                        kc.updateProfile(profile_C)
                        ke.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"Update Bio All Kicker to : " + string)
                        print ("Update Bio All Kicker")

                elif text.lower() == "Rakey":
                    if msg._from in Family:
                        profile = ki.getProfile()
                        text = profile.displayName + ""
                        ki.sendMessage(to, text)                                
                        profile = kk.getProfile()
                        text = profile.displayName + ""
                        kk.sendMessage(to, text)                                
                        profile = kc.getProfile()
                        text = profile.displayName + ""
                        kc.sendMessage(to, text)
                        profile = ke.getProfile()                        
                        text = profile.displayName + ""
                        ke.sendMessage(to, text)                        
                        print ("喔副喙堗竾喔勦弗喔脆箟喔佮箑喔傕箟喔�")

  

#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == '喙�喔涏复喔斷竵喔编笝':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")

                elif msg.text.lower() == '喔涏复喔斷竵喔编笝':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝   ")

                elif msg.text.lower() == '喔佮副喔權涪喔�':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")

                elif msg.text.lower() == '喔涏复喔斷竵喙夃笝喔⑧竵':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿釜喔∴覆喔娻复喔�   ")

                elif msg.text.lower() == '喔佮副喔權箑喔娻复喔�':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�   ")

                elif msg.text.lower() == '喔涏复喔斷竵喔编笝喙�喔娻复喔�':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�  ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔�  ")

                elif msg.text.lower() == '喔佮副喔權弗喔脆箟喔�':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")

                elif msg.text.lower() == '喔涏复喔斷竵喔编笝喔ム复喙夃竾':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�   ")

                elif msg.text.lower() == '喔佮副喔權釜喔∴覆喔娻复喔�':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵 喔佮弗喔膏箞喔�  ")

                elif msg.text.lower() == '喔涏复喔斷竵喔编笝喔浮喔侧笂喔脆竵':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�   ")

                elif msg.text.lower() == '喔佮副喔權竸喔權箑喔傕箟喔�':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")

                elif msg.text.lower() == '喔涏复喔斷竵喔编笝喔勦笝喙�喔傕箟喔�':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮   ")

                elif msg.text.lower() == '喙�喔涏复喔斷斧喔∴笖':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔椸副喙夃竾喔浮喔斷箑喔｀傅喔⑧笟喔｀箟喔涪喙佮弗喙夃抚")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔椸副喙夃竾喔浮喔斷箑喔｀傅喔⑧笟喔｀箟喔涪喙佮弗喙夃抚")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿竵喔ム父喙堗浮")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔ム复喔佮箑喔娻复喔嵿竵喔ム父喙堗浮")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔曕赴喔浮喔侧笂喔脆竵喔勦笝喙冟笝喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔曕赴喔浮喔侧笂喔脆竵喔勦笝喙冟笝喔佮弗喔膏箞喔�")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔ム复喙夃竾喔佮弗喔膏箞喔�")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔氞父喔勦竸喔ム笭喔侧涪喔權箟喔竵喙�喔傕箟喔侧竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔氞父喔勦竸喔ム笭喔侧涪喔權箟喔竵喙�喔傕箟喔侧竵喔ム父喙堗浮")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔氞父喔勦竸喔ム笭喔侧涪喔權箟喔竵喙�喔傕箟喔侧竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喙�喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔氞父喔勦竸喔ム笭喔侧涪喔權箟喔竵喙�喔傕箟喔侧竵喔ム父喙堗浮")

                elif msg.text.lower() == '喔涏复喔斷斧喔∴笖':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔椸副喙夃竾喔浮喔斷箑喔｀傅喔⑧笟喔｀箟喔涪喙佮弗喙夃抚")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔椸副喙夃竾喔浮喔斷箑喔｀傅喔⑧笟喔｀箟喔涪喙佮弗喙夃抚")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔娻复喔嵿釜喔∴覆喔娻复喔佮竵喔ム父喙堗浮")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔娻复喔嵿釜喔∴覆喔娻复喔佮竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔娻复喔嵿釜喔∴覆喔娻复喔佮竵喔ム父喙堗浮")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔⑧竵喙�喔娻复喔嵿釜喔∴覆喔娻复喔佮竵喔ム父喙堗浮")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔曕赴喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔曕赴喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔曕赴喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔曕赴喔浮喔侧笂喔脆竵喔佮弗喔膏箞喔�")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔涏复喔斷弗喔脆箟喔囙竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔涏复喔斷弗喔脆箟喔囙竵喔ム父喙堗浮")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔涏复喔斷弗喔脆箟喔囙竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喙�喔涏复喔斷弗喔脆箟喔囙竵喔ム父喙堗浮")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔佮弗喔膏箞喔�")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮")
                        else:
                            line.sendMessage(msg.to,"喔涏复喔斷笡喙夃腑喔囙竵喔编笝喔勦笝喙�喔傕箟喔侧竵喔ム父喙堗浮")
#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == '喙�喔涏复喔斷竸喔權箑喔傕箟喔�':
                        if settings["Sd"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喙�喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔曕箟喔笝喔｀副喔氞竸喔權箑喔傕箟喔侧竵喔ム父喙堗浮")
                        else:
                            settings["Sd"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喙�喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔曕箟喔笝喔｀副喔氞竸喔權箑喔傕箟喔侧竵喔ム父喙堗浮")
                elif msg.text.lower() == '喔涏复喔斷竸喔權箑喔傕箟喔�':
                        if settings["Sd"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔曕箟喔笝喔｀副喔氞竸喔權箑喔傕箟喔侧竵喔ム父喙堗浮")
                        else:
                            settings["Sd"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔曕箟喔笝喔｀副喔氞竸喔權箑喔傕箟喔侧竵喔ム父喙堗浮")

                elif msg.text.lower() == '喙�喔涏复喔斷竸喔權腑喔竵':
                        if settings["Nn"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喙�喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔勦笝喔腑喔�")
                        else:
                            settings["Nn"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喙�喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔勦笝喔腑喔�")
                elif msg.text.lower() == '喔涏复喔斷竸喔權腑喔竵':
                        if settings["Nn"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔勦笝喔腑喔�")
                        else:
                            settings["Nn"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"喔涏复喔斷競喙夃腑喔勦抚喔侧浮喔勦笝喔腑喔�")

                elif text.lower() == '1喔ム笟喔｀副喔�':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "喔ム笟喔｀副喔權箑喔福喙囙笀喙佮弗喙夃抚喔傕腑喔｀副喔�")
                    line.sendMessage(to, "喔｀赴喔⑧赴喙�喔о弗喔侧笚喔掂箞喙冟笂喙�: %s喔о复喔權覆喔椸傅" % (elapsed_time))								
								
                elif "Allban" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"喔浮喔侧笂喔脆竵喔椸副喙夃竾喔浮喔斷箘喔斷箟喔｀副喔氞竵喔侧福喙�喔炧复喙堗浮喙佮笟喔權箒喔ム箟喔�")
										   
                elif 'ban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"喙�喔炧复喙堗浮喔傕付喙夃笝喔赋喔福喔编笟喔氞副喔嵿笂喔掂笖喔� ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"喙勦浮喙堗笧喔�")

                elif 'unban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"喔⑧竵喙�喔ム复喔佮笟喔编笉喔娻傅喔堗覆喔佮笟喔编笉喔娻傅喔斷赋")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"喙勦浮喙堗笧喔�")

                elif msg.text in ["喙�喔娻箛喔勦笖喔�"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"喙勦浮喙堗笧喔�") 
                    else:
                        line.sendMessage(msg.to,"喔｀覆喔⑧笂喔粪箞喔笢喔灌箟喔曕复喔斷笖喔�")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "鉃� " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "   鈿旓笍 S臋艂f 脽每.鈥�*鈩溾湸嗒權翰銇傅唳о箤鉁粹劀*鈥� 鈿旓笍"
                    ret_ += "\nSTICKER ID : {}".format(stk_id)
                    ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n   `~|掳鈥� 蟺醼斸�膏韩嗪傅喙堛伄喔掂Η 喙屆椻��"
                    line.sendMessage(to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
          if op.param2 in Family:
            pass
          if op.param2 in RfuBot:
          	pass
          else:
            if op.param3 in lineMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kk.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = kk.reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  line.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in kiMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kc.updateGroup(G)
                  ticket = kc.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kk.updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kkMID:
              if op.param2 not in Family:
                try:
                  G = kc.getGroup(op.param1)
                  G = ki.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  kc.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kk.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in kcMID:
              if op.param2 not in Family:
                try:
                  G = kk.getGroup(op.param1)
                  G = ke.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  kc.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in keMID:
              if op.param2 not in Family:
                try:
                  G = ki.getGroup(op.param1)
                  G = kc.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki.updateGroup(G)
                  ticket = ki.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ke.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  

        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
                kk.leaveRoom(op.param1)
                kc.leaveRoom(op.param1)
                ke.leaveRoom(op.param1)                
#==============================================================================#
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                                                
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True                       

                elif op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kkMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in kcMID:
                    if op.param2 in kkMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                elif op.param3 in keMID:
                    if op.param2 in kcMID:
                        G = ke.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kc.updateGroup(G)
                    else:
                        G = ke.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ke.updateGroup(G)
                        ticket = ke.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ke.updateGroup(G)
                        settings["blacklist"][op.param2] = True
            except:
                pass
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"喙�喔涏弗喔掂箞喔⑧笝喔｀腹喔涏笭喔侧笧喙�喔｀傅喔⑧笟喔｀箟喔涪喙佮弗喙夃抚")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                    ki.sendChatChecked(to, msg_id)
                    kk.sendChatChecked(to, msg_id)
                    kc.sendChatChecked(to, msg_id)
                    ke.sendChatChecked(to, msg_id)					
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)

                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["\n " + cName ]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          line.sendMessage(to,str(settings["Respontag"]))
                                          #sendMessageWithMention(to, contact.mid)
                                          line.sendMessage(msg.to, None, contentMetadata={"STKID":"405","STKPKGID":"1","STKVER":"100"}, contentType=7)
                                          break




        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["Sd"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendMessage(op.param1,str(settings["welcome"]))
             line.sendImageWithURL(op.param1,image)
        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["Nn"] == True:
             if op.param2 in lineMID:
                 return
             ginfo = line.getGroup(op.param1)
             contact = line.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             line.sendImageWithURL(op.param1,image)
             line.sendMessage(op.param1,str(settings["bye"]) + "\n\n" + line.getContact(op.param2).displayName)
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n" + Name
                            pref=['喙佮腑喔氞腑喙堗覆喔權笚喔赤箘喔� 喔椸赋喙勦浮喔∴赴喔腑喔佮浮喔侧竸喔膏涪喔佮副喔權弗喔�  ']
                            line.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n " + Name + "\n"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("[ 55 ] ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
