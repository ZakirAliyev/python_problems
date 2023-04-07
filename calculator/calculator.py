import tkinter as tk
from tkinter import *


def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.geometry("800x800")
    new_window.config(bg="light green")
    label_wel = tk.Label(new_window,
                         text="\nAbout the Project\n\nProject name : Calculator with Tkinter\n"
                              "Date and Time : 07/04/2023 04:45:34\nUniversity : BSU - "
                              "Baku State University\nFaculty : Applied Mathematics and Cybernetics "
                              "\n(SABAH Groups)\nMajority : Computer Sciences\nCourse : Two (2)\nGroup "
                              "name : KE022S1 and KE022S2\nAuthors : Gulchohra Sultanova Cavanshir and\nAliyev Zakir "
                              "Agamehdi "
                              "\n\nNote : If there is any "
                              "problem with the issue,\n please contact\naliyevzakir814@gmail.com or \n"
                              "gulcohrsultanov@gmail.com:)",
                         font=("TkDefaultFont", 25), fg="dark blue", bg="light green")
    label_wel.pack()
    button = tk.Button(new_window, text="Close", command=new_window.destroy, bg="#E74C3C", font=25)
    button.pack(pady=20)


def button_click(number):
    current = entry2.get()
    entry2.delete(0, END)
    entry2.insert(0, str(current) + str(number))


def button_clear():
    entry2.delete(0, END)
    entry1.delete(0, END)


def button_multiply():
    entry1.delete(0, END)
    first_number = entry2.get()
    global f_num
    global math
    entry1.insert(0, first_number + " x ")
    math = "multiplication"
    f_num = float(first_number)
    entry2.delete(0, END)


def button_addition():
    entry1.delete(0, END)
    first_number = entry2.get()
    global f_num
    global math
    entry1.insert(0, first_number + " + ")
    math = "addition"
    f_num = float(first_number)
    entry2.delete(0, END)


def button_subtraction():
    entry1.delete(0, END)
    first_number = entry2.get()
    global f_num
    global math
    entry1.insert(0, first_number + " - ")
    math = "subtraction"
    f_num = float(first_number)
    entry2.delete(0, END)


def button_division():
    entry1.delete(0, END)
    first_number = entry2.get()
    global f_num
    global math
    entry1.insert(0, first_number + " / ")
    math = "division"
    f_num = float(first_number)
    entry2.delete(0, END)


def button_equal():
    second_number = entry2.get()
    entry2.delete(0, END)
    global r
    if math == "multiplication":
        r = f_num * int(second_number)
        entry1.insert(len(str(f_num)) + 3, second_number)
        entry2.insert(0, r)
    elif math == "division":
        r = f_num / float(second_number)
        entry1.insert(len(str(f_num)) + 3, second_number)
        entry2.insert(0, r)
    elif math == "subtraction":
        r = f_num - int(second_number)
        entry1.insert(len(str(f_num)) + 3, second_number)
        entry2.insert(0, r)
    elif math == "addition":
        r = f_num + int(second_number)
        entry1.insert(len(str(f_num)) + 3, second_number)
        entry2.insert(0, r)


root = tk.Tk()
frame = tk.Frame(root)

root.geometry("1230x870")
root.title("Calculator")
root.config(bg="#DADADA")

label_blue = tk.Label(root, width=175, bg="#4286F3", text="Scientific Calculator", fg="#FFFFFF", font=("Arial", 33),
                      pady=27)
label_blue.config(anchor='w', padx=35)
label_blue.pack()

button_about = tk.Button(label_blue, text="About", font=("Arial", 24), bg="#57BFF4", fg="#FAFAFA",
                         command=open_new_window)
button_about.place(x=1085, y=20)

entry1 = tk.Entry(root, width=35, font=("Arial", 45), borderwidth=3)
entry1.pack(pady=32)

entry2 = tk.Entry(root, width=35, font=("Arial", 45), borderwidth=3)
entry2.pack()

button_mod = tk.Button(root, font=("Arial", 25, "bold"), text="mod", pady=0)
button_mod.place(x=35, y=350)

button_mc = tk.Button(root, font=("Arial", 25, "bold"), text="MC", padx=9)
button_mc.place(x=35 + 106 * 6, y=350)

button_mr = tk.Button(root, font=("Arial", 25, "bold"), text="MR", padx=9)
button_mr.place(x=35 + 106 * 7, y=350)

button_ms = tk.Button(root, font=("Arial", 25, "bold"), text="MS", padx=10)
button_ms.place(x=35 + 106 * 8, y=350)

button_m_plus = tk.Button(root, font=("Arial", 25, "bold"), text="M+", padx=11)
button_m_plus.place(x=35 + 106 * 9, y=350)

button_m_minus = tk.Button(root, font=("Arial", 25, "bold"), text="M-", padx=15)
button_m_minus.place(x=35 + 106 * 10, y=350)

button_sinh = tk.Button(root, font=("Arial", 25, "bold"), text="sinh", padx=2, fg="#444444")
button_sinh.place(x=35, y=430)

