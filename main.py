from tkinter import *
import ttkthemes as td  #pip install ttkthemes
from tkinter import ttk
s='abcdefghijklmnopqrstuvwxyz'
#####################functionality#############################
def select(event):   #event which is binded
    b=event.widget
    val=b['text']
    if val=='space':
        textarea.insert(INSERT,' ')
    elif val=='Enter':
        textarea.insert(INSERT,'\n')
    elif val=='Tab':
        textarea.insert(INSERT,'\t')
    elif val=='Del':
        textarea.delete(1.0,END)
    elif val=='Backs':
        c=textarea.get(1.0,END)
        newtext=c[:-2]
        textarea.delete(1.0,END)
        textarea.insert(INSERT,newtext)
    elif val=='Caps':
        buttoncaps.grid_remove()
        buttonCAPS.grid()
        le=s.upper()
        co=0
        for but in li:
            let=le[co]
            di[but].config(text=let)
            co+=1

    elif val=='CAPS':
        buttonCAPS.grid_remove()
        buttoncaps.grid()
        le = s
        co = 0
        for but in li:
            let = le[co]
            di[but].config(text=let)
            co += 1
    else:
        textarea.insert(INSERT,val)
def shift():
    aposthrophyButton.grid_remove()
    button1.grid_remove()
    button2.grid_remove()
    button3.grid_remove()
    button4.grid_remove()
    button5.grid_remove()
    button6.grid_remove()
    button7.grid_remove()
    button8.grid_remove()
    button9.grid_remove()
    button0.grid_remove()
    buttonminus.grid_remove()
    buttonequal.grid_remove()
    buttonopenbrac.grid_remove()
    buttonsemicolon.grid_remove()
    buttoncomma.grid_remove()
    buttonfullstop.grid_remove()
    buttonforwardslash.grid_remove()




    buttonexclamtion.grid()
    tildButton.grid()
    buttonattehrate.grid()
    buttonhash.grid()
    buttondollar.grid()
    buttonpercent.grid()
    buttonpower.grid()
    buttonampersand.grid()
    buttoninto.grid()
    buttonopensmallbracket.grid()
    buttonclosesmallbracket.grid()
    buttonunderscore.grid()
    buttonplus.grid()
    buttonclosebrac.grid()
    buttoncolon.grid()
    buttonlessthan.grid()
    buttongreaterthan.grid()
    buttonquestionmark.grid()



def shift1():
    aposthrophyButton.grid()
    button1.grid()
    button2.grid()
    button3.grid()
    button4.grid()
    button5.grid()
    button6.grid()
    button7.grid()
    button8.grid()
    button9.grid()
    button0.grid()
    buttonminus.grid()
    buttonequal.grid()
    buttonopenbrac.grid()
    buttonsemicolon.grid()
    buttoncomma.grid()
    buttonfullstop.grid()
    buttonforwardslash.grid()




    buttonexclamtion.grid_remove()
    tildButton.grid_remove()
    buttonattehrate.grid_remove()
    buttonhash.grid_remove()
    buttondollar.grid_remove()
    buttonpercent.grid_remove()
    buttonpower.grid_remove()
    buttonampersand.grid_remove()
    buttoninto.grid_remove()
    buttonopensmallbracket.grid_remove()
    buttonclosesmallbracket.grid_remove()
    buttonunderscore.grid_remove()
    buttonplus.grid_remove()
    buttonclosebrac.grid_remove()
    buttoncolon.grid_remove()
    buttonlessthan.grid_remove()
    buttongreaterthan.grid_remove()
    buttonquestionmark.grid_remove()


##################################GUI###############################

root = td.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.title('on-screen keyboard created by BVG')
root.config(bg='red')
#root.resizable(0, 0)
# root.overrideredirect(True) for removing titile and exit

titleLabel = Label(root, text='on-screen keyboard', font=('arial', 28, 'bold'), fg='white', bg='red')
titleLabel.grid(row=0, columnspan=40)
textarea = Text(root, font=('arial', 15, 'bold'), height=10, width=100, wrap='word')
textarea.grid(row=1, columnspan=40)
textarea.focus_set()

keysframe = Frame(root, bg='whitesmoke')
keysframe.grid(row=2)


#first row===
aposthrophyButton = ttk.Button(keysframe, text='`', width=5)
aposthrophyButton.grid(row=0, column=0)
tildButton=ttk.Button(keysframe, text='~' , width=5, )
tildButton.grid(row=0, column=0)
tildButton.grid_remove()

