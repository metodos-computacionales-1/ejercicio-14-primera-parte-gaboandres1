grafica.png : graficar.py data.dat Euler.x
	python graficar.py

data.dat : Euler.x
	./Euler.x 50 > data.dat
Euler.x : Euler.cpp
	c++ Euler.cpp -o Euler.x
	
clean :
	rm -r *.x *.dat *.png