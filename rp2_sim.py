def asm_pio(*args, **kwargs):
    # Simulación de raspberry en consola sin hardware. Parámetros: variables con etiqueta "*args", y sin etiqueta "**kwargs"
    def decorador(programa):
        # Decorador. Parámetro es la función instanciada o que se pretende decorar
        def compilador():
            # Permite compilar e imprimir los datos de la función en la consola
            print("Parámetros", kwargs)
            programa()
            return None
        return compilador
    return decorador


def decorador_instr(fun_inst):
    # Decorador. Parámetro es la función instanciada o que se pretende decorar
    def decoracion_instr(self, *args, **kwargs):
        # Decorador. Parámetros: *args es una variable empaquetada, **kwargs es una variable desempaquetada
        fun_inst(self, *args, **kwargs)
        return None
    return decoracion_instr


pins = 'pins'


class PIO():
    OUT_LOW = 'PIO.OUT_LOW'


class StateMachine:
    def __init__(self, id_, program, freq=125000000, **kwargs):
        # Constructor de la clase stage. Parámetros: self llama la variable a sí misma, id__ devuelve la identidad de la variable, program , freq es la frecuencia de trabajo del RP2040, **kwargs es una variable sin etiqueta
        global sm_iniciandose, fsms
        sm_iniciandose = self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr = []
        program()
        print('Fueron leidas', len(self.lista_instr), 'instrucciones')
        sm_iniciandose = None
        fsms[id_] = self
        pass

    def active(self, x=None):
        '''Esta rutina simula exclisivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
        if x == 1:
            print('Está pendiente de realizar la simulacón')


fsms = [None]*8

sm_iniciandose = None


class nop:
    @decorador_instr
    def __init__(self, *args, **kwargs):
        # Contructor de la clase nop
        global sm_iniciandose
        print(self.__class__.__name__)  # ,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass

    def __getitem__(self, name):
        # Toma la variable u objeto
        # print('nop.__getattr__',name)
        pass


class set(nop):
    def __init__(self, *args, **kwargs):
        # constructor de la clase set
        super().__init__(*args, **kwargs)
        pass


class wrap_target(nop):
    def __init__(self, *args, **kwargs):
        # Contructor de la clase wrap_target
        super().__init__(*args, **kwargs)
        pass


class wrap(nop):
    def __init__(self, *args, **kwargs):
        # Constructor de la clase wrap
        super().__init__(*args, **kwargs)
        pass