button1=ttk.Button(keysframe, text='1', width=5, )
button1.grid(row=0, column=1)
buttonexclamtion=ttk.Button(keysframe, text='!', width=5, )
buttonexclamtion.grid(row=0, column=1)
buttonexclamtion.grid_remove()

button2=ttk.Button(keysframe, text='2',  width=5, )
button2.grid(row=0, column=2)
buttonattehrate=ttk.Button(keysframe, text='@',  width=5, )
buttonattehrate.grid(row=0, column=2)
buttonattehrate.grid_remove()


button3=ttk.Button(keysframe, text='3',  width=5, )
button3.grid(row=0, column=3)
buttonhash=ttk.Button(keysframe, text='#',  width=5, )
buttonhash.grid(row=0, column=3)
buttonhash.grid_remove()

button4=ttk.Button(keysframe, text='4',  width=5, )
button4.grid(row=0, column=4)
buttondollar=ttk.Button(keysframe, text='$',  width=5, )
buttondollar.grid(row=0, column=4)
buttondollar.grid_remove()

button5=ttk.Button(keysframe, text='5',  width=5, )
button5.grid(row=0, column=5)
buttonpercent=ttk.Button(keysframe, text='%',  width=5, )
buttonpercent.grid(row=0, column=5)
buttonpercent.grid_remove()

button6=ttk.Button(keysframe, text='6',  width=5, )
button6.grid(row=0, column=6)
buttonpower=ttk.Button(keysframe, text='^',  width=5, )
buttonpower.grid(row=0, column=6)
buttonpower.grid_remove()

button7=ttk.Button(keysframe, text='7',  width=5, )
button7.grid(row=0, column=7)
buttonampersand=ttk.Button(keysframe, text='&',  width=5, )
buttonampersand.grid(row=0, column=7)
buttonampersand.grid_remove()

button8=ttk.Button(keysframe, text='8',  width=5, )
button8.grid(row=0, column=8)
buttoninto=ttk.Button(keysframe, text='*',  width=5, )
buttoninto.grid(row=0, column=8)
buttoninto.grid_remove()

button9=ttk.Button(keysframe, text='9',  width=5, )
button9.grid(row=0, column=9)
buttonopensmallbracket=ttk.Button(keysframe, text='(',  width=5, )
buttonopensmallbracket.grid(row=0, column=9)
buttonopensmallbracket.grid_remove()


button0=ttk.Button(keysframe, text='0',  width=5, )
button0.grid(row=0, column=10)
buttonclosesmallbracket=ttk.Button(keysframe, text=')',  width=5, )
buttonclosesmallbracket.grid(row=0, column=10)
buttonclosesmallbracket.grid_remove()

buttonminus=ttk.Button(keysframe, text='-',  width=5, )
buttonminus.grid(row=0, column=11)
buttonunderscore=ttk.Button(keysframe, text='_',  width=5, )
buttonunderscore.grid(row=0, column=11)
buttonunderscore.grid_remove()

buttonequal=ttk.Button(keysframe, text='=',  width=5, )
buttonequal.grid(row=0, column=12)
buttonplus=ttk.Button(keysframe, text='+',  width=5, )
buttonplus.grid(row=0, column=12)
buttonplus.grid_remove()

buttonback=ttk.Button(keysframe, text='Backs',  width=5, )
buttonback.grid(row=0, column=13)
buttondelete=ttk.Button(keysframe, text='Del',  width=5, )
buttondelete.grid(row=0, column=14)

#row2==
buttonTab=ttk.Button(keysframe, text='Tab',  width=5, )
buttonTab.grid(row=1, column=0)
buttonq=ttk.Button(keysframe, text='q',  width=5, )
buttonq.grid(row=1, column=1)
buttonw=ttk.Button(keysframe, text='w',  width=5, )
buttonw.grid(row=1, column=2)
buttone=ttk.Button(keysframe, text='e',  width=5, )
buttone.grid(row=1, column=3)
buttonr=ttk.Button(keysframe, text='r',  width=5, )
buttonr.grid(row=1, column=4)
buttont=ttk.Button(keysframe, text='t',  width=5, )
buttont.grid(row=1, column=5)
buttony=ttk.Button(keysframe, text='y',  width=5, )
buttony.grid(row=1, column=6)
buttonu=ttk.Button(keysframe, text='u',  width=5, )
buttonu.grid(row=1, column=7)
buttoni=ttk.Button(keysframe, text='i',  width=5, )
buttoni.grid(row=1, column=8)
buttono=ttk.Button(keysframe, text='o',  width=5, )
buttono.grid(row=1, column=9)

