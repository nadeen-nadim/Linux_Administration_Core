#include <iostream>
#include <pigpio.h>
#include <unistd.h>
#include "LED_MAT.h"

int main()
{
	if(gpioInitialise() < 0) return 1;
   ledMatrix myledMatrix;
   myledMatrix.MAT_init();
   while(1)
   {
		myledMatrix.MAT_nameDisplay();
   }
   
   return 0;
}
