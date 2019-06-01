import tkinter as tk
import main

russians_names_dict = main.make_dict_for_search()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #variables block
        # labelText = tk.StringVar()
        # labelText.set("")

        # block for description and entry for user input with item name
        self.description_user_input = tk.Label(self, text="Введите точное название предмета для поиска в поле ниже").grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        user_input_var = tk.StringVar()
        user_input_var.set("")
        self.user_input = tk.Entry(self, textvariable=user_input_var).grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="WE")

        # header row with colums names
        city_name_column_name = tk.StringVar()
        city_name_column_name.set("Имя города")
        self.city_name_column = tk.Label(self, textvariable=city_name_column_name, height=3, width=13).grid(row=3, column=0) #"Название города"
        sell_price_colunb_name = tk.StringVar()
        sell_price_colunb_name.set("Цена продажи \nминимум \nи максимум")
        self.sell_price_colunb = tk.Label(self, textvariable=sell_price_colunb_name, height=3, width=20).grid(row=3, column=1)
        buy_price_column_name = tk.StringVar()
        buy_price_column_name.set("Цена покупки \nминимум \nи максимум")
        self.buy_price_column = tk.Label(self, textvariable=buy_price_column_name, height=3, width=13).grid(row=3, column=2)

        # city names column
        black_market_city_name_var = tk.StringVar()
        black_market_city_name_var.set("Black Market")
        self.black_market_city_name = tk.Label(self, textvariable=black_market_city_name_var, height=3, width=10).grid(row=4, column=0)
        bridgewatch_city_name_var = tk.StringVar()
        bridgewatch_city_name_var.set("Bridgewatch")
        self.bridgewatch_city_name = tk.Label(self, textvariable=bridgewatch_city_name_var, height=3, width=10).grid(row=5, column=0)
        caerleon_city_name_var = tk.StringVar()
        caerleon_city_name_var.set("Caerleon")
        self.caerleon_city_name = tk.Label(self, textvariable=caerleon_city_name_var, height=3, width=10).grid(row=6, column=0)
        fort_sterling_city_name_var = tk.StringVar()
        fort_sterling_city_name_var.set("Fort Sterling")
        self.fort_sterling_city_name = tk.Label(self, textvariable=fort_sterling_city_name_var, height=3, width=10).grid(row=7, column=0)
        lymhurst_city_name_var = tk.StringVar()
        lymhurst_city_name_var.set("Lymhurst")
        self.lymhurst_city_name = tk.Label(self, textvariable=lymhurst_city_name_var, height=3, width=10).grid(row=8, column=0)
        martlock_city_name_var = tk.StringVar()
        martlock_city_name_var.set("Martlock")
        self.martlock_city_name = tk.Label(self, textvariable=martlock_city_name_var, height=3, width=10).grid(row=9, column=0)
        thetford_city_name_var = tk.StringVar()
        thetford_city_name_var.set("Thetford")
        self.thetford_city_name = tk.Label(self, textvariable=thetford_city_name_var, height=3, width=10).grid(row=10, column=0)

        # min price column
        black_market_min_prices = tk.StringVar()
        black_market_min_prices.set("")
        self.black_market_min = tk.Label(self, textvariable=black_market_min_prices, height=3, width=10).grid(row=4, column=1)
        bridgewatch_min_prices = tk.StringVar()
        bridgewatch_min_prices.set("")
        self.bridgewatch_min = tk.Label(self, textvariable=bridgewatch_min_prices, height=3, width=10).grid(row=5, column=1)
        caerleon_min_prices = tk.StringVar()
        caerleon_min_prices.set("")
        self.caerleon_min = tk.Label(self, textvariable=caerleon_min_prices, height=3, width=10).grid(row=6, column=1)
        fort_sterling_min_prices = tk.StringVar()
        fort_sterling_min_prices.set("")
        self.fort_sterling_min = tk.Label(self, textvariable=fort_sterling_min_prices, height=3, width=10).grid(row=7, column=1)
        lymhurst_min_prices = tk.StringVar()
        lymhurst_min_prices.set("")
        self.lymhurst_min = tk.Label(self, textvariable=lymhurst_min_prices, height=3, width=10).grid(row=8, column=1)
        martlock_min_prices = tk.StringVar()
        martlock_min_prices.set("")
        self.martlock_min = tk.Label(self, textvariable=martlock_min_prices, height=3, width=10).grid(row=9, column=1)
        thetford_min_prices = tk.StringVar()
        thetford_min_prices.set("")
        self.thetford_min = tk.Label(self, textvariable=thetford_min_prices, height=3, width=10).grid(row=10, column=1)

        # max price column
        black_market_max_prices = tk.StringVar()
        black_market_max_prices.set("")
        self.black_market_max = tk.Label(self, textvariable=black_market_max_prices, height=3, width=10).grid(row=4, column=2)
        bridgewatch_max_prices = tk.StringVar()
        bridgewatch_max_prices.set("")
        self.bridgewatch_max = tk.Label(self, textvariable=bridgewatch_max_prices, height=3, width=10).grid(row=5, column=2)
        caerleon_max_prices = tk.StringVar()
        caerleon_max_prices.set("")
        self.caerleon_max = tk.Label(self, textvariable=caerleon_max_prices, height=3, width=10).grid(row=6, column=2)
        fort_sterling_max_prices = tk.StringVar()
        fort_sterling_max_prices.set("")
        self.fort_sterling_max = tk.Label(self, textvariable=fort_sterling_max_prices, height=3, width=10).grid(row=7, column=2)
        lymhurst_max_prices = tk.StringVar()
        lymhurst_max_prices.set("")
        self.lymhurst_max = tk.Label(self, textvariable=lymhurst_max_prices, height=3, width=10).grid(row=8, column=2)
        martlock_max_prices = tk.StringVar()
        martlock_max_prices.set("")
        self.martlock_max = tk.Label(self, textvariable=martlock_max_prices, height=3, width=10).grid(row=9, column=2)
        thetford_max_prices = tk.StringVar()
        thetford_max_prices.set("")
        self.thetford_max = tk.Label(self, textvariable=thetford_max_prices, height=3, width=10).grid(row=10, column=2)

        # functions part
        local_data_list_min = {
            black_market_city_name_var.get(): black_market_min_prices, 
            bridgewatch_city_name_var.get(): bridgewatch_min_prices, 
            caerleon_city_name_var.get(): caerleon_min_prices, 
            fort_sterling_city_name_var.get(): fort_sterling_min_prices, 
            lymhurst_city_name_var.get(): lymhurst_min_prices, 
            martlock_city_name_var.get(): martlock_min_prices, 
            thetford_city_name_var.get(): thetford_min_prices,
            }
        local_data_list_max = {
            black_market_city_name_var.get(): black_market_max_prices, 
            bridgewatch_city_name_var.get(): bridgewatch_max_prices, 
            caerleon_city_name_var.get(): caerleon_max_prices, 
            fort_sterling_city_name_var.get(): fort_sterling_max_prices, 
            lymhurst_city_name_var.get(): lymhurst_max_prices, 
            martlock_city_name_var.get(): martlock_max_prices, 
            thetford_city_name_var.get(): thetford_max_prices,
            }
        def search_function():
            # Семена моркови
            user_input_in_entry = user_input_var.get()
            russians_names_dict = main.make_dict_for_search()
            if user_input_in_entry == "":
                pass
            else:
                # global russians_names_dict
                try:
                    prices_from_server, cities_from_server = main.make_cities_list(main.make_request_for_data, item_name=russians_names_dict[user_input_in_entry])
                # local_data_list = [black_market_city_name_var, bridgewatch_city_name_var, caerleon_city_name_var, fort_sterling_city_name_var, lymhurst_city_name_var, martlock_city_name_var, thetford_city_name_var]
                    for city_name in local_data_list_min.keys():
                        for city_key_from_server in prices_from_server.keys():
                            if city_name == city_key_from_server:
                                local_data_list_min[city_name].set(f'min - {prices_from_server[city_key_from_server]["sell_price_min"]}\nmax - {prices_from_server[city_key_from_server]["sell_price_max"]}')
                    for city_name in local_data_list_max.keys():
                        for city_key_from_server in prices_from_server.keys():
                            if city_name == city_key_from_server:
                                local_data_list_max[city_name].set(f'min - {prices_from_server[city_key_from_server]["buy_price_min"]}\nmax - {prices_from_server[city_key_from_server]["buy_price_max"]}')
                except:
                    pass

        # def zxc():
            # print(black_market_name_var.get())
            # print(black_market_name_var.get() == "Black Market")
            # print(user_input_var.get())
        self.search_button = tk.Button(self, text="Поиск", command=search_function).grid(row=1, column=2, padx=10, pady=10) # 

root = tk.Tk()
root.geometry("375x500")
root.resizable(False, False)
app = Application(master=root)
app.mainloop()