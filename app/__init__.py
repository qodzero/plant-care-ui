
from kivy.app import App
from kivy.metrics import dp, sp
from kivy.utils import rgba, QueryDict

from .view import MainWindow

class MainApp(App):
    colors = QueryDict()
    colors.primary = rgba("#0c3b2e")
    colors.secondary = rgba("#bbcbc2")
    colors.warning = rgba("#ffba00")
    colors.danger = rgba("#E86767")
    colors.success = rgba("##6d9773")
    colors.white = rgba("#FFFFFF")
    colors.grey = rgba("#C4C4C4")
    colors.grey_light = rgba("#EAEAEA")

    fonts = QueryDict()
    fonts.heading = 'assets/fonts/BlackMango/BlackMango-Bold.otf'
    fonts.subheading = 'assets/fonts/Roboto/Roboto-Regular.ttf'
    fonts.body = 'assets/fonts/Roboto/Roboto-Light.ttf'
    
    fonts.size = QueryDict()
    fonts.size.h1 = sp(24)
    fonts.size.h2 = sp(22)
    fonts.size.h3 = sp(18)
    fonts.size.h4 = sp(16)
    fonts.size.h5 = sp(14)
    fonts.size.h6 = sp(12)
    def build(self):
        return MainWindow()
