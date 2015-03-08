# CNBankCard 中国各大银行卡号查询


----------


通过银行卡卡号解析出 *发卡行* 和 *银行卡类别*（储蓄卡/信用卡），返回值为JSON数据。

## 获取方式

支付宝提供的接口。按以下格式发送HTTP请求即可。

`curl "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?_input_charset=utf-8&cardNo=银行卡卡号&cardBinCheck=true"`

不知道有没有单位时间内的次数限制。

例子：
```bash
zhu@tp430:~/Dev/cnbankcard$ http "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?_input_charset=utf-8&cardNo=6228430120000000000&cardBinCheck=true"
HTTP/1.1 200 OK
Connection: keep-alive
Content-Language: zh-CN
Content-Length: 101
Content-Type: application/json;charset=GBK
Date: Sun, 08 Mar 2015 15:21:17 GMT
Server: spanner/1.0.6
Set-Cookie: JSESSIONID=CCDE8AA9E2DAEC082A7614734AF729FB; Path=/; HttpOnly
Set-Cookie: JSESSIONID=CCDE8AA9E2DAEC082A7614734AF729FB; Path=; Secure; HttpOnly
Set-Cookie: spanner=dauWw2JHEhbWoKV/zrMf2LLFCxFf8h1G;path=/;secure;
Strict-Transport-Security: max-age=31536000

{
    "bank": "ABC", 
    "cardType": "DC", 
    "key": "6228430120000000000", 
    "messages": [], 
    "stat": "ok", 
    "validated": true
}
```


## 银行大Logo

支付宝提供的sprite image：

![big-logo][1]

链接中的银行代码和图片中的Logo由上至下一一对应。准备用工具自动切一下。

## 银行小Logo

支付宝提供的sprite image：

![small-logo][2]


  [1]: https://apimg.alipay.com/combo.png?d=cashier&t=ABC,ARCU,ASCB,AYCB,BGB,BHB,BJBANK,BJRCB,BOC,BOCD,BOCY,BOD,BODD,BOHAIB,BOJZ,BOP,BOSZ,BOYK,BOZK,BZMD,CCB,CCQTGB,CDCB,CDRCB,CEB,CGNB,CIB,CITIC,CMB,CMBC,COMM,CQBANK,CSCB,CSRCB,CZBANK,CZCB,CZRCB,DAQINGB,DLB,DRCBCL,DYCB,DYCCB,EGBANK,FDB,FJHXBC,FSCB,FXCB,GCB,GDB,GDRCC,GLBANK,GYCB,GZB,H3CB,HANABANK,HBC,HKB,HKBEA,HRXJB,HSBANK,HXBANK,HZCB,HZCCB,ICBC,JINCHB,JNBANK,JSB,JSBANK,JSRCU,JXBANK,JZBANK,KLB,LANGFB,LSBANK,LSBC,LSCCB,LYCB,LZYH,MTBANK,NBBANK,NCB,NHB,NJCB,ORBANK,PSBC,QDCCB,QLBANK,RCB,SCB,SDEB,SDRCU,SHBANK,SHRCB,SJBANK,SPABANK,SPDB,SRBANK,SRCB,SXCB,TCRCB,TRCB,TZCB,URMQCCB,WJRCB,WZCB,XABANK,XTB,YCCB,YNRCC,YQCCB,YXCCB,YYPT,ZBCB,ZGCCB,ZJNX,ZJTLCB,ZRCBANK,ZYCBANK,ZZBANK
  [2]: https://i.alipayobjects.com/i/ecmng/png/201408/3EiPVyEM6f.png
