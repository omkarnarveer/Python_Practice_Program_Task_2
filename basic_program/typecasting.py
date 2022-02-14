'''Use type casting to check every possibility of type casting  ( int to other types,float to other type,..).Form a table as below to maintain track.[P:Possible N=Not Possible]
Cast to→		int	float	bool	complex	str
int			            P	
float			P
bool			P
complex		N
str			             *P         '''

class Typecasting:	
	def display(self):
		print("Cast to->\tint\tfloat\tbool\tComplex\tstr")
		print("int\t\tP\tP\tP\tP\tP")
		print("float\t\tP\tP\tP\tP\tP")
		print("bool\t\tP\tP\tP\tP\tP")
		print("complex\t\tN\tN\tP\tP\tP")
		print("str\t\tN\tN\tP\tN\tP")
c=Typecasting()
c.display()
