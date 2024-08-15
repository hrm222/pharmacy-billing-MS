from tkinter import *
import math, random, os
from tkinter import messagebox
from PIL import Image

class Super:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700+0+5')
        self.root.title('إدارة فواتير صيدلية')
        
        # Title Label
        title = Label(self.root, text='إدارة فواتير صيدلية', fg='white', bg='#0B2f3A', font=('tagawal', 15))
        title.pack(fill=X)
        #variables
        #مستلزمات اخرى
        self.q1 = IntVar()
        self.q2 = IntVar()
        self.q3 = IntVar()
        self.q4 = IntVar()
        self.q5 = IntVar()
        self.q6 = IntVar()
        self.q7 = IntVar()
        self.q8 = IntVar()
        self.q9 = IntVar()
        self.q10 = IntVar()
        self.q11 = IntVar()
        self.q12 = IntVar()
        self.q13 = IntVar()
        self.q14 = IntVar()
        self.q15 = IntVar()
        #مستحضرات التجميل
        self.qq1 = IntVar()
        self.qq2 = IntVar()
        self.qq3 = IntVar()
        self.qq4 = IntVar()
        self.qq5 = IntVar()
        self.qq6 = IntVar()
        self.qq7 = IntVar()
        self.qq8 = IntVar()
        self.qq9 = IntVar()
        self.qq10 = IntVar()
        self.qq11 = IntVar()
        self.qq12 = IntVar()
        self.qq13 = IntVar()
        self.qq14 = IntVar()
        self.qq15 = IntVar()
        #الأدوية
        #=============================
        self.qqq1 = IntVar()
        self.qqq2 = IntVar()
        self.qqq3 = IntVar()
        self.qqq4 = IntVar()
        self.qqq5 = IntVar()
        self.qqq6 = IntVar()
        self.qqq7 = IntVar()
        self.qqq8 = IntVar()
        self.qqq9 = IntVar()
        self.qqq10 = IntVar()
        self.qqq11 = IntVar()
        self.qqq12 = IntVar()
        self.qqq13 = IntVar()
        self.qqq14 = IntVar()
        self.qqq15 = IntVar()
        #=============================
        #متغيرات بيانات المشتري
        self.name = StringVar()
        self.phon = StringVar()
        self.fatora = StringVar()
        x = random.randint(1000,9999)
        self.fatora.set(str(x))
        #=============================
        #متغيرات الحساب الكلي
        self.other=StringVar()
        self.tagmel=StringVar()
        self.dwaa=StringVar()
        # Frame F1 for customer data
        F1 = Frame(root, bd=2, width=365, height=160, bg='#0B2f3A')
        F1.place(x=911, y=30)
        tit = Label(F1, text=':بيانات المشترى', font=('tagawal', 13, 'bold'), bg='#0B2f3A', fg='gold')
        tit.place(x=250, y=0)
        his_name = Label(F1, text='اسم المشترى', font=('tajawal', 11), bg='#0B2f3A', fg='white')
        his_name.place(x=290, y=40)
        his_phone = Label(F1, text='رقم المشترى', font=('tajawal', 11), bg='#0B2f3A', fg='white')
        his_phone.place(x=290, y=70)
        bill_num = Label(F1, text='رقم الفاتورة', font=('tajawal', 11), bg='#0B2f3A', fg='white')
        bill_num.place(x=290, y=100)
        Ent_name = Entry(F1, justify='center',textvariable=self.name)
        Ent_name.place(x=100, y=45)
        Ent_phone = Entry(F1, justify='center',textvariable=self.phon)
        Ent_phone.place(x=100, y=75)
        Ent_bill = Entry(F1, justify='center',textvariable=self.fatora)
        Ent_bill.place(x=100, y=105)
       
        # Frame F3 for displaying text
        titdd = Label(text="[الفواتير]", font=('tajawal', 13, 'bold'), bg='#0B2f3A', fg='gold')
        titdd.place(x=1100, y=165)
        F3 = Frame(root, bd=2, width=50, height=50, bg='#0B2f3A')
        F3.place(x=911, y=198)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3, yscrollcommand=scrol_y.set,width=43,height=24)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Frame F4 for buttons and entries
        F4 = Frame(root, bd=2, width=665, height=100, bg='#0B2f3A')
        F4.place(x=610, y=595)
        hesab = Button(F4, text="الحساب", width=13, height=1, font='tajawal', bg='#DBA901', command=self.total)
        hesab.place(x=500, y=10)
        fatora = Button(F4, text='تصدير الفاتورة', width=13, height=1, font='tajawal', bg='#DBA901',command=self.billing)
        fatora.place(x=500, y=50)
        clear = Button(F4, text='افراغ الحقول', width=13, height=1, font='tajawal', bg='#DBA901',command=self.clear)
        clear.place(x=370, y=10)
        exite = Button(F4, text='اغلاق البرنامج', width=13, height=1, font='tajawal', bg='#DBA901',command=self.close)
        exite.place(x=370, y=50)
        lblo1 = Label(F4, text='الحساب الكلي المستلزمات الأخرى ', font=('tajawal', 10, 'bold'), bg='#0B4C5F', fg='gold')
        lblo1.place(x=180, y=10)
        lblo2 = Label(F4, text='الحساب الكلي لمستحضرات التجميل', font=('tajawal', 10, 'bold'), bg='#0B4C5F', fg='gold')
        lblo2.place(x=180, y=40)
        lblo3 = Label(F4, text='الحساب الكلي  للأدوية', font=('tajawal', 10, 'bold'), bg='#0B4C5F', fg='gold')
        lblo3.place(x=180, y=70)
        ento1 = Entry(F4,textvariable=self.other, width=24)
        ento1.place(x=10, y=12)
        ento2 = Entry(F4,textvariable=self.tagmel, width=24)
        ento2.place(x=10, y=42)
        ento3 = Entry(F4,textvariable=self.dwaa, width=24)
        ento3.place(x=10, y=72)
        #---------Items---------
        FF1 = Frame(root,bd=2, width=300, height=700,bg='#0B4C5F')
        FF1.place(x=1,y=30)
        t = Label(FF1, text='مستلزمات أخرى', font=('tajawal', 15, 'bold'),bg=('#0B4C5F'),fg=('gold') )
        t.place(x=110,y=0)
       
        
       
 
        bq1= Label(FF1, text= 'مناديل ورقية',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq1.place(x=210,y=70)
        bq2= Label(FF1, text= 'كمامات',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq2.place(x=210,y=100)
        bq3= Label(FF1, text= 'قفازات',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq3.place(x=210,y=130)
        bq4= Label(FF1, text= 'معقمات',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq4.place(x=210,y=170)
        bq5= Label(FF1, text= 'أكياس',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq5.place(x=210,y=200)
        bq6= Label(FF1, text= 'رولات',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq6.place(x=210,y=230)
        bq7= Label(FF1, text= 'شباشب طبية',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq7.place(x=210,y=270)
        bq8= Label(FF1, text= 'ادوات تنظيف',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq8.place(x=210,y=300)
        bq9= Label(FF1, text= 'أدوات طبية',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq9.place(x=210,y=330)
        bq10= Label(FF1, text= 'علب بلاستيك',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq10.place(x=210,y=370)
        bq11= Label(FF1, text= 'منظفات',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq11.place(x=210,y=400)
        bq12= Label(FF1, text= 'كحول',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq12.place(x=210,y=430)
        bq13= Label(FF1, text= 'فازلين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq13.place(x=210,y=470)
        bq14= Label(FF1, text= 'كريمات العظام',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq14.place(x=210,y=500)
        bq15= Label(FF1, text= 'صابون',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bq15.place(x=210,y=530)
        
        bqent1= Entry(FF1, width= 12,textvariable=self.q1)
        bqent1.place(x=70,y=70)
        
        bqent2= Entry(FF1, width= 12,textvariable=self.q2)
        bqent2.place(x=70,y=100)
        
        bqent3= Entry(FF1, width= 12,textvariable=self.q3)
        bqent3.place(x=70,y=130)
        
        bqent4= Entry(FF1, width= 12,textvariable=self.q4)
        bqent4.place(x=70,y=170)
        
        bqent5= Entry(FF1, width= 12,textvariable=self.q5)
        bqent5.place(x=70,y=200)
        
        bqent6= Entry(FF1, width= 12,textvariable=self.q6)
        bqent6.place(x=70,y=230)
        
        bqent7= Entry(FF1, width= 12,textvariable=self.q7)
        bqent7.place(x=70,y=270)
        
        bqent8= Entry(FF1, width= 12,textvariable=self.q8)
        bqent8.place(x=70,y=300)
        
        bqent9= Entry(FF1, width= 12,textvariable=self.q9)
        bqent9.place(x=70,y=330)
        
        bqent10= Entry(FF1, width= 12,textvariable=self.q10)
        bqent10.place(x=70,y=370)
        
        bqent11= Entry(FF1, width= 12,textvariable=self.q11)
        bqent11.place(x=70,y=400)
        
        bqent12= Entry(FF1, width= 12,textvariable=self.q12)
        bqent12.place(x=70,y=430)
        
        bqent13= Entry(FF1, width= 12,textvariable=self.q13)
        bqent13.place(x=70,y=470)
        
        bqent14= Entry(FF1, width= 12,textvariable=self.q14)
        bqent14.place(x=70,y=500)
        
        bqent15= Entry(FF1, width= 12,textvariable=self.q15)
        bqent15.place(x=70,y=530)
        
        #-------Items[2]--------
        
        FF2 = Frame(root,bd=2, width=300, height=700,bg='#0B4C5F')
        FF2.place(x=305,y=30)
        
        tt = Label(FF2, text='مستحضرات التجميل', font=('tajawal', 15, 'bold'),bg=('#0B4C5F'),fg=('gold') )
        tt.place(x=100,y=0)
       
        
       
 
        bqr1= Label(FF2, text= 'روج',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr1.place(x=200,y=70)
        bqr2= Label(FF2, text= 'محدد عيون',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr2.place(x=200,y=100)
        bqr3= Label(FF2, text= 'ماسكرا',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr3.place(x=200,y=130)
        bqr4= Label(FF2, text= 'تونر',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr4.place(x=200,y=170)
        bqr5= Label(FF2, text= 'الجل',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr5.place(x=200,y=200)
        bqr6= Label(FF2, text= 'ماسك',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr6.place(x=200,y=230)
        bqr7= Label(FF2, text= 'سيروم',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr7.place(x=200,y=270)
        bqr8= Label(FF2, text= 'كريم نهاري',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr8.place(x=200,y=300)
        bqr9= Label(FF2, text= 'غسول وجه',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr9.place(x=200,y=330)
        bqr10= Label(FF2, text= 'كريم ليلي',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr10.place(x=200,y=370)
        bqr11= Label(FF2, text= 'ملمع اظافر',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr11.place(x=200,y=400)
        bqr12= Label(FF2, text= 'بلسم',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr12.place(x=200,y=430)
        bqr13= Label(FF2, text= 'كريم ترطيب',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr13.place(x=200,y=470)
        bqr14= Label(FF2, text= 'زيت شعر',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr14.place(x=200,y=500)
        bqr15= Label(FF2, text= 'شامبو',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqr15.place(x=200,y=530)
        
        bqrent1= Entry(FF2, width= 12,textvariable=self.qq1)
        bqrent1.place(x=70,y=70)
        
        bqrent2= Entry(FF2, width= 12,textvariable=self.qq2)
        bqrent2.place(x=70,y=100)
        
        bqrent3= Entry(FF2, width= 12,textvariable=self.qq3)
        bqrent3.place(x=70,y=130)
        
        bqrent4= Entry(FF2, width= 12,textvariable=self.qq4)
        bqrent4.place(x=70,y=170)
        
        bqrent5= Entry(FF2, width= 12,textvariable=self.qq5)
        bqrent5.place(x=70,y=200)
        
        bqrent6= Entry(FF2, width= 12,textvariable=self.qq6)
        bqrent6.place(x=70,y=230)
        
        bqrent7= Entry(FF2, width= 12,textvariable=self.qq7)
        bqrent7.place(x=70,y=270)
        
        bqrent8= Entry(FF2, width= 12,textvariable=self.qq8)
        bqrent8.place(x=70,y=300)
        
        bqrent9= Entry(FF2, width= 12,textvariable=self.qq9)
        bqrent9.place(x=70,y=330)
        
        bqrent10= Entry(FF2, width= 12,textvariable=self.qq10)
        bqrent10.place(x=70,y=370)
        
        bqrent11= Entry(FF2, width= 12,textvariable=self.qq11)
        bqrent11.place(x=70,y=400)
        
        bqrent12= Entry(FF2, width= 12,textvariable=self.qq12)
        bqrent12.place(x=70,y=430)
        
        bqrent13= Entry(FF2, width= 12,textvariable=self.qq13)
        bqrent13.place(x=70,y=470)
        
        bqrent14= Entry(FF2, width= 12,textvariable=self.qq14)
        bqrent14.place(x=70,y=500)
        
        bqrent15= Entry(FF2, width= 12,textvariable=self.qq15)
        bqrent15.place(x=70,y=530)
        #----------Items[3]---------------
        FF3 = Frame(root,bd=2, width=300, height=562,bg='#0B4C5F')
        FF3.place(x=610,y=30)
        ttt = Label(FF3, text='الأدوية', font=('tajawal', 15, 'bold'),bg=('#0B4C5F'),fg=('gold') )
        ttt.place(x=150,y=0)
       
        
       
 
        bqrt1= Label(FF3, text= 'ميثوتريكسات',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt1.place(x=210,y=70)
        bqrt2= Label(FF3, text= 'الباراسيتامول',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt2.place(x=210,y=100)
        bqrt3= Label(FF3, text= 'الاسبرين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt3.place(x=210,y=130)
        bqrt4= Label(FF3, text= 'بنادول',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt4.place(x=210,y=170)
        bqrt5= Label(FF3, text= 'ديكلوفيناك',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt5.place(x=210,y=200)
        bqrt6= Label(FF3, text= 'ايبوبروفين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt6.place(x=210,y=230)
        bqrt7= Label(FF3, text= 'سيفالكسين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt7.place(x=210,y=270)
        bqrt8= Label(FF3, text= 'البنسلين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt8.place(x=210,y=300)
        bqrt9= Label(FF3, text= 'الاريثروميسين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt9.place(x=210,y=330)
        bqrt10= Label(FF3, text= 'ميترونيدازول',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt10.place(x=210,y=370)
        bqrt11= Label(FF3, text= 'تيتراسايكلن',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt11.place(x=210,y=400)
        bqrt12= Label(FF3, text= 'نيستاتين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt12.place(x=210,y=430)
        bqrt13= Label(FF3, text= 'فلوكونازول',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt13.place(x=210,y=470)
        bqrt14= Label(FF3, text= 'الكلورامفينيكول',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt14.place(x=210,y=500)
        bqrt15= Label(FF3, text= 'بيسيليامين',font=('tajawal', 11),bg='#0B4C5F',fg='white' )
        bqrt15.place(x=210,y=530)
        
        bqrtent1= Entry(FF3, width= 12,textvariable=self.qqq1)
        bqrtent1.place(x=70,y=70)
        
        bqrtent2= Entry(FF3, width= 12,textvariable=self.qqq2)
        bqrtent2.place(x=70,y=100)
        
        bqrtent3= Entry(FF3, width= 12,textvariable=self.qqq3)
        bqrtent3.place(x=70,y=130)
        
        bqrtent4= Entry(FF3, width= 12,textvariable=self.qqq4)
        bqrtent4.place(x=70,y=170)
        
        bqrtent5= Entry(FF3, width= 12,textvariable=self.qqq5)
        bqrtent5.place(x=70,y=200)
        
        bqrtent6= Entry(FF3, width= 12,textvariable=self.qqq6)
        bqrtent6.place(x=70,y=230)
        
        bqrtent7= Entry(FF3, width= 12,textvariable=self.qqq7)
        bqrtent7.place(x=70,y=270)
        
        bqrtent8= Entry(FF3, width= 12,textvariable=self.qqq8)
        bqrtent8.place(x=70,y=300)
        
        bqrtent9= Entry(FF3, width= 12,textvariable=self.qqq9)
        bqrtent9.place(x=70,y=330)
        
        bqrtent10= Entry(FF3, width= 12,textvariable=self.qqq10)
        bqrtent10.place(x=70,y=370)
        
        bqrtent11= Entry(FF3, width= 12,textvariable=self.qqq11)
        bqrtent11.place(x=70,y=400)
        
        bqrtent12= Entry(FF3, width= 12,textvariable=self.qqq12)
        bqrtent12.place(x=70,y=430)
        
        bqrtent13= Entry(FF3, width= 12,textvariable=self.qqq13)
        bqrtent13.place(x=70,y=470)
        
        bqrtent14= Entry(FF3, width= 12,textvariable=self.qqq14)
        bqrtent14.place(x=70,y=500)
        
        bqrtent15= Entry(FF3, width= 12,textvariable=self.qqq15)
        bqrtent15.place(x=70,y=530)
        self.welcome()
    def total(self):
        self.tusses = self.q1.get()*2.5
        self.kemama = self.q2.get()*2
        self.gloves = self.q3.get()*3
        self.sterilizers = self.q4.get()*50
        self.bags = self.q5.get()*10
        self.roles = self.q6.get()*15
        self.medical_slippers = self.q7.get()*60
        self.cleaning_tools = self.q8.get()*40
        self.medical_tools = self.q9.get()*70
        self.blastic_bottle = self.q10.get()*10
        self.cleaners = self.q11.get()*30
        self.alchohol = self.q12.get()*20
        self.vaseline = self.q13.get()*60
        self.bone_creams = self.q14.get()*100
        self.soaps = self.q15.get()*15
        self.total1 = float(
            self.tusses+
            self.kemama+
            self.gloves+
            self.sterilizers+
            self.bags+
            self.roles+
            self.medical_slippers+
            self.cleaning_tools+
            self.medical_tools+
            self.blastic_bottle+
            self.cleaners+
            self.alchohol+
            self.vaseline+
            self.bone_creams+
            self.soaps
        )
        self.other.set(str(self.total1)+" $ ")

        self.roge = self.qq1.get()*10
        self.eyelighner = self.qq2.get()*50
        self.maskara = self.qq3.get()*30
        self.toner = self.qq4.get()*5
        self.gel = self.qq5.get()*30
        self.mask = self.qq6.get()*60
        self.serum = self.qq7.get()*200
        self.white_cream = self.qq8.get()*50
        self.wash_cleanser = self.qq9.get()*100
        self.night_cream = self.qq10.get()*50
        self.acetone = self.qq11.get()*15
        self.balsam = self.qq12.get()*70
        self.kinder_cr = self.qq13.get()*100
        self.hair_oil = self.qq14.get()*50
        self.shampoo = self.qq15.get()*80
        self.total2 = float(
            self.roge+
            self.eyelighner+
            self.maskara+
            self.toner+
            self.gel+
            self.mask+
            self.serum+
            self.white_cream+
            self.wash_cleanser+
            self.night_cream+
            self.acetone+
            self.balsam+
            self.kinder_cr+
            self.hair_oil+
            self.shampoo

        )
        self.tagmel.set(str(self.total2)+" $ ")


        self.methotrexate = self.qqq1.get()*10
        self.paracetamol = self.qqq2.get()*50
        self.aspiren = self.qqq3.get()*30
        self.panadol = self.qqq4.get()*5
        self.diclophinace = self.qqq5.get()*30
        self.ipubrufen = self.qqq6.get()*60
        self.cifalcasin = self.qqq7.get()*200
        self.pensilene = self.qqq8.get()*50
        self.arithromycin = self.qqq9.get()*100
        self.metronidazole = self.qqq10.get()*50
        self.tetracycline = self.qqq11.get()*15
        self.nystatine = self.qqq12.get()*70
        self.fluconazole = self.qqq13.get()*100
        self.chloramifinichole = self.qqq14.get()*50
        self.bycelyamine = self.qqq15.get()*80
        self.total3 = float(
            self.methotrexate+
            self.paracetamol+
            self.aspiren+
            self.panadol+
            self.diclophinace+
            self.ipubrufen+
            self.cifalcasin+
            self.pensilene+
            self.arithromycin+
            self.metronidazole+
            self.tetracycline+
            self.nystatine+
            self.fluconazole+
            self.chloramifinichole+
            self.bycelyamine

        )
        self.dwaa.set(str(self.total3)+ " $ ")
        self.all = float(self.total1+
                         self.total2+ 
                         self.total3
                         )     

    def welcome(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome To Our Pharmacy")
        self.textarea.insert(END,"\n*******************************************")
        self.textarea.insert(END,f"\n\t B.NUM  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t NAME   :{self.name.get()}")
        self.textarea.insert(END,f"\n\t PHONE  :{self.phon.get()}")
        self.textarea.insert(END,"\n*******************************************")
        self.textarea.insert(END,f"\nالسعر\t        العدد\t          المشتريات")
        self.textarea.insert(END,"\n*******************************************")

    
    def clear(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        #####################
        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        #####################
        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)
        ######################
        self.other.set(0)
        self.tagmel.set(0)
        self.dwaa.set(0)
        ######################
        self.name.set('')
        self.phon.set('')
        self.fatora.set('')
    def close(self):
        self.root.destroy()
    
    def save(self):
        op = messagebox.askyesno("حفظ","هل تريد حفظ الفاتورة")
        if op>0:
            self.bb = self.textarea.get('1.0',END)
            f1 =open('"C:\\Users\\ahmed\\OneDrive\\Bureau\\bills"'+str(self.fatora.get())+".txt","w",encoding="utf-8")
            f1.write(self.bb)
            f1.close()
        else:
            return
    def billing(self):
        if self.name.get()=="" or self.phon.get()=="":
            messagebox.showerror("لا يجوز ترك حقل الاسم و رقم الهاتف فارغ")
        elif self.other.get()=="0.0 $" and self.tagmel.get()=="0.0 $" and self.dwaa.get()=="0.0 $":
            messagebox.showerror("لم تقم بتحديد اي منتجات لشراىْها")
        else:
            self.welcome()
            if self.q1.get()!=0:
                self.textarea.insert(END,f"\n {self.tusses}\t\t{self.q1.get()}\t مناديل ورقية")
            if self.q2.get()!=0:
                self.textarea.insert(END,f"\n {self.kemama}\t\t{self.q2.get()}\t كمامات")
            if self.q3.get()!=0:
                self.textarea.insert(END,f"\n {self.gloves}\t\t{self.q3.get()}\t قفازات")
            if self.q4.get()!=0:
                self.textarea.insert(END,f"\n {self.sterilizers}\t\t{self.q4.get()}\t معقمات")
            if self.q5.get()!=0:
                self.textarea.insert(END,f"\n {self.bags}\t\t{self.q5.get()}\t اْكياس")
            if self.q6.get()!=0:
                self.textarea.insert(END,f"\n {self.roles}\t\t{self.q6.get()}\t رولات")
            if self.q7.get()!=0:
                self.textarea.insert(END,f"\n {self.medical_slippers}\t\t{self.q7.get()}\t  شباشب")
            if self.q8.get()!=0:
                self.textarea.insert(END,f"\n {self.cleaning_tools}\t\t{self.q8.get()}\t ادوات تنظيف ")
            if self.q9.get()!=0:
                self.textarea.insert(END,f"\n {self.blastic_bottle}\t\t{self.q9.get()}\t  علب بلاستيك")
            if self.q10.get()!=0:
                self.textarea.insert(END,f"\n {self.cleaners}\t\t{self.q10.get()}\t  منظفات")
            if self.q11.get()!=0:
                self.textarea.insert(END,f"\n {self.alchohol}\t\t{self.q11.get()}\t كحول")
            if self.q12.get()!=0:
                self.textarea.insert(END,f"\n {self.vaseline}\t\t{self.q12.get()}\t فازلين")
            if self.q13.get()!=0:
                self.textarea.insert(END,f"\n {self.bone_creams}\t\t{self.q13.get()}\t  كريم ")
            if self.q14.get()!=0:
                self.textarea.insert(END,f"\n {self.soaps}\t\t{self.q14.get()}\t صابون ")
            ###############################################################################
            if self.qq1.get()!=0:
                self.textarea.insert(END,f"\n {self.roge}\t\t{self.qq1.get()}\t روج")
            if self.qq2.get()!=0:
                self.textarea.insert(END,f"\n {self.eyelighner}\t\t{self.qq2.get()}\t محدد عيون")
            if self.qq3.get()!=0:
                self.textarea.insert(END,f"\n {self.maskara}\t\t{self.qq3.get()}\t ماسكارا")
            if self.qq4.get()!=0:
                self.textarea.insert(END,f"\n {self.toner}\t\t{self.qq4.get()}\t تونر")
            if self.qq5.get()!=0:
                self.textarea.insert(END,f"\n {self.gel}\t\t{self.qq5.get()}\t جل")
            if self.qq6.get()!=0:
                self.textarea.insert(END,f"\n {self.mask}\t\t{self.qq6.get()}\t ماسك")
            if self.qq7.get()!=0:
                self.textarea.insert(END,f"\n {self.serum}\t\t{self.qq7.get()}\t سيروم")
            if self.qq8.get()!=0:
                self.textarea.insert(END,f"\n {self.white_cream}\t\t{self.qq8.get()}\t كريم نهاري")
            if self.qq9.get()!=0:
                self.textarea.insert(END,f"\n {self.wash_cleanser}\t\t{self.qq9.get()}\t غسول وجه")
            if self.qq10.get()!=0:
                self.textarea.insert(END,f"\n {self.night_cream}\t\t{self.qq10.get()}\t ملمع اظافر")
            if self.qq11.get()!=0:
                self.textarea.insert(END,f"\n {self.acetone}\t\t{self.qq11.get()}\t اسيتون")
            if self.qq12.get()!=0:
                self.textarea.insert(END,f"\n {self.balsam}\t\t{self.qq12.get()}\t بلسم ")
            if self.qq13.get()!=0:
                self.textarea.insert(END,f"\n {self.kinder_cr}\t\t{self.qq13.get()}\t كريم ترطيب")
            if self.qq14.get()!=0:
                self.textarea.insert(END,f"\n {self.hair_oil}\t\t{self.qq14.get()}\t زيت شعر")
            if self.qq15.get()!=0:
                self.textarea.insert(END,f"\n {self.shampoo}\t\t{self.qq15.get()}\t شامبو")
            ############################################################################
            if self.qqq1.get()!=0:
                self.textarea.insert(END,f"\n {self.methotrexate}\t\t{self.qqq1.get()}\t ميثوتريكسات")
            if self.qqq2.get()!=0:
                self.textarea.insert(END,f"\n {self.paracetamol}\t\t{self.qqq2.get()}\t باراستومول")
            if self.qqq3.get()!=0:
                self.textarea.insert(END,f"\n {self.aspiren}\t\t{self.qqq3.get()}\t اسبرين")
            if self.qqq4.get()!=0:
                self.textarea.insert(END,f"\n {self.panadol}\t\t{self.qqq4.get()}\t بنادول")
            if self.qqq5.get()!=0:
                self.textarea.insert(END,f"\n {self.diclophinace}\t\t{self.qqq5.get()}\t ديكلوفيناك")
            if self.qqq6.get()!=0:
                self.textarea.insert(END,f"\n {self.ipubrufen}\t\t{self.qqq6.get()}\t ايبورفين")
            if self.qqq7.get()!=0:
                self.textarea.insert(END,f"\n {self.cifalcasin}\t\t{self.qqq7.get()}\t سيفالكسين")
            if self.qqq8.get()!=0:
                self.textarea.insert(END,f"\n {self.pensilene}\t\t{self.qqq8.get()}\t بنسلين")
            if self.qqq9.get()!=0:
                self.textarea.insert(END,f"\n {self.arithromycin}\t\t{self.qqq9.get()}\t اريثروميسين")
            if self.qqq10.get()!=0:
                self.textarea.insert(END,f"\n {self.metronidazole}\t\t{self.qqq10.get()}\t ميترونيدازول")
            if self.qqq11.get()!=0:
                self.textarea.insert(END,f"\n {self.tetracycline}\t\t{self.qqq11.get()}\t تيتراسين")
            if self.qqq12.get()!=0:
                self.textarea.insert(END,f"\n {self.nystatine}\t\t{self.qqq12.get()}\t نيستاترين")
            if self.qqq13.get()!=0:
                self.textarea.insert(END,f"\n {self.fluconazole}\t\t{self.qqq13.get()}\t فلوكونازول")
            if self.qqq14.get()!=0:
                self.textarea.insert(END,f"\n {self.chloramifinichole}\t\t{self.qqq14.get()}\t كولوراميفينيكول")
            if self.qqq15.get()!=0:
                self.textarea.insert(END,f"\n {self.bycelyamine}\t\t{self.qqq15.get()}\t بيسيليامين")

            self.textarea.insert(END,"\n.......................................")
            self.textarea.insert(END,f"\n\t{self.all} $\t        المجموع الكلي" )
            self.textarea.insert(END,"\n.......................................")
            self.save()
        
root = Tk()
app = Super(root)
root.mainloop()
