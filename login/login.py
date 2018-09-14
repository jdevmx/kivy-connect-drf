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
import requests
import json

from home.home import Home
from ws.ws import WSRequests


class Login(BoxLayout):
    ws_url = 'http://localhost:8000/client-token/'

    def do_login(self, login, passwd):
        headers = {'content-type': 'application/json'}
        params = {
            'username': login,
            'password': passwd
        }
        response = requests.post(url=self.ws_url, data=json.dumps(params), headers=headers)
        if response.status_code == 200:
            token_dict = json.loads(response.text)
            self.save_token(str=token_dict['token'])
            ws_req = WSRequests()
            user_response = ws_req.get_ws_data(
                action_url='empresa/rest/get_user_info/',
                params={'username': login}
            )
            if user_response.resp_status == 403:
                print('Permiso Denegado')
            else:
                app = App.get_running_app()
                app.root_window.remove_widget(app.root)
                home_window = Home(username=login, login_window=self)
                app.root_window.add_widget(home_window)
        else:
            print(f'Usuario o contraseña inválida')

    def save_token(self, str):
        with open('token', 'w') as outfile:
            outfile.write(str)

