import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import ttk
from tkinter import font

from bs4 import BeautifulSoup
import requests

# ------------------------------------------------- #
def callback(url):
    webbrowser.open_new(url)

def get_article_newsmax():
  source = requests.get("https://www.newsmax.com/politics/").text
  soup = BeautifulSoup(source, 'html.parser')
  articles = soup.findAll("li", {"class" : "article_link"})
  
  count = 1
  for article in articles:
    headline = article.a.text
    desc = article.div.text

    formatted_headline = str(count) + ". " + headline
    formatted_desc = desc + '\n\n'

    label = tk.Label(myframe1, text=formatted_headline, font=('Arial Greek', 16, 'bold'), wraplength=0.37*root.winfo_screenwidth(), anchor="nw").pack()  
    label = tk.Label(myframe1, text=formatted_desc, font=('Arial Greek', 15), wraplength=0.37*root.winfo_screenwidth(), anchor="nw", justify="left").pack()

    count += 1

def get_article_nytimes():
  source = requests.get("https://www.nytimes.com/section/politics").text
  soup = BeautifulSoup(source, 'html.parser')
  
  count = 1

  highlights = soup.findAll("section", {"id": "collection-highlights-container"})[0].findAll("ol")
  highlights1 = highlights[0].findAll("li")
  highlights2 = highlights[1].findAll("li")

  for highlight in highlights1:
    headline = highlight.h2.text
    desc = highlight.p.text

    formatted_headline = str(count) + ". " + headline
    formatted_desc = desc + '\n\n'

    label = tk.Label(myframe2, text=formatted_headline, font=('Arial Greek', 16, 'bold'), wraplength=0.37*root.winfo_screenwidth(), anchor="nw").pack()  
    label = tk.Label(myframe2, text=formatted_desc, font=('Arial Greek', 15), wraplength=0.37*root.winfo_screenwidth(), anchor="nw", justify="left").pack()

    count += 1

  for highlight in highlights2:
    headline = highlight.h2.text
    desc = highlight.p.text

    formatted_headline = str(count) + ". " + headline
    formatted_desc = desc + '\n\n'

    label = tk.Label(myframe2, text=formatted_headline, font=('Arial Greek', 16, 'bold'), wraplength=0.37*root.winfo_screenwidth(), anchor="nw").pack()  
    label = tk.Label(myframe2, text=formatted_desc, font=('Arial Greek', 15), wraplength=0.37*root.winfo_screenwidth(), anchor="nw", justify="left").pack()

    count += 1

  stream_panels = soup.findAll("section", {"id" : "stream-panel"})[0].ol.findAll("li")
  for article in stream_panels:
    headline = article.h2.text
    desc = article.p.text

    formatted_headline = str(count) + ". " + headline
    formatted_desc = desc + '\n\n'

    label = tk.Label(myframe2, text=formatted_headline, font=('Arial Greek', 16, 'bold'), wraplength=0.37*root.winfo_screenwidth(), anchor="nw").pack()   
    label = tk.Label(myframe2, text=formatted_desc, font=('Arial Greek', 15), wraplength=0.37*root.winfo_screenwidth(), anchor="nw", justify="left").pack()

    count += 1


# ------------------------------------------ #  

root = tk.Tk()
root.title("Politics News")
root.configure(background='black')
root.state('zoomed')

# Newsmax - New York Times #
names = tk.Frame(root, bg='#80c1ff', bd=5)
names.place(relx = 0.5, rely = 0.05, relwidth = 0.85, relheight = 0.05, anchor = 'n')

button = tk.Button(names, text = "Newsmax", font=('Lucida Bright', 22, 'bold'), bg="blue", fg="white")
button.place(relx = 0, relheight = 1, relwidth = 0.47)

button = tk.Button(names, text = "New York Times", font=('Lucida Bright', 22, 'bold'), bg="red", fg="white")
button.place(relx = 0.53, relheight = 1, relwidth = 0.47)

# --- LEFT FRAME --- #

left_frame = tk.Frame(root, bg='#80c1ff', bd=10)
left_frame.place(relx = 0.275, rely = 0.15, relwidth = 0.40, relheight = 0.8, anchor = 'n')

readmore1 = tk.Label(left_frame, text="Read More", fg="blue", cursor="hand2", font=('Courier', 14))
readmore1.pack()
readmore1.bind("<Button-1>", lambda e: callback("https://www.newsmax.com/politics/"))

# Scrollable #
wrapper1 = LabelFrame(left_frame)

mycanvas1 = Canvas(wrapper1)
mycanvas1.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=mycanvas1.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas1.configure(yscrollcommand=yscrollbar.set)

mycanvas1.bind('<Configure>', lambda e: mycanvas1.configure(scrollregion = mycanvas1.bbox('all')))

myframe1 = Frame(mycanvas1)
mycanvas1.create_window((0,0), window=myframe1, anchor="nw")

wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)

# Get the contents #
get_article_newsmax()

# --- RIGHT FRAME --- #

right_frame = tk.Frame(root, bg='#80c1ff', bd=10)
right_frame.place(relx = 0.725, rely = 0.15, relwidth = 0.40, relheight = 0.8, anchor = 'n')

readmore2 = tk.Label(right_frame, text="Read More", fg="blue", cursor="hand2", font=('Courier', 14))
readmore2.pack()
readmore2.bind("<Button-1>", lambda e: callback("https://www.nytimes.com/section/politics"))

# Scrollable #
wrapper2 = LabelFrame(right_frame)

mycanvas2 = Canvas(wrapper2)
mycanvas2.pack(side=LEFT, fill="both", expand="yes")

yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas2.yview)
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas2.configure(yscrollcommand=yscrollbar.set)

mycanvas2.bind('<Configure>', lambda e: mycanvas2.configure(scrollregion = mycanvas2.bbox('all')))

myframe2 = Frame(mycanvas2)
mycanvas2.create_window((0,0), window=myframe2, anchor="nw")

wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

# Get the contents #
get_article_nytimes()

# Run #
root.mainloop()