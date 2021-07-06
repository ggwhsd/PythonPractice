#include "pch.h"
#include "dataStruct.h"

char ShowHello[10] = "Hello";
int callBackStartWork(MsgCallback fun)
{
	DevMsg msg;
	msg.cardID = 1;
	msg.bidPrice = 99.0;
	
	strcpy_s(msg.InstrumentID,"testInstrument");
	msg.isTrade = true;
	msg.type = MsgType::MsgLast;
	msg.Other = &ShowHello[0];
	fun(msg);
	return 0;
}

EXP_API char * getData(char* arg)
{
	int len = strlen(arg);
	char* p = new char[len+1];
	int i = 0;
	while (i < len)
	{
		p[i] = toupper(arg[i]);
		i++;
	}
	p[i] = '\0';
	//strcpy_s(p,len+1,arg);
	//return  &ShowHello[0];
	return p;
}


