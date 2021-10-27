class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ("rojo","verde","amarillo","negro","blanco"):
            self.color = color
    
    pass

class Auto:

    cantidadCreados = None
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        cantidad = 0
        for x in self.asientos:
            if isinstance(x, Asiento):
                cantidad += 1
        return cantidad
    
    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        else:
            for x in self.asientos:
                if (x !=None | x.registro != self.registro):
                    return "Las piezas no son originales"
        return "Auto original"

    pass

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        if isinstance(registro, int):
            self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ("electrico" ,"gasolina"):
            self.tipo = tipo
    pass
