class OptimalPageReplacement:
    def __init__(self):
        self.faults = 0
        self.hits = 0
        self.refstring = None
        self.memory = None
        self.frames = None
        self.optimal = {}

    def REFSTRING(self, reference_string) :
        self.refstring = reference_string

    def FRAMES(self, frames):
        self.frames = frames
        self.memory = [None] * self.frames
        print(f"Current Memory = {self.memory}")
    
    def OPTIMAL_PROCESS(self, access, reference_string):
        if self.frames is None:
            raise ValueError("Number of frames is not set. Please set frames using FRAMES() method.")

        for i, page in enumerate(reference_string):
            if access == page : 
                if access in self.optimal and i < self.optimal[page] :
                    continue 
                elif access in self.optimal and i == self.optimal[page] :   
                    if access in self.memory :
                        self.hits += 1
                        print(self.memory)
                    elif access not in self.memory :
                        self.faults += 1
                        FORMULA = -1
                        REPAGE = None
                        for frame in self.memory:
                            if frame not in self.optimal:
                                REPAGE = frame
                                break
                            if self.optimal[frame] > FORMULA:
                                FORMULA = self.optimal[frame]
                                REPAGE = frame
                        self.memory[self.memory.index(REPAGE)] = page
                        print(self.memory)
                    

                elif page not in self.memory:
                    self.faults += 1
                    if None in self.memory:
                        self.memory[self.memory.index(None)] = page
                        print(self.memory)
                    else:
                        FORMULA = -1
                        REPAGE = None
                        for frame in self.memory:
                            if frame not in self.optimal:
                                REPAGE = frame
                                break
                            if self.optimal[frame] > FORMULA:
                                FORMULA = self.optimal[frame]
                                REPAGE = frame
                        self.memory[self.memory.index(REPAGE)] = page
                        print(self.memory)

                self.optimal[page] = float('inf') 
                for j in range(i + 1, len(reference_string)): 
                    if reference_string[j] == page:
                        self.optimal[page] = j
                        break
                break

        print(f"Page Faults: {self.faults}")
        print(f"Page Hits: {self.hits}")

    def CLEAR(self):
        self.memory = [None] * self.frames
        self.faults = 0
        self.hits = 0
        self.optimal = {}
        print("!!! Memory cleared !!!")

    def PRINT(self) :
        print(f"Current Memory = {self.memory}")


# Example usage:
Mulai = OptimalPageReplacement()
while True :
    print("\n--------= MENU =--------\n1. Reference String\n2. Clear Memory\n3. Print Memory\n4. Exit")
    pilih = int(input("Your Choice >>> "))
    if pilih == 1 :
        frame = int(input("Select Memory Frame >>> "))
        Mulai.FRAMES(frame)
        pages = list(map(int,input("Input Reference String >>> ").split()))
        Mulai.REFSTRING(pages)
        salah = 0
        k = 3
        for i in range(len(pages)) : # [2 8 9 3 0 9 8 9 2 0 3 2 0 3 9 0]
            try :
                if salah == 3 :
                    break
                else :
                    acc = int(input("Choose Page to Access >>> "))
                    Mulai.OPTIMAL_PROCESS(acc, pages)
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