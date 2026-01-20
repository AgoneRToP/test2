class car:
    def __init__(self, motor, bak, benzin_miqdori, probeg):
        self.motor = motor
        self.bak = bak
        self.benzin_miqddori = benzin_miqdori
        self.probeg = probeg
        self.prk = True

    def yurmoq(self):
        if not self.benzin_miqddori >= self.motor / self.bak * self.probeg:
            print("NE ", end="")
            self.prk = False
        print("DOYEDYET")
        self.benzin()

    def benzin(self):
        if self.prk:
            print("OSTALOS: ", end="")
            print(self.benzin_miqddori - self.motor / self.bak * self.probeg, end="")
            print(" LITRA")
            

tx1 = car(8, 100, 20, 200)

tx1.yurmoq()