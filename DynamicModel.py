class MassSpringDamper:
    '''
    создаём физическую систему из пружины жесткостью rigitity,
    груза массой mass и сопротивлением resistance 
    (симуляция реально происходящих процессов)
    Цель - установить пружину на нужной координате.
    Силой forse мы двигаем пружину
    
    Пример из реальной жизни - коптер изначально на 0 , нужно - на 100
    сопротивление - ветер
    жесткость пружины - это как вес коптера
    '''
    def __init__(self, rigitity, resistance, mass,
                 coordinate_start=0, speed_start=0, micro_time=0.01):
        '''
        инициализация переменных
        '''
        self.rigitity = rigitity
        self.resistance = resistance
        self.mass = mass
        self.micro_time = micro_time
        self.coordinate = coordinate_start
        self.speed = speed_start
    def update(self, forse):
        '''
        xnew - новая координата 
        vnew - новая скорость(считается из формул физики)
        '''
        xnew = self.speed * self.micro_time + self.coordinate
        vnew = self.micro_time / self.mass * \
            (forse - self.resistance * self.speed - self.rigitity * self.coordinate) + self.speed
        self.coordinate = xnew
        self.speed = vnew
        return self.coordinate
