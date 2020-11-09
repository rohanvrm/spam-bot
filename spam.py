
#Run this program and click where you want to type
import time, pyautogui, random
from RandomWordGenerator import RandomWord
time.sleep(5)
wrd = ("henlo","yems","good morning")

#f=open("sp.txt", 'r')
#for word in f:  
for i in range(100):
  time.sleep(3)
  #for random words of 5 alphabets
  word = RandomWord(max_word_size=5,constant_word_size=False)
  pyautogui.typewrite(word.generate())
  pyautogui.press("enter")
  word2 = random.choice(wrd)  
  time.sleep(1)
  pyautogui.typewrite(word2)
  pyautogui.press("enter")