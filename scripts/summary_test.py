from process_changes import summarize_text

txt ="""
## 背景

项目要求使用国密加密算法保障安全性,go和java需要通过接口互通,请求时使用sm4加密数据,sm2加密sm4秘钥,必将加密数据和加密后的sm4秘钥发送到第三方接口,
响应用相反的方式解密数据.
java 使用hutool里的工具函数实现,go使用"github.com/tjfoc/gmsm"实现.
<!--more-->

2点需要注意:
1. hutool工具函数名带有hex的会转成16进制,go需要调用hex.EncodeToString保证编码一致
2. sm2/sm4均有多种加密模式,编码时go与java加密模式保持一致

## sm2非对称加密

sm2: 基于椭圆曲线公钥密码算法标准，主要用于数字签名、密钥交换和数据加密
sm2有2种模式加密模式:C1C2C3,C1C3C2,hutool中默认使用C1C3C2模式

下面分别介绍go/java实现

```go
// "github.com/tjfoc/gmsm/sm2"
// "github.com/tjfoc/gmsm/sm4"
func encryptKey(key []byte, pubKey *sm2.PublicKey) (string, error) {
	v, err := sm2.Encrypt(pubKey, key, rand.Reader, sm2.C1C3C2)
	if err != nil {
		return "", errors.Wrapf(err, "sm2加密失败")
	}
	logx.Debugf("加密秘钥,%s", hex.EncodeToString(v))
	return hex.EncodeToString(v), nil
}
```

```java
// publicSM2KeyHex 公钥的16进制字符串,04开头,如
SM2 sm2 = SmUtil.sm2(null, publicSM2KeyHex);
String encryptKey = sm2.encryptHex(sm4Key, KeyType.PublicKey);
```


解密
```go
func decryptKey(data []byte, privKey *sm2.PrivateKey) ([]byte, error) {
	v, err := sm2.Decrypt(privKey, data, sm2.C1C3C2)
	if err != nil {
		return nil, errors.Wrapf(err, "sm2解密失败")
	}
	return v, nil
}
```

```java
// 根据SM2密钥对sm4密钥进行解密
SM2 decryptSM2 = SmUtil.sm2(privateSM2KeyHex, null);
String decryptSM4Key = decryptSM2.decryptStr(encryptKey, KeyType.PrivateKey);
```

### sm4对称加密

加密
```go
func encryptData(key, data []byte) (string, error) {
	encrypted, err := sm4.Sm4Ecb(key, data, true)
	if err != nil {
		return "", errors.Wrapf(err, "sm4加密失败")
	}
	return hex.EncodeToString(encrypted), nil
}
```

```java
// import cn.hutool.crypto.SmUtil;
// sm4算法密钥
String sm4Key = "565a5d91b637656e2a8ed56b6f3ffb87"; 
SM4 sm4 = SmUtil.sm4(ByteUtils.fromHexString(sm4Key));
// 对请求数据进行sm4加密
String encryptData = sm4.encryptHex(jsonRequest);
```

解密
```go
func decryptData(key, data []byte) ([]byte, error) {
	decrypted, err := sm4.Sm4Ecb(key, data, false)
	if err != nil {
		return nil, errors.Wrapf(err, "sm4解密失败")
	}
	return decrypted, nil
}
```

```java
// sm4算法密钥
String sm4Key = "565a5d91b637656e2a8ed56b6f3ffb87"; 
SM4 sm4 = SmUtil.sm4(ByteUtils.fromHexString(sm4Key));
// 对请求数据进行sm4加密
String encryptData = sm4.decryptStr(data);
```

具体可参考 [go-tool/crypto](https://github.com/yiGmMk/go-tool/blob/master/crypto/crypto_sm_test.go)
"""

summary=summarize_text(txt)
print(summary)