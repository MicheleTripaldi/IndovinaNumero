import random

class Model(object):
    def __init__(self):
        self._NMax = 100
        self._TMax = 6 # vite massime
        self._T = self._TMax # vite rimanenti, quando inizio il gioco uguali a t max
        self._segreto = None # quando creiamo il modello non lo sappiamo.

    def reset(self):
        # questo metodo resetta il gioco in qualsiasi momento
        self._segreto = random.randint(0, self._NMax)
        self._T = self._TMax
        print(self._segreto)


    def play(self, guess):
        '''
        Funzione che esegue uno step del gioco
        :param guess:  int
        :return: 0 se ho vinto, 2 se ho perso o ho finito le vite, 1 se il mio numero è piu piccolo , -1 se è più grande
        '''
        # da fuori ci arriva un tentativo, confrontiamo il tentativo con il numero seggreeto
        self._T -= 1 # uso una vita e vedo se ho vinto

        if guess == self._segreto:
            return 0 # ho vinto , scegliamo di restituire 0 se si vince
        if self._T == 0: # ho perso definitivamente
            return 2 # sempre aritrario

        if guess > self._segreto:
            return -1 # il segreto è più piccolo
        return 1 # il segreto è più grande

    @property
    def NMax(self):
        return self._NMax

    @property
    def TMax(self):
        return self._TMax

    @property
    def T(self):
        return self._T
    @property
    def segreto(self):
        return self._segreto


if __name__ == '__main__':
    m = Model()
    m.reset()
    print(m.play(50))
    print(m.play(10))

