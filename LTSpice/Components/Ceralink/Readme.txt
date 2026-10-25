SPICE-Library for LTspice (Linear Technologies)
for TDK Electronics: B5803x.lib
Version 2.3.1
assembled March 2024

This SPICE library contains all models for 
CeraLink ceramic capacitors. The models are implemented
in different files corresponding to the voltage available
classes (500V, 700V and 900V). For each class there is 
a frequency domain (FD) and a time domain (TD) model.
The TD model is suited for transient simulations, whereas 
the FD model should be used for AC simulations. The parameter
"fg" in the TD model adjusts the discrimination between DC
bias and AC magnitude, which are determined form the signal
automatically in the TD model. For the FD model DC bias and 
AC amplitude have to be specified in advance by the parameters
"Vdc" and "Vaceff", respectively. "Vaceff" is the effective
value of the AC signal. The parameter "captemp" is common
for both model types and specifies the temperature of the 
capacitor. 

For each voltage class different models are available for 
the different available packages (LP, FAx and 2220). 

Both TD and FD model consider the change in capacity 
depending on temperature, DC bias and AC amplitude
-> C(T,Vdc,Vac). The TD model further considers the 
change of ESR with respect to frequency -> ESR(f).
Temperature and DC bias influence on ESR is not 
implemented in the TD model, because it can be neglected
in most operation cases. The FD model further considers
the change of ESR depending on temperature, DC bias and 
frequency -> ESR(T,Vdc,f). 

Accurate results can be expected below
the first resonant frequency. Using these models 
outside its specification can lead to false results.

The models describe the behaviour of typical 
elements. Please keep in mind, that real components
can vary in the range given in the datasheets.

Library listing of all parts:
 - File B5803x_500V_TD.sub
	B58031I5105M062_1uF_LP_TD CeraLink 1uF ceramic capacitor; time domain simulation model (1uF)
	B58035U5205M062_2uF_FA2_TD CeraLink 2uF ceramic capacitor; time domain simulation model (2uF)
	B58035U5305M062_3uF_FA3_TD CeraLink 3uF ceramic capacitor; time domain simulation model (3uF)
	B58035U5106M001_10uF_FA10_TD CeraLink 10uF ceramic capacitor; time domain simulation model (10uF)


 - File B5803x_500V_FD.sub
	B58031I5105M062_1uF_LP_FD CeraLink 1uF ceramic capacitor; frequency domain simulation model (1uF)
 	B58035U5205M062_2uF_FA2_FD CeraLink 2uF ceramic capacitor; time domain simulation model (2uF)
	B58035U5305M062_3uF_FA3_FD CeraLink 3uF ceramic capacitor; time domain simulation model (3uF)
	B58035U5106M001_10uF_FA10_FD CeraLink 10uF ceramic capacitor; time domain simulation model (10uF)


 - File B5803x_700V_TD.sub
	B58031I7504M062_0.5uF_LP_TD CeraLink 0.5uF ceramic capacitor; time domain simulation model (0.5uF)
	B58035U7105M062_1uF_FA2_TD CeraLink 1uF ceramic capacitor; time domain simulation model (1uF)
	B58035U7155M062_1.5uF_FA3_TD CeraLink 1.5uF ceramic capacitor; time domain simulation model (1.5uF)
	B58035U7505M001_5uF_FA10_TD CeraLink 5uF ceramic capacitor; time domain simulation model (5uF)


 - File B5803x_700V_FD.sub 
	B58031I7504M062_0.5uF_LP_FD CeraLink 0.5uF ceramic capacitor; frequency domain simulation model (0.5uF)
	B58035U7105M062_1uF_FA2_FD CeraLink 1uF ceramic capacitor; frequency domain simulation model (1uF)
	B58035U7155M062_1.5uF_FA3_FD CeraLink 1.5uF ceramic capacitor; frequency domain simulation model (1.5uF)
	B58035U7505M001_5uF_FA10_FD CeraLink 5uF ceramic capacitor; frequency domain simulation model (5uF)


 - File B5803x_900V_TD.sub 
	B58031I9254M062_0.25uF_LP_TD CeraLink 0.25uF ceramic capacitor; time domain simulation model (0.25uF)
	B58035U9504M062_0.5uF_FA2_TD CeraLink 0.5uF ceramic capacitor; time domain simulation model (0.5uF)
	B58035U9754M062_0.75uF_FA3_TD CeraLink 0.75uF ceramic capacitor; time domain simulation model (0.75uF)
	B58035U9255M001_2.5uF_FA10_TD CeraLink 2.5uF ceramic capacitor; time domain simulation model (2.5uF)


 - File B5803x_900V_FD.sub
	B58031I9254M062_0.25uF_LP_FD CeraLink 0.25uF ceramic capacitor; frequency domain simulation model (0.25uF)
	B58035U9504M062_0.5uF_FA2_FD CeraLink 0.5uF ceramic capacitor; frequency domain simulation model (0.5uF)	
	B58035U9754M062_0.75uF_FA3_FD CeraLink 0.75uF ceramic capacitor; frequency domain simulation model (0.75uF)
	B58035U9255M001_2.5uF_FA10_FD CeraLink 2.5uF ceramic capacitor; frequency domain simulation model (2.5uF)


 - File B5804x_2220_500V_TD.sub
	B58043I5254M052_0.25uF_TD CeraLink 0.25uF ceramic capacitor; time domain simulation model (0.25uF)

 - File B5804x_2220_500V_FD.sub
	B58043I5254M052_0.25uF_FD CeraLink 0.25uF ceramic capacitor; frequency domain simulation model (0.25uF)
	
 - File B5804x_2220_900V_TD.sub
	B58043I9563M052_0.056uF_TD CeraLink 0.056uF ceramic capacitor; time domain simulation model (0.056uF)

 - File B5804x_2220_900V_FD.sub
	B58043I9563M052_0.056uF_FD CeraLink 0.056uF ceramic capacitor; frequency domain simulation model (0.056uF)


