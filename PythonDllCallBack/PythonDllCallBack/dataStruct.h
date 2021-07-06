#pragma once
#define _CRT_SECURE_NO_WARNINGS
#define EXP_API __declspec(dllexport)

typedef enum {
	MsgOne,
	MsgTwo,
	MsgLast
} MsgType;

// 由于消息类型的不同，不是所有的值都有意义
typedef struct {
	MsgType type;
	int cardID;         // 标签/腕带ID,当DevType为DevCard时有意义
	char InstrumentID[30];
	double bidPrice;
	bool isTrade;
	char *Other;
} DevMsg;

typedef void(*MsgCallback)(DevMsg msg);

extern "C" {
	//包含了回调函数，数据指针，结构体内部指针等常用情况。
	EXP_API int callBackStartWork(MsgCallback fun);
	EXP_API char *getData(char *arg);
}