#from posix import listdir
from tkinter import*
import math
import os
import random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1528x828+0+0")
        self.root.title("Faruq Software")
        bg_color = "#074463"
        title = Label(self.root, text="**********Shop App**********", bd=14, relief=GROOVE, bg=bg_color, fg="white", font=(
            "times new roman", 30, "bold"), pady=2).pack(fill=X)

        #===========Variables==========================#
        # ja variabele asbe ta store hobe tarpor show korbe #
        #===========Cosmetics==========================#
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        self.haircut = IntVar()
        self.powder = IntVar()

        #===========Grocery==========================#
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        self.cotpoti = IntVar()
        self.fucka = IntVar()

        #===========Cold drinks==========================#

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        self.spreed = IntVar()
        self.mojo = IntVar()

        #===========Total product price and tax variable==========================#
        #akhane type hbe string#
        #akhane calculte korar dorkar nai opor theke calculate hoa ase akhane show hobe#

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        #===========Customer er jonno==========================#

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()

        # 4 no work ata aka akai genrate e click korle auto show korbe bill area te.......
        # tar jonno self.bill_no = StringVar() to ata amra customer e initaial vabe define kore rakhcilam akhane ata akta search bill
        # to atar nice banabo  aka akai show korbe jeta to akhane tar jonno 1st package import kora lagbe import math,random #
        x = random.randint(1000, 9999)
        # akhane x variable er vitor random dia randint dia atar value ta set kore dilam
        self.bill_no.set(str(x))
        #akhane self er vitor billno set kore dibo tarpor str dia x k pass kore dibo jeta random vabe generate kore asbe#
        #arpor nice cole jabo welcome_bill er nice#
        self.search_bill = StringVar()

        # akhon ai variable gulo details frem e add korbo#

        #============Customer Detail Frame=============#

        F1 = LabelFrame(self.root, bd=9, relief=GROOVE, text="Customer Details", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=(
            "times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=20, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Phone no", bg=bg_color, fg="white", font=(
            "times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=20, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=(
            "times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=20, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7,
                          font="arial 12 bold").grid(row=0, column=6, padx=10, pady=10)

        bill_btn = Button(F1, text="OK", width=4, bd=7,
                          font="arial 12 bold").grid(row=0, column=7, padx=10, pady=10)

        #==============Cosmetics Frame================#
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=5, y=180, width=325, height=490)

        #===now cosmetics content set=====#

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman", 16, "bold"),
                         bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        bath_txt = Entry(F2, width=10, textvariable=self.soap, font=("times new roman", 16, "bold"),
                         bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        #==another same add korbo tai jonno#
        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold"),
                               bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        Face_cream_txt = Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"),
                               bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        Face_w_txt = Entry(F2, width=10, textvariable=self.face_wash, font=("times new roman", 16, "bold"),
                           bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        Hair_s_txt = Entry(F2, width=10, textvariable=self.spray, font=("times new roman", 16, "bold"),
                           bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gell", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        Hair_g_txt = Entry(F2, width=10, textvariable=self.gell, font=("times new roman", 16, "bold"),
                           bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        Body_l_lbl = Label(F2, text="Body Loshan ", font=("times new roman", 16, "bold"),
                           bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        Body_l_txt = Entry(F2, width=10, textvariable=self.loshan, font=("times new roman", 16, "bold"),
                           bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        haircut_l_lbl = Label(F2, text="Haircut ", font=("times new roman", 16, "bold"),
                              bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        haircut_l_txt = Entry(F2, width=10, textvariable=self.haircut, font=("times new roman", 16, "bold"),
                              bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        powder_l_lbl = Label(F2, text="Powder ", font=("times new roman", 16, "bold"),
                             bg=bg_color, fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        powder_l_txt = Entry(F2, width=10, textvariable=self.powder, font=("times new roman", 16, "bold"),
                             bd=5, relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)

        #2 akhane amra onno colum banabo same#

        #==============Grocery Frame================#
        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Food", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=340, y=180, width=325, height=490)

        #===now cosmetics content set=====#

        g1_lbl = Label(F3, text="Rice", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g1_txt = Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        #==another same add korbo tai jonno#
        g2_lbl = Label(F3, text="Food oil", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g2_txt = Entry(F3, width=10, textvariable=self.food_oil, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_lbl = Label(F3, text="Daal", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g3_txt = Entry(F3, width=10, textvariable=self.daal, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3, text="Wheat", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g4_txt = Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3, text="Sugar", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g5_txt = Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3, text="Tea", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g6_txt = Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        g7_lbl = Label(F3, text="Cotpoti", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g7_txt = Entry(F3, width=10, textvariable=self.cotpoti, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        g8_lbl = Label(F3, text="Fucka", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        g8_txt = Entry(F3, width=10, textvariable=self.fucka, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)

        #2 akhane amra onno colum banabo same#

        #==============drinks Frame================#
        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Drink's", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=675, y=180, width=325, height=490)

        #===now cosmetics content set=====#

        h1_lbl = Label(F4, text="Maza", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h1_txt = Entry(F4, width=10, textvariable=self.maza, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        #==another same add korbo tai jonno#
        h2_lbl = Label(F4, text="Cock", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h2_txt = Entry(F4, width=10, textvariable=self.cock, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        h3_lbl = Label(F4, text="Frooti", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h3_txt = Entry(F4, width=10, textvariable=self.frooti, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        h4_lbl = Label(F4, text="Tumbs Up", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h4_txt = Entry(F4, width=10, textvariable=self.thumbsup, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        h5_lbl = Label(F4, text="Limca", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h5_txt = Entry(F4, width=10, textvariable=self.limca, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        h6_lbl = Label(F4, text="Sprite", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h6_txt = Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        h7_lbl = Label(F4, text="Spreed", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h7_txt = Entry(F4, width=10, textvariable=self.spreed, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=6, column=1, padx=10, pady=10)

        h8_lbl = Label(F4, text="Mojo", font=("times new roman", 16, "bold"),
                       bg=bg_color, fg="lightgreen").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        #sticky use holo karon center show na hower jonno#
        h8_txt = Entry(F4, width=10, textvariable=self.mojo, font=("times new roman", 16, "bold"),
                       bd=5, relief=SUNKEN).grid(row=7, column=1, padx=10, pady=10)

        #==== BIll Area ===#
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=522, height=490)
        bill_title = Label(
            F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)  # orientation vartical#
        # scrollbar kothai nibo seta akhane define kora hoice#
        self.textarea = Text(F5, yscrollcommand=scrol_y.set)
        #self dewa hoice karo global vabe space nibe tarpor text e add hobe and yscrollbarcomand e set hbe#
        # scrol_y pack korbo seta kkora hoice right and fill hbe y karon bodycally fill hbe#
        scrol_y.pack(side=RIGHT, fill=Y)
        # scrol_y k config korbo pack korar por
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #akhon ata korar por dekhte parbo j run korle scrol bar tototukui kore ace ata norocara korcena height baralew sthir hoa ace#
        # tar jonno korbo holo self.textarea.pack(fill=BOTH,expand=1) ata kore dile hoa holo bodar fill hoa jabe and scroll bar kaj korbe#

        #====akhon nice menu button add korbo=====#
        #========== Bill Button Frame =========#

        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=673, relwidth=1, height=166)

        m1 = Label(F6, text="Total Cosmetics Price", bg=bg_color, fg="white", font=(
            "time new roamn", 14, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)

        m2 = Label(F6, text="Total Grocery Price", bg=bg_color, fg="white", font=(
            "time new roamn", 14, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        m3 = Label(F6, text="Total Drink's Price", bg=bg_color, fg="white", font=(
            "time new roamn", 14, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)

        c1 = Label(F6, text="Cosmetics Tax", bg=bg_color, fg="white", font=(
            "time new roamn", 14, "bold")).grid(row=0, column=2, padx=20, pady=5, sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        c2 = Label(F6, text="Grocery Tax", bg=bg_color, fg="white", font=(
            "time new roamn", 14, "bold")).grid(row=1, column=2, padx=20, pady=5, sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)

        c3 = Label(F6, text="Drink's Tax", bg=bg_color, fg="white", font=(
            "time new roamn", 14, "bold")).grid(row=2, column=2, padx=20, pady=5, sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7,
                       relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)

        #========= Button frem er jonno kora last konai ======= #

        btn_F = Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=755, width=750, height=110)

        #=== Button er vitor 4 button add korbo ======#

        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=0, padx=5, pady=5)

        GBill_btn = Button(btn_F, text="Genrate Bill", command=self.bill_area, bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=1, padx=5, pady=5)

        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=2, padx=5, pady=5)

        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=3, padx=5, pady=5)

        Delete_btn = Button(btn_F, text="Delete", bg="cadetblue", fg="white", bd=2, pady=15, width=10, font="arial 15 bold").grid(
            row=0, column=4, padx=5, pady=5)

        self.welcome_bill()

    def total(self):
        #akhane je string variable banaici seta intver ja ace sob gula asssign korbo ta nicer column e show hbe tar jonno#
        #tar jonno new variable bania tar vitore kaj#

        # 7 no kaj nic theke akhane korbo. akhane sb ak variable change kore dibo
        self.c_s_p = self.soap.get()*40
        self.c_fc_p = self.face_cream.get()*120
        self.c_fw_p = self.face_wash.get()*60
        self.c_hs_p = self.spray.get()*180
        self.c_hg_p = self.gell.get()*140
        self.c_bl_p = self.loshan.get()*180
        self.c_hc_p = self.haircut.get()*50
        self.c_pd_p = self.powder.get()*80
        # avabe variable change korlam er por nice j (self.soap.get()*40) ata assign kore dibo r aiat jaigai oi variable ta dia dibo#
        # avabe sob kore nibo ja ace sob#
        self.total_cosmetic_price = float(
            self.c_s_p +
            self.c_fc_p +
            self.c_fw_p +
            self.c_hs_p +
            self.c_hg_p +
            self.c_bl_p +
            self.c_hc_p +
            self.c_pd_p
        )
        #ai ja variable e store hoice total cosmetic er variable ke  self.cosmetic_price atake .set function er help e self.total_cosmetic_price add kore dibo......#
        # to atar por ai pura result int e asbe to atake self.total_cosmetic_price ar age str kore dibo (str(self.total_cosmetic_price))

        self.cosmetic_price.set("TK. "+str(self.total_cosmetic_price))

        #round add korlam amader onk valu aste pare tr jonno.#
        # atar nice self.cosmetic_tax.set(str(self.total_cosmetic_price*0.05))
        #ata bosabo  atar bekkha holo j self.cosmetic_tax.set add korbo tarpor total_cosmetic_price ata self e add korbo and tarpor multiple korbo * joto tax amra nite cai product er opor seta add korbo *0.05#
        # update 8 no work
        self.c_tax = round((self.total_cosmetic_price*0.05), 2)
        self.cosmetic_tax.set("TK. "+str(self.c_tax))
        # atotuku age cilo 8 no work er jonno update work korbo self.cosmetic_tax.set(
        #"TK. "+str(round((self.total_cosmetic_price*0.05), 2)))#

        # akhon total functio k call kori total_btn jeta ace okhane btn_f er pore command=self.total korle#
        #kaj kora suru korbe run korle dekhbo 0 ase gece karon kono jinish add korini tai jonno. 0.0 anar jonno  self.total_cosmetic_price= atar pore float set kore dibo#

        #to ata gelo total cosmetics er proice er kaj#

        #------akhon same vabe grocary er kaj korbo--------#

        # 7 no work akivabe akhane korte hbe#
        self.g_r_p = self.rice.get()*80
        self.g_f_p = self.food_oil.get()*180
        self.g_d_p = self.daal.get()*80
        self.g_w_p = self.wheat.get()*60
        self.g_s_p = self.sugar.get()*45
        self.g_t_p = self.tea.get()*150
        self.g_c_p = self.cotpoti.get()*30
        self.g_fc_p = self.fucka.get()*30

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_f_p +
            self.g_d_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p +
            self.g_c_p +
            self.g_fc_p
        )
        #ai ja variable e store hoice total cosmetic er variable ke  self.cosmetic_price atake .set function er help e self.total_cosmetic_price add kore dibo......#
        # to atar por ai pura result int e asbe to atake self.total_cosmetic_price ar age str kore dibo (str(self.total_cosmetic_price))

        self.grocery_price.set("TK. "+str(self.total_grocery_price))
        # update 8 no work
        self.g_tax = round((self.total_grocery_price*0.1), 2)
        self.grocery_tax.set(
            "TK. "+str(self.g_tax))
        # atotuku age cilo 8 no work er jonno update work korbo self.grocery_tax.set(
        # "TK. "+str(round((self.total_grocery_price*0.1), 2)))

        #--------akhon banabo drinks er jonno--------#

        # 7 no work atar jonno#
        self.d_m_p = self.maza.get()*60
        self.d_c_p = self.cock.get()*60
        self.d_f_p = self.frooti.get()*50
        self.d_t_p = self.thumbsup.get()*45
        self.d_l_p = self.limca.get()*40
        self.d_s_p = self.sprite.get()*60
        self.d_sp_p = self.spreed.get()*40
        self.d_mo_p = self.mojo.get()*40
        self.total_drinks_price = float(
            self.d_m_p +
            self.d_c_p +
            self.d_f_p +
            self.d_t_p +
            self.d_l_p +
            self.d_s_p +
            self.d_sp_p +
            self.d_mo_p
            #7 no work atotuku ses korar por abar nice cole jabo bill_area te price show korabo#
        )
        #ai ja variable e store hoice total cosmetic er variable ke  self.cosmetic_price atake .set function er help e self.total_cosmetic_price add kore dibo......#
        # to atar por ai pura result int e asbe to atake self.total_cosmetic_price ar age str kore dibo (str(self.total_cosmetic_price))

        self.cold_drink_price.set("TK. "+str(self.total_drinks_price))
        # update 8 no work
        self.d_tax = round((self.total_drinks_price*0.05), 2)
        self.cold_drink_tax.set(
            "TK. "+str(self.d_tax))
        # atotuku age cilo 8 no work er jonno update work korbo self.cold_drink_tax.set(
        # "TK. "+str(round((self.total_drinks_price*0.05), 2)))
        # tk likha anar jonno self.cold_drink_price.set("tk. "str+(self.total_drinks_price))
        # 3 no 1 2 kaj holo price r tax er kaj koreci...#
        # 3 no ----------------------------akhon amra korbo genrate bill e click korle ja aja value diacci product e seta bill area te dekhabe tar bill area te kaj korbo-----------------------------------#

        #8 no work total sum calculate#
        self.Total_bill = float(self.total_cosmetic_price +
                                self.total_grocery_price +
                                self.total_drinks_price +
                                self.c_tax +
                                self.g_tax +
                                self.d_tax
                                )
        # then agula sob gulak print korabo bill area te nice jabo
    #1st welcome show korbe#
    #5 no work holo welcome ta jokhon general bill e click korbo tokhon show korbe...............#
    #tar jonno jabo jekhane generate bill btn ace sekhane jabo akhane call korbo Genrate Bill ar pore command=self.welcome_bill#

    def welcome_bill(self):
        self.textarea.delete('1.0', END)
        #atar vitore self.text area jeta ace seta insert korbo tarpor end diaci karon end e show korbe welcome ta END,"\tWelcome Webcode Reatil"#
        #akhon run hobe tar jonno aka akai call hoa jabe tai  tar jonno opore cole jabo code add korbo#
        # seta holo total_btn ace sekhane tar nice akdom nice self.welcome_bill() ata set kore dibo call korbe ata akhon run#
        self.textarea.insert(END, "\t\t\tWelcome Webcode Reatil\n")
        #74 line por akhane kaj korbo #
        #bill no#
        self.textarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        # akhon akhane je bill variable banaicilam atake define korbo  f string use korbo tarpor ata {self.bill_no.get()} set korbo#
        #customer#
        #same oporer moto#
        self.textarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        #customer no#
        self.textarea.insert(END, f"\n Phone Number : {self.c_phone.get()}\n")

        # Total er jonno kaj#
        self.textarea.insert(
            END, f"\n============================================================")

        self.textarea.insert(
            END, f"\n Products\t\t\tQTY\t\t\tPrice")

        self.textarea.insert(
            END, f"\n============================================================")
        # total er kaj atotuku korar por bill area te jabo#nice

    def bill_area(self):
        # 9 no work
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
            # 9 no work item er jonno check korbo
        elif self.cosmetic_price.get() == "TK. 0.0" and self.grocery_price.get() == "TK. 0.0" and self.cold_drink_price.get() == "TK. 0.0":
            messagebox.showerror("Error", "No Product Puchased")
        else:

            self.welcome_bill()
            # self dia welcome k call korci
            #tar por akhane constructor calabo for loop calabo if else akhane if colle 0 ace condition order e secunce check korbo 1st 2nd 3rd 0 ace ta bill area print hbena not 0 proint hbe and countaty and price total print hbe bill area te#

            # =========================cosmetics er jonno price add================#
            if self.soap.get() != 0:
                # if condition diaci jodi not eqal 0 hoi tahole
                #opore 7 no work ses korar por akhane kaj korbo price show korbo#
                # atotuku kaj holo price show korar tar por Bill_area ta print korar jonno  btn cole jabo okhane bill e welcome_bill er akhane bill_area dia dibo#

                #{self.c_s_p} avabe nice sob variable gula add kore dibo#

                self.textarea.insert(
                    END, f"\n Bath Soap\t\t\t{self.soap.get()}\t\t\t{self.c_s_p}")

            if self.face_cream.get() != 0:
                self.textarea.insert(
                    END, f"\n Face cream\t\t\t{self.face_cream.get()}\t\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.textarea.insert(
                    END, f"\n Face Wash\t\t\t{self.face_wash.get()}\t\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.textarea.insert(
                    END, f"\n Spray\t\t\t{self.spray.get()}\t\t\t{self.c_hs_p}")
            if self.gell.get() != 0:
                self.textarea.insert(
                    END, f"\n Hair Gell\t\t\t{self.gell.get()}\t\t\t{self.c_hg_p}")
            if self.loshan.get() != 0:
                self.textarea.insert(
                    END, f"\n Body Loshan\t\t\t{self.loshan.get()}\t\t\t{self.c_bl_p}")
            if self.haircut.get() != 0:
                self.textarea.insert(
                    END, f"\n Haircut\t\t\t{self.haircut.get()}\t\t\t{self.c_hc_p}")
            if self.powder.get() != 0:
                self.textarea.insert(
                    END, f"\n Powder\t\t\t{self.powder.get()}\t\t\t{self.c_pd_p}")

            # =========================Grocery er jonno price add================#
            if self.rice.get() != 0:
                self.textarea.insert(
                    END, f"\n Rice\t\t\t{self.rice.get()}\t\t\t{self.g_r_p}")
            if self.food_oil.get() != 0:
                self.textarea.insert(
                    END, f"\n Food Oil\t\t\t{self.food_oil.get()}\t\t\t{self.g_f_p}")
            if self.daal.get() != 0:
                self.textarea.insert(
                    END, f"\n Daal\t\t\t{self.daal.get()}\t\t\t{self.g_d_p}")
            if self.wheat.get() != 0:
                self.textarea.insert(
                    END, f"\n Wheat\t\t\t{self.wheat.get()}\t\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.textarea.insert(
                    END, f"\n Sugar\t\t\t{self.sugar.get()}\t\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.textarea.insert(
                    END, f"\n Tea\t\t\t{self.tea.get()}\t\t\t{self.g_t_p}")
            if self.cotpoti.get() != 0:
                self.textarea.insert(
                    END, f"\n Cotpoti\t\t\t{self.cotpoti.get()}\t\t\t{self.g_c_p}")
            if self.fucka.get() != 0:
                self.textarea.insert(
                    END, f"\n Fucka\t\t\t{self.fucka.get()}\t\t\t{self.g_fc_p}")

                # =========================Drink's er jonno price add================#
            if self.maza.get() != 0:
                self.textarea.insert(
                    END, f"\n Rice\t\t\t{self.maza.get()}\t\t\t{self.d_m_p}")
            if self.cock.get() != 0:
                self.textarea.insert(
                    END, f"\n Cock\t\t\t{self.cock.get()}\t\t\t{self.d_c_p}")
            if self.frooti.get() != 0:
                self.textarea.insert(
                    END, f"\n Frooti\t\t\t{self.frooti.get()}\t\t\t{self.d_f_p}")
            if self.thumbsup.get() != 0:
                self.textarea.insert(
                    END, f"\n Thumbsup\t\t\t{self.thumbsup.get()}\t\t\t{self.d_t_p}")
            if self.limca.get() != 0:
                self.textarea.insert(
                    END, f"\n Limca\t\t\t{self.limca.get()}\t\t\t{self.d_l_p}")
            if self.sprite.get() != 0:
                self.textarea.insert(
                    END, f"\n Sprite\t\t\t{self.sprite.get()}\t\t\t{self.d_s_p}")
            if self.spreed.get() != 0:
                self.textarea.insert(
                    END, f"\n Spreed\t\t\t{self.spreed.get()}\t\t\t{self.d_sp_p}")
            if self.mojo.get() != 0:
                self.textarea.insert(
                    END, f"\n MOjo\t\t\t{self.mojo.get()}\t\t\t{self.d_mo_p}")
                # er por \t\t er por price calculate korbo kivabe korbo seta.
                # to amra je def total(self): mane total je price add korcilam protita product er sekhane kaj korbo
                # akhane total result kono variable e store korte pari tarpor take add korte pari. to amader price milbe
                # to atar aktu modify kora lagbe  tar jonno  def total(self): akhane cole jabo nice edit korbo.

            #8 no work start#
            self.textarea.insert(
                END, f"\n------------------------------------------------------------")
            # akhane check korbo jodi 3 ta product er moddhe jodi kono ekta na nei tahole
            #total tax 0.0 tekhabena ja ja product nieyeci setai dekhabe#
            if self.cosmetic_tax.get() != "TK. 0.0":
                self.textarea.insert(
                    END, f"\n Cosmetic Tax\t\t\t\t\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get() != "TK. 0.0":
                self.textarea.insert(
                    END, f"\n Grocery Tax\t\t\t\t\t\t{self.grocery_tax.get()}")
            if self.cold_drink_tax.get() != "TK. 0.0":
                self.textarea.insert(
                    END, f"\n Cold Drink Tax\t\t\t\t\t\t{self.cold_drink_tax.get()}")

            #.get er madddhome value fatch korbe#
            # 8 no work add 471 line er po akhane print korar jonno total bill
            self.textarea.insert(
                END, f"\n Total Bill : \t\t\t\t\t\t TK.{self.Total_bill}")
            self.textarea.insert(
                END, f"\n------------------------------------------------------------")

        # 10 no work........akhane bill generate korar por call hbe tr jonno
            self.save_bill()

    def save_bill(self):
        # message box
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        # jode user yes kore tahole
        if op > 0:
            # data fatch kore tetextarea rakhbo and os er maddhome file create +str(self.bill_no.get()) atat help e then txt file rakhlam then "w" dia wride e generate korlam

            self.bill_data = self.textarea.get('1.0', END)
            # file open korlam and file name bill then bills folder e new file banaici
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)  # write korlam
            f1.close()
            # bill generate hobar por message show hobe
            messagebox.showinfo(
                "Saved", f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return

        # 11 no work

    def find_bill(self):                # 0     1
        # split korar por variable banabo
        present = "no"
        for i in os.listdir("bills/"):  # 3333.txt
            # print(i)
            # 102 no line e then opore cole jabo command add korar jonno command er maddhome calanor jonno
            # bill data fatch kore show korabo tar jonnno
            if i.split('.')[0] == self.search_bill.get():
                # file open korbe read e tai r dici
                f1 = open(f"bills/{i}", "r")
                # delete korar jonno
                self.textarea.delete('1.0', END)
                # akhane insert k call korbe and f1 set korbe

                # self.textarea.insert(END, f1) atar karone error asbe karon akhane f1 calabona akhane alada foe loop calabo
                for d in f1:
                    self.textarea.insert(END, d)

                f1.close()
                present = "yes"
            # present no er equal hole messageshow korbe invalid bill number
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

        # 12 no work clear er kaj

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear ...?")
        if op > 0:

            # er por top variavle er function gula nia asbo
            # tarpor intvar k set kore 0 kore dibo int k and string k blank kore dibo
            #===========Cosmetics==========================#
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)
            self.haircut.set(0)
            self.powder.set(0)

            #===========Grocery==========================#
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            self.cotpoti.set(0)
            self.fucka.set(0)

            #===========Cold drinks==========================#

            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            self.spreed.set(0)
            self.mojo.set(0)

            #===========Total product price and tax variable==========================#
            #akhane type hbe string#
            #akhane calculte korar dorkar nai opor theke calculate hoa ase akhane show hobe#

            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #===========Customer er jonno==========================#

            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

        # er por opore clear function k call korbo clear button e

        # 13 no work exit er kaj korbo

    def Exit_app(self):
        # user k jiggas korbo
        op = messagebox.askyesno(
            "Exit", "Do you really want to exit this app...?")
        if op > 0:
            self.root.destroy()

        # 10 no work........akhane bill generate korar por call hbe tr jonno 635 line e
        # so 8 no e total tax er kaj ses ekhan last e total er sum add korbo tar jonno opore jabo
        # tar age self total cosmetic er string jeta nicilam oita c_tax variable e rakhbo then nice variable pass kore dico 389 no line e 426,458
        # 8 no work opore total function e jabo welcome bill er age variable banabo self.Total_bill= akhane sum korbo self.cosmetic_price.get 471 no line

        # 4 no work opore likha ace..#
        #5 no work holo welcome ta jokhon general bill e click korbo tokhon show korbe...............#
        # 6 no work sb korar por run korle dekhbo auto akta bill set hoa gece to amra opore button e name phn no dile oitaw add hoa jabe to atar set korar por
        #  6 no work geneal bill button e click korle dekhbo noce ar akta asce to amra ata set korle auto oporer ta kete jabe .ata akhon kaj korbo#
        #tar jonno def welcome_bill(self): atar nice self.textarea.delete('1.0,END)#
        # atar mane holo delete function use korce and 1, suru kore END porjonto bill area sb delete hoa jabe#

        #7 no owrk#
        #akhane ami korbo total er kaj amader j total ace ota te clic korle ja ja total niaci ta bill area te show korbe#

        # 8 no work akhane total price and tax show korabo bord e and total ta sum hoa calculate korbe


        # 9 no work 0 ace kintu total e kaj korce 2 ta posibility hote pare 1. name phone no empty hote hbe na hoi jekono akta prodct kina lagbe
        # jodi sob 0 ba name na dewa hoi tahole akta message show hbe no product has been selected. tar jonno bill_area er nice kaj korbo
        # 10 no work jokhon amra generate bill e click korbo tokhon variable k pichone generate korte cai ki na?
        #tai ses e function banabo 553 line theke#
        # 11 no work search er kaj  korbo
        # 12 no work clear er kaj korbo
        # 13 no work exit er kaj korbo
root = Tk()
obj = Bill_App(root)
root.mainloop()
