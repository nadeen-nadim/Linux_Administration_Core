#include <pigpio.h>
#include <unistd.h>
#include "LED_MAT.h"

void ledMatrix:: MAT_nameDisplay()
{
	char PORT[8] = {1,2,4,8,16,32,64,128};//pin values of COL_PORT
	
		for(int i=0;i<7;i++)
		{
			for(int n = 0; n < 1000; n++)
			{
			   for(int j =0; j < 4; j++)
			   {
				   char val = PORT[j];
				  for(int p =0;p<4;p++)
				  {
					gpioWrite(UPPER_ROW_PORT[p],((((val)>>p)&1)));
				  }
				   
				  for(int p =0;p<8;p++)
				  {
					gpioWrite(COL_PORT[p],((((charArray[i][j])>>p)&1)));
				  }
				  usleep(500);
			   }

				for(int p =0;p<4;p++)
				{
					gpioWrite(UPPER_ROW_PORT[p],0);
				}
				
				for(int k =0;k<4;k++)
				{
					char val = PORT[k];
					for(int p =0;p<4;p++)
				  {
					gpioWrite(LOWER_ROW_PORT[p],((((val)>>p)&1)));
				  }
				  for(int p =0;p<8;p++)
				  {
					gpioWrite(COL_PORT[p],((((charArray[i][4+k])>>p)&1)));
					
				  }
				  usleep(500);
				}

				for(int p =0;p<4;p++)
				{
					gpioWrite(LOWER_ROW_PORT[p],0);
				}
			}
		}
		usleep(500000);
	
	
}

/*void ledMatrix:: MAT_init()
{
	for(int i =0;i<8;i++)
	{
		gpioWrite(ROW_PORT[i],1);
		gpioWrite(COL_PORT[i],0);	
		usleep(500000);
	}
	for(int i =0;i<8;i++)
	{
		gpioWrite(ROW_PORT[i],0);
		//gpioWrite(COL_PORT[i],0);
		usleep(500000);
	}
}*/

ledMatrix::ledMatrix()
{

}

void ledMatrix:: MAT_init()
{
    int i;
    for(i=0;i<8;i++) 
    {
        
        gpioSetMode(COL_PORT[i],PI_OUTPUT);
    }
	 for(i=0;i<4;i++) 
    {
        
        gpioSetMode(LOWER_ROW_PORT[i],PI_OUTPUT);
		gpioSetMode(UPPER_ROW_PORT[i],PI_OUTPUT);
    }

}