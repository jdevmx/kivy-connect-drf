# coding: utf-8

# ######################### #
#                           #
# Autor: Jorge Dominguez    #
#                           #
# MandarinaSoft - 2018      #
#                           #
# ######################### #
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Home(BoxLayout):
    username = 'Nombre de Usuario'

    def __init__(self, username, login_window, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.username = username
        self.ids['label_username'].text = f'Bienvenido {self.username}'
        self.login_window = login_window

    def go_pv(self):
        pass

    def logout(self):
        app = App.get_running_app()
        app.root_window.remove_widget(app.root)
        app.root_window.add_widget(self.login_window)
