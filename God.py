def God_trigger(func):
    def wrapper(self, *args, **kwargs):
        print(f'Вы осмелились потревожить {self._name}', end = "\n")
        return func(self, *args, *kwargs)
    return wrapper

class God():
    def __init__(self, name,  element):
        self._name, self._element = name, element

    @God_trigger
    def listen_praying(self, text_of_praying):
        print("Молитва выслушана\n")

    @property
    def name(self): #
        return self._name

    @property
    @God_trigger
    def elem(self): # +  @God_trigger
        return self._element


    @God_trigger
    def __str__(self):
        return (f'Имя: {self._name}\n'
                f'Стихия: {self._element}\n')

