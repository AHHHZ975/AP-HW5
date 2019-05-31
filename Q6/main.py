
import math        
from math import cos
from math import sin
from math import exp

class GauseSolver(object):
	"""docstring for GauseSolver"""
	def __init__(self, polynomialDegree, downBoundry, upBoundry):# function):
		super(GauseSolver, self).__init__()		
		self.polynomialDegree = polynomialDegree
		self.downBoundry = downBoundry
		self.upBoundry = upBoundry
		# self.function = function(variable) 

	def legendre(self, polynomialDegree, variable):
		if polynomialDegree is 0:
			return 1
		elif polynomialDegree is 1:
			return variable
		else:								
			return ((2.0 * polynomialDegree - 1) / polynomialDegree) * variable * self.legendre(polynomialDegree - 1, variable) - ((1.0 * polynomialDegree - 1) / polynomialDegree) * self.legendre(polynomialDegree - 2, variable)

	def legendreDeivative(self, polynomialDegree, variable):				
		return (1.0 * polynomialDegree / (variable * variable - 1)) * ((variable * self.legendre(polynomialDegree, variable)) - self.legendre(polynomialDegree - 1, variable))

	def legendreZeroes(self, polynomialDegree, i):
		xnew = 0.0
		xold = math.cos(3.141592*(i-1/4.0)/((polynomialDegree+1)/2.0))
		iteration = 1
		while True:
			if not (iteration is 1):
				xold = xnew				
			xnew = xold - (self.legendre(polynomialDegree, xold) / self.legendreDeivative(polynomialDegree, xold));			
			iteration += 1
			if (1 + abs((xnew - xold))) <= 1.0:				
				break
		return xnew
			
	def weight(self, polynomialDegree, variable):		
		return 2 / ((1 - pow(variable, 2)) * pow(self.legendreDeivative(polynomialDegree, variable), 2))

	def exec(self):		
		integral = 0.0
		counter = 1
		while counter <= self.polynomialDegree:							
			integral += (self.polynomialFunction(self.legendreZeroes(self.polynomialDegree, counter))*self.weight(self.polynomialDegree, self.legendreZeroes(self.polynomialDegree, counter)))
			counter += 1
		return abs(((self.upBoundry - self.downBoundry) / 2.0) * integral);

	def polynomialFunction(self, variable):
		return ((variable ** 3)/(variable+1))*cos(variable**2)	
		# return cos(variable**2)	


a = 0
b = 1
n = 2
aSolver  = GauseSolver(n, a, b)
print(aSolver.exec())