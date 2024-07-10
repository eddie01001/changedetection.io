
from changedetectionio.model.Watch import model as BaseWatch


class Restock(dict):
    def __init__(self, *args, **kwargs):
        # Define default values
        default_values = {
            'in_stock': None,
            'price': None,
            'currency': None,
            'original_price': None
        }

        # Initialize the dictionary with default values
        super().__init__(default_values)

        # Update with any provided positional arguments (dictionaries)
        if args:
            if len(args) == 1 and isinstance(args[0], dict):
                self.update(args[0])
            else:
                raise ValueError("Only one positional argument of type 'dict' is allowed")

        # Update with keyword arguments
        self.update(kwargs)


    def __setitem__(self, key, value):
        # Custom logic to handle setting price and original_price
        if key == 'price':
            if value and not self.get('original_price'):
                self['original_price'] = value
        super().__setitem__(key, value)

class Watch(BaseWatch):
    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)
        self.update({'restock': Restock()})

    def clear_watch(self):
        super().clear_watch()
        self.update({'restock': Restock()})