buttonp=ttk.Button(keysframe, text='p',  width=5, )
buttonp.grid(row=1, column=10)
buttonopenbrac=ttk.Button(keysframe, text='[',  width=5, )
buttonopenbrac.grid(row=1, column=11)
buttonclosebrac=ttk.Button(keysframe, text=']',  width=5, )
buttonclosebrac.grid(row=1, column=11)
buttonclosebrac.grid_remove()

buttonseven=ttk.Button(keysframe, text='7',  width=5, )
buttonseven.grid(row=1, column=12)
buttoneight=ttk.Button(keysframe, text='8',  width=5, )
buttoneight.grid(row=1, column=13)
buttonnine=ttk.Button(keysframe, text='9',  width=5, )
buttonnine.grid(row=1, column=14)


#row3==
buttoncaps=ttk.Button(keysframe, text='Caps',  width=5, )
buttoncaps.grid(row=2, column=0)
buttonCAPS=ttk.Button(keysframe, text='CAPS',  width=5, )
buttonCAPS.grid(row=2, column=0)
buttonCAPS.grid_remove()

buttona=ttk.Button(keysframe, text='a',  width=5, )
buttona.grid(row=2, column=1)
buttons=ttk.Button(keysframe, text='s',  width=5, )
buttons.grid(row=2, column=2)
buttond=ttk.Button(keysframe, text='d',  width=5, )
buttond.grid(row=2, column=3)
buttonf=ttk.Button(keysframe, text='f',  width=5, )
buttonf.grid(row=2, column=4)

buttong=ttk.Button(keysframe, text='g',  width=5, )
buttong.grid(row=2, column=5)
buttonh=ttk.Button(keysframe, text='h',  width=5, )
buttonh.grid(row=2, column=6)
buttonj=ttk.Button(keysframe, text='j',  width=5, )
buttonj.grid(row=2, column=7)
buttonk=ttk.Button(keysframe, text='k',  width=5, )
buttonk.grid(row=2, column=8)
buttonl=ttk.Button(keysframe, text='l',  width=5, )
buttonl.grid(row=2, column=9)

buttonsemicolon=ttk.Button(keysframe, text=';',  width=5, )
buttonsemicolon.grid(row=2, column=10)
buttoncolon=ttk.Button(keysframe, text=':',  width=5, )
buttoncolon.grid(row=2, column=10)
buttoncolon.grid_remove()

buttonenter=ttk.Button(keysframe, text='Enter',  width=5, )
buttonenter.grid(row=2, column=11)
buttonfour=ttk.Button(keysframe, text='4',  width=5, )
buttonfour.grid(row=2, column=12)
buttonfive=ttk.Button(keysframe, text='5',  width=5, )
buttonfive.grid(row=2, column=13)
buttonsix=ttk.Button(keysframe, text='6',  width=5, )
buttonsix.grid(row=2, column=14)

#row4=

buttonshift=ttk.Button(keysframe, text='Shift',  width=5,command=shift )
buttonshift.grid(row=3, column=0)
buttonz=ttk.Button(keysframe, text='z',  width=5, )
buttonz.grid(row=3, column=1)

buttonx=ttk.Button(keysframe, text='x',  width=5, )
buttonx.grid(row=3, column=2)
buttonc=ttk.Button(keysframe, text='c',  width=5, )
buttonc.grid(row=3, column=3)
buttonv=ttk.Button(keysframe, text='v',  width=5, )
buttonv.grid(row=3, column=4)
buttonb=ttk.Button(keysframe, text='b',  width=5, )
buttonb.grid(row=3, column=5)
buttonn=ttk.Button(keysframe, text='n',  width=5, )
buttonn.grid(row=3, column=6)
buttonm=ttk.Button(keysframe, text='m',  width=5, )
buttonm.grid(row=3, column=7)

buttoncomma=ttk.Button(keysframe, text=',',  width=5, )
buttoncomma.grid(row=3, column=8)
buttonlessthan=ttk.Button(keysframe, text='<',  width=5, )
buttonlessthan.grid(row=3, column=8)
buttonlessthan.grid_remove()

buttonfullstop=ttk.Button(keysframe, text='.',  width=5, )
buttonfullstop.grid(row=3, column=9)
buttongreaterthan=ttk.Button(keysframe, text='>',  width=5, )
buttongreaterthan.grid(row=3, column=9)
buttongreaterthan.grid_remove()

buttonforwardslash=ttk.Button(keysframe, text='/',  width=5, )
buttonforwardslash.grid(row=3, column=10)

