# Importing the necessary module 
from tkinter import * 
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading

# creating a window 
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.configure(background='blue')

# Setting the dimensions and position and making the window non-resizable
root.geometry('940x735+200+10')
root.resizable(0,0)


# defining varible 
totaltime=60
time=0
elapsedtimeinmunit=0
wrongword=0

#  Funktion to start a timer when called uppon and do certin stuff when it's called uppon 
def start_timer():
    Start_button.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()
 # creting a Loop to update timer and remaing timer labels
    for time in range(1,61):
        elapsed_timer_label.config(text=time) 
        remainingtimer=totaltime-time   
        remaining_timer_label.config(text=remainingtimer)
        sleep(1)
        root.update()
    
    textarea.config(state=DISABLED)  

# Function to count words, calculate statistics, and update labels
def count():
    global wrongword
    while time!=totaltime:
       written_paragraph=textarea.get(1.0,END).split() # turn the text insid the textarea  into a lsit with index
       totalword=len(written_paragraph)
      

    
       totalword_count_label.config(text=totalword)# updating the  value of totalword_count_label label to valu of totalword
       paragraph_wordlist=Label_paragrape['text'].split() #  retrieves text Label_paragrape, spliting  into words  and storing them as a list in paragraph_wordlist.
       Reset_button.config(state=NORMAL)
   
   #  comparing words from the 2 list  and counting wrong words  
    for pair in zip(paragraph_wordlist,written_paragraph):
         if pair[0]!=pair[1]:
            wrongword +=1

    
    Wrongword_counter_label.config(text=wrongword) 
 # Calculate words per minute (WPM) and update WPM count label
    elapsedtimeinmunit=time/60
    wpm=((totalword-wrongword)/elapsedtimeinmunit)
    wpm_count_label.config(text=wpm)
    
# Function to start timer and counting simultaneously using threads
def start():
    t1=threading.Thread(target=start_timer)
    t1.start()

    t2=threading.Thread(target=count)
    t2.start()

# Function to reset the timer and clear statistics
def reset():
    global time,elapsedtimeinmunit
    time=0
    elapsedtimeinmunit=0
    Start_button.config(state=NORMAL)
    Reset_button.config(state=DISABLED)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')  
    wpm_count_label.config(text='0')
    Wrongword_counter_label.config(text='0')
    totalword_count_label.config(text='0')
#Creating a root window


#creating a  main frame inside wondow and setting border coleeer 
mainframe=Frame(root,bd=4,)
mainframe.grid()

#creating a title frame inside the main frame
titleframe=Frame(mainframe,bg='gold',bd=4)
titleframe.grid()

# Adding a title label to the title frame
titlelabel=Label(titleframe,text='Become a champion',font=('algerian',28,'bold'),bg='orange',fg='white',width=41,bd=4)
titlelabel.grid(pady=5)

# Now adding  a pharagraph fram
pharagraph_frame=Frame(mainframe)
pharagraph_frame.grid(row=1,column=0)

# creating a list for paragraphs 
pharagraph_list=[' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

                    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

                    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

                    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

                    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
                    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
                    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

                    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
]
# Shuffling the pharagraph index to random every time 
random.shuffle(pharagraph_list)

# craeting a label frame inside phragrafe frame And adding indez 0 string from the pharargraph list  
Label_paragrape=Label(pharagraph_frame, text=pharagraph_list[0],wraplength=(840),justify=LEFT,font=("arial",12,'bold'))
Label_paragrape.grid()

#creating a frame for text area in mainframe
textarea_frame=Frame(mainframe)
textarea_frame.grid(row=2,column=0)

#now adding a texarea in the textarea_fram 
textarea=Text(textarea_frame,font=('arial', 12,'bold'), width=80,height=6,bd=2,relief=GROOVE,wrap='word',state=DISABLED)
textarea.grid()

