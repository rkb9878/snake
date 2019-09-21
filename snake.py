from tkinter import Tk,PhotoImage,Canvas,Frame,Button,Label,NW
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
import random
PLAYER1=0
PLAYER2=0
OLD_PLAYER1=0
OLD_PLAYER2=0

IMAGE=['', 'cut_images/1.png', 'cut_images/2.png', 'cut_images/3.png', 'cut_images/4.png', 'cut_images/5.png', 'cut_images/6.png', 'cut_images/7.png',
      'cut_images/8.png', 'cut_images/9.png', 'cut_images/10.png', 'cut_images/11.png', 'cut_images/12.png', 'cut_images/13.png', 'cut_images/14.png',
      'cut_images/15.png', 'cut_images/16.png', 'cut_images/17.png', 'cut_images/18.png', 'cut_images/19.png', 'cut_images/20.png', 'cut_images/21.png',
      'cut_images/22.png', 'cut_images/23.png', 'cut_images/24.png', 'cut_images/25.png', 'cut_images/26.png', 'cut_images/27.png', 'cut_images/28.png',
      'cut_images/29.png', 'cut_images/30.png', 'cut_images/31.png', 'cut_images/32.png', 'cut_images/33.png', 'cut_images/34.png', 'cut_images/35.png',
      'cut_images/36.png', 'cut_images/37.png', 'cut_images/38.png', 'cut_images/39.png', 'cut_images/40.png', 'cut_images/41.png', 'cut_images/42.png',
      'cut_images/43.png', 'cut_images/44.png', 'cut_images/45.png', 'cut_images/46.png', 'cut_images/47.png', 'cut_images/48.png', 'cut_images/49.png',
      'cut_images/50.png', 'cut_images/51.png', 'cut_images/52.png', 'cut_images/53.png', 'cut_images/54.png', 'cut_images/55.png', 'cut_images/56.png',
      'cut_images/57.png', 'cut_images/58.png', 'cut_images/59.png', 'cut_images/60.png', 'cut_images/61.png', 'cut_images/62.png', 'cut_images/63.png',
      'cut_images/64.png', 'cut_images/65.png', 'cut_images/66.png', 'cut_images/67.png', 'cut_images/68.png', 'cut_images/69.png', 'cut_images/70.png',
      'cut_images/71.png', 'cut_images/72.png', 'cut_images/73.png', 'cut_images/74.png', 'cut_images/75.png', 'cut_images/76.png', 'cut_images/77.png',
      'cut_images/78.png', 'cut_images/79.png', 'cut_images/80.png', 'cut_images/81.png', 'cut_images/82.png', 'cut_images/83.png', 'cut_images/84.png',
      'cut_images/85.png', 'cut_images/86.png','cut_images/87.png', 'cut_images/88.png', 'cut_images/89.png', 'cut_images/90.png', 'cut_images/91.png',
      'cut_images/92.png', 'cut_images/93.png','cut_images/94.png', 'cut_images/95.png', 'cut_images/96.png', 'cut_images/97.png', 'cut_images/98.png',
      'cut_images/99.png', 'cut_images/100.png']

SNAKE={22:5, 47:25, 73:49, 93:64, 99:77}
LADDER={11:32, 15:45, 38:61, 48:71, 66:97}

