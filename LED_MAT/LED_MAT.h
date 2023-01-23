#include <iostream>
class ledMatrix
{
    private:
    /*const char charArray[6][8] = {
        {0x00,0x00,0x00,0x44,0x64,0x54,0x4c,0x44},
        {0x00,0x00,0x38,0x44,0x7c,0x44,0x44,0x44},
        {0x00,0x00,0x00,0x78,0x44,0x44,0x44,0x78},
        {0x00,0x00,0x00,0x78,0x40,0x78,0x40,0x78},
        {0x00,0x00,0x00,0x78,0x40,0x78,0x40,0x78},
        {0x00,0x00,0x00,0x44,0x64,0x54,0x4c,0x44}
    };*/
	
	const char charArray[7][8] = {
        {0xff,0xff,0xff,0xbb,0x9b,0xab,0xb3,0xbb},
        {0xff,0xff,0xff,0xe3,0xdd,0xc1,0xdd,0xdd},
        {0xff,0xff,0xff,0xc7,0xdb,0xdb,0xdb,0xc7},
        {0xff,0xff,0xff,0xc3,0xdf,0xc3,0xdf,0xc3},
        {0xff,0xff,0xff,0xc3,0xdf,0xc3,0xdf,0xc3},
        {0xff,0xff,0xff,0xbb,0x9b,0xab,0xb3,0xbb},
		{0xff,0xff,0x71,0x2a,0x4e,0x31,0x7f,0xff}
    };

    const char nameArray[6] = {0,1,2,3,3,0};

    const char UPPER_ROW_PORT[4]= {2,3,4,17};
	const char LOWER_ROW_PORT[4]={27,22,10,9}; 
    const char COL_PORT[8]= {14,15,18,23,24,25,8,7};
	


    public:
    ledMatrix();
    void MAT_init();
    void MAT_nameDisplay();



};