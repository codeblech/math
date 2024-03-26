# __sub__ is broke

class Polynomial:
    def __init__(self, *args):
        self.coefficients = [i for i in args]
        for coeff in self.coefficients.copy():
            if coeff == 0:
                self.coefficients.remove(coeff)
            elif coeff != 0:
                break 

        for index, coeff in enumerate(self.coefficients):
                self.degree = len(self.coefficients) - 1 - index
                break

    def __repr__(self):
        return self.coefficients

    def __str__(self):
        # 1x^3 + 2x^2 + 3x + 4
        output = ''
        power = self.degree
        for coeff in self.coefficients:
            output += str(coeff) + 'x^' + str(power) + ' + '
            power -= 1
        
        output = output.rstrip('x^0 + ')
        
        if output[0:2] == '1x':
            output = output[1:]
        elif output[0:2] == '-1':
            output = output[2:]
            output = '-' + output
        
        return output.rstrip()

    def __add__(self, other):
        resultant_coefficients = []
        smaller_degree_polynomial_coefficients = self.coefficients
        larger_degree_polynomial_coefficients = other.coefficients
        
        if len(self.coefficients) > len(other.coefficients):
            smaller_degree_polynomial_coefficients = other.coefficients
            larger_degree_polynomial_coefficients = self.coefficients

        for i in range(len(larger_degree_polynomial_coefficients) - len(smaller_degree_polynomial_coefficients)):
            smaller_degree_polynomial_coefficients.insert(0, 0)

        for i, j in zip(larger_degree_polynomial_coefficients, smaller_degree_polynomial_coefficients):
            resultant_coefficients.append(i+j)
        
        return Polynomial(*resultant_coefficients)

    def __sub__(self, other):
        resultant_coefficients = []
        smaller_degree_polynomial_coefficients = self.coefficients
        larger_degree_polynomial_coefficients = other.coefficients
        
        if len(self.coefficients) > len(other.coefficients):
            smaller_degree_polynomial_coefficients = other.coefficients
            larger_degree_polynomial_coefficients = self.coefficients

        for i in range(len(larger_degree_polynomial_coefficients) - len(smaller_degree_polynomial_coefficients)):
            smaller_degree_polynomial_coefficients.insert(0, 0)
        print(smaller_degree_polynomial_coefficients, larger_degree_polynomial_coefficients)

        for i, j in zip(larger_degree_polynomial_coefficients, smaller_degree_polynomial_coefficients):
            resultant_coefficients.append(i-j)
        
        return Polynomial(*resultant_coefficients)





p1 = Polynomial(6, 6, 10, 10)
p2 = Polynomial(4, 4, 5)

a = p1 - p2
print(a)


