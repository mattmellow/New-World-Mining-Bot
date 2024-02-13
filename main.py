import pyautogui
import pydirectinput
import time
import random
import mss as mss
import numpy as np
from PIL import Image
import gc
import cv2
import os
from split_image import split_image
import math
from pytesseract import pytesseract


#global variables
    #Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
    #screen capture areas
with mss.mss() as sct:
    # The screen part to capture
    mon_cords={"top": 20, "left": 1645, "width": 270, "height": 13}
    bag={"top":946, "left":1388, "width":2, "height":2}
    e_screen={"top":0, "left":0, "width":1920, "height":1080}
    #resource paths
iron_path=[[8419,2328],[8451,2257],[8419,2191],[8385,2168],[8346,2199],[8270,2198],[8269,2194],[8200,2191],[8267,2156],[8278,2133],[8303,2128],[8273,2072],[8269,2068],[8344,2068],[8383,2127],[8496,2069],[8533,2002],[8571,2069],[8528,2131],[8605,2131],[8635,2073],[8714,2065],[8791,2064],[8750,2001],[8825,1999],[8760,2164],[8603,2243],[8497,2312]]
storage_to_iron=[[9287,2685],[9272.8,2700],[9253,2700],[9240,2679],[9237,2667],[9099,2673],[9080.3,2688.4],[8989,2687],[8950,2666],[8943,2638],[8918,2616],[8875,2614],[8813.6,2641],[8777.7,2632],[8718,2595],[8584,2589],[8532,2521],[8548,2516],[8549,2454],[8551,2362]]
    #text recognition