button_cosh = tk.Button(root, font=("Arial", 25, "bold"), text="cosh", fg="#444444")
button_cosh.place(x=35 + 106, y=430)

button_tgh = tk.Button(root, font=("Arial", 25, "bold"), text="tanh", fg="#444444")
button_tgh.place(x=35 + 110 * 2, y=430)

button_exp = tk.Button(root, font=("Arial", 25, "bold"), text="exp", padx=9, fg="#444444")
button_exp.place(x=35 + 109 * 3, y=430)

button_bracket_left = tk.Button(root, font=("Arial", 25, "bold"), text="(", padx=26, fg="#444444")
button_bracket_left.place(x=35 + 109 * 4, y=430)

button_bracket_right = tk.Button(root, font=("Arial", 25, "bold"), text=")", padx=26, fg="#444444")
button_bracket_right.place(x=35 + 107 * 5, y=430)

button_delete = tk.Button(root, font=("Arial", 25, "bold"), text="<━━━━", padx=11, bg="#E74C3C", fg="#FAFAFA")
button_delete.place(x=35 + 106 * 6, y=430)

button_c = tk.Button(root, font=("Arial", 25, "bold"), text="C", padx=23, bg="#E74C3C", fg="#FAFAFA",
                     command=button_clear)
button_c.place(x=35 + 106 * 8, y=430)

button_plus_minus = tk.Button(root, font=("Arial", 25, "bold"), text="+/-", padx=15, bg="#E74C3C", fg="#FAFAFA")
button_plus_minus.place(x=35 + 106 * 9, y=430)

button_sqrt = tk.Button(root, font=("Arial", 25, "bold"), text="√", padx=26, fg="#444444")
button_sqrt.place(x=35 + 106 * 10, y=430)

button_sinh_1 = tk.Button(root, font=("Arial", 16, "bold"), text="sinh^-1", padx=3, fg="#444444", height=2)
button_sinh_1.place(x=35, y=510)

button_cosh_1 = tk.Button(root, font=("Arial", 16, "bold"), text="cosh^-1", padx=3, fg="#444444", height=2)
button_cosh_1.place(x=35 + 106, y=510)

button_tgh_1 = tk.Button(root, font=("Arial", 16, "bold"), text="tanh^-1", padx=2, fg="#444444", height=2)
button_tgh_1.place(x=35 + 110 * 2, y=510)

button_log2x = tk.Button(root, font=("Arial", 16, "bold"), text="log  x", padx=14, fg="#444444", height=2)
button_log2x.place(x=35 + 109 * 3, y=510)

two = tk.Label(root, text="2", font=("Arial", 11, "bold"), fg="#444444")
two.place(x=415, y=540)

button_ln = tk.Button(root, font=("Arial", 24, "bold"), text="ln", padx=17, fg="#444444")
button_ln.place(x=35 + 109 * 4, y=510)

button_log = tk.Button(root, font=("Arial", 24, "bold"), text="log", padx=8, fg="#444444")
button_log.place(x=35 + 107 * 5, y=510)

button_7 = tk.Button(root, font=("Arial", 24, "bold"), text="7", padx=26, fg="#444444", command=lambda: button_click(7))
button_7.place(x=35 + 106 * 6, y=510)

button_8 = tk.Button(root, font=("Arial", 24, "bold"), text="8", padx=27, fg="#444444", command=lambda: button_click(8))
button_8.place(x=35 + 106 * 7, y=510)

button_9 = tk.Button(root, font=("Arial", 24, "bold"), text="9", padx=27, fg="#444444", command=lambda: button_click(9))
button_9.place(x=35 + 106 * 8, y=510)

button_divide = tk.Button(root, font=("Arial", 24, "bold"), text="/", padx=31, fg="#444444", command=button_division)
button_divide.place(x=35 + 106 * 9, y=510)

button_percent = tk.Button(root, font=("Arial", 24, "bold"), text="%", padx=22, fg="#444444")
button_percent.place(x=35 + 106 * 10, y=510)

button_pi = tk.Button(root, font=("Arial", 24, "bold"), text="π", padx=22, fg="#444444")
button_pi.place(x=35, y=590)

button_e = tk.Button(root, font=("Arial", 24, "bold"), text="e", padx=29, fg="#444444")
button_e.place(x=35 + 106, y=590)

button_fak = tk.Button(root, font=("Arial", 24, "bold"), text="n!", padx=21, fg="#444444")
button_fak.place(x=35 + 109 * 2, y=590)

button_logyx = tk.Button(root, font=("Arial", 16, "bold"), text="log  x", padx=14, fg="#444444", height=2)
button_logyx.place(x=35 + 109 * 3, y=590)

y = tk.Label(root, text="y", font=("Arial", 11, "bold"), fg="#444444")
y.place(x=415, y=620)

button_e_x = tk.Button(root, font=("Arial", 24, "bold"), text="e^x", padx=4, fg="#444444")
button_e_x.place(x=35 + 109 * 4, y=590)

