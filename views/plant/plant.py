from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from kivy.properties import StringProperty, ListProperty, ColorProperty, NumericProperty

Builder.load_file('views/plant/plant.kv')
class PlantView(BoxLayout):
    name = StringProperty("")
    station = StringProperty("")
    source = StringProperty("")
    price = NumericProperty(0)
    def __init__(self, **kw) -> None:
        super().__init__(**kw)