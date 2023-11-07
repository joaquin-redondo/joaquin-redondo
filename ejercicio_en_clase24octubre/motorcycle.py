class motorcycle:
    #metodos de clase:
    state="nuevo"
    engine=False
    
    #atributos de objeto:
    def __init__(self, colour, tuition, fuel, wheels, brand, model, date_manu, speed_max, weight):
        self.colour=colour
        self.tuition=tuition
        self.fuel=fuel
        self.wheels=wheels
        self.brand=brand
        self.model=model
        self.date_manu=date_manu
        self.speed_max=speed_max
        self.weight=weight
        
    #metodos start y stop para el motor:
    def start(self):
        if self.engine:
            self.engine = True
            print("el motor ha arrancado")
        else:
            print("El motor ya estaba encendido")
            
    def stop(self):
        if not self.engine :
            self.engine = False
            print("el motor se ha detenido")
        else:
            print("El motor ya estaba apagado")
            
    
    