from ui.Button import Button

class Menu():
    def __init__(self, buttons, texts):
        self.BUTTONS = buttons
        self.TEXTS = texts
    def collision(m_pos):
        for b in self.BUTTONS:
            if b.POS[0] < m_pos and m_pos < b.SIZE[0] + b.POS[0]:
                if b.POS[1] > m_pos and m_pos > b.SIZE[1] + b.POS[1]:
                    b.pressed()
    def render():
        for t in self.TEXTS:
            t.render()
        for b in self.BUTTONS:
            b.render()
        