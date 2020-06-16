import tkinter as tk
from tkinter import messagebox

w = 16
h = 7
f = 5000


class TicTacToe:
    def __init__(self):
        self.player_dic = {"X": 'Player1', 'O': 'Player2'}

        self.root = tk.Tk()
        self.root.title('Enter Names')

        self.label = tk.Label(self.root, text='Player 1 (X):')
        self.label.grid(row=0, column=0, padx=10, pady=5)

        self.p1input = tk.Entry(self.root)
        self.p1input.grid(row=0, column=1, padx=10, pady=5)

        self.label1 = tk.Label(self.root, text='Player 2 (O):')
        self.label1.grid(row=1, column=0, padx=10, pady=5)

        self.p2input = tk.Entry(self.root)
        self.p2input.grid(row=1, column=1, padx=10, pady=5)

        self.sub = tk.Button(self.root, text='Submit', command=self.name_input_submit)
        self.sub.grid(row=2, column=0, columnspan=2, pady=5)
        self.root.bind('<Return>', lambda event=None: self.sub.invoke())

        self.root.mainloop()

        self.count = 0
        self.li = [' ' for _ in range(9)]
        self.exit_flag = False
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')

        self.btn0 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(0))
        self.btn0.grid(row=0, column=0)

        self.btn1 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(1))
        self.btn1.grid(row=0, column=1)

        self.btn2 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(2))
        self.btn2.grid(row=0, column=2)

        self.btn3 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(3))
        self.btn3.grid(row=1, column=0)

        self.btn4 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(4))
        self.btn4.grid(row=1, column=1)

        self.btn5 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(5))
        self.btn5.grid(row=1, column=2)

        self.btn6 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(6))
        self.btn6.grid(row=2, column=0)

        self.btn7 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(7))
        self.btn7.grid(row=2, column=1)

        self.btn8 = tk.Button(self.root, text=' ', height=h, width=w, font=f, command=lambda: self.change(8))
        self.btn8.grid(row=2, column=2)

        self.root.mainloop()

    def change(self, num):
        self.count += 1
        if self.count % 2:
            y = 'X'
        else:
            y = 'O'
        exec('self.btn' + str(num) + '.config(text=y, state="disable")')
        self.li[num] = y
        self.root.update()
        self.check()

    def check(self):
        li = self.li
        if li[0] == li[1] == li[2] != ' ':
            self.check_part(0, 1, 2)
        elif li[0] == li[3] == li[6] != ' ':
            self.check_part(0, 3, 6)
        elif li[3] == li[4] == li[5] != ' ' :
            self.check_part(3, 4, 5)
        elif li[1] == li[4] == li[7] != ' ':
            self.check_part(1, 4, 7)
        elif li[6] == li[7] == li[8] != ' ':
            self.check_part(6, 7, 8)
        elif li[2] == li[5] == li[8] != ' ':
            self.check_part(2, 5, 8)
        elif li[0] == li[4] == li[8] != ' ':
            self.check_part(0, 4, 8)
        elif li[2] == li[4] == li[6] != ' ':
            self.check_part(2, 4, 6)
        if ' ' not in li and not self.exit_flag:
            self.winner_popup('!TIEtie')
            self.root.destroy()

    def check_part(self, *num):
        li = self.li
        for z in num:
            exec('self.btn' + str(z) + '.config(bg="#90EE90")')
        self.winner_popup(self.player_dic[li[num[0]]])
        self.root.destroy()
        self.exit_flag = True

    def winner_popup(self, winner):
        if winner != '!TIEtie':
            messagebox._show('Game Over', winner.title() + ' wins the game!!')
        else:
            messagebox._show('Game Over', "It was a tie!!")

    def name_input_submit(self):
        self.player_dic['X'] = self.p1input.get()
        self.player_dic['O'] = self.p2input.get()
        self.root.destroy()



TicTacToe()