class SA:

    def player1_dice_throw(self):
        global PLAYER1
        global PLAYER2
        global OLD_PLAYER1
        global IMAGE
        OLD_PLAYER1 = PLAYER1
        self.canvas.delete("all")
        dice_image_name = ["", 'dice/dice1.png', 'dice/dice2.png', 'dice/dice3.png', 'dice/dice4.png', 'dice/dice5.png', 'dice/dice6.png']
        i = random.randrange(1, 6)
        img = Image.open(dice_image_name[i])
        filename = ImageTk.PhotoImage(img)
        self.canvas2 = Canvas(self.right, height=img.size[0], width=img.size[0])
        self.canvas2.image = filename  # <--- keep reference of your image
        self.canvas2.create_image(0, 0, anchor='nw', image=filename)
        self.canvas2.grid(row=1, column=1)
        PLAYER1 = PLAYER1 + i
        # ----------------------------------------------------
        if PLAYER1 in SNAKE:
            t = SNAKE[PLAYER1]
            file1 = PhotoImage(file='cut_images/3.png')
            self.can_list[t].image = file1
            self.can_list[t].create_image(0, 0, anchor='nw', image=file1)
            PLAYER1 = t
        elif PLAYER1 in LADDER:
            t = LADDER[PLAYER1]
            file1 = PhotoImage(file='cut_images/3.png')
            self.can_list[t].image = file1
            self.can_list[t].create_image(0, 0, anchor='nw', image=file1)
            PLAYER1 = t
        # ----------------------------------------------------
        if PLAYER1 < 100:
            if PLAYER1 == PLAYER2:
                filename = PhotoImage(file='bt/double.png')
                self.can_list[PLAYER1].image = filename
                self.can_list[PLAYER1].create_image(0, 0, anchor='nw', image=filename)
                if OLD_PLAYER1 > 0:
                    f = IMAGE[OLD_PLAYER1]
                    filename1 = PhotoImage(file=f)
                    self.can_list[OLD_PLAYER1].image = filename1
                    self.can_list[OLD_PLAYER1].create_image(0, 0, anchor='nw', image=filename1)
            else:
                filename = PhotoImage(file='bt/green.png')
                self.can_list[PLAYER1].image = filename
                self.can_list[PLAYER1].create_image(0, 0, anchor='nw', image=filename)
                if OLD_PLAYER1 > 0:
                    f = IMAGE[OLD_PLAYER1]
                    filename1 = PhotoImage(file=f)
                    self.can_list[OLD_PLAYER1].image = filename1
                    self.can_list[OLD_PLAYER1].create_image(0, 0, anchor='nw', image=filename1)
            # -----------------------------------------------------
            self.player1.config(state='disable')
            self.player2.config(state='normal')
        else:
            f1 = IMAGE[OLD_PLAYER1]
            filename2 = PhotoImage(file=f1)
            self.can_list[OLD_PLAYER1].image = filename2
            self.can_list[OLD_PLAYER1].create_image(0, 0, anchor='nw', image=filename2)
            f = "bt/winner_p1.png"
            filename1 = PhotoImage(file=f)
            self.can_list[100].image = filename1
            self.can_list[100].create_image(0, 0, anchor='nw', image=filename1)
            showinfo("Winner","player 1 winner")
            self.player1.config(state='disable')
            self.player2.config(state='disable')
    def player2_dice_throw(self):
        global PLAYER2
        global PLAYER1
        global OLD_PLAYER2
        global IMAGE
        global SNAKE
        global LADDER
        OLD_PLAYER2 = PLAYER2
        self.canvas.delete("all")
        dice_image_name = ["", 'dice/dice1.png', 'dice/dice2.png', 'dice/dice3.png', 'dice/dice4.png', 'dice/dice5.png', 'dice/dice6.png']
        j = random.randrange(1, 6)
        img = Image.open(dice_image_name[j])
        filename = ImageTk.PhotoImage(img)
        self.canvas1 = Canvas(self.right, height=img.size[0], width=img.size[0])
        self.canvas1.image = filename  # <--- keep reference of your image
        self.canvas1.create_image(0, 0, anchor='nw', image=filename)
        self.canvas1.grid(row=1, column=1)
        PLAYER2 = PLAYER2 + j

        # ------cut-----------------------------------
        if PLAYER2 in SNAKE:
            t = SNAKE[PLAYER2]
            file1 = PhotoImage(file='cut_images/1.png')
            self.can_list[t].image = file1
            self.can_list[t].create_image(0, 0, anchor='nw', image=file1)
            PLAYER2 = t
        elif PLAYER2 in LADDER:
            t = LADDER[PLAYER2]
            file1 = PhotoImage(file='cut_images/2.png')
            self.can_list[t].image = file1
            self.can_list[t].create_image(0, 0, anchor='nw', image=file1)
            PLAYER2 = t
        # -----------------------------------------
        if PLAYER2 <100:
            if PLAYER2 ==PLAYER1:
                filename = PhotoImage(file='bt/double.png')
                self.can_list[PLAYER2].image = filename
                self.can_list[PLAYER2].create_image(0, 0, anchor='nw', image=filename)
                if OLD_PLAYER2 > 0:
                    filename1 = PhotoImage(file=IMAGE[OLD_PLAYER2])
                    self.can_list[OLD_PLAYER2].image = filename1
                    self.can_list[OLD_PLAYER2].create_image(0, 0, anchor='nw', image=filename1)
            else:

                filename = PhotoImage(file='bt/red.png')
                self.can_list[PLAYER2].image = filename
                self.can_list[PLAYER2].create_image(0, 0, anchor='nw', image=filename)
                if OLD_PLAYER2 > 0:
                    f = IMAGE[OLD_PLAYER2]
                    filename1 = PhotoImage(file=f)
                    self.can_list[OLD_PLAYER2].image = filename1
                    self.can_list[OLD_PLAYER2].create_image(0, 0, anchor='nw', image=filename1)
        # -----------------------------------------------
            self.player2.config(state='disable')
            self.player1.config(state='normal')
        else:
            f1 = IMAGE[OLD_PLAYER1]
            filename2 = PhotoImage(file=f1)
            self.can_list[OLD_PLAYER2].image = filename2
            self.can_list[OLD_PLAYER2].create_image(0, 0, anchor='nw', image=filename2)
            f = "bt/winner_p2.png"
            filename1 = PhotoImage(file=f)
            self.can_list[100].image = filename1
            self.can_list[100].create_image(0, 0, anchor='nw', image=filename1)
            showinfo("Winner", "player 2 winner")
            self.player1.config(state='disable')
            self.player2.config(state='disable')



    def __init__(self):


        root=Tk()
        root.title("SNAKE AND LADDERS")
        head = Frame(root)
        head.pack(side='top')
        body = Frame(root)
        body.pack()
        # -------------------------------------------------------
        left = Frame(body)  # THIS IS FOR LEFT SIDE OF THE BODY FRAME
        self.right = Frame(body)  # THIS IS FOR RIGHT SIDE OF THE BODY FRAME
        left.pack(side='left')
        self.right.pack(side='right')
        # ------------------HEADING OF SNAKE AND LADDER ---------------
