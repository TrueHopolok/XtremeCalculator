from ui.Button import Button

class SaveButton(Button):
    def __init__(self, pos, size, img, text):
        super(SaveButton, self).__init__(screen, pos, size, img, text)
    def pressed(self):
        # logic
        pass
    def render(self):
        super(SaveButton, self).render()