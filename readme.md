**Note: this repo is developing**

# Micropython Easy Menu

![view](Doc/profilephoto.png)
![view2](Doc/profilephoto2.png)
##usage

** simple example is update. You can see it in the repo

1. init a menu object
```python
m=menu.menu(ssd1306object,0,0,128,64)
```
2. init a menu text list, The first element is the text to display, and the second element is arg offset is use to display middle parts of the menu.
```python
menutext=[['menuText1','print("this is the menuText1")'],['menuText2','print("this is the menuText2")']]
m.initText(menutext)
```
3. When your Device detects  Events, use `m.moveUp()`,`m.moveDown()`,`m.click()` or `m.clickSpecial()` to control menu bar.