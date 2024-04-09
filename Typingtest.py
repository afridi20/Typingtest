# importing everything from tkinter.
from tkinter import * 

#Creating windwo with  widgt and hight and making the size permenent
root=Tk()
root.geometry('940x735+200+10')
root.resizable(0,0)

#creating a  main frame inside wondow
mainframe=Frame(root)
mainframe.grid()

#creating a title frame inside the main frame
titleframe=Frame(mainframe)
titleframe.grid()

titlelabel=Label(titleframe,text='Becmone a champion',font=('algerian',28,'bold'),bg='darkgoldenrod',fg='white',width=41)
titlelabel.grid()
root.mainloop()