tuple_0=((255,255,197),(255,255,198),(255,255,199),(255,255,200),(255,255,201),(255,255,202),(255,255,203))
tuple_2=((255,255,197),(255,255,198),(255,255,199),(255,255,200),(255,255,201),(255,255,202),(255,255,203))
tuple_3_top=((250,250,192),(250,250,193),(250,250,194),(250,250,195),(250,250,196),(250,251,192),(250,251,193),(250,251,194),(250,251,195),(250,251,196),(250,252,192),(250,252,193),(250,252,194),(250,252,195),(250,252,196),(251,250,192),(251,250,193),(251,250,194),(251,250,195),(251,250,196),(251,251,192),(251,251,193),(251,251,194),(251,251,195),(251,251,196),(251,252,192),(251,252,193),(251,252,194),(251,252,195),(251,252,196),(252,250,192),(252,250,193),(252,250,194),(252,250,195),(252,250,196),(252,251,192),(252,251,193),(252,251,194),(252,251,195),(252,251,196),(252,252,192),(252,252,193),(252,252,194),(252,252,195),(252,252,196))
tuple_3_bot=((255,255,197),(255,255,198),(255,255,199),(255,255,200),(255,255,201),(255,255,202),(255,255,203))
tuple_6_top=((251,251,194),(251,251,195),(251,251,196),(251,251,197),(251,251,198),(251,251,199),(251,251,200),(251,251,201),(251,251,202),(251,251,203),(251,251,204),(251,252,194),(251,252,195),(251,252,196),(251,252,197),(251,252,198),(251,252,199),(251,252,200),(251,252,201),(251,252,202),(251,252,203),(251,252,204),(251,253,194),(251,253,195),(251,253,196),(251,253,197),(251,253,198),(251,253,199),(251,253,200),(251,253,201),(251,253,202),(251,253,203),(251,253,204),(251,254,194),(251,254,195),(251,254,196),(251,254,197),(251,254,198),(251,254,199),(251,254,200),(251,254,201),(251,254,202),(251,254,203),(251,254,204),(251,255,194),(251,255,195),(251,255,196),(251,255,197),(251,255,198),(251,255,199),(251,255,200),(251,255,201),(251,255,202),(251,255,203),(251,255,204),(252,251,194),(252,251,195),(252,251,196),(252,251,197),(252,251,198),(252,251,199),(252,251,200),(252,251,201),(252,251,202),(252,251,203),(252,251,204),(252,252,194),(252,252,195),(252,252,196),(252,252,197),(252,252,198),(252,252,199),(252,252,200),(252,252,201),(252,252,202),(252,252,203),(252,252,204),(252,253,194),(252,253,195),(252,253,196),(252,253,197),(252,253,198),(252,253,199),(252,253,200),(252,253,201),(252,253,202),(252,253,203),(252,253,204),(252,254,194),(252,254,195),(252,254,196),(252,254,197),(252,254,198),(252,254,199),(252,254,200),(252,254,201),(252,254,202),(252,254,203),(252,254,204),(252,255,194),(252,255,195),(252,255,196),(252,255,197),(252,255,198),(252,255,199),(252,255,200),(252,255,201),(252,255,202),(252,255,203),(252,255,204),(253,251,194),(253,251,195),(253,251,196),(253,251,197),(253,251,198),(253,251,199),(253,251,200),(253,251,201),(253,251,202),(253,251,203),(253,251,204),(253,252,194),(253,252,195),(253,252,196),(253,252,197),(253,252,198),(253,252,199),(253,252,200),(253,252,201),(253,252,202),(253,252,203),(253,252,204),(253,253,194),(253,253,195),(253,253,196),(253,253,197),(253,253,198),(253,253,199),(253,253,200),(253,253,201),(253,253,202),(253,253,203),(253,253,204),(253,254,194),(253,254,195),(253,254,196),(253,254,197),(253,254,198),(253,254,199),(253,254,200),(253,254,201),(253,254,202),(253,254,203),(253,254,204),(253,255,194),(253,255,195),(253,255,196),(253,255,197),(253,255,198),(253,255,199),(253,255,200),(253,255,201),(253,255,202),(253,255,203),(253,255,204),(254,251,194),(254,251,195),(254,251,196),(254,251,197),(254,251,198),(254,251,199),(254,251,200),(254,251,201),(254,251,202),(254,251,203),(254,251,204),(254,252,194),(254,252,195),(254,252,196),(254,252,197),(254,252,198),(254,252,199),(254,252,200),(254,252,201),(254,252,202),(254,252,203),(254,252,204),(254,253,194),(254,253,195),(254,253,196),(254,253,197),(254,253,198),(254,253,199),(254,253,200),(254,253,201),(254,253,202),(254,253,203),(254,253,204),(254,254,194),(254,254,195),(254,254,196),(254,254,197),(254,254,198),(254,254,199),(254,254,200),(254,254,201),(254,254,202),(254,254,203),(254,254,204),(254,255,194),(254,255,195),(254,255,196),(254,255,197),(254,255,198),(254,255,199),(254,255,200),(254,255,201),(254,255,202),(254,255,203),(254,255,204),(255,251,194),(255,251,195),(255,251,196),(255,251,197),(255,251,198),(255,251,199),(255,251,200),(255,251,201),(255,251,202),(255,251,203),(255,251,204),(255,252,194),(255,252,195),(255,252,196),(255,252,197),(255,252,198),(255,252,199),(255,252,200),(255,252,201),(255,252,202),(255,252,203),(255,252,204),(255,253,194),(255,253,195),(255,253,196),(255,253,197),(255,253,198),(255,253,199),(255,253,200),(255,253,201),(255,253,202),(255,253,203),(255,253,204),(255,254,194),(255,254,195),(255,254,196),(255,254,197),(255,254,198),(255,254,199),(255,254,200),(255,254,201),(255,254,202),(255,254,203),(255,254,204),(255,255,194),(255,255,195),(255,255,196),(255,255,197),(255,255,198),(255,255,199),(255,255,200),(255,255,201),(255,255,202),(255,255,203),(255,255,204))
tuple_6_bot=((255,255,198),(255,255,199),(255,255,200),(255,255,201),(255,255,202))
tuple_7=((255,255,201),(255,255,199),(255,255,200))
tuple_8=((254,254,196),(255,255,198),(255,255,199),(255,255,200),(255,255,201),(255,255,202))
tuple_9=((255,255,201),(255,255,199),(255,255,200))

def stop_automove():
    cords=get_cords()
    time.sleep(0.1)
    if not abs(cords[0]-get_cords()[0])<=0.05 and abs(cords[1]-get_cords()[1])<=0.05:
        pydirectinput.press("=")
    return()

