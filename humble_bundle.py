import time
running = True
fail_cap = 1
fails = 0

while(running):   
    if(exists("1494164103482.png",0)==None): #If button not found
        if(fails<fail_cap):    
            print("Button not found, try scrolling")
            type(Key.PAGE_DOWN)
            fails+=1
        else:
            print("Button not found,  exiting")
            running = False
    else:
        fails = 0
        click("1494164103482.png")
        time.sleep(3)
        type("c",KEY_CTRL)
        click("1494164193607.png")
        time.sleep(0.2)
        click("Games-Steam.jpg")
        time.sleep(0.2)
        click("activate-steam.jpg")
        time.sleep(0.2)
        type(Key.ENTER+Key.ENTER)
        type("v",KEY_CTRL)
        type(Key.ENTER)
        time.sleep(4)
        type(Key.TAB+Key.ENTER)
        click("1494164354780.png")
    
    

    
    
    
    
