from tkinter import *

# to import tkinter to open the browse screen
from tkinter.filedialog import askopenfile

class MyButtons:
  def __init__(self,root):
    # to create a space on window for our use
    self.f= Frame(root, height=600, width= 500)
    self.f.propagate(0)
    self.f.pack()

    # To insert text on the root window
    self.l3= Label(text = 'LIST OF CONTACTS', font='courier')
    self.l3.place(x=160, y= 25)

    # to create label and entry box to take user input
    self.l1= Label(text = 'NAME :')
    self.l2= Label(text= 'TELEPHONE:')
    self.e1= Entry(self.f, width=25)
    self.e2= Entry(self.f,width= 25)

    # to place the entry box at the desired location in the root window
    self.l1.place(x=100, y= 100)
    self.e1.place(x=200, y= 100)
    self.l2.place(x=85, y= 150)
    self.e2.place(x=200, y= 150)

    # creating buttons using Button and assigning the command for
    the button click
    self.b1= Button(self.f, text = 'ADD', width=15, height=2,command = self.add)
    self.b1.place(x=50,y=450)
    self.b2= Button(self.f, text = 'DELETE',width=15,height=2,command = self.delete)
    self.b2.place(x=200,y=450)
    self.b3= Button(self.f, text = 'SAVE TO FILE',width=15,height=2,command = self.save_to_file)
    self.b3.place(x=350,y=450)
    self.b4= Button(self.f, text = 'Open File',width=10,height=1,command = self.open_file)
    self.b4.place(x=25,y=550)
                
    # To create a text box in the root window to accept nameand
    phone number in the form of a dictionary
    self.t = Text(self.f, width = 40 , height = 13, wrap= WORD)
    self.t.place(x=100,y= 200)
                
  # creating a function on command for ADD button, so it adds the text in the entry box to the text box as a dictionary.
  def add(self):
    txt1= (" %s : %s" % (self.e1.get(), self.e2.get()))
    self.t.insert(END,"\n"+txt1)
                
  # creating a function on command for SAVE button, so it save the text in the entry box to a text folder whose path is given.
  def save_to_file(self):
    file_name = self.t.get(0.1, END)
    with open('/Users/samarth/Desktop/phnumb.txt', 'a+') as
  file_object:
      file_object.write(file_name+ "\n")
  # creating a function on command for OPEN FILE button, so it opens the saved phone numbers in the folder.
  def open_file(self):
    file = askopenfile(mode ='r', filetypes =[('notepad Files','*.txt')])
    if file is not None:
       content = file.read()
       print(content)
                
  # creating a function on command for DELETE button, so it deletes the text entered into the text box.
  def delete(self):
    self.t.delete(0.1,END)
                
root=Tk()
obj = MyButtons(root)
root.mainloop()
