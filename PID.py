class PID:
    '''
    система регулировки силы , которой мы действуем на пружину(forse) 
    '''
    def __init__(self, k_p : int , k_d : int, k_i : int,
                 micro_time,lower_bound , upper_bound):
        '''
        инициализация переменных
        '''
        self.k_p = k_p
        self.k_d = k_d
        self.k_i = k_i
        self.micro_time = micro_time
        self.prev_err = None
        self.proportionality = 0
        self.diff = 0
        self.integral = 0
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    def _constrain(self , now_x):
        '''
        ограничение изменения силы
        '''
        if now_x > self.upper_bound:
            return self.upper_bound
        elif now_x < self.lower_bound:
            return self.lower_bound
        else:
            return now_x
    def update(self, now_x, xdes):
        '''
        смотрим ,насколько изменилась координата груза
        также копим ошибку для дифференцирующей части PID регулятора
        '''
        err = now_x - xdes
        self.proportionality = self.k_p * err
        if self.prev_err is not None:
            self.diff = self.k_d * (err - self.prev_err) / self.micro_time
        self.integral += self.k_i * err
        self.prev_err = err
        outp = self.proportionality + self.diff + self.integral
        return self._constrain(outp)
