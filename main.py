from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.font_definitions import theme_font_styles
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen


class MyTableHeader(MDCard):
    pass


class CotadorApp(MDApp):
    def build(self):
        return Builder.load_file('cotador/kv/cotador.kv')

class RootScreen(MDScreen):
    shift_x_signin_button = NumericProperty(0)

    def generate_table(self):
        fornecedores = []
        items = []
        num_fornecedores = int(self.ids.cota_field.text)
        num_items = int(self.ids.items_field.text)
        tabela = self.ids.tabela
        header = MyTableHeader()
        for forn_num in range(num_fornecedores):
            fornecedor = input("Nome do Fornecedor: ")
            fornecedores.append(fornecedor)
        # for item_type in range(num_items):
        #     item = input("Nome do Item: ")
        #     items.append(item)
        for fornecedor in fornecedores:
            header.add_widget(MDLabel(text=str(fornecedor)))
        # for item in items:
        #     tabela.add_widget(MDLabel(text='Item'))
        tabela.add_widget(header)



CotadorApp().run()