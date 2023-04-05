import tkinter as tk
from tkinter import ttk


def calculate_eratosthenes(n):
    if n == 1:
        return "One is not prime or composite."
    else:
        prime = [True for _ in range(n + 1)]
        p = 2
        while p * p <= n:

            if prime[p]:

                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        primes = "Prime numbers : \n"
        say = 0
        for p in range(2, n + 1):
            if prime[p]:
                primes += str(p) + " "
                say += 1
                if say % 14 == 0:
                    primes += "\n"

        return primes


def calculate_khwarizmi(a, b, c):
    d = b ** 2 - 4 * a * c

    if d < 0:
        return "This equation has no real root."

    elif d > 0:
        x1 = (-b + (d ** 0.5)) / (2 * a)
        x2 = (-b - (d ** 0.5)) / (2 * a)
        str1 = "This equation has 2 real roots: \n\n" + str(x1) + "\n" + str(x2)
        return str1

    else:
        x = -b / (2 * a)
        str1 = "This equation has 1 real root : \n\n" + str(x)
        return str1


def calculate_fibonacci(n):
    a, b = 0, 1
    say = 0
    result = "Fibonacci series : \n\n"
    # loop through remaining terms
    while b < n:
        result += str(b) + " "
        say += 1
        a, b = b, a + b
        if say % 4 == 0:
            result += "\n"

    return result


def calculate_pythagorean(n):
    result = "Pythagorean triples : \n\n"
    say = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j + 1, n + 1):
                if i ** 2 + j ** 2 == k ** 2:
                    result += "(" + str(i) + ", " + str(j) + ", " + str(k) + ")    "
                    say += 1
                    if say % 5 == 0:
                        result += "\n"

    return result


