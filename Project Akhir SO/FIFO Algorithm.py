class FIFOPageReplacement:
    def __init__(self):
        self.frames = None
        self.memory = None
        self.faults = 0
        self.hits = 0
        self.fifo = 0

    def FRAMES(self, frames):
        self.frames = frames
        self.memory = [None] * frames
        print(f"Current Memory = {self.memory}")

    def FIFO_PROCESS(self, page):  
        if self.frames is None:
            raise ValueError  ("Number of frames is not set. Please set frames using FRAMES() method.")
        
        if page not in self.memory:
            self.memory[self.fifo] = page
            self.fifo = (self.fifo + 1) % self.frames
            self.faults += 1
            print(self.memory)
        else:
            self.hits += 1
            print(self.memory)
        print(f"Page Faults: {self.faults}")
        print(f"Page Hits: {self.hits}")

    def CLEAR(self):
        self.memory = [None] * self.frames
        self.faults = 0
        self.hits = 0
        self.fifo = 0
        print("!!! Memory cleared !!!")

    def PRINT(self) :
        print(f"Current Memory = {self.memory}")

Mulai = FIFOPageReplacement()

while True :
    print("\n--------= MENU =--------\n1. Reference String\n2. Clear Memory\n3. Print Memory\n4. Exit")
    pilih = int(input("Your Choice >>> "))
    if pilih == 1 :
        frame = int(input("Select Memory Frame >>> "))
        Mulai.FRAMES(frame)
        i = 1
        salah = 0
        k = 3
        while i <= 16 : # [2 8 9 3 0 9 8 9 2 0 3 2 0 3 9 0]
            try :
                if salah == 3 :
                    break
                else :
                    page = int(input("Input Reference String >>> "))
                    Mulai.FIFO_PROCESS(page)
                    i += 1
            except :
                salah += 1
                k -= 1
                print(f"!!! Enter integer number !!!\n!!! you have {k} attempt left !!!")       
    elif pilih == 2 :
        Mulai.CLEAR()
    elif pilih == 3 :
        Mulai.PRINT()
    elif pilih == 4 :
        print("--------= THANK YOU =--------")
        break
    else :
        print("Please select the number above")