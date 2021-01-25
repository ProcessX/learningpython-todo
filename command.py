class Command:
    'Command object contains: shortcut, effect, description'

    shortcut = ''
    effect = None
    description = 'A command'

    def __init__(self, shortcut, effect, description) -> None:
        self.shortcut = shortcut
        self.effect = effect
        self.description = description
        pass


    def run(self):
        #Call the function passed as effect
        self.effect()