import numpy as np

def sigmoid(sop):
	return 1.0/(1+ np.exp(-1*sop))

def errorCalculation(predicted,target):
	return np.power(predicted-target,2)

def errorPredictedDerivative(predicted,target):
	return 2*(predicted-target)

def activationSopDerivative(sop):
	return sigmoid(sop) *(1.0 - sigmoid(sop))

def sopwDerivative(x):
	return x

def updateW(w,grad, learningrate):
	return w-learningrate * grad


x 				=	 0.1
target 			=    0.3
learningrate    =    0.01

w 				= 	 np.random.rand()
print("Initial weight :",w)

for k in range(1000000):
	#Forward pass
	y			=	w*x
	predicted 	=   sigmoid(y)
	error 	    =   errorCalculation(predicted,target)

	#Backward pass
	g1			=  errorPredictedDerivative(predicted,target)
	g2			=  activationSopDerivative(predicted)
	g3          =  sopwDerivative(x)

	grad		= g3*g2*g1

	print(predicted)

	w = updateW(w,grad,learningrate)
