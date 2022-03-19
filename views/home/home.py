from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.clock import Clock

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/home/home.kv')
class Home(BoxLayout):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
        Clock.schedule_once(self.render, .1)

    def render(self, _):
        plants = [
            {
            'name': 'Mini Jade',
            'station': 'Desktop',
            'source': 'assets/imgs/mini-jade.png',
            'price': 25,
            },
            {
            'name': 'Aloe Vera',
            'station': 'Work Desk',
            'source': 'assets/imgs/aloe-vera.png',
            'price': 14,
            },
            {
            'name': 'Chinese Money Tree',
            'station': 'Balcony',
            'source': 'assets/imgs/chinese-money-tree.png',
            'price': 32,
            },
            {
            'name': 'Monstera Deliciosa',
            'station': 'FrontPoach',
            'source': 'assets/imgs/green-monstera-Deliciosa.png',
            'price': 18,
            },
            {
            'name': 'Green Succulent',
            'station': 'Office Desktop',
            'source': 'assets/imgs/green-succulent.png',
            'price': 25,
            },
            {
            'name': 'Rubber plant',
            'station': 'Living Room',
            'source': 'assets/imgs/rubber-plant.png',
            'price': 54,
            },
            {
            'name': 'Green Kenaf',
            'station': 'Kitchen',
            'source': 'assets/imgs/green-kenaf.png',
            'price': 25,
            },
            {
            'name': 'Chinese Bonsai',
            'station': 'Office Desk',
            'source': 'assets/imgs/bonsai.png',
            'price': 148,
            },
        ]

        self.ids.plants.clear_widgets()
        for p in plants:
            pl = Plant()
            pl.name = p['name']
            pl.source = p['source']
            pl.price = p['price']
            pl.station = p['station']
            pl.bind(on_release=self.view_plant)

            self.ids.plants.add_widget(pl)

    def view_plant(self, inst):
        pv = App.get_running_app().root.ids.plant
        mngr = App.get_running_app().root.ids.scrn_mngr

        pv.name = inst.name
        pv.price = inst.price
        pv.source = inst.source
        pv.station = inst.station

        mngr.current = 'scrn_plant'

class Plant(ButtonBehavior, BoxLayout):
    name = StringProperty("")
    station = StringProperty("")
    source = StringProperty("")
    price = NumericProperty(0)
    radius = NumericProperty(dp(24))
    def __init__(self, **kw) -> None:
        super().__init__(**kw)