# creating another frame for elapsed time wpm counter and so pn in mainframe
frame_output=Frame(mainframe)
frame_output.grid(row=3,column=0)

# creating labels that are going to be inside fram_output
# Label 1
elapsed_time_label=Label(frame_output,text='Elapsed Time',font=('Tahoma',12,'bold'),fg='blue')
elapsed_time_label.grid(row=0,column=0,padx=5)

elapsed_timer_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='red')
elapsed_timer_label.grid(row=0,column=1,padx=5)
#label 2
remaining_time_label=Label(frame_output,text='Remaining Time',font=('Tahoma',12,'bold'),fg='blue')
remaining_time_label.grid(row=0,column=2,padx=5)

remaining_timer_label=Label(frame_output,text='60',font=('Tahoma',12,'bold'),fg='red')
remaining_timer_label.grid(row=0,column=3,padx=5)
#label 3
wpm_label=Label(frame_output,text='WPM',font=('Tahoma',12,'bold'),fg='blue')
wpm_label.grid(row=0,column=4,padx=5)

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='red')
wpm_count_label.grid(row=0,column=5,padx=5)
#label 4
totalword_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='blue')
totalword_label.grid(row=0,column=6,padx=5)

totalword_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='red')
totalword_count_label.grid(row=0,column=7,padx=5)

#label 5
Wrongword_label=Label(frame_output,text='Wrong Words',font=('Tahoma',12,'bold'),fg='blue')
Wrongword_label.grid(row=0,column=8,padx=5)

Wrongword_counter_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='red')
Wrongword_counter_label.grid(row=0,column=9,padx=5)

# Creating a frame for buttons like reset exit and start 
Button_frame=Frame(mainframe)
Button_frame.grid(row=4,column=0)
 
 # Creating buttosn start reset and exeit inside the button_frame   
Start_button=ttk.Button(Button_frame,text='Start',command=start)
Start_button.grid(padx=15)

Reset_button=ttk.Button(Button_frame,text='Reset',state=DISABLED,command=reset)
Reset_button.grid(row=0,column=1,padx=15)

Exit_button=ttk.Button(Button_frame,text='Exit',command=root.destroy)
Exit_button.grid(row=0,column=2,padx=15)

# Now Creating a frame for for keybord
keyboard_frame=Frame(mainframe)
keyboard_frame.grid(row=5,column=0)

# creating another frame for keys 1 to 0 inside the keyboard frame and then adding the keys labels  in it seperatly
def create_key_label(frame, text):
    return Label(frame, text=text, bg='black', fg='white', font=('arial', 10, 'bold'), width=5, height=2, bd=10, relief=GROOVE)

key1to0_frame=Frame(keyboard_frame)
key1to0_frame.grid(pady=5)

# Create labels for keys 1 to 0
KeyLabel_1 = create_key_label(key1to0_frame, '1')
KeyLabel_2 = create_key_label(key1to0_frame, '2')
KeyLabel_3 = create_key_label(key1to0_frame, '3')
KeyLabel_4 = create_key_label(key1to0_frame, '4')
KeyLabel_5 = create_key_label(key1to0_frame, '5')
KeyLabel_6 = create_key_label(key1to0_frame, '6')
KeyLabel_7 = create_key_label(key1to0_frame, '7')
KeyLabel_8 = create_key_label(key1to0_frame, '8')
KeyLabel_9 = create_key_label(key1to0_frame, '9')
KeyLabel_0 = create_key_label(key1to0_frame, '0')

# Grid the keys 1 to 0
KeyLabel_1.grid(row=0, column=0, padx=10)
KeyLabel_2.grid(row=0, column=1, padx=10)
KeyLabel_3.grid(row=0, column=2, padx=10)
KeyLabel_4.grid(row=0, column=3, padx=10)
KeyLabel_5.grid(row=0, column=4, padx=10)
KeyLabel_6.grid(row=0, column=5, padx=10)
KeyLabel_7.grid(row=0, column=6, padx=10)
KeyLabel_8.grid(row=0, column=7, padx=10)
KeyLabel_9.grid(row=0, column=8, padx=10)
KeyLabel_0.grid(row=0, column=9, padx=10)