buttonquestionmark=ttk.Button(keysframe, text='?',  width=5, )
buttonquestionmark.grid(row=3, column=10)
buttonquestionmark.grid_remove()

buttonshift1=ttk.Button(keysframe, text='Shift',  width=5,command=shift1 )
buttonshift1.grid(row=3, column=11)
buttonone=ttk.Button(keysframe, text='1', width=5, )
buttonone.grid(row=3, column=12)
buttontwo=ttk.Button(keysframe, text='2',  width=5, )
buttontwo.grid(row=3, column=13)
buttonthree=ttk.Button(keysframe, text='3',  width=5, )
buttonthree.grid(row=3, column=14)

#row5==
buttonSpace=ttk.Button(keysframe,text='space',width=38)
buttonSpace.grid(row=4,columnspan=40)
li=['buttona','buttonb','buttonc','buttond','buttone','buttonf','buttong','buttonh','buttoni','buttonj','buttonk','buttonl','buttonm','buttonn','buttono','buttonp','buttonq','buttonr','buttons','buttont','buttonu','buttonv','buttonw','buttonx','buttony','buttonz']
di={'buttona':buttona,'buttonb':buttonb,'buttonc':buttonc,'buttond':buttond,'buttone':buttone,'buttonf':buttonf,'buttong':buttong,'buttonh':buttonh,'buttoni':buttoni,'buttonj':buttonj,'buttonk':buttonk,'buttonl':buttonl,'buttonm':buttonm,'buttonn':buttonn,'buttono':buttono,'buttonp':buttonp,'buttonq':buttonq,'buttonr':buttonr,'buttons':buttons,'buttont':buttont,'buttonu':buttonu,'buttonv':buttonv,'buttonw':buttonw,'buttonx':buttonx,'buttony':buttony,'buttonz':buttonz}

#we have to bind here to the one <button-1>
#we have to bind each and every button except both the shift button
button1.bind('<Button-1>',select)
button2.bind('<Button-1>',select)
button3.bind('<Button-1>',select)
button4.bind('<Button-1>',select)
button5.bind('<Button-1>',select)
button6.bind('<Button-1>',select)
button7.bind('<Button-1>',select)
button8.bind('<Button-1>',select)
button9.bind('<Button-1>',select)
button0.bind('<Button-1>',select)
buttonminus.bind('<Button-1>',select)
buttonequal.bind('<Button-1>',select)
buttonback.bind('<Button-1>',select)
tildButton.bind('<Button-1>',select)
buttondelete.bind('<Button-1>',select)
for but in li:
    di[but].bind('<Button-1>', select)
buttoncolon.bind('<Button-1>',select)
buttoncomma.bind('<Button-1>',select)
buttonforwardslash.bind('<Button-1>',select)
buttoncaps.bind('<Button-1>',select)

buttonone.bind('<Button-1>',select)
buttontwo.bind('<Button-1>',select)
buttonthree.bind('<Button-1>',select)
buttonfour.bind('<Button-1>',select)
buttonfive.bind('<Button-1>',select)
buttonsix.bind('<Button-1>',select)
buttonseven.bind('<Button-1>',select)
buttoneight.bind('<Button-1>',select)
buttonnine.bind('<Button-1>',select)
buttonSpace.bind('<Button-1>',select)
buttonenter.bind('<Button-1>',select)
buttonopenbrac.bind('<Button-1>',select)
buttonTab.bind('<Button-1>',select)
buttonfullstop.bind('<Button-1>',select)
buttonCAPS.bind('<Button-1>',select)


buttonexclamtion.bind('<Button-1>',select)
buttonattehrate.bind('<Button-1>',select)
buttonhash.bind('<Button-1>',select)
buttondollar.bind('<Button-1>',select)
buttonpercent.bind('<Button-1>',select)
buttonpower.bind('<Button-1>',select)
buttonampersand.bind('<Button-1>',select)
buttoninto.bind('<Button-1>',select)
buttonopensmallbracket.bind('<Button-1>',select)
buttonclosesmallbracket.bind('<Button-1>',select)
buttonunderscore.bind('<Button-1>',select)
buttonplus.bind('<Button-1>',select)
buttonclosebrac.bind('<Button-1>',select)
aposthrophyButton.bind('<Button-1>',select)
buttonsemicolon.bind('<Button-1>',select)
buttonlessthan.bind('<Button-1>',select)
buttongreaterthan.bind('<Button-1>',select)
buttonquestionmark.bind('<Button-1>',select)

root.mainloop()