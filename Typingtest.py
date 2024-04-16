# Importing the necessary module 
from tkinter import * 
import random


#Creating a root window
root=Tk()

# Setting the dimensions and position and making the window non-resizable
root.geometry('940x735+200+10')
root.resizable(0,0)

#creating a  main frame inside wondow and setting border coleeer 
mainframe=Frame(root,bd=4,)
mainframe.grid()

#creating a title frame inside the main frame
titleframe=Frame(mainframe,bg='black',bd=4)
titleframe.grid()

# Adding a title label to the title frame
titlelabel=Label(titleframe,text='Become a champion',font=('algerian',28,'bold'),bg='darkgoldenrod',fg='white',width=41,bd=4)
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
textarea=Text(textarea_frame,font=('arial', 12,'bold'), width=80,height=15,bd=2,relief=GROOVE,wrap='word',state=DISABLED)
textarea.grid()

# creating another frame for time in mainframe
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

wpm_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),)
wpm_count_label.grid(row=0,column=5,padx=5)
#label 4
totalword_label=Label(frame_output,text='Total Words',font=('Tahoma',12,'bold'),fg='blue')
totalword_label.grid(row=0,column=4,padx=5)

totalword_count_label=Label(frame_output,text='0',font=('Tahoma',12,'bold'),)
totalword_count_label.grid(row=0,column=5,padx=5)


root.mainloop()