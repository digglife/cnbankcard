# CNBankCard 中国各大银行卡号查询


通过银行卡卡号解析出 *发卡行* 和 *银行卡类别*（储蓄卡/信用卡），返回值为JSON数据。

## 获取方式

支付宝提供的接口。按以下格式发送HTTP请求即可。

```
curl "https://ccdcapi.alipay.com/validateAndCacheCardInfo.json?_input_charset=utf-8&cardNo=银行卡卡号&cardBinCheck=true"
```

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


## 银行Logo图片 API

```
https://apimg.alipay.com/combo.png?d=cashier&t=*银行代码*
```
多个银行代码可用半角逗号隔开，生成sprite图片。

例子：

`https://apimg.alipay.com/combo.png?d=cashier&t=ABC` 会生成农业银行的logo图片。

![abc-logo][1]


## 银行代码<->银行中文名对照

写了一个[简单的 Python 脚本][2]从 [支付宝合作银行列表页面][3] 提取。结果在[这里][4]。


  [1]: https://apimg.alipay.com/combo.png?d=cashier&t=ABC
  [2]: parsebanks.py
  [3]: http://ab.alipay.com/i/yinhang.htm
  [4]: bankname.json