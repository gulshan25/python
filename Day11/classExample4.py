
# ***
# class bassclass:
#     pass


# class derivedclass(baseClass):
#     pass


 # super __init__ (polymerphism)
# ***



# Parent class
class Bird:
    def __init__(self) -> None:
        print('Bird is ready')
    def whoisThis(self):
        print('Bird')

class Penguin(Bird):
    def __init__(self) -> None:
        super().__init__()               
        print('Penguin is ready')

    def whoisThis(self):
        print('Penguin')
    

P = Penguin()
P.whoisThis()


