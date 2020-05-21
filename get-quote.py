#import random
def primary():
 #  print("Keep it logically awesome.")

  f = open("quotes.txt","a")
  f.write("I am learnig Paython \n")
  f.close
  f=open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=len(quotes)-1
  #rnd = random.randint(0, last)
  print(quotes[0],quotes[last])

if __name__== "__main__":
  primary()
