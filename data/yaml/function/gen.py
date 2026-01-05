import numpy

for i in range(314):
    print(f"{i/100:0.2f}:{round(numpy.tan(i/100),2)},",end="")