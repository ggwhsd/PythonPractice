#pragma once
#define _CRT_SECURE_NO_WARNINGS
#define EXP_API __declspec(dllexport)

typedef enum {
	MsgOne,
	MsgTwo,
	MsgLast
} MsgType;

// ������Ϣ���͵Ĳ�ͬ���������е�ֵ��������
typedef struct {
	MsgType type;
	int cardID;         // ��ǩ/���ID,��DevTypeΪDevCardʱ������
	char InstrumentID[30];
	double bidPrice;
	bool isTrade;
	char *Other;
} DevMsg;

typedef void(*MsgCallback)(DevMsg msg);

extern "C" {
	//�����˻ص�����������ָ�룬�ṹ���ڲ�ָ��ȳ��������
	EXP_API int callBackStartWork(MsgCallback fun);
	EXP_API char *getData(char *arg);
}