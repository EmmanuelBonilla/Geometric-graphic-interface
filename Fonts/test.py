from math import *
from graphics import *
from os import getcwd

def selButton():
    selWin = GraphWin("Select Triangle",240,235)
    
    myPath = getcwd () + "\\"
    bckGrnd = Image(Point(150,200), myPath + "BackGround.gif")
    aasB = Image(Point(120,34), myPath + "AASB.gif")
    aasR = Image(Point(120,34), myPath + "AASR.gif")
    asaB = Image(Point(120,78), myPath + "ASAB.gif")
    asaR = Image(Point(120,78), myPath + "ASAR.gif")
    sasR = Image(Point(120,122), myPath + "SASR.gif")
    sasB = Image(Point(120,122), myPath + "SASB.gif")
    ssaR = Image(Point(120,166), myPath + "SSAR.gif")
    ssaB = Image(Point(120,166), myPath + "SSAB.gif")
    sssB = Image(Point(120,210), myPath + "SSSB.gif")
    sssR = Image(Point(120,210), myPath + "SSSR.gif")

    bckGrnd.draw(selWin)
    aasB.draw(selWin)
    asaB.draw(selWin)
    ssaB.draw(selWin)
    sasB.draw(selWin)
    sssB.draw(selWin)
                             
##    aaBtn = Rectangle(Point(50,15),Point(190,55))
##    aaBtn.draw(selWin)
##    
##    asaBtn = Rectangle(Point(50,58),Point(190,98))
##    asaBtn.draw(selWin)
##    
##    ssaBtn = Rectangle(Point(54,102),Point(186,142))
##    ssaBtn.draw(selWin)
##    
##    sasBtn = Rectangle(Point(54,146),Point(186,186))
##    sasBtn.draw(selWin)
##    
##    sssBtn = Rectangle(Point(58,190),Point(181,230))
##    sssBtn.draw(selWin)
    return

selButton()
