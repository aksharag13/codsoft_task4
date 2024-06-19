import tkinter as tk
import random
user_score=0
computer_score=0
def displayscore():
    user_s_display.set(f"player score:{user_score}")
    computer_s_display.set(f"Computer's score:{computer_score}")
def game(userin):
    global user_score,computer_score
    choicelist=("rock","paper","scissors")
    computer_c=random.choice(choicelist)
    computer_choice=computer_c.lower()
    user_choice_display.set(f"player choice: {userin}")
    comp_choice_display.set(f"computer choice: {computer_choice}")
    print("Player choice:",userin)
    print("Computer choice:",computer_choice)
    if userin==computer_choice:
        result.set("It is a tie.")
        user_score+=0.5
        computer_score+=0.5
    elif(userin=="rock" and computer_choice=="scissors") or (userin=="scissors" and computer_choice=="paper") or(userin=="paper" and computer_choice=="rock"):
        result.set("User wins.")
        user_score+=1
    else:
        result.set("Bad luck..Computer wins.")
        computer_score+=1
    print("User score: ",user_score)
    print("Computer score: ",computer_score)
    displayscore()
window = tk.Tk()#window is name of parent variable
#to rename the title of window
window.title("Rock Paper Scissors")
window.geometry('500x500')
window.configure(background="light blue")
label = tk.Label(window, text="Hello, Welcome to the Rock Paper Scissor game",font=("Arial",20))
label.grid(row=0,column=0,columnspan=5,padx=20,pady=20)
label_rules=tk.Label(window,text="Rules of the game:\n 1.Rock beats Scissors\n 2.Scissors beats Paper\n 3.Paper beats Rock.\nSelect your choice and let the game begin!",font=("Arial",15,"bold"))
label_rules.grid(row=1,column=0,columnspan=5,padx=40,pady=40)
label_player=tk.Label(window,text="Player",font=("Arial",20))
label_player.grid(row=2,column=0,padx=20,pady=20)
label_computer=tk.Label(window,text="Computer",font=("Arial",20))
label_computer.grid(row=2,column=2,padx=40,pady=40)
user_s_display=tk.StringVar(value=f"player score:{user_score}")#score to be changed to string so'f' used
computer_s_display=tk.StringVar(value=f"computer's score:{computer_score}")
#user score display
user_score_dis=tk.Label(window,textvariable=user_s_display,font=("Arial",20))
user_score_dis.grid(row=3,column=0,padx=20,pady=20)
#computer score display
comp_score_dis=tk.Label(window,textvariable=computer_s_display,font=("Arial",20))
comp_score_dis.grid(row=3,column=2,padx=20,pady=20)
#stringvars part is a widget to update the string everytime
user_choice_display=tk.StringVar(value="User choice:")
comp_choice_display=tk.StringVar(value="Computer choice:")
result=tk.StringVar(value="result:")
#user choice display
user_choice_dis= tk.Label(window, textvariable=user_choice_display, font=("Arial", 20))
user_choice_dis.grid(row=4, column=0, padx=20, pady=20)
#comp choice display
comp_choice_dis=tk.Label(window,textvariable=comp_choice_display,font=("Arial",20))
comp_choice_dis.grid(row=4,column=2,padx=20,pady=20)
#result display
resultdisplay = tk.Label(window, textvariable=result, font=("Arial", 20, "bold"))
resultdisplay.grid(row=5, column=0, columnspan=3, padx=20, pady=20)
#textvariable is used to update the text associated with StringVars
bt_rock=tk.Button(window,width=15,height=3,text="Rock",font=("Arial",20,"bold"),command=lambda:game("rock"))
bt_rock.grid(row=6,column=0,padx=20,pady=20)
bt_paper=tk.Button(window,width=15,height=3,text="Paper",font=("Arial",20,"bold"),command=lambda:game("paper"))
bt_paper.grid(row=6,column=1,padx=20,pady=20)
bt_scissors=tk.Button(window,width=15,height=3,text="Scissors",font=("Arial",20,"bold"),command=lambda:game("scissors"))
bt_scissors.grid(row=6,column=2,padx=40,pady=20)
window.mainloop()