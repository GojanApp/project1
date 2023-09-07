from kivy.app import App
from kivy.uix.label import Label

class BuildApp(App):
	def build(self):
		return Label(text = 'hello rizwan')

BuildApp().run()




















