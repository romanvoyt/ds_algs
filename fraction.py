def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            
            m = oldn
            n = oldm%oldn
        return n

class Fraction:
    def __init__(self, numerator, denumerator):
        self.num = numerator
        self.den = denumerator
        
    def show_fr(self):
        print(str(self.num),"/",str(self.den))

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __eq__(self, other_fraction):
        num1 = self.num * other_fraction.den
        num2 = self.den * other_fraction.num
        return num1 == num2
    
    def __mul__(self, other_fraction):
        newnum = self.num * other_fraction.num
        newden = self.den * other_fraction.den
        common_dev = gcd(newnum, newden)
        return Fraction(newnum//common_dev, newden//common_dev)
    
    def __sub__(self, other_fraction):
        common_den = self.den * other_fraction.den
        newnum = int(self.num * common_den/self.den) - int(other_fraction.num * common_den/other_fraction.den)
        common = gcd(newnum, common_den)
        return Fraction(newnum//common, common_den//common)
    
    def __dev__(self, other_fraction):
        newnum = self.num * other_fraction.den
        newden = self.den * other_fraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __gt__(self, other_fraction):
        common_den = self.den * other_fraction.den
        num1 = self.num * common_den
        num2 = other_fraction.num * common_den
        return num1 > num2
    
    def __lt__(self, other_fraction):
        common_den = self.den * other_fraction.den
        num1 = self.num * common_den
        num2 = other_fraction.num * common_den
        return num1 < num2
        
    

f1 = Fraction(1,4)
f2 = Fraction(3,4)

print("show f1 =", str(f1) + " and f2=", str(f2))

print("Does f1 == f2?", f1 == f2)
print("Product of f1 and f2: ", f1*f2)
print("Subtraction f1 from f2", f1-f2)
print("Devision f1 on f2", f1.__dev__(f2))
print("Does f1 > than f2? ", f1.__gt__(f2))
print("Does f1 < than f2? ", f1.__lt__(f2))




    
