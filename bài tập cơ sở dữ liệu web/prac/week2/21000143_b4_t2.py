# class Polynomial
class Polynomial:
    def __init__(self, degree,coefficients):
        self.degree = degree
        self.coefficients = coefficients

    # method to_string
    def __str__(self) -> str:
        result = ""
        for i in range(self.degree+1):
            if self.coefficients[i] == 0:
                continue
            if i == 0:
                result = str(self.coefficients[i]) + " + " + result
            if i == 1:
                result = str(self.coefficients[i]) + "x" + " + "+ result
            if i > 1:
                result = str(self.coefficients[i]) + "x^" + str(i) + " + "+ result
        return result[:-3]
    
    # method evaluate
    def evaluate(self,x):
        result = 0
        for i in range(self.degree+1):
            result += self.coefficients[i]*x**i
        return result
    
    # method to add two polynomials
    def add_polynomial(self,other):
        result = Polynomial(max(self.degree,other.degree),[0]*(max(self.degree,other.degree)+1))
        for i in range(self.degree+1):
            result.coefficients[i] += self.coefficients[i]
        for i in range(other.degree+1):
            result.coefficients[i] += other.coefficients[i]
        return result
    
    #method to subtract two polynomials
    def subtract_polynomial(self,other):
        result = Polynomial(max(self.degree,other.degree),[0]*(max(self.degree,other.degree)+1))
        for i in range(self.degree+1):
            result.coefficients[i] += self.coefficients[i]
        for i in range(other.degree+1):
            result.coefficients[i] -= other.coefficients[i]
        return result
    
    # method to multiply two polynomials
    def multiply_polynomial(self,other):
        result = Polynomial(self.degree+other.degree,[0]*(self.degree+other.degree+1))
        for i in range(self.degree+1):
            for j in range(other.degree+1):
                result.coefficients[i+j] += self.coefficients[i]*other.coefficients[j]
        return result
    
    
    
#test
p1 = Polynomial(2,[1,2,3])
p2 = Polynomial(1,[1,2])
print("p1:",p1)
print("p2:",p2)
print("p1 add p2 =",p1.add_polynomial(p2))
print("p1 subtract p2 =",p1.subtract_polynomial(p2))
print("p1 multiply p2 =",p1.multiply_polynomial(p2))



    


    