from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.event import EventDispatcher
from kivy.lang import Builder

Builder.load_file("event_comm.kv")


class GlobalState(EventDispatcher):
    current_status = StringProperty("Inicial")


class StatusDisplayWidget(BoxLayout):
    global_state_obj = ObjectProperty(None)


class StatusChangerWidget(BoxLayout):
    global_state_obj = ObjectProperty(None)

    def update_status(self, new_status):
        self.global_state_obj.current_status = new_status


class EventCommApp(App):
    def build(self):
        # Cria uma instância compartilhada de estado global
        self.shared_state = GlobalState()

        # Cria widgets e injeta o estado global
        root = BoxLayout(orientation='vertical', spacing=20, padding=20)

        display = StatusDisplayWidget()
        changer = StatusChangerWidget()
        display.global_state_obj = self.shared_state
        changer.global_state_obj = self.shared_state

        root.add_widget(display)
        root.add_widget(changer)
        return root


if __name__ == "__main__":
    EventCommApp().run()