#new
def check_bag():
    sct_img_bag=sct.grab(bag)
    img_bag=Image.frombytes('RGB', (sct_img_bag.size.width, sct_img_bag.size.height), sct_img_bag.rgb)
    mss.tools.to_png(sct_img_bag.rgb, sct_img_bag.size, output="bag.png")
    im = Image.open("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\bag.png")
    piq = im.load()
    bag_pixels={}
    for g in range(2):
        for l in range(2):
            bag_pixels["{},{}".format(g,l)]=piq[g,l]
    if bag_pixels["0,0"]==(255,255,255) and bag_pixels["0,1"]==(255,255,255) and bag_pixels["1,0"]==(255,255,255) and bag_pixels["1,1"]==(255,255,255):
        return(True)
    else:
        return(False)

def collect():
    e_pressed=False
    im = pyautogui.screenshot()
    e_pixels=str(pyautogui.locate("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\e_mark.png", im, grayscale=True, confidence=.7))
    num="0123456789"
    listx=[]
    text=""
    if e_pixels is not None:
        for char in e_pixels:
            if char=="," or char==")":
                listx.append(text)
                text=""
            elif char in num:
                text+=char
        if listx!=[]:
            im = pyautogui.screenshot(region=(int(listx[0])+47,int(listx[1]), 85, 24))
            e_text = str(pytesseract.image_to_string(im))
            print(e_text)
            if "OU" not in e_text:
                pydirectinput.press("e")
                e_pressed=True
    while(check_pork()==False):
        time.sleep(0.1)
    return(e_pressed)


def check_pork():
    im = pyautogui.screenshot(region=(1719,797,50,50))
    im.save("cockpork.png")
    pic = im.load()
    pork_pixels={}
    for w in range(4):
        for h in range(3):
            pork_pixels["{},{}".format(w,h)]=pic[w,h]
    if pork_pixels["0,0"]==(255,255,255) and pork_pixels["3,2"]==(255,255,255):
        return(True)
    else:
        return(False)


def start():
    # find and select new world window
    newWorldWindows = pyautogui.getWindowsWithTitle("New World")
    for window in newWorldWindows:
        if window.title == "New World":
            newWorldWindow = window
            break
    newWorldWindow.activate()
    centerW = newWorldWindow.left + (newWorldWindow.width/2)
    centerH = newWorldWindow.top + (newWorldWindow.height/2)
    pyautogui.moveTo(centerW, centerH)
    time.sleep(.1)
    return()

