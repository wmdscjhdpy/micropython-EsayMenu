# MicroPython menu driver on ssd1306 interfaces
#Code By WMD 2019-4-16 21:18:28
from micropython import const

import ssd1306

class menu:
    def __init__(self,display,x,y,w,h):
        '''
        Init menu bar area in a screen.
        Arg display is the ssd1306 object
        X and y is the start point of the screen
        w and h set the width and height of the menu.
        Tips: You can create a menu area which not use all of the screen space,so that you can use remaining area to display other views.
        Warning: This area couldn't bigger than the screen display area
        '''
        self.display=display
        self.hightlightnum=0
        self.menux=x
        self.menuy=y
        self.menuw=w
        self.menuh=h
    def initText(self,TextList,offset=0,hightlightnum=0):
        '''
        Init menuText in menu bar.
        this function will refresh menu area to new TextList
        arg TextList should be a list. The first element is the text to display, and the second element is 
        arg offset is use to display middle parts of the menu.
        the command.When submenu is needed, the command should be 'initText(theSubTextList)'
        '''
        self.display.fill_rect(self.menux,self.menuy,self.menuw,self.menuh,0) #clear old menu
        self.menuoffset=offset #Save offset value
        self.nowlist=TextList
        for i in range(len(TextList)):
            if (i+1)*10>self.menuh: #Text is out of range
                break
            self.display.text(TextList[i+offset][0],self.menux+1,self.menuy+i*10+1,1)
        self.moveHighLight(hightlightnum)
    def moveHighLight(self,num):
        '''
        Select HightLight num 
        The argument num is relative the manu bar, not equal to Selected element
        '''
        self.display.rect(self.menux, self.menuy+self.hightlightnum*10, self.menuw, 10,0) #clear old rect
        self.hightlightnum=num 
        self.display.rect(self.menux, self.menuy+self.hightlightnum*10, self.menuw, 10,1) #set new rect
    def moveDown(self):
        '''
        User function.
        Make menu downside one element
        '''
        if(self.menuoffset+self.hightlightnum == len(self.nowlist)-1): ## equal to max value
            return
        if (self.hightlightnum+2)*10>self.menuh: #Text is out of range
            self.initText(self.nowlist,self.menuoffset+1,self.hightlightnum) #refresh the Text List
        else:
            self.moveHighLight(self.hightlightnum+1)
    def moveUp(self):
        '''
        User function.
        Make menu upside one element
        '''
        if(self.menuoffset+self.hightlightnum == 0): ## equal to min value
            return
        if self.hightlightnum==0: #Text is out of range
            self.initText(self.nowlist,self.menuoffset+1,self.hightlightnum) #refresh the Text List
        else:
            self.moveHighLight(self.hightlightnum-1)
    def click(self):
        '''
        User function.
        run the selected element command.
        '''
        #if self.nowlist[self.menuoffset+self.hightlightnum][1][0]=='@': #this point to another menu
        #    tmp=self.nowlist[self.menuoffset+self.hightlightnum][1].lstrip('@')
        #    self.initText() 
        eval(self.nowlist[self.menuoffset+self.hightlightnum][1])
    def clickSpecial(self):
        '''
        User function.
        run the selected element command.
        it can be use like a "long press"
        '''
        if self.nowlist[self.menuoffset+self.hightlightnum][2] is True:
            eval(self.nowlist[self.menuoffset+self.hightlightnum][2])