# now creating a frame for  keys Q to Å 
Frame_QtoA=Frame(keyboard_frame)
Frame_QtoA.grid(row=1,column=0,pady=5)

# Create labels for keys Q to Å
KeyLabel_Q = create_key_label(Frame_QtoA, 'Q')
KeyLabel_W = create_key_label(Frame_QtoA, 'W')
KeyLabel_E = create_key_label(Frame_QtoA, 'E')
KeyLabel_R = create_key_label(Frame_QtoA, 'R')
KeyLabel_T = create_key_label(Frame_QtoA, 'T')
KeyLabel_Y = create_key_label(Frame_QtoA, 'Y')
KeyLabel_U = create_key_label(Frame_QtoA, 'U')
KeyLabel_I = create_key_label(Frame_QtoA, 'I')
KeyLabel_O = create_key_label(Frame_QtoA, 'O')
KeyLabel_P = create_key_label(Frame_QtoA, 'P')
KeyLabel_Å = create_key_label(Frame_QtoA, 'Å')

# Grid the keys Q to Å
KeyLabel_W.grid(row=0, column=1, padx=9)
KeyLabel_Q.grid(row=0, column=0, padx=9)
KeyLabel_E.grid(row=0, column=2, padx=9)
KeyLabel_R.grid(row=0, column=3, padx=9)
KeyLabel_T.grid(row=0, column=4, padx=9)
KeyLabel_Y.grid(row=0, column=5, padx=9)
KeyLabel_U.grid(row=0, column=6, padx=9)
KeyLabel_I.grid(row=0, column=7, padx=9)
KeyLabel_O.grid(row=0, column=8, padx=9)
KeyLabel_Å.grid(row=0, column=9, padx=9)


# Creating frame for Keys A-Ä 
Frame_AtoÄ=Frame(keyboard_frame)
Frame_AtoÄ.grid(row=2,column=0,pady=5)


# Create labels for keys A to Ä
KeyLabel_A = create_key_label(Frame_AtoÄ, 'A')
KeyLabel_S = create_key_label(Frame_AtoÄ, 'S')
KeyLabel_D = create_key_label(Frame_AtoÄ, 'D')
KeyLabel_F = create_key_label(Frame_AtoÄ, 'F')
KeyLabel_G = create_key_label(Frame_AtoÄ, 'G')
KeyLabel_H = create_key_label(Frame_AtoÄ, 'H')
KeyLabel_J = create_key_label(Frame_AtoÄ, 'J')
KeyLabel_K = create_key_label(Frame_AtoÄ, 'K')
KeyLabel_L = create_key_label(Frame_AtoÄ, 'L')
KeyLabel_Ö = create_key_label(Frame_AtoÄ, 'Ö')
KeyLabel_Ä = create_key_label(Frame_AtoÄ, 'Ä')

# Grid the keys A to Ä
KeyLabel_A.grid(row=0, column=0, padx=5)
KeyLabel_S.grid(row=0, column=1, padx=5)
KeyLabel_D.grid(row=0, column=2, padx=5)
KeyLabel_F.grid(row=0, column=3, padx=5)
KeyLabel_G.grid(row=0, column=4, padx=5)
KeyLabel_H.grid(row=0, column=5, padx=5)
KeyLabel_J.grid(row=0, column=6, padx=5)
KeyLabel_K.grid(row=0, column=7, padx=5)
KeyLabel_L.grid(row=0, column=8, padx=5)
KeyLabel_Ö.grid(row=0, column=9, padx=5)
KeyLabel_Ä.grid(row=0, column=10, padx=5)


#Now doing the same thing last time with keys z to m
Frame_ZtoM=Frame(keyboard_frame)
Frame_ZtoM.grid(row=3,column=0,pady=5)


