from data_test import input_test, output_test

GP_mode = ['sin_inicilizar']*32
GP_pull = ['sin_inicilizar']*32
GP_out_value = ['sin_inicilizar']*32


class Pin():
    (IN,  OUT, PULL_DOWN, PULL_UP) = (0, 1, 2, 1)

    def __init__(self, id, mode=- 1, pull=- 1, value=None):
        self.id = id
        GP_mode[id] = mode
        GP_pull[id] = pull
        GP_out_value[id] = value

    def value(self, x=None):
        if x == None:
            if GP_mode[self.id] == Pin.IN:
                return input_test(self.id)
            else:
                return 'indefinido'
        else:
            GP_out_value[self.id] = x
            output_test(self.id, x)
            return None
