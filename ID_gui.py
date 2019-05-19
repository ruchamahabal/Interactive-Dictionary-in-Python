from tkinter import *
import json
from difflib import get_close_matches

data=json.load(open("data.json","r")) #loading data.json file which consists of all the words and meanings as key,value pairs

#function to return the meaning on clicking the query button
def return_meaning():
    key=e.get()#getting the entry entered by the user
    key=key.lower()
    if key in data:
      result=data[key]
      txt=""
      for item in result:
          txt=txt+"\n"+item
      lbl2.config(text=txt)
    elif key.title() in data:
         result=data[key.title()]
         txt=""
         for item in result:
             txt=txt+"\n"+item
         lbl2.config(text=txt)
    elif len(get_close_matches(key,data.keys(),cutoff=0.8))>0:
        item=get_close_matches(key,data.keys(),cutoff=0.8)[0]
        lbl2.config(text="Did you mean %s instead?"%item)
        y.grid(row=3,column=0)
        n.grid(row=3,column=1)
        y.config(command=corrected_meaning(item))
        n.config(command=corrected_meaning(item))
    else:
        lbl2.config(text="The word doesn't exist. Please double check it.")

#function to return the meaning when the entry is wrong
def corrected_meaning(i):
    key=i
    if v.get()==1:
      result=data[key]
      txt=""
      for item in result:
          txt=txt+"\n"+item
      e.set(key)
      lbl2.config(text=txt)
      y.grid_forget()
      n.grid_forget()
    elif v.get()==2:
        lbl2.config(text="The word doesn't exist. Please double check it.")
        y.grid_forget()
        n.grid_forget()

#function to clear all fields when clear button is clicked
def clear_entry():
        e.set("")
        lbl2.config(text="")
        y.grid_forget()
        n.grid_forget()
        v.set(0)
win=Tk()
win.title("Interactive Dictionary")
win.geometry("500x300")
win.resizable(height=False,width=False)
fr=Frame(win,height=400,width=600,bd=10,bg="black")
fr.pack(expand=True,fill=BOTH)
v=IntVar()
lbl=Label(fr,text="Enter a word: ")
lbl.grid(row=0,column=0,padx=5,pady=5)
e=StringVar()
e1=Entry(fr,textvariable=e)
e1.grid(row=0,column=1)
search=Button(fr,text="Quest",command=return_meaning)
search.grid(row=1,column=0,padx=5,pady=5)
clear=Button(fr,text="Clear",command=clear_entry)
clear.grid(row=1,column=1,padx=5,pady=5)
lbl2=Label(fr,text="",bg="black",fg="white",activebackground="black",justify=LEFT,anchor=W)
lbl2.grid(row=2,columnspan=2,padx=5,pady=5)
y=Radiobutton(fr,text="Yes",variable=v,value=1)
n=Radiobutton(fr,text="No",variable=v,value=2)
fr.grid_columnconfigure(0,weight=1)
fr.grid_columnconfigure(1,weight=1)
fr.grid_rowconfigure(0,weight=1)
fr.grid_rowconfigure(1,weight=1)
fr.grid_rowconfigure(2,weight=3)
win.mainloop()
