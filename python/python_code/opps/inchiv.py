class Distance:
    def accept(self,feet,inch):
        print("Accept called!")
        self.feet=feet
        self.inch=inch
    def disp(self):
        if self.inch>=12:
            self.feet=self.feet+self.inch//12
            self.inch=self.inch%12
        print("Feet=",self.feet,",inch=",self.inch)

# print("Feet=",self.feet,",inch=",self.inch)
x=Distance()
# x.disp()
x.accept(5,15)
x.disp()
y=Distance()
y.accept(8,17)
x.disp()
y.disp()