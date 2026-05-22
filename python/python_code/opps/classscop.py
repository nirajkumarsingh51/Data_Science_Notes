class Distance:
    feet=4 #class scope variable
    inch=13 #class scope variable
    def accept(self,feet,inch):
        print("Accept called!")
        Distance.feet=feet
        Distance.inch=inch
    def disp(self):
        if self.inch>=12:
            Distance.feet=self.feet+self.inch//12
            Distance.inch=self.inch%12
        print("Feet=",self.feet,",inch=",self.inch)

print("Feet=",Distance.feet,",inch=",Distance.inch)
x=Distance()
x.disp()
x.accept(5,15)
x.disp()
y=Distance()
y.disp()
y.accept(8,17)
x.disp()
y.disp()