Installation of B58031 Model Library
===============================================================

The model library of B5803x (Current compensated ring core dual chokes) for the
circuit design program LTspice comprises the 
following 12 files:

B5803x_x00V_TD.sub	ASCII data file:
	        	These files represent the actual library 
			for the TD model of each voltage class and 
	        	contains the data required for simulation.

B5803x_x00V_FD.sub	ASCII data file:
	        	These files represent the actual library 
			for the FD model of each voltage class and 
	        	contains the data required for simulation.
		
B5803x_x00V_TD.asy	Symbol data file:
	        	These files contain the graphics information
		        required by the graphic user interface for 
			the TD model of each voltage class

B5803x_x00V_FD.asy	Symbol data file:
	        	These files contain the graphics information
		        required by the graphic user interface for 
			the FD model of each voltage class
		
Testbench_B5803x_FD.asc
                LTspice schematic file:
	        This file contains a testbench to experience
	        the setup and behaviour of the FD simulation models

Testbench_B5803x_TD.asc
                LTspice schematic file:
	        This file contains a testbench to experience
	        the setup and behaviour of the TD simulation models

LTspice IV:

1)  Change to the library containing folder of your LTspice
    installation:
    C:/Program Files/LTC/LTspiceIV/lib
    
2)  Place the library file (B5803x_500V_TD.sub, B5803x_500V_FD.sub, 
    B5803x_700V_TD.sub, B5803x_700V_FD.sub, B5803x_900V_TD.sub, 
    B5803x_900V_FD.sub, B5804x_2220_500V_TD.sub and 
	B5804x_2220_900V_TD.sub) in the folder sub.

3)  Place the symbol file (B5803x_500V_TD.asy, B5803x_500V_FD.asy, 
    B5803x_700V_TD.asy, B5803x_700V_FD.asy, B5803x_900V_TD.asy,  
    B5803x_900V_FD.asy, B5804x_2220_500V_TD.asy and 
	B5804x_2220_900V_TD.asy) in the folder sym/TDK. (create if missing)
 
4)  On the next start of LTspice you will find the elements
    using:
    Edit  -> Component (F2) -> TDK -> 	B5803x_500V_FD
					B5803x_500V_TD
					B5803x_700V_FD
					B5803x_700V_TD
					B5803x_900V_FD
					B5803x_900V_TD
					B5804x_2220_500V_FD
					B5804x_2220_500V_TD
					B5804x_2220_900V_FD
					B5804x_2220_900V_TD
  
5)  To select one element out of this library make a right click
    on the Symbol. Double-click on the "Value" field on the right
    side of the "Spice Model" line to open the drop-down menu.


