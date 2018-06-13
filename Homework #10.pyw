#-------------------------------------------------------------------
# Emmanuel Bonilla  
# Washington State University, Tri-Cities
# CptS111: Introduction to Algorithmic Problem Solving
# Summer 2016: Homework 10
# System: Python v3.5.1 IDLE (MS Windows OS)
#-------------------------------------------------------------------

from math import *
from graphics import *
from os import getcwd

#Purpose: set the minimum and maximum values of the rectangle
#Parameters: Pt must be real numbers only
#Return: value of inFlage, True or False
def pt_in_rect(Pt, Rect):
    X1 = min(Rect.getP1().getX(), Rect.getP2().getX())
    X2 = max(Rect.getP1().getX(), Rect.getP2().getX())
    Y1 = min(Rect.getP1().getY(), Rect.getP2().getY())
    Y2 = max(Rect.getP1().getY(), Rect.getP2().getY())
    inFlag = (Pt.getX() >= X1 and Pt.getX() <= X2 and Pt.getY() >= Y1 and Pt.getY() <= Y2)
    return inFlag

#Purpose: To get the area of a side, side, side Triangle
#Parameters:tsl = triangle side list, sp = semi perimeter
#Return: Triangle Area 
def sssTri_Area(tsl):
    sp = (tsl[0] + tsl[1] + tsl[2]) / 2
    triArea = sqrt(sp * (sp - tsl[0]) * (sp - tsl[1]) * (sp - tsl[2]))
    return triArea

#Purpose:To get the angles of a side, side, side Triangle
#Parameters: Triangle Side 1 must be real numbers only
#Return: Triangle angles
def sssTri_Angles(tsl):
    angA = degrees(acos((tsl[1] ** 2 + tsl[2] ** 2 - tsl[0] ** 2) / (2 * tsl[1] * tsl[2])))
    angB = degrees(acos((tsl[0] ** 2 + tsl[2] ** 2 - tsl[1] ** 2) / (2 * tsl[0] * tsl[2])))
    angC = degrees(acos((tsl[0] ** 2 + tsl[1] ** 2 - tsl[2] ** 2) / (2 * tsl[0] * tsl[1])))
    triAngles = [angA, angB, angC]
    return triAngles

#purpose: Find trianlge side B
#parameters: Expect only positive integers, inputs seperated by commas, angle input in degrees
#return: Side B of a triangle  
def sasTriSideB(sideA, angleB, sideC):
    sideB = -1
    try:
        if sideA > 0 and angleB > 0 and sideC > 0:
            sideB = sqrt(sideA ** 2 + sideC ** 2 - 2 * sideA * sideC * cos(radians(angleB)))
    except:
        sideB = -1

    return sideB

# Purpose: Open new window with error message
# Parameter: error messages catched, File directory/location
# Return: Nothing
def errorWin(msgTxt, thePath):
    errorWin = GraphWin('Problem', 400, 150)
    Image(Point(0,0), thePath + 'okaybtn.gif').draw(errorWin)

    theTxt = Text(Point(200, 35), msgTxt)
    theTxt.setStyle('bold')
    theTxt.setTextColor('white')
    theTxt.draw(errorWin)

    try:
        errorWin.getMouse()
    except:
        pass

    errorWin.close()
    return

#Purpose: set the minimum and maximum values of the rectangle
#Parameters: Pt must be real numbers only
#Return: value of inFlage, True or False
def pt_in_rect(Pt, Rect):
    inFlag = False
    X1 = min(Rect.getP1().getX(),Rect.getP2().getX())
    X2 = max(Rect.getP1().getX(),Rect.getP2().getX())
    Y1 = min(Rect.getP1().getY(),Rect.getP2().getY())
    Y2 = max(Rect.getP1().getY(),Rect.getP2().getY())

    if Pt.getX() >= X1 and Pt.getX() <= X2 and Pt.getY() >= Y1 and Pt.getY() <= Y2:
        inFlag = True

    return inFlag

#Purpose: Format the Txt of the headers
#Parameters: values must be separated by commas in extact way
#Return: formated txt for display
def txtFrmt(Xcrd,Ycrd,Txt,Font,Size,Styl):
    """Xcrd,Ycrd,Txt,Font,Size,Styl"""
    txt = Text(Point(Xcrd,Ycrd),Txt)
    txt.setFace(Font)
    txt.setStyle(Styl)
    txt.setTextColor('white')
    txt.setSize(Size)
    return txt

