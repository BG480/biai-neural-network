from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class GUI:

    def __init__(self, root):
        root.title("BIAI Neural Network")
        root.resizable(width=False, height=False)
        # Combobox with 'SELECT' button
        self.players_positions_combobox = ttk.Combobox(root, state="readonly", values=["GOALKEEPERS", "CENTRE BACKS",
        "SIDE BACKS", "CENTRE MIDFIELDERS", "WINGERS", "STRIKERS"])
        self.players_positions_combobox.grid(row=0, column=0, columnspan=3)
        self.select_players_button = Button(root, text="SELECT")
        self.select_players_button.grid(row=0, column=3)
        # Listbox with players and scrollbar for listbox
        self.players_listbox_scrollbar = Scrollbar(root)
        self.players_listbox_scrollbar.grid(row=1, column=1, rowspan=5, sticky=S+W+N+E)
        self.players_listbox = Listbox(root, yscrollcommand=self.players_listbox_scrollbar.set)
        self.players_listbox.grid(row=1, column=0, rowspan=5, sticky=N+S+E+W)
        self.players_listbox_scrollbar.config(command=self.players_listbox.yview)
        # Predict section
        self.player_name_label = Label(root, text="PLAYER")
        self.player_name_label.grid(row=1,column=2, columnspan=2)
        self.real_overall_label = Label(root, text="REAL OVERALL")
        self.real_overall_label.grid(row=2,column=2)
        self.real_overall_value_label = Label(root,text="---")
        self.real_overall_value_label.grid(row=2, column=3)
        self.predicted_overall_label = Label(root, text="PREDICTED OVR")
        self.predicted_overall_label.grid(row=3,column=2)
        self.predicted_overall_value_label = Label(root, text="---")
        self.predicted_overall_value_label.grid(row=3, column=3)
        self.deviation_label = Label(root, text="DEVIATION")
        self.deviation_label.grid(row=4,column=2)
        self.deviation_value_label = Label(root, text="---")
        self.deviation_value_label.grid(row=4, column=3)
        self.predict_button = Button(root, text="PREDICT")
        self.predict_button.grid(row=5,column=2,columnspan=2)
        # Buttons section
        self.train_button = Button(root, text="TRAIN NETWORK")
        self.train_button.grid(row=6,column=0)
        self.load_weights_button = Button(root, text="LOAD WEIGHTS")
        self.load_weights_button.grid(row=6,column=2)
        self.save_weights_button = Button(root, text="SAVE WEIGHTS")
        self.save_weights_button.grid(row=6,column=3)

    def show_info_message_box(self, title, message):
        messagebox.showinfo(title, message)

    def show_error_message_box(self, title, message):
        messagebox.showerror(title, message)


