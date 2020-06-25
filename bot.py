import pyautogui   # pip3 install pyautogui
import time


def get_data_and_posetion(): 
    """
    use this function to get the telegram text areat position

    return :pos_x  X pos of courser
           :pos_y  Y pos of courser
    """

    print("you have 5 sec to point the courser to telegram input text pos")
    time.sleep(5)
    pos_x,pos_y = pyautogui.position()
    return  pos_x,pos_y





def run():
    """
    this function use get_data_and_position to get palce that bot want to write

    also get the text and count.

    """
    text = input('gimme yor text in english: > ')
    count = input('how many send : > ')
    pos_x,pos_y = get_data_and_posetion() 
    print("bot is started")
    print('')
    for i in range(int(count)):
        # every 50 times wait for 0.4 sec
        if i % 50 == 0:
            time.sleep(.4)
        
        # every relatively count, print a log     
        if i % 10**(len(str(i//10))) == 0:
            remain = int(count) - i 
            print(f"{remain} more to go :D" )

        # do the job here
        # pyautogui.moveTo(pos_x,pos_y) 
        pyautogui.click(pos_x,pos_y) 
        pyautogui.typewrite(text)  
        pyautogui.hotkey("enter")
    
    print('')
    print('im Done!')


if __name__ == "__main__":
    run()
    print('')
    print('_______________________')
    print("> Join: @rabbitix :D")
    print('_______________________')

