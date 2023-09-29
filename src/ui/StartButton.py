from ui.Button import Button

class StartButton(Button):
    def __init__(self, pos, size, img, text):
        super(StartButton, self).__init__(screen, pos, size, img, text)
    def pressed(self):
        # logic
        pass
    def render(self):
        super(StartButton, self).render()