def get_cords():
    sct_img_cords=sct.grab(mon_cords)
    img_cords = Image.frombytes('RGB', (sct_img_cords.size.width, sct_img_cords.size.height), sct_img_cords.rgb)
    mss.tools.to_png(sct_img_cords.rgb, sct_img_cords.size, output="sct-0x0_1920x1080.png")
    split_image("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\sct-0x0_1920x1080.png", 30, 1, False, False, True)
    all_pixel_dict={}
    cords_str=""
    counter=0
    for i in range(30):
        im = Image.open("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\sct-0x0_1920x1080_{}.png".format(i))
        pix = im.load()
        for x in range(9):
            for y in range(13):
                all_pixel_dict["{},{}".format(x,y)]=pix[x,y] 
        if all_pixel_dict["4,1"] == (255,255,201) and all_pixel_dict["4,2"] == (255,255,201) and all_pixel_dict["4,3"] == (255,255,201) and all_pixel_dict["4,4"] == (255,255,201) and all_pixel_dict["4,5"] == (255,255,201) and all_pixel_dict["4,6"] == (255,255,201) and all_pixel_dict["4,7"] == (255,255,201) and all_pixel_dict["4,8"] == (255,255,201) and all_pixel_dict["4,9"] == (255,255,201) and all_pixel_dict["4,10"] == (255,255,201) and all_pixel_dict["4,11"] == (255,255,201) and all_pixel_dict["4,12"] == (255,255,201) and all_pixel_dict["5,12"] == (255,255,201) and all_pixel_dict["5,1"] == (255,255,201):
            char="["
        elif all_pixel_dict["4,1"] == (255,255,201) and all_pixel_dict["4,2"] == (255,255,201) and all_pixel_dict["4,3"] == (255,255,201) and all_pixel_dict["4,4"] == (255,255,201) and all_pixel_dict["4,5"] == (255,255,201) and all_pixel_dict["4,6"] == (255,255,201) and all_pixel_dict["4,7"] == (255,255,201) and all_pixel_dict["4,8"] == (255,255,201) and all_pixel_dict["4,9"] == (255,255,201) and all_pixel_dict["4,10"] == (255,255,201) and all_pixel_dict["4,11"] == (255,255,201) and all_pixel_dict["4,12"] == (255,255,201) and all_pixel_dict["3,12"] == (255,255,201) and all_pixel_dict["3,1"] == (255,255,201):
            char="]"
        elif all_pixel_dict["4,2"] == (255,255,201) and all_pixel_dict["4,3"] == (255,255,201) and all_pixel_dict["4,4"] == (255,255,201) and all_pixel_dict["4,5"] == (255,255,201) and all_pixel_dict["4,6"] == (255,255,201) and all_pixel_dict["4,7"] == (255,255,201) and all_pixel_dict["4,8"] == (255,255,201) and all_pixel_dict["4,9"] == (255,255,201) and all_pixel_dict["4,10"] == (255,255,201):
            char="1"
        elif all_pixel_dict["6,2"] == (255,255,201) and all_pixel_dict["6,3"] == (255,255,201) and all_pixel_dict["6,4"] == (255,255,201) and all_pixel_dict["6,5"] == (255,255,201) and all_pixel_dict["6,6"] == (255,255,201) and all_pixel_dict["6,7"] == (255,255,201) and all_pixel_dict["6,8"] == (255,255,201) and all_pixel_dict["6,9"] == (255,255,201) and all_pixel_dict["6,10"] == (255,255,201):
            char="4"
        elif all_pixel_dict["2,2"] == (255,255,201) and all_pixel_dict["2,3"] == (255,255,201) and all_pixel_dict["2,4"] == (255,255,201) and all_pixel_dict["2,5"] == (255,255,201):
            char="5"
        elif all_pixel_dict["2,3"] in tuple_0 and all_pixel_dict["4,6"] in tuple_0 and all_pixel_dict["7,6"] in tuple_0:
            char="0"
        elif all_pixel_dict["7,4"] in tuple_2 and all_pixel_dict["4,8"] in tuple_2:
            char="2"
        elif all_pixel_dict["7,3"] in tuple_3_top and all_pixel_dict["7,8"] in tuple_3_bot:
            char="3"
        elif all_pixel_dict["4,5"] in tuple_6_top and all_pixel_dict["7,8"] in tuple_6_bot:
            char="6"
        elif all_pixel_dict["7,3"] in tuple_8 and all_pixel_dict["7,8"] in tuple_8:
            char="8"
        elif all_pixel_dict["7,6"] in tuple_9 and all_pixel_dict["4,7"] in tuple_9:
            char="9"
        elif all_pixel_dict["4,8"] in tuple_7:
            char="7"
        elif all_pixel_dict["4,10"]==(255,255,201):
            counter+=1
            if counter%2==1:
                char="."
            else:
                char=","
        else:
            char=""
        cords_str+=char
    list=cords_str.split(",")
    cords=[float(list[0][1:]),float(list[1])]
    assert(len(str(int(cords[0])))==4)
    return(cords)

def turn(direction):
    pydirectinput.move(int(direction*100),0,relative=True)
    return()