#        self.lb1 = Label(self.right, text="player 1's name")
#        self.lb2 = Label(self.right, text="player 2's name")
#        self.box1 = Entry(self.right)
#        self.box2 = Entry(self.right)
        img100 = Image.open("dice/dice6.png")
        # =======================Buttons====================================================
        self.canvas = Canvas(self.right, height=img100.size[0], width=img100.size[0])
        self.canvas.grid(row=1, column=1)
        self.player1 = Button(self.right, text='Player 1', bg='#03A235', command=self.player1_dice_throw)
        self.player2 = Button(self.right, text='Player 2', bg='#AF7135', state='disable',command=self.player2_dice_throw)
#        self.lb1.grid(row=0, column=0, pady=50)
#        self.lb2.grid(row=0, column=2, pady=50)
#        self.box1.grid(row=1, column=0)
#        self.box2.grid(row=1, column=2)

        self.player1.grid(row=2, column=0, pady=50)
        self.player2.grid(row=2, column=2, pady=50)
        # Disable colour #AF7135


# ---------------------------heading label for game----------------------------------

        Label(head, text="Snake & Ladder", font=("times new roman", 48, "bold", "underline"), bg="snow",fg="green").pack()
        # ===================IMG0 WILL SET THE CANVAS SIZE FOR ALL THE CANVAS=================
        img0 = Image.open('cut_images/1.png')
        #--------------------button for players--------------------------------
        # bt1=Button(self.right,text="Player 1") #PLAYER 1's button
        # bt1.pack(side='bottom')
        # bt2=Button(self.right,text="Player 2")
        # bt2.pack(side='bottom')
        # -------------------NOW THE CAN IS CREATING THE SNAKE AND LADDER BOARD-----------------------
        self.can1 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can1.grid(row=10, column=1)
        img1 = PhotoImage(file='cut_images/1.png')
        self.can1.create_image(0, 0, image=img1, anchor=NW)
        #---------------------------------------------------------------------------------
        self.can2=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can2.grid(row = 10, column = 2)
        img2= PhotoImage(file = 'cut_images/2.png')
        self.can2.create_image(0,0, image = img2, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can3=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can3.grid(row = 10, column = 3)
        img3= PhotoImage(file = 'cut_images/3.png')
        self.can3.create_image(0,0, image = img3, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can4=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can4.grid(row = 10, column = 4)
        img4= PhotoImage(file = 'cut_images/4.png')
        self.can4.create_image(0,0, image = img4, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can5=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can5.grid(row = 10, column = 5)
        img5= PhotoImage(file = 'cut_images/5.png')
        self.can5.create_image(0,0, image = img5, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can6=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can6.grid(row = 10, column = 6)
        img6= PhotoImage(file = 'cut_images/6.png')
        self.can6.create_image(0,0, image = img6, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can7=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can7.grid(row = 10, column = 7)
        img7= PhotoImage(file = 'cut_images/7.png')
        self.can7.create_image(0,0, image = img7, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can8=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can8.grid(row = 10, column = 8)
        img8= PhotoImage(file = 'cut_images/8.png')
        self.can8.create_image(0,0, image = img8, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can9=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can9.grid(row = 10, column = 9)
        img9= PhotoImage(file = 'cut_images/9.png')
        self.can9.create_image(0,0, image = img9, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can10=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can10.grid(row = 10, column = 10)
        img10= PhotoImage(file = 'cut_images/10.png')
        self.can10.create_image(0,0, image = img10, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can11=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can11.grid(row = 9, column = 10)
        img11= PhotoImage(file = 'cut_images/11.png')
        self.can11.create_image(0,0, image = img11, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can12=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can12.grid(row = 9, column = 9)
        img12= PhotoImage(file = 'cut_images/12.png')
        self.can12.create_image(0,0, image = img12, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can13=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can13.grid(row = 9, column = 8)
        img13= PhotoImage(file = 'cut_images/13.png')
        self.can13.create_image(0,0, image = img13, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can14=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can14.grid(row = 9, column = 7)
        img14= PhotoImage(file = 'cut_images/14.png')
        self.can14.create_image(0,0, image = img14, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can15=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can15.grid(row = 9, column = 6)
        img15= PhotoImage(file = 'cut_images/15.png')
        self.can15.create_image(0,0, image = img15, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can16=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can16.grid(row = 9, column = 5)
        img16= PhotoImage(file = 'cut_images/16.png')
        self.can16.create_image(0,0, image = img16, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can17=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can17.grid(row = 9, column = 4)
        img17= PhotoImage(file = 'cut_images/17.png')
        self.can17.create_image(0,0, image = img17, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can18=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can18.grid(row = 9, column = 3)
        img18= PhotoImage(file = 'cut_images/18.png')
        self.can18.create_image(0,0, image = img18, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can19=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can19.grid(row = 9, column = 2)
        img19= PhotoImage(file = 'cut_images/19.png')
        self.can19.create_image(0,0, image = img19, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can20=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can20.grid(row = 9, column = 1)
        img20= PhotoImage(file = 'cut_images/20.png')
        self.can20.create_image(0,0, image = img20, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can21=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can21.grid(row = 8, column = 1)
        img21= PhotoImage(file = 'cut_images/21.png')
        self.can21.create_image(0,0, image = img21, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can22=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can22.grid(row = 8, column = 2)
        img22= PhotoImage(file = 'cut_images/22.png')
        self.can22.create_image(0,0, image = img22, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can23=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can23.grid(row = 8, column = 3)
        img23= PhotoImage(file = 'cut_images/23.png')
        self.can23.create_image(0,0, image = img23, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can24=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can24.grid(row = 8, column = 4)
        img24= PhotoImage(file = 'cut_images/24.png')
        self.can24.create_image(0,0, image = img24, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can25=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can25.grid(row = 8, column = 5)
        img25= PhotoImage(file = 'cut_images/25.png')
        self.can25.create_image(0,0, image = img25, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can26=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can26.grid(row = 8, column = 6)
        img26= PhotoImage(file = 'cut_images/26.png')
        self.can26.create_image(0,0, image = img26, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can27=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can27.grid(row = 8, column = 7)
        img27= PhotoImage(file = 'cut_images/27.png')
        self.can27.create_image(0,0, image = img27, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can28=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can28.grid(row = 8, column = 8)
        img28= PhotoImage(file = 'cut_images/28.png')
        self.can28.create_image(0,0, image = img28, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can29=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can29.grid(row = 8, column = 9)
        img29= PhotoImage(file = 'cut_images/29.png')
        self.can29.create_image(0,0, image = img29, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can30=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can30.grid(row = 8, column = 10)
        img30= PhotoImage(file = 'cut_images/30.png')
        self.can30.create_image(0,0, image = img30, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can31=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can31.grid(row = 7, column = 10)
        img31= PhotoImage(file = 'cut_images/31.png')
        self.can31.create_image(0,0, image = img31, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can32=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can32.grid(row = 7, column = 9)
        img32= PhotoImage(file = 'cut_images/32.png')
        self.can32.create_image(0,0, image = img32, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can33=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can33.grid(row = 7, column = 8)
        img33= PhotoImage(file = 'cut_images/33.png')
        self.can33.create_image(0,0, image = img33, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can34=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can34.grid(row = 7, column = 7)
        img34= PhotoImage(file = 'cut_images/34.png')
        self.can34.create_image(0,0, image = img34, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can35=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can35.grid(row = 7, column = 6)
        img35= PhotoImage(file = 'cut_images/35.png')
        self.can35.create_image(0,0, image = img35, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can36=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can36.grid(row = 7, column = 5)
        img36= PhotoImage(file = 'cut_images/36.png')
        self.can36.create_image(0,0, image = img36, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can37=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can37.grid(row = 7, column = 4)
        img37= PhotoImage(file = 'cut_images/37.png')
        self.can37.create_image(0,0, image = img37, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can38=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can38.grid(row = 7, column = 3)
        img38= PhotoImage(file = 'cut_images/38.png')
        self.can38.create_image(0,0, image = img38, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can39=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can39.grid(row = 7, column = 2)
        img39= PhotoImage(file = 'cut_images/39.png')
        self.can39.create_image(0,0, image = img39, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can40=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can40.grid(row = 7, column = 1)
        img40= PhotoImage(file = 'cut_images/40.png')
        self.can40.create_image(0,0, image = img40, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can41=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can41.grid(row = 6, column = 1)
        img41= PhotoImage(file = 'cut_images/41.png')
        self.can41.create_image(0,0, image = img41, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can42=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can42.grid(row = 6, column = 2)
        img42= PhotoImage(file = 'cut_images/42.png')
        self.can42.create_image(0,0, image = img42, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can43=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can43.grid(row = 6, column = 3)
        img43= PhotoImage(file = 'cut_images/43.png')
        self.can43.create_image(0,0, image = img43, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can44=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can44.grid(row = 6, column = 4)
        img44= PhotoImage(file = 'cut_images/44.png')
        self.can44.create_image(0,0, image = img44, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can45=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can45.grid(row = 6, column = 5)
        img45= PhotoImage(file = 'cut_images/45.png')
        self.can45.create_image(0,0, image = img45, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can46=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can46.grid(row = 6, column = 6)
        img46= PhotoImage(file = 'cut_images/46.png')
        self.can46.create_image(0,0, image = img46, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can47=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can47.grid(row = 6, column = 7)
        img47 = PhotoImage(file = 'cut_images/47.png')
        self.can47.create_image(0,0, image = img47, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can48=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can48.grid(row = 6, column = 8)
        img48= PhotoImage(file = 'cut_images/48.png')
        self.can48.create_image(0,0, image = img48, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can49=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can49.grid(row = 6, column = 9)
        img49= PhotoImage(file = 'cut_images/49.png')
        self.can49.create_image(0,0, image = img49, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can50=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can50.grid(row = 6, column = 10)
        img50= PhotoImage(file = 'cut_images/50.png')
        self.can50.create_image(0,0, image = img50, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can51=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can51.grid(row = 5, column = 10)
        img51= PhotoImage(file = 'cut_images/51.png')
        self.can51.create_image(0,0, image = img51, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can52=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can52.grid(row = 5, column = 9)
        img52= PhotoImage(file = 'cut_images/52.png')
        self.can52.create_image(0,0, image = img52, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can53 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can53.grid(row = 5, column = 8)
        img53= PhotoImage(file = 'cut_images/53.png')
        self.can53.create_image(0,0, image = img53, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can54=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can54.grid(row = 5, column = 7)
        img54= PhotoImage(file = 'cut_images/54.png')
        self.can54.create_image(0,0, image = img54, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can55=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can55.grid(row = 5, column = 6)
        img55= PhotoImage(file = 'cut_images/55.png')
        self.can55.create_image(0,0, image = img55, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can56=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can56.grid(row = 5, column = 5)
        img56= PhotoImage(file = 'cut_images/56.png')
        self.can56.create_image(0,0, image = img56, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can57=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can57.grid(row = 5, column = 4)
        img57= PhotoImage(file = 'cut_images/57.png')
        self.can57.create_image(0,0, image = img57, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can58=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can58.grid(row = 5, column = 3)
        img58= PhotoImage(file = 'cut_images/58.png')
        self.can58.create_image(0,0, image = img58, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can59=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can59.grid(row = 5, column = 2)
        img59= PhotoImage(file = 'cut_images/59.png')
        self.can59.create_image(0,0, image = img59, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can60=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can60.grid(row = 5, column = 1)
        img60= PhotoImage(file = 'cut_images/60.png')
        self.can60.create_image(0,0, image = img60, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can61=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can61.grid(row = 4, column = 1)
        img61= PhotoImage(file = 'cut_images/61.png')
        self.can61.create_image(0,0, image = img61, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can62=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can62.grid(row = 4, column = 2)
        img62= PhotoImage(file = 'cut_images/62.png')
        self.can62.create_image(0,0, image = img62, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can63=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can63.grid(row = 4, column = 3)
        img63= PhotoImage(file = 'cut_images/63.png')
        self.can63.create_image(0,0, image = img63, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can64=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can64.grid(row = 4, column = 4)
        img64= PhotoImage(file = 'cut_images/64.png')
        self.can64.create_image(0,0, image = img64, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can65=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can65.grid(row = 4, column = 5)
        img65= PhotoImage(file = 'cut_images/65.png')
        self.can65.create_image(0,0, image = img65, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can66=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can66.grid(row = 4, column = 6)
        img66= PhotoImage(file = 'cut_images/66.png')
        self.can66.create_image(0,0, image = img66, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can67=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can67.grid(row = 4, column = 7)
        img67= PhotoImage(file = 'cut_images/67.png')
        self.can67.create_image(0,0, image = img67, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can68=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can68.grid(row = 4, column = 8)
        img68= PhotoImage(file = 'cut_images/68.png')
        self.can68.create_image(0,0, image = img68, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can69=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can69.grid(row = 4, column = 9)
        img69= PhotoImage(file = 'cut_images/69.png')
        self.can69.create_image(0,0, image = img69, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can70=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can70.grid(row = 4, column = 10)
        img70= PhotoImage(file = 'cut_images/70.png')
        self.can70.create_image(0,0, image = img70, anchor = NW)

        # ---------------------------------------------------------------------------------
        self.can71 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can71.grid(row=3, column=10)
        img71 = PhotoImage(file='cut_images/71.png')
        self.can71.create_image(0, 0, image=img71, anchor=NW)
        #---------------------------------------------------------------------------------
        self.can72=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can72.grid(row = 3, column = 9)
        img72= PhotoImage(file = 'cut_images/72.png')
        self.can72.create_image(0,0, image = img72, anchor = NW)

        #---------------------------------------------------------------------------------
        self.can73=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can73.grid(row = 3, column = 8)
        img73= PhotoImage(file = 'cut_images/73.png')
        self.can73.create_image(0,0, image = img73, anchor = NW)

        # ---------------------------------------------------------------------------------
        self.can74 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can74.grid(row=3, column=7)
        img74 = PhotoImage(file='cut_images/74.png')
        self.can74.create_image(0, 0, image=img74, anchor=NW)
        #---------------------------------------------------------------------------------
        self.can75=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can75.grid(row = 3, column = 6)
        img75= PhotoImage(file = 'cut_images/75.png')
        self.can75.create_image(0,0, image = img75, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can76=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can76.grid(row = 3, column = 5)
        img76= PhotoImage(file = 'cut_images/76.png')
        self.can76.create_image(0,0, image = img76, anchor = NW)

        # ---------------------------------------------------------------------------------
        self.can77 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can77.grid(row=3, column=4)
        img77 = PhotoImage(file='cut_images/77.png')
        self.can77.create_image(0, 0, image=img77, anchor=NW)
        #---------------------------------------------------------------------------------
        self.can78=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can78.grid(row = 3, column = 3)
        img78= PhotoImage(file = 'cut_images/78.png')
        self.can78.create_image(0,0, image = img78, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can79=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can79.grid(row = 3, column = 2)
        img79= PhotoImage(file = 'cut_images/79.png')
        self.can79.create_image(0,0, image = img79, anchor = NW)

        # ---------------------------------------------------------------------------------
        self.can80 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can80.grid(row=3, column=1)
        img80 = PhotoImage(file='cut_images/80.png')
        self.can80.create_image(0, 0, image=img80, anchor=NW)
        #---------------------------------------------------------------------------------
        self.can81=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can81.grid(row = 2, column = 1)
        img81= PhotoImage(file = 'cut_images/81.png')
        self.can81.create_image(0,0, image = img81, anchor = NW)
        #---------------------------------------------------------------------------------
        self.can82=Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can82.grid(row = 2, column = 2)
        img82= PhotoImage(file = 'cut_images/82.png')
        self.can82.create_image(0,0, image = img82, anchor = NW)

        # ---------------------------------------------------------------------------------
        self.can83 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can83.grid(row=2, column=3)
        img83 = PhotoImage(file='cut_images/83.png')
        self.can83.create_image(0, 0, image=img83, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can84 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can84.grid(row=2, column=4)
        img84 = PhotoImage(file='cut_images/84.png')
        self.can84.create_image(0, 0, image=img84, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can85 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can85.grid(row=2, column=5)
        img85 = PhotoImage(file='cut_images/85.png')
        self.can85.create_image(0, 0, image=img85, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can86 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can86.grid(row=2, column=6)
        img86 = PhotoImage(file='cut_images/86.png')
        self.can86.create_image(0, 0, image=img86, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can87 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can87.grid(row=2, column=7)
        img87 = PhotoImage(file='cut_images/87.png')
        self.can87.create_image(0, 0, image=img87, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can88 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can88.grid(row=2, column=8)
        img88 = PhotoImage(file='cut_images/88.png')
        self.can88.create_image(0, 0, image=img88, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can89 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can89.grid(row=2, column=9)
        img89 = PhotoImage(file='cut_images/89.png')
        self.can89.create_image(0, 0, image=img89, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can90 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can90.grid(row=2, column=10)
        img90 = PhotoImage(file='cut_images/90.png')
        self.can90.create_image(0, 0, image=img90, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can91 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can91.grid(row=1, column=10)
        img91 = PhotoImage(file='cut_images/91.png')
        self.can91.create_image(0, 0, image=img91, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can92 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can92.grid(row=1, column=9)
        img92 = PhotoImage(file='cut_images/92.png')
        self.can92.create_image(0, 0, image=img92, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can93 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can93.grid(row=1, column=8)
        img93 = PhotoImage(file='cut_images/93.png')
        self.can93.create_image(0, 0, image=img93, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can94 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can94.grid(row=1, column=7)
        img94 = PhotoImage(file='cut_images/94.png')
        self.can94.create_image(0, 0, image=img94, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can95 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can95.grid(row=1, column=6)
        img95 = PhotoImage(file='cut_images/95.png')
        self.can95.create_image(0, 0, image=img95, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can96 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can96.grid(row=1, column=5)
        img96 = PhotoImage(file='cut_images/96.png')
        self.can96.create_image(0, 0, image=img96, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can97 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can97.grid(row=1, column=4)
        img97 = PhotoImage(file='cut_images/97.png')
        self.can97.create_image(0, 0, image=img97, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can98 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can98.grid(row=1, column=3)
        img98 = PhotoImage(file='cut_images/98.png')
        self.can98.create_image(0, 0, image=img98, anchor=NW)
        # ---------------------------------------------------------------------------------
        self.can99 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can99.grid(row=1, column=2)
        img99 = PhotoImage(file='cut_images/99.png')
        self.can99.create_image(0, 0, image=img99, anchor=NW)

        # ---------------------------------------------------------------------------------
        self.can100 = Canvas(left, height=img0.size[0], width=img0.size[0])
        self.can100.grid(row=1, column=1)
        img100 = PhotoImage(file='cut_images/100.png')
        self.can100.create_image(0, 0, image=img100, anchor=NW)

        self.can_list = ["", self.can1, self.can2, self.can3, self.can4, self.can5, self.can6, self.can7, self.can8,
                         self.can9, self.can10, self.can11, self.can12, self.can13, self.can14, self.can15, self.can16,
                         self.can17, self.can18, self.can19, self.can20, self.can21, self.can22, self.can23, self.can24,
                         self.can25, self.can26, self.can27, self.can28, self.can29, self.can30, self.can31, self.can32,
                         self.can33, self.can34, self.can35, self.can36, self.can37, self.can38, self.can39, self.can40,
                         self.can41, self.can42, self.can43, self.can44, self.can45, self.can46, self.can47, self.can48,
                         self.can49, self.can50, self.can51, self.can52, self.can53, self.can54, self.can55, self.can56,
                         self.can57, self.can58, self.can59, self.can60, self.can61, self.can62, self.can63, self.can64,
                         self.can65, self.can66, self.can67, self.can68, self.can69, self.can70, self.can71, self.can72,
                         self.can73, self.can74, self.can75, self.can76, self.can77, self.can78, self.can79, self.can80,
                         self.can81, self.can82, self.can83, self.can84, self.can85, self.can86, self.can87, self.can88,
                         self.can89, self.can90, self.can91, self.can92, self.can93, self.can94, self.can95, self.can96,
                         self.can97, self.can98, self.can99, self.can100]

        root.mainloop()
if __name__ == '__main__':
    SA()