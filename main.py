import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np

import csv

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    """
        CSV reading class
    """

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Stonks Analyzer")

        self.filename = 'closed_all.csv'

        self.all_profit = 0
        self.all_net_profit = 0

        self.symbol_list = []
        self.position_list = []
        self.type_list = []
        self.lots_list = []
        self.open_time_list = []
        self.open_price_list = []
        self.close_time_list = []
        self.close_price_list = []
        self.profit_list = []
        self.net_profit_list = []
        self.rollover_list = []
        self.comment_list = []

        self.cum_net_profit_list = [0]

        self.main_array = [self.symbol_list, self.position_list, self.type_list, self.lots_list, self.open_time_list,
                           self.open_price_list, self.close_time_list, self.close_price_list, self.profit_list,
                           self.net_profit_list, self.rollover_list, self.comment_list]

    def reader(self):
        with open(self.filename, newline='') as main_file:
            closed_all = csv.reader(main_file, delimiter=';')
            for row in closed_all:
                # print(' | '.join(row))
                try:
                    self.all_profit = self.all_profit + float(row[8])
                    self.all_net_profit = self.all_net_profit + float(row[9])

                    for n in range(12):
                        self.main_array[n].append(row[n])


                except:
                    pass

            for n in range(len(self.net_profit_list)):
                self.net_profit_list[n] = float(self.net_profit_list[n])
                self.cum_net_profit_list.append(self.cum_net_profit_list[n] + self.net_profit_list[n])

            print(self.all_profit)
            print(self.all_net_profit)

            print(self.main_array)

            plt.plot(self.cum_net_profit_list)
            plt.show()


App = App()
App.reader()
# App.mainloop()