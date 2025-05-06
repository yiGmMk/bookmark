---
layout: post
---
Title: 自部署 DeepLX 满足日常翻译需求

URL Source: https://topnec.org/blog/how-to-use-deeplx/

Published Time: 2024-06-17T22:44:28+08:00

Markdown Content:
免费的翻译服务 DeepL 翻译效果要远远好于微软和谷歌翻译，在 OpenAI 出现之前一直是备受推崇的 ( 注意，虽然但是，普通人还是比较难自己开通 OpenAI的API，参考我上上篇写到的经历）。

如果想在翻译软件中使用其API，或者自己的代码执行中调用其API来完成任务。就得注册账号并绑定信用卡。然后可以使用其免费的计划提供的API，每个月有50万 Token 的额度。

可是，但是。。中国的信用卡无法绑定。

但我们可以通过淘宝买一个绑定过信用卡的账号（不贵），但每个月 50万 Token 有时候又可能会不够用，比如我日常调用 API 翻译 新闻阅读，很多时候半月就用光了。而购买的账号也会担心隐私问题。

这时候，就要推荐一个开源项目 **DeepLX** ： [https://github.com/OwO-Network/DeepLX](https://github.com/OwO-Network/DeepLX) ，其核心优点是模拟官方客户端的API请求，调用API，可以自部署 且 无限用量 ，虽然也有一些不足，比如短时间高频率调用会触发 `429` 错误，但总体来说是个很棒的工具。

部署
--

当然选择 Docker

```
services:
    deeplx:
        image: ghcr.io/owo-network/deeplx:latest
        container_name: deeplx
        restart: always
        logging:
            options:
                max-size: 10m
        ports:
          - "1188:1188"
         
        # environment:
          # - AUTHKEY=your_offical_deepl_api_key
          # - TOKEN=your_access_token
```

*   支持设置自己的加密访问 Token，也支持将已有的官方 API Key 设置进去，作为 Backup。
    
*   API地址很简单：http://localhost:1188/translate
    
*   也可以通过Caddy或者Nginx设置反代来实现 https 域名访问。
    

使用
--

在浏览器翻译插件 《简约翻译》 中使用，如果设置了 token，就填写到KEY那里，没设置就留空

![Image 1](https://4e9fdc1.webp.li/202406/7702936af064101b47608e92470789a6.jpg)

在 Python 代码中使用

```
import httpx,json

deeplx_api = "https://your-api-domain.com/translate"
deeplx_access_token = "your-api-access-token"
text = "Top Japan Bank Builds Startup Fund as Policy Push Lures Lenders"


def tr_deeplx(content):
     data = {
          "text": content,
          "source_lang": "EN",
          "target_lang": "ZH"
     }

     headers = {'Content-Type': 'application/json',
                'Authorization': f'Bearer {deeplx_access_token}'
     }

     post_data = json.dumps(data)
     r = httpx.post(url = deeplx_api, data = post_data, headers=headers).text
     return json.loads(r)["data"]

print(tr_deeplx(text))
```

同样的，看自己的需求是否设定并使用 access\_token ，如果有，就通过 Header 设置进去即可。

小结
--

优点：

*   免费、不限量
*   速度快，比openai等速度要快很多
*   安全、隐私OK，自部署嘛，对吧
*   翻译质量相对较高，虽然和 GPT4 这种高级大模型比可能差一些，但比很多其他的翻译服务还是要好很多

缺点：

*   自部署就可以考虑 API 安全性，防止盗刷（自己做好访问鉴权保护）有一定的技术门槛
*   429错误有时候还是会有
*   偶尔会出现“事实性”翻译错误，就是意思完全相反的那种。遇到过几次。