def travel(next):
    cords=get_cords()
    diff_x=next[0]-cords[0]
    diff_y=next[1]-cords[1]
    if diff_x==0:
        if diff_y>0:
            compass_need=0
        elif diff_y<0:
            compass_need=180
    elif diff_y==0:
        if diff_x>0:
            compass_need=90
        elif diff_x<0:
            compass_need=270
    else:
        angle=math.atan(abs(diff_x/diff_y))
        angle=angle*180/math.pi
        if diff_x>0 and diff_y>0:
            compass_need=angle
        if diff_x>0 and diff_y<0:
            compass_need=180-angle
        if diff_x<0 and diff_y<0:
            compass_need=180+angle
        if diff_x<0 and diff_y>0:
            compass_need=360-angle
    turn(compass_need)
    time.sleep(0.1)
    pydirectinput.press("=")
    counter=0
    while abs(diff_x)>1.2 and abs(diff_y)>1.2:
        if abs(cords[0]-get_cords()[0])<=0.05 and abs(cords[1]-get_cords()[1])<=0.05:
            counter+=1
            if counter==10 or counter==9:
                pydirectinput.press("d",5,0.2)
            if counter==15:
                cords=get_cords()
                time.sleep(0.2)
                if not cords==get_cords():
                    pydirectinput.press("=")
                turn(120)
                time.sleep(0.2)
                pydirectinput.press("=")
                time.sleep(2)
                pydirectinput.press("=")
                turn(240)
                travel(next)
            pydirectinput.press("=")
            pydirectinput.press(" ")
        cords=get_cords()
        diff_x=next[0]-cords[0]
        diff_y=next[1]-cords[1]
    time.sleep(0.1)
    pydirectinput.press("=")
    time.sleep(0.1)
    turn(360-compass_need)


def empty_to_storage():
    travel([9287,2685])
    sct_img_e_screen=sct.grab(e_screen)
    img_e_screen=Image.frombytes('RGB', (sct_img_e_screen.size.width, sct_img_e_screen.size.height), sct_img_e_screen.rgb)
    mss.tools.to_png(sct_img_e_screen.rgb, sct_img_e_screen.size, output="e_screen.png")
    im = Image.open("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\e_screen.png")
    while pyautogui.locate("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\e_mark.png", "C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\e_screen.png", grayscale=True, confidence=.8) == None:
        sct_img_e_screen=sct.grab(e_screen)
        img_e_screen=Image.frombytes('RGB', (sct_img_e_screen.size.width, sct_img_e_screen.size.height), sct_img_e_screen.rgb)
        mss.tools.to_png(sct_img_e_screen.rgb, sct_img_e_screen.size, output="e_screen.png")
        im = Image.open("C:\\Users\\Matthew\\Desktop\\GRANDFINALE\\e_screen.png")
        travel([9287,2685])
    pydirectinput.press("e")
    time.sleep(0.2)
    pydirectinput.moveTo(942,192)
    pydirectinput.click(0,0,10,0.2)
    pydirectinput.moveTo(1230,189)
    pydirectinput.click(0,0,10,0.2)
    time.sleep(0.1)
    pydirectinput.press("esc")
    return()

def scan():
    for i in range(9):
        pydirectinput.move(40*100,0,relative=True)
        collect()
    pydirectinput.move(180*100,0,relative=True)
    pydirectinput.press("=")
    time.sleep(1.1)
    pydirectinput.press("=")
    pydirectinput.move(90*100,0,relative=True)
    for i in range(9):
        pydirectinput.move(40*100,0,relative=True)
        collect()
    pydirectinput.move(180*100,0,relative=True)
    pydirectinput.press("=")
    time.sleep(1.1)
    pydirectinput.press("=")
    for i in range(9):
        pydirectinput.move(40*100,0,relative=True)
        collect()
    pydirectinput.move(270*100,0,relative=True)
    pydirectinput.press("=")
    time.sleep(2)
    pydirectinput.press("=")
    for i in range(9):
        pydirectinput.move(40*100,0,relative=True)
        collect()
    pydirectinput.move(270*100,0,relative=True)
    pydirectinput.press("=")
    time.sleep(2)
    pydirectinput.press("=")
    for i in range(9):
        pydirectinput.move(40*100,0,relative=True)
        collect()
    pydirectinput.move(90*100,0,relative=True)
    return()

start()
cords=get_cords()
time.sleep(5)
while check_bag()==False:
    for i in storage_to_iron:
        travel(i)
    while check_bag()==False:
        for i in iron_path:
            travel(i)
            if check_bag()==False:
                scan()
    for i in storage_to_iron[::-1]:    
        travel(i)
    empty_to_storage()

