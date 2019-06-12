import tkinter as tk
import user_interface as ui
import services
import network
import math


class ApplicationController:

    def __init__(self):
        self.root = tk.Tk()
        self.gui = ui.GUI(self.root)
        self.network = network.NeuralNetwork()
        self.players_list = None
        self.selected_players_list = None
        self.gui.train_button.config(command=self.train_network)
        self.gui.predict_button.config(command=self.predict_overall)
        self.gui.select_players_button.config(command=self.select_players)
        self.gui.load_weights_button.config(command=self.load_network_config)
        self.gui.save_weights_button.config(command=self.save_network_config)

    def start(self, path):
        try:
            self.players_list = services.load_players(path)
            self.network.beta_forward_propagation = 0.1
            self.network.beta_backward_propagation = 0.01
            self.gui.players_positions_combobox.current(0)
            self.root.mainloop()
        except FileNotFoundError:
            self.gui.show_error_message_box("START", "Cannot find csv file with players.")

    def train_network(self):
        try:
            self.network.threshold_input_hidden = 15
            self.network.threshold_hidden_output = 3
            self.network.weights_input_hidden = services.generate_matrix(34, 6)
            self.network.weights_hidden_output = services.generate_matrix(6, 1)
            for i in range(100):
                for player in self.selected_players_list:
                    input = services.convert_player_to_input_matrix(player)
                    output = services.convert_player_to_output_matrix(player)
                    input = input / 100
                    output = output / 100
                    calculated_output = self.network.forward_propagation(input)
                    self.network.backward_propagation(input, calculated_output, output)
            self.gui.show_info_message_box("TRAIN NETWORK", "Network trained successfully.")
        except TypeError:
            self.gui.show_error_message_box("TRAIN NETWORK", "You have to select players first.")

    def load_network_config(self):
        try:
            combobox_index = self.gui.players_positions_combobox.current()
            if combobox_index == 0:
                self.network.weights_input_hidden = services.load_weights("weights\gk_input_hidden.txt")
                self.network.weights_hidden_output = services.load_weights("weights\gk_hidden_output.txt")
                thresholds = services.load_thresholds("thresholds\gk_thresholds.txt")
                self.network.threshold_input_hidden = float(thresholds[0])
                self.network.threshold_hidden_output = float(thresholds[1])
            elif combobox_index == 1:
                self.network.weights_input_hidden = services.load_weights("weights\cb_input_hidden.txt")
                self.network.weights_hidden_output = services.load_weights("weights\cb_hidden_output.txt")
                thresholds = services.load_thresholds("thresholds\cb_thresholds.txt")
                self.network.threshold_input_hidden = float(thresholds[0])
                self.network.threshold_hidden_output = float(thresholds[1])
            elif combobox_index == 2:
                self.network.weights_input_hidden = services.load_weights("weights\sb_input_hidden.txt")
                self.network.weights_hidden_output = services.load_weights("weights\sb_hidden_output.txt")
                thresholds = services.load_thresholds("thresholds\sb_thresholds.txt")
                self.network.threshold_input_hidden = float(thresholds[0])
                self.network.threshold_hidden_output = float(thresholds[1])
            elif combobox_index == 3:
                self.network.weights_input_hidden = services.load_weights("weights\cm_input_hidden.txt")
                self.network.weights_hidden_output = services.load_weights("weights\cm_hidden_output.txt")
                thresholds = services.load_thresholds("thresholds\cm_thresholds.txt")
                self.network.threshold_input_hidden = float(thresholds[0])
                self.network.threshold_hidden_output = float(thresholds[1])
            elif combobox_index == 4:
                self.network.weights_input_hidden = services.load_weights("weights\w_input_hidden.txt")
                self.network.weights_hidden_output = services.load_weights("weights\w_hidden_output.txt")
                thresholds = services.load_thresholds("thresholds\w_thresholds.txt")
                self.network.threshold_input_hidden = float(thresholds[0])
                self.network.threshold_hidden_output = float(thresholds[1])
            elif combobox_index == 5:
                self.network.weights_input_hidden = services.load_weights("weights\st_input_hidden.txt")
                self.network.weights_hidden_output = services.load_weights("weights\st_hidden_output.txt")
                thresholds = services.load_thresholds("thresholds\st_thresholds.txt")
                self.network.threshold_input_hidden = float(thresholds[0])
                self.network.threshold_hidden_output = float(thresholds[1])
            self.gui.show_info_message_box("LOAD WEIGHTS", "Weights loaded successfully.")
        except FileNotFoundError:
            self.gui.show_error_message_box("LOAD WEIGHTS", "Files with weights are missing.")

    def save_network_config(self):
        try:
            combobox_index = self.gui.players_positions_combobox.current()
            if combobox_index == 0:
                services.save_weights("weights\gk_input_hidden.txt", self.network.weights_input_hidden)
                services.save_weights("weights\gk_hidden_output.txt", self.network.weights_hidden_output)
                services.save_threshold("thresholds\gk_thresholds.txt", self.network.threshold_input_hidden,
                                        self.network.threshold_hidden_output)
            elif combobox_index == 1:
                services.save_weights("weights\cb_input_hidden.txt", self.network.weights_input_hidden)
                services.save_weights("weights\cb_hidden_output.txt", self.network.weights_hidden_output)
                services.save_threshold("thresholds\cb_thresholds.txt", self.network.threshold_input_hidden,
                                        self.network.threshold_hidden_output)
            elif combobox_index == 2:
                services.save_weights("weights\sb_input_hidden.txt", self.network.weights_input_hidden)
                services.save_weights("weights\sb_hidden_output.txt", self.network.weights_hidden_output)
                services.save_threshold("thresholds\sb_thresholds.txt", self.network.threshold_input_hidden,
                                        self.network.threshold_hidden_output)
            elif combobox_index == 3:
                services.save_weights("weights\cm_input_hidden.txt", self.network.weights_input_hidden)
                services.save_weights("weights\cm_hidden_output.txt", self.network.weights_hidden_output)
                services.save_threshold("thresholds\cm_thresholds.txt", self.network.threshold_input_hidden,
                                        self.network.threshold_hidden_output)
            elif combobox_index == 4:
                services.save_weights("weights\w_input_hidden.txt", self.network.weights_input_hidden)
                services.save_weights("weights\w_hidden_output.txt", self.network.weights_hidden_output)
                services.save_threshold("thresholds\w_thresholds.txt", self.network.threshold_input_hidden,
                                        self.network.threshold_hidden_output)
            elif combobox_index == 5:
                services.save_weights("weights\st_input_hidden.txt", self.network.weights_input_hidden)
                services.save_weights("weights\st_hidden_output.txt", self.network.weights_hidden_output)
                services.save_threshold("thresholds\st_thresholds.txt", self.network.threshold_input_hidden,
                                        self.network.threshold_hidden_output)
            self.gui.show_info_message_box("SAVE WEIGHTS", "Weights saved successfully.")
        except ValueError:
            self.gui.show_error_message_box("SAVE WEIGHTS", "You should train or load weights first before saving them.")

    def select_players(self):
        combobox_index = self.gui.players_positions_combobox.current()
        if combobox_index == 0:
            self.selected_players_list = services.select_goalkeepers(self.players_list)
        elif combobox_index == 1:
            self.selected_players_list = services.select_centre_backs(self.players_list)
        elif combobox_index == 2:
            self.selected_players_list = services.select_side_backs(self.players_list)
        elif combobox_index == 3:
            self.selected_players_list = services.select_centre_midfielders(self.players_list)
        elif combobox_index == 4:
            self.selected_players_list = services.select_wingers(self.players_list)
        elif combobox_index == 5:
            self.selected_players_list = services.select_strikers(self.players_list)
        self.gui.players_listbox.delete(0, tk.END)
        for i in range(len(self.selected_players_list)):
            self.gui.players_listbox.insert(i, self.selected_players_list[i])
        self.gui.show_info_message_box("SELECT PLAYERS", "Players loaded successfully.")

    def predict_overall(self):
        try:
            listbox_index = self.gui.players_listbox.curselection()[0]
            selected_player = self.selected_players_list[listbox_index]
            input = services.convert_player_to_input_matrix(selected_player)
            input = input / 100
            test_output = self.network.forward_propagation(input)
            self.gui.player_name_label['text'] = selected_player.name
            self.gui.real_overall_value_label['text'] = selected_player.overall
            self.gui.predicted_overall_value_label['text'] = (math.floor(test_output*100))
            self.gui.deviation_value_label['text'] = abs((math.floor(test_output*100) - int(selected_player.overall)))
        except IndexError:
            self.gui.show_error_message_box("PREDICT OVERALL", "You should choose player first.")
        except TypeError:
            self.gui.show_error_message_box("PREDICT OVERALL", "You should train or load weights first.")