#Purpose: Format the entry header
#Parameters: values must be separated by commas in extact way
#Return: formated entry box 
def entryFrmt(Xcrd,Ycrd,Font,stle,txt,color):
    '''Xcrd,Ycrd,Font,stle,txt,color'''
    entry = Entry(Point(Xcrd, Ycrd),Font)
    entry.setStyle(stle)
    entry.setText(txt)
    entry.setFill(color)
    return entry

def main():
    myPath = getcwd() + '\\Fonts\\' # Subdirectory for picture files
    fileExt = '.gif'  # Text file extension
    myFrmt = '{0:5.1f}'
    lblTriTypeLst = ['Angle,Angle,Side', 'Angle,Side,Angle', 'Side,Side,Angle', 'Side,Angle,Side', 'Side,Side,Side']

    AAS, ASA, SSA, SAS, SSS = 0, 1, 2, 3, 4
    sideMax = 1000 # Client specified upper limit on length
    
    triWin = GraphWin("Cpts111 - HW10", 550, 550)
    Image(Point(275, 275), myPath + "triBckGrnd" + fileExt).draw(triWin)
    
    calcBtn = Rectangle(Point(40,500),Point(175,535))
    clrBtn = Rectangle(Point(210,500),Point(338,535))
    quitBtn = Rectangle(Point(380,500),Point(500,535))

    menuWin = GraphWin('Triangle Select', 240, 270)
    Image(Point(275, 275), myPath + "BackGround" + fileExt).draw(menuWin)
    menuBtnA = []
    menuBtnB = []
    menuBtnRect = []
    
    for slct in range(5):
        menuBtnA.append(Image(Point(120, 27 + slct * 54), myPath + 'select' + str(slct) + 'b.gif'))
        menuBtnA[slct].draw(menuWin)
        menuBtnB.append(Image(Point(120, 27 + slct * 54), myPath + 'select' + str(slct) + 'r.gif'))
        menuBtnRect.append(Rectangle(Point(0, slct * 54), Point(330, 54 + slct * 54)))

    triType = SSS
    titleTxt = Text(Point(125, 40), 'Triangle: \n' + lblTriTypeLst[triType])
    titleTxt.setTextColor('white')
    titleTxt.setStyle('bold')
    titleTxt.setSize(16)
    titleTxt.setFace('arial')
    titleTxt.draw(triWin)

    lblSA = txtFrmt(160,205,'A','arial',16,'bold')
    lblSB = txtFrmt(325,325,'B','arial',14,'bold')
    lblSC = txtFrmt(440,105,'C','arial',14,'bold')
    lblAA = txtFrmt(460,185,'a','arial',14,'bold')
    lblAB = txtFrmt(310,105,'b','arial',14,'bold')
    lblAC = txtFrmt(125,365,'c','arial',14,'bold')
    lblArea = txtFrmt(305,215,'Area','arial',14,'bold')
    
    dspSA = txtFrmt(160,225,'','courier',12,'bold')
    dspSB = txtFrmt(325,345,'','courier',12,'bold')
    dspSC = txtFrmt(440,130,'','courier',12,'bold')
    dspAA = txtFrmt(460,205,'','courier',12,'bold')
    dspAB = txtFrmt(310,125,'','courier',12,'bold')
    dspAC = txtFrmt(125,385,'','courier',12,'bold')
    dspArea = txtFrmt(305,235,'','courier',14,'bold')

    ueSA = entryFrmt(160,225,6,'bold','','white')
    ueSB = entryFrmt(325,345,6,'bold','','white')
    ueSC = entryFrmt(440,130,6,'bold','','white')
    ueAA = entryFrmt(460,205,6,'bold','','white')
    ueAB = entryFrmt(310,125,6,'bold','','white')

    lblSA.draw(triWin)
    lblSB.draw(triWin)
    lblSC.draw(triWin)
    lblAA.draw(triWin)
    lblAB.draw(triWin)
    lblAC.draw(triWin)
    dspAC.draw(triWin)
    lblArea.draw(triWin)
    dspArea.draw(triWin)
    
    if triType == ASA: 
        dspSA.draw(triWin)
    else:
        ueSA.draw(triWin)

    if triType == SSS: 
        ueSB.draw(triWin)
    else:
        dspSB.draw(triWin)

    if triType == AAS:
        dspSC.draw(triWin)
    else:
        ueSC.draw(triWin)

    if triType == SAS or triType == SSS: 
        dspAA.draw(triWin)
    else:
        ueAA.draw(triWin)

    if triType == SSA or triType == SSS:
        dspAB.draw(triWin) 
    else:
        ueAB.draw(triWin)
        
    loopy = True
    
    while loopy:
        try:
            menuClick = menuWin.checkMouse()
        except:
            loopy = False
        else:
            if not menuClick is None:
                menuBtnClick = -1
                for iBtn in range(5):
                    if pt_in_rect(menuClick, menuBtnRect[iBtn]):
                        menuBtnClick = iBtn

                if menuBtnClick >= 0:
                    menuBtnB[triType].undraw()

                    if triType == ASA:
                        dspSA.undraw()
                    else:
                        ueSA.undraw() 

                    if triType == SSS:
                        ueSB.undraw() 
                    else:
                        dspSB.undraw()

                    if triType == AAS:
                        dspSC.undraw()
                    else:
                        ueSC.undraw()

                    if triType == SAS or triType == SSS:
                        dspAA.undraw()
                    else:
                        ueAA.undraw()

                    if triType == SSA or triType == SSS:
                        dspAB.undraw()
                    else:
                        ueAB.undraw()

                    triType = menuBtnClick
                    menuBtnB[triType].draw(menuWin)

                    ueSA.setText('')
                    ueSB.setText('')
                    ueSC.setText('')
                    ueAA.setText('')
                    ueAB.setText('')
                    dspSA.setText('')
                    dspSB.setText('')
                    dspSC.setText('')
                    dspAA.setText('')
                    dspAB.setText('')
                    dspAC.setText('')
                    dspArea.setText('')
                    titleTxt.setText('Triangle: \n' + lblTriTypeLst[triType])

                    if triType == ASA:
                        dspSA.draw(triWin)
                    else:
                        ueSA.draw(triWin)

                    if triType == SSS:
                        ueSB.draw(triWin)
                    else:
                        dspSB.draw(triWin)

                    if triType == AAS:
                        dspSC.draw(triWin)
                    else:
                        ueSC.draw(triWin)

                    if triType == SAS or triType == SSS:
                        dspAA.draw(triWin)
                    else:
                        ueAA.draw(triWin)

                    if triType == SSA or triType == SSS:
                        dspAB.draw(triWin)
                    else:
                        ueAB.draw(triWin)

        try:
            triClick = triWin.checkMouse()
        except:
            loopy = False
        else:
            if not triClick is None:
                if pt_in_rect(triClick, calcBtn):
                    errorTxt = ''

                    if triType == AAS:
                        tmpAngA = ueAA.getText()
                        tmpAngB = ueAB.getText()
                        tmpSidA = ueSA.getText()

                        try:
                            tmpAngA = abs(round(eval(tmpAngA), 1))
                        except:
                            errorTxt = errorTxt + '\nAngle A entry must be a number'

                        try:
                            tmpAngB = abs(round(eval(tmpAngB), 1))
                        except:
                            errorTxt = errorTxt + '\nAngle B entry must be a number'

                        try:
                            tmpSidA = abs(round(eval(tmpSidA), 1))
                        except:
                            errorTxt = errorTxt + '\nSide A entry must be a number'

                        if not len(errorTxt) and tmpAngA and tmpAngB and tmpSidA and tmpAngA + tmpAngB < 180 and tmpSidA < sideMax:
                            tmpAngC = 180 - (tmpAngA + tmpAngB)
                            
                            sinA = (tmpSidA / sin(radians(tmpAngA)))
                            tmpSidB = sin(radians(tmpAngB)) * sinA
                            tmpSidC = sin(radians(tmpAngC)) * sinA

                            dspAC.setText(myFrmt.format(tmpAngC))
                            dspSB.setText(myFrmt.format(tmpSidB))
                            dspSC.setText(myFrmt.format(tmpSidC))

                            ueAA.setText(myFrmt.format(tmpAngA))
                            ueAB.setText(myFrmt.format(tmpAngB))
                            ueSA.setText(myFrmt.format(tmpSidA))
                        else:
                            dspAC.setText('')
                            dspSB.setText('')
                            dspSC.setText('')
                            errorTxt = errorTxt + '\nNumerical entries not appropriate value'

                    if triType == ASA:
                        tmpAngA = ueAA.getText()
                        tmpAngB = ueAB.getText()
                        tmpSidC = ueSC.getText()

                        try:
                            tmpAngA = abs(round(eval(tmpAngA), 1))
                        except:
                            errorTxt = errorTxt + '\nAngle A entry must be a number'

                        try:
                            tmpAngB = abs(round(eval(tmpAngB), 1))
                        except:
                            errorTxt = errorTxt + '\nAngle B entry must be a number'

                        try:
                            tmpSidC = abs(round(eval(tmpSidC), 1))
                        except:
                            errorTxt = errorTxt + '\nSide C entry must be a number'

                        if not len(errorTxt) and tmpAngA and tmpAngB and tmpSidC and tmpAngA + tmpAngB < 180 and tmpSidC < sideMax:
                            tmpAngC = 180 - (tmpAngA + tmpAngB)

                            sinC = (tmpSidC / sin(radians(tmpAngC)))
                            tmpSidA = sin(radians(tmpAngA)) * sinC
                            tmpSidB = sin(radians(tmpAngB)) * sinC

                            dspAC.setText(myFrmt.format(tmpAngC))
                            dspSA.setText(myFrmt.format(tmpSidA))
                            dspSB.setText(myFrmt.format(tmpSidB))

                            ueAA.setText(myFrmt.format(tmpAngA))
                            ueAB.setText(myFrmt.format(tmpAngB))
                            ueSC.setText(myFrmt.format(tmpSidC))
                        else:
                            dspAC.setText('')
                            dspSA.setText('')
                            dspSB.setText('')
                            errorTxt = errorTxt + '\nNumerical entries not appropriate value'

                    if triType == SSA:
                        tmpAngA = ueAA.getText()
                        tmpSidA = ueSA.getText()
                        tmpSidC = ueSC.getText()

                        try:
                            tmpAngA = abs(round(eval(tmpAngA), 1))
                        except:
                            errorTxt = errorTxt + '\nAngle A entry must be a number'

                        try:
                            tmpSidA = abs(round(eval(tmpSidA), 1))
                        except:
                            errorTxt = errorTxt + '\nSide A entry must be a number'

                        try:
                            tmpSidC = abs(round(eval(tmpSidC), 1))
                        except:
                            errorTxt = errorTxt + '\nSide C entry must be a number'

                        if not len(errorTxt) and tmpAngA and tmpSidA and tmpSidC and tmpAngA < 180 and tmpSidA < sideMax and tmpSidC < sideMax:
                            if sin(radians(tmpAngA)) > tmpSidA / tmpSidC:
                                errorTxt = errorTxt + '\nEntries do not make a legitimate triangle'
                            else:
                                tmpAngC = degrees(acos(tmpSidC * sin(radians(tmpAngA)) / tmpSidA))
                                tmpAngB = 180 - (tmpAngA + tmpAngC)
                                tmpSidB = sasTriSideB(tmpSidA, tmpAngB, tmpSidC)

                                dspAB.setText(myFrmt.format(tmpAngB))
                                dspAC.setText(myFrmt.format(tmpAngC))
                                dspSB.setText(myFrmt.format(tmpSidB))

                                ueAA.setText(myFrmt.format(tmpAngA))
                                ueSA.setText(myFrmt.format(tmpSidA))
                                ueSC.setText(myFrmt.format(tmpSidC))
                        else:
                            dspAB.setText('')
                            dspAC.setText('')
                            dspSB.setText('')
                            errorTxt = errorTxt + '\nNumerical entries not appropriate value'

                    if triType == SAS:
                        tmpAngB = ueAB.getText()
                        tmpSidA = ueSA.getText()
                        tmpSidC = ueSC.getText()

                        try:
                            tmpAngB = abs(round(eval(tmpAngB), 1))
                        except:
                            errorTxt = errorTxt + '\nAngle B entry is not a number'

                        try:
                            tmpSidA = abs(round(eval(tmpSidA), 1))
                        except:
                            errorTxt = errorTxt + '\nSide A entry is not a number'

                        try:
                            tmpSidC = abs(round(eval(tmpSidC), 1))
                        except:
                            errorTxt = errorTxt + '\nSide C entry is not a number'

                        if not len(errorTxt) and tmpAngB and tmpSidA and tmpSidC and tmpAngB < 180 and tmpSidA < sideMax and tmpSidC < sideMax:
                            tmpSidB = sasTriSideB(tmpSidA, tmpAngB, tmpSidC)
                            tmpAngA, tmpThing, tmpAngC = sssTri_Angles([tmpSidA, tmpSidB, tmpSidC])

                            dspAA.setText(myFrmt.format(tmpAngA))
                            dspAC.setText(myFrmt.format(tmpAngC))
                            dspSB.setText(myFrmt.format(tmpSidB))

                            ueAB.setText(myFrmt.format(tmpAngB))
                            ueSA.setText(myFrmt.format(tmpSidA))
                            ueSC.setText(myFrmt.format(tmpSidC))
                        else:
                            dspAA.setText('')
                            dspAC.setText('')
                            dspSB.setText('')
                            errorTxt = errorTxt + '\nNumerical entries not appropriate value'

                    if triType == SSS:
                        tmpSidA = ueSA.getText()
                        tmpSidB = ueSB.getText()
                        tmpSidC = ueSC.getText()

                        try:
                            tmpSidA = abs(round(eval(tmpSidA), 1))
                        except:
                            errorTxt = errorTxt + '\nSide A entry is not a number'

                        try:
                            tmpSidB = abs(round(eval(tmpSidB), 1))
                        except:
                            errorTxt = errorTxt + '\nSide B entry is not a number'

                        try:
                            tmpSidC = abs(round(eval(tmpSidC), 1))
                        except:
                            errorTxt = errorTxt + '\nSide C entry is not a number'

                        if not len(errorTxt) and tmpSidA and tmpSidB and tmpSidC and tmpSidA < sideMax and tmpSidB < sideMax and tmpSidC < sideMax:
                            if not (tmpSidB + tmpSidC > tmpSidA and tmpSidA + tmpSidC > tmpSidB and tmpSidA + tmpSidB > tmpSidC):
                                dspAA.setText('')
                                dspAB.setText('')
                                dspAC.setText('')
                                errorTxt = errorTxt + '\nNumerical entries not appropriate value'
                            else:
                                tmpAngA, tmpAngB, tmpAngC = sssTri_Angles([tmpSidA, tmpSidB, tmpSidC])

                                dspAA.setText(myFrmt.format(tmpAngA))
                                dspAB.setText(myFrmt.format(tmpAngB))
                                dspAC.setText(myFrmt.format(tmpAngC))

                                ueSA.setText(myFrmt.format(tmpSidA))
                                ueSB.setText(myFrmt.format(tmpSidB))
                                ueSC.setText(myFrmt.format(tmpSidC))
                        else:
                            dspAA.setText('')
                            dspAB.setText('')
                            dspAC.setText('')
                            errorTxt = errorTxt + '\nNumerical entries not appropriate value'

                    if len(errorTxt):
                        dspArea.setText('')
                        errorWin(errorTxt, myPath)
                    else:
                        tmpArea = sssTri_Area([tmpSidA, tmpSidB, tmpSidC])
                        dspArea.setText(myFrmt.format(tmpArea))
                    
                if pt_in_rect(triClick, clrBtn):
                    ueSA.setText('')
                    ueSB.setText('')
                    ueSC.setText('')
                    ueAA.setText('')
                    ueAB.setText('')
                    dspSA.setText('')
                    dspSB.setText('')
                    dspSC.setText('')
                    dspAA.setText('')
                    dspAB.setText('')
                    dspAC.setText('')
                    dspArea.setText('')

                if pt_in_rect(triClick, quitBtn):
                    loopy = False
    triWin.close()
    menuWin.close()
    return
main()
