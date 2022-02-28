# Phonebook-with-pyhton-GUI
Building a phonebook to save and retrieve contacts using python GUI.
GUI- Tkinter

Python offers multiple options for developing GUI(Graphical User
Interface). It is a standard Python interface to the Tk GUI toolkit shipped
with Python. Python with tkinter is the fastest and easiest way to create
the GUI applications. Creating a GUI using tkinter is an easy task.

To create a tkinter app:
1. Importing the module – tkinter
2. Create the main window (container)
3. Add any number of widgets to the main window
4. Apply the event Trigger on the widgets.

Tk():
To create a main window, tkinter offers a method
‘Tk(screenName=None, baseName=None, className=’Tk’, useTk=
1)’. To change the name of the window, you can change the className
to the desired one. The basic code used to create the main window of
the application is.
Syntax:
Root = Tk(), where root is the name of the main window object.

mainloop():
There is a method known by the name mainloop() is used when your
application is ready to run. mainloop() is an infinite loop used to run the
application, wait for an event to occur and process the event as long as
the window is not closed.
Syntax: mainloop()

place() method:
It organizes the widgets by placing them on specific positions directed by
the programmer.
Syntax:
place(x=, y= )

Button:
To add a button in your application, this widget is used.
Syntax:Button(self.f, text = 'label',width=,height=, command = )
