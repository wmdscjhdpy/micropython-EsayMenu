from ssd1306 import SSD1306_I2C
from machine import I2C
import menu
oled_iic=I2C(scl='B15',sda='D9') #edit to your IIC OLED Pin
oled=SSD1306_I2C(128,64,oled_iic) #edit to your IIC OLED DPI
oled.fill(0xff)
text=[['music','print("perform a music")'],['photo','m.initText(subtext)','print("Special click detacted")'],['game','a']]
subtext=[['back','m.initText(text)'],['see photo a','a']]
m=menu.menu(oled,0,0,128,64)
m.initText(text) # main menu
oled.show()
