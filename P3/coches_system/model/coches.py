class Coches:
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._caballaje = caballaje
        self._plazas = plazas
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @property
    def velocidad(self):
        return self._velocidad
    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad
    
    @property
    def caballaje(self):
        return self._caballaje
    @caballaje.setter
    def caballaje(self, caballaje):
        self._caballaje = caballaje
    
    @property
    def plazas(self):
        return self._plazas
    @plazas.setter
    def plazas(self, plazas):
        self._plazas = plazas

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self._traccion = traccion
        self._cerrada = cerrada
    
    @property
    def traccion(self):
        return self._traccion
    @traccion.setter
    def traccion(self, traccion):
        self._traccion = traccion
    
    @property
    def cerrada(self):
        return self._cerrada
    @cerrada.setter
    def cerrada(self, cerrada):
        self._cerrada = cerrada

class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas, toneladas):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self._toneladas = toneladas
    
    @property
    def toneladas(self):
        return self._toneladas
    @toneladas.setter
    def toneladas(self, toneladas):
        self._toneladas = toneladas