def calculate_euclidean(a, b):
    result = "The greatest common divisor (GCD) : \n\n"
    if a == 0:
        return result + str(b)
    else:
        return calculate_euclidean(b % a, a)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.result_label4 = None
        self.entry_b4 = None
        self.entry_a4 = None
        self.result_label3 = self.entry_n3 = self.result_label2 = self.entry_n2 = self.entry_n = None
        self.result_label1 = self.result_label = self.entry_c = self.entry_b = self.entry_a = self.notebook = None
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        page_texts = ["About", "Al-Khwarizmi algorithm", "Algorithm of Eratosthenes", "Pythagorean algorithm",
                      "Fibonacci algorithm",
                      "Euclidean algorithm"]
        self.notebook = ttk.Notebook(self.master)

        for i in range(6):
            page = tk.Frame(self.notebook, width=300, height=300)
            if i == 0:
                label_wel = tk.Label(page,
                                     text="Exporting the Project\n\nProject name : Named algorithms\n"
                                          "Date and Time : 05/04/2023 08:57:12\nUniversity : BSU - "
                                          "Baku State University\nFaculty : Applied Mathematics and Cybernetics "
                                          "(SABAH Groups)\nMajority : Computer Sciences\nCourse : Two (2)\nGroup "
                                          "name : KE022S2\nStudents : Aliyev Zakir Agamehdi\n\nNote : If there is any "
                                          "problem with the issue, please contact\naliyevzakir814@gmail.com :)",
                                     font=("TkDefaultFont", 16))
                label_wel.pack(pady=150)
            elif i == 1:

                label_space = tk.Label(page)
                label_space.pack(pady=40)
                label_a = tk.Label(page, text="Enter the number A : ", font=("TkDefaultFont", 16))
                label_a.pack(pady=10)
                self.entry_a = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_a.pack(pady=10)

                label_b = tk.Label(page, text="Enter the number B : ", font=("TkDefaultFont", 16))
                label_b.pack(pady=10)
                self.entry_b = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_b.pack(pady=10)

                label_c = tk.Label(page, text="Enter the number C : ", font=("TkDefaultFont", 16))
                label_c.pack(pady=10)
                self.entry_c = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_c.pack(pady=10)

                self.result_label = tk.Label(page, font=("TkDefaultFont", 16))
                self.result_label.pack(pady=10)

                button = tk.Button(page, text="Calculate", font=("TkDefaultFont", 16),
                                   command=self.calculate_khwarizmi_try)
                button.pack(pady=10)
            elif i == 2:

                label_n = tk.Label(page, text="Enter the number N : (0 - ∞)", font=("TkDefaultFont", 16))
                label_n.pack(pady=20)

                self.entry_n = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_n.pack(pady=10)

                self.result_label1 = tk.Label(page, font=("TkDefaultFont", 12))
                self.result_label1.pack(pady=10)

                button = tk.Button(page, text="Calculate", font=("TkDefaultFont", 16),
                                   command=self.calculate_eratosthenes_try)
                button.pack(pady=10)
            elif i == 3:
                label_n2 = tk.Label(page, text="Enter the number N : (0 - ∞)", font=("TkDefaultFont", 16))
                label_n2.pack(pady=20)

                self.entry_n2 = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_n2.pack(pady=10)

                self.result_label2 = tk.Label(page, font=("TkDefaultFont", 12))
                self.result_label2.pack(pady=10)

                button = tk.Button(page, text="Calculate", font=("TkDefaultFont", 16),
                                   command=self.calculate_pythagorean_try)
                button.pack(pady=10)
            elif i == 4:
                label_n3 = tk.Label(page, text="Enter the number N : (0 - ∞)", font=("TkDefaultFont", 16))
                label_n3.pack(pady=20)

                self.entry_n3 = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_n3.pack(pady=10)

                self.result_label3 = tk.Label(page, font=("TkDefaultFont", 16))
                self.result_label3.pack(pady=10)

                button = tk.Button(page, text="Calculate", font=("TkDefaultFont", 16),
                                   command=self.calculate_fibonacci_try)
                button.pack(pady=10)
            elif i == 5:
                label_a4 = tk.Label(page, text="Enter the number A : (0 - ∞)", font=("TkDefaultFont", 16))
                label_a4.pack(pady=20)

                self.entry_a4 = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_a4.pack(pady=10)

                label_b4 = tk.Label(page, text="Enter the number B : (0 - ∞)", font=("TkDefaultFont", 16))
                label_b4.pack(pady=20)

                self.entry_b4 = tk.Entry(page, font=("TkDefaultFont", 16))
                self.entry_b4.pack(pady=10)

                self.result_label4 = tk.Label(page, font=("TkDefaultFont", 20))
                self.result_label4.pack(pady=10)

                button = tk.Button(page, text="Calculate", font=("TkDefaultFont", 16),
                                   command=self.calculate_euclidean_try)
                button.pack(pady=10)
            else:
                label = tk.Label(page, text=page_texts[i], font=("TkDefaultFont", 16))
                label.pack(padx=50, pady=50)

            self.notebook.add(page, text=page_texts[i])

            self.notebook.pack(padx=10, pady=10)

    def calculate_khwarizmi_try(self):

        try:
            a = int(self.entry_a.get())
            b = int(self.entry_b.get())
            c = int(self.entry_c.get())

            result = calculate_khwarizmi(a, b, c)
            self.result_label.configure(text=f"{result}")
        except ValueError:
            self.result_label.configure(text="Please enter a number.")

    def calculate_eratosthenes_try(self):
        try:
            n = int(self.entry_n.get())

            result = calculate_eratosthenes(n)
            self.result_label1.configure(text=f"{result}")
        except ValueError:
            self.result_label1.configure(text="Please enter a number.")

    def calculate_pythagorean_try(self):
        try:
            n = int(self.entry_n2.get())

            result = calculate_pythagorean(n)
            self.result_label2.configure(text=f"{result}")
        except ValueError:
            self.result_label2.configure(text="Please enter a number.")

    def calculate_fibonacci_try(self):
        try:
            n = int(self.entry_n3.get())

            result = calculate_fibonacci(n)
            self.result_label3.configure(text=f"{result}")
        except ValueError:
            self.result_label3.configure(text="Please enter a number.")

    def calculate_euclidean_try(self):
        try:
            a = int(self.entry_a4.get())
            b = int(self.entry_b4.get())

            result = calculate_euclidean(a, b)
            self.result_label4.configure(text=f"{result}")
        except ValueError:
            self.result_label4.configure(text="Please enter a number.")


root = tk.Tk()
root.config(bg="#0AFCD7")
root.geometry("800x800")
app = Application(master=root)
app.mainloop()