# Create labels for keys Z to M
KeyLabel_Z = create_key_label(Frame_ZtoM, 'Z')
KeyLabel_X = create_key_label(Frame_ZtoM, 'X')
KeyLabel_C = create_key_label(Frame_ZtoM, 'C')
KeyLabel_V = create_key_label(Frame_ZtoM, 'V')
KeyLabel_B = create_key_label(Frame_ZtoM, 'B')
KeyLabel_N = create_key_label(Frame_ZtoM, 'N')
KeyLabel_M = create_key_label(Frame_ZtoM, 'M')

# Grid the keys Z to M
KeyLabel_Z.grid(row=0, column=0, padx=8)
KeyLabel_X.grid(row=0, column=1, padx=8)
KeyLabel_C.grid(row=0, column=2, padx=8)
KeyLabel_V.grid(row=0, column=3, padx=8)
KeyLabel_B.grid(row=0, column=4, padx=8)
KeyLabel_N.grid(row=0, column=5, padx=8)
KeyLabel_M.grid(row=0, column=6, padx=8)

# Creating a frame for the space button and adding in the  The button
Spacekey_Frame=Frame(keyboard_frame)
Spacekey_Frame.grid(row=4,column=0,pady=3)


Spacekey=Label(Spacekey_Frame,text='Space',bg='black',fg='white',font=('arial',10,'bold'),width=30,height=2,bd=10,relief=GROOVE)
Spacekey.grid()

#Creating  a  funtion  to cahnge a coloer of a widget  whenever it coalled 

def changeBG(widget):
    widget.config(bg='red')
    widget.after(100,lambda:widget.config(bg='black'))


#NOW creating 3  list and adding all the numbers and alphabets  and space   labels in it 
NumberzLabel=[KeyLabel_1,KeyLabel_2,KeyLabel_3,KeyLabel_4,KeyLabel_5,KeyLabel_6,KeyLabel_7,KeyLabel_8,KeyLabel_9,KeyLabel_0]
Albhabetslabels=[KeyLabel_A,KeyLabel_B,KeyLabel_C,KeyLabel_D,KeyLabel_E,KeyLabel_F,KeyLabel_G,KeyLabel_H,KeyLabel_I,KeyLabel_J,KeyLabel_K,KeyLabel_L,KeyLabel_M,KeyLabel_N,KeyLabel_O,KeyLabel_P,KeyLabel_Q,KeyLabel_R,KeyLabel_S,KeyLabel_T,KeyLabel_U,KeyLabel_V,KeyLabel_W,KeyLabel_Y,KeyLabel_Z,KeyLabel_Å,KeyLabel_Ä,KeyLabel_Ö]
Spacelabel=[Spacekey]

# now creating  numbers and alphabets list  to bind with keys

Binding_numbers=['1','2','3','4','5','6','7','8','9','0']
Binding_alabhabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Bindingcap_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


#Bind each number key to a label from NumberzLabel list and associate it with changeBG function to cnangge its backgroudn 
for numbers in range(len(Binding_numbers)):
    root.bind(Binding_numbers[numbers], lambda event, label=NumberzLabel[numbers]: changeBG(label))

# Binding each lowercase key to a label from Alphabetslabels list and associating it with changeBG function to cnage its background
for small_alphabets in range(len(Binding_alabhabets)):
    root.bind(Binding_alabhabets[small_alphabets], lambda event, label=Albhabetslabels[small_alphabets]: changeBG(label))

# Doing the same as the last one but for uppercase alphabets
for captital_alphabets in range(len(Bindingcap_alphabet)):
    root.bind(Bindingcap_alphabet[captital_alphabets], lambda event, label=Albhabetslabels[captital_alphabets]: changeBG(label))

#Binding the space key to the changeBG function with the label from Spacelabel list
root.bind('<space>', lambda event:changeBG(Spacelabel[0]))
root.mainloop()