button_10x = tk.Button(root, font=("Arial", 15, "bold"), text="10^x", padx=15, fg="#444444", height=2)
button_10x.place(x=35 + 107 * 5, y=589)

button_4 = tk.Button(root, font=("Arial", 24, "bold"), text="4", padx=26, fg="#444444", command=lambda: button_click(4))
button_4.place(x=35 + 106 * 6, y=590)

button_5 = tk.Button(root, font=("Arial", 24, "bold"), text="5", padx=26, fg="#444444", command=lambda: button_click(5))
button_5.place(x=35 + 106 * 7, y=590)

button_6 = tk.Button(root, font=("Arial", 24, "bold"), text="6", padx=26, fg="#444444", command=lambda: button_click(6))
button_6.place(x=35 + 106 * 8, y=590)

button_multiply = tk.Button(root, font=("Arial", 24, "bold"), text="*", padx=29, fg="#444444", command=button_multiply)
button_multiply.place(x=35 + 106 * 9, y=590)

button_1dividex = tk.Button(root, font=("Arial", 24, "bold"), text="1/x", padx=13, fg="#444444")
button_1dividex.place(x=35 + 106 * 10, y=590)

button_sin = tk.Button(root, font=("Arial", 24, "bold"), text="sin", padx=11, fg="#444444")
button_sin.place(x=35, y=670)

button_cos = tk.Button(root, font=("Arial", 24, "bold"), text="cos", padx=9, fg="#444444")
button_cos.place(x=35 + 106, y=670)

button_tan = tk.Button(root, font=("Arial", 24, "bold"), text="tan", padx=12, fg="#444444")
button_tan.place(x=35 + 108 * 2, y=670)

button_xpowy = tk.Button(root, font=("Arial", 24, "bold"), text="x^y", padx=11, fg="#444444")
button_xpowy.place(x=35 + 108 * 3, y=670)

button_xpow3 = tk.Button(root, font=("Arial", 24, "bold"), text="x^3", padx=4, fg="#444444")
button_xpow3.place(x=35 + 109 * 4, y=670)

button_xpow2 = tk.Button(root, font=("Arial", 24, "bold"), text="x^2", padx=4, fg="#444444")
button_xpow2.place(x=35 + 107 * 5, y=670)

button_1 = tk.Button(root, font=("Arial", 24, "bold"), text="1", padx=26, fg="#444444", command=lambda: button_click(1))
button_1.place(x=35 + 106 * 6, y=670)

button_2 = tk.Button(root, font=("Arial", 24, "bold"), text="2", padx=26, fg="#444444", command=lambda: button_click(2))
button_2.place(x=35 + 106 * 7, y=670)

button_3 = tk.Button(root, font=("Arial", 24, "bold"), text="3", padx=26, fg="#444444", command=lambda: button_click(3))
button_3.place(x=35 + 106 * 8, y=670)

button_minus = tk.Button(root, font=("Arial", 24, "bold"), text="-", padx=29, fg="#444444", command=button_subtraction)
button_minus.place(x=35 + 106 * 9, y=670)

button_equal = tk.Button(root, font=("Arial", 25, "bold"), text="=", padx=25, bg="#2ECC71", height=3, fg="#FAFAFA",
                         command=button_equal)
button_equal.place(x=35 + 106 * 10, y=670)

button_sin_1 = tk.Button(root, font=("Arial", 16, "bold"), text="sin^-1", padx=8, fg="#444444", height=2)
button_sin_1.place(x=35, y=750)

button_cos_1 = tk.Button(root, font=("Arial", 16, "bold"), text="cos^-1", padx=7, fg="#444444", height=2)
button_cos_1.place(x=35 + 106, y=750)

button_tan_1 = tk.Button(root, font=("Arial", 16, "bold"), text="tan^-1", padx=8, fg="#444444", height=2)
button_tan_1.place(x=35 + 108 * 2, y=750)

button_yrootx = tk.Button(root, font=("Arial", 24, "bold"), text="y√x", padx=12, fg="#444444")
button_yrootx.place(x=35 + 108 * 3, y=750)

button_3rootx = tk.Button(root, font=("Arial", 24, "bold"), text="3√x", padx=5, fg="#444444")
button_3rootx.place(x=35 + 109 * 4, y=750)

button_module = tk.Button(root, font=("Arial", 24, "bold"), text="|x|", padx=13, fg="#444444")
button_module.place(x=35 + 107 * 5, y=750)

button_0 = tk.Button(root, font=("Arial", 24, "bold"), text="0", padx=79, fg="#444444", command=lambda: button_click(0))
button_0.place(x=35 + 106 * 6, y=750)

button_dot = tk.Button(root, font=("Arial", 24, "bold"), text=".", padx=30, fg="#444444")
button_dot.place(x=35 + 106 * 8, y=750)

button_plus = tk.Button(root, font=("Arial", 24, "bold"), text="+", padx=25, fg="#444444", command=button_addition)
button_plus.place(x=35 + 106 * 9, y=750)

root.mainloop()