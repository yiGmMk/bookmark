---
layout: post
---
Title: 这样设置Prompt，让ChatGPT输出更好的效果！为ChatGPT提供更合适的Prompt输入，我们就能得到更优质的 - 掘金

URL Source: https://juejin.cn/post/7232480698879623223

Markdown Content:
#### 写在前面

帮朋友推广一下公众号，欢迎朋友们关注，谢谢！

![Image 21: 公众号二维码.jpg](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d40f2e156ec40e196c434e55dcf596f~tplv-k3u1fbpfcp-zoom-in-crop-mark:1512:0:0:0.awebp#?w=258&h=258&e=jpg&b=fefefe)

#### 引言

众所周知，为ChatGPT提供更合适的Prompt输入，我们就能得到更优质的结果。

为了帮助初学者更好地学习这些知识和技能，吴恩达老师与 OpenAI 合作推出了《ChatGPT Prompt Engineering for Developers》教程的中文版。该课程通过简单易懂的讲解和范例代码演示，深入介绍了如何使用 Prompt 和 OpenAI 的 API 来开发应用程序，包括如何构造 Prompt 并基于 OpenAI 提供的 API 实现多种常用功能，如总结、推断、转换等。这是入门 LLM 开发的经典教程。

本序列文章是深度参考吴恩达老师的教程之后，提炼的一些关键点。希望可以帮助到大家。

本文章主要聚焦于：**编写 Prompt 的原则。** 了解基本原则后，也可以进一步阅读[《这样逐步优化Prompt，让ChatGPT输出你想要的结果！》](https://juejin.cn/post/7232550589963419706 "https://juejin.cn/post/7232550589963419706")

#### 大纲

给OpenAI API 提供更优质的Prompt，需要遵循两个原则：

*   原则一：编写清晰、具体的指令
    
    > 策略1：使用合理的分隔符，更清晰地表示输入的不同部分。
    > 
    > 策略2：给模型指示，要求结构化地输出内容。
    > 
    > 策略3：可以要求模型检查是否满足条件。
    > 
    > 策略4：可以给模型提供少量示例，以获得更优的结果。
    
*   原则二：给模型可以思考的时间
    
    > 策略5：给模型指定完成任务所需的步骤。
    > 
    > 策略6：引导模型在下结论之前找出一个自己的解法。
    

接下来结合具体的代码实践，来一起学习上面的原则和具体的策略。

> 提示：在本教程中，我们将使用 OpenAI 开放的 ChatGPT API。为此，您需要先获得 ChatGPT 的 API\_KEY（您也可以直接访问官方网站进行在线测试），然后安装 openai 的第三方库。

#### 安装openai库

```
pip install openai
```

#### 准备辅助函数

这个辅助函数在后续的示例中经常会用到。主要功能是根据输入的Prompt内容，调用openai API，并获得输出结果。

```
import openai
​
# 设置key
# Key的查看入口：https://beta.openai.com/account/api-keys
# 也可以通过环境变量的方式来设置，为了简单起见，这里直接通过设置参数的方式来设置
openai.api_key = "sk-XXX"
​
# 一个封装 OpenAI 接口的函数，参数为 Prompt，返回对应结果
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # 模型输出的温度系数，控制输出的随机程度
    )
    return response.choices[0].message["content"] 
```

#### **策略1：使用合理的分隔符**

使用合理的分隔符，向模型更清晰地表示输入的不同部分。

分隔符可以是任何标记，只要让模型明确知道这是一个单独的部分即可。例如分隔符可以是：\`\`\`，""，<\>，，<\\tag\>等。

以下是一个例子，我们给出一段话并要求 GPT 进行总结，在该示例中我们使用 \`\`\` 来作为分隔符。

```
# 原始的内容
text = f"""
    你应该提供尽可能清晰、具体的指示，以表达你希望模型执行的任务。\
    这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
    不要将写清晰的提示与写简短的提示混淆。\
    在许多情况下，更长的提示可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。"""
​
# 通过分隔符要求ChatGPT总结分隔符包含的内容。
prompt = f"""
    把用三个反引号包裹起来的文本内容总结成一句话。
    ```{text}```
    """
# 调用ChatGPT API
response = get_completion(prompt)
print(response)
```

输出结果：

```
提供清晰、具体的指示，避免无关或不正确响应。不要混淆清晰和简短，更长的提示可以提供更多清晰度和上下文信息。
```

#### **策略2：格式化输出内容**

要求ChatGPT以某种格式化的方式输出内容，这样的输出更容易被我们的程序解析。可以是 Json、HTML 等格式。

下面的示例中，我们要求 GPT 生成虚拟的三本书的书名、作者、出版社等信息，并以 Json 格式返回结果。为了方便解析，我们指定了 Json 键（key）。

```
prompt = """
    请生成3本虚拟的书，包括书名、作者、出版社等信息。\
    并以json形式输出结果，其中包括以下json key:\
    book_name, author, publisher\
    """
response = get_completion(prompt)
print(response)
```

输出结果：

```
[  {    "book_name": "时光之旅",    "author": "张三",    "publisher": "人民文学出版社"  },  {    "book_name": "未来的世界",    "author": "李四",    "publisher": "科学出版社"  },  {    "book_name": "爱情的故事",    "author": "王五",    "publisher": "上海文艺出版社"  }]
```

#### **策略3：要求模型检查是否满足条件**

有时候，我们希望模型只有在满足某些条件的情况下才执行具体的任务。如果条件不满足，我们希望模型停止执行，并告知我们。

下面有两个示例，分别用来展示“满足某些条件”和“不满足某些条件”的情况。

**示例1：** 给模型输入一段泡茶的步骤，让模型判断是否包括明确的指令，如果包括，则以我们指定的格式来输出指令序列。

```
text = f"""
    泡一杯茶很容易。首先需要把水烧开。在等待期间，拿一个杯子并把茶叶放进去。\
    等到水烧开了，就把开始倒在茶叶上。然后，等待几分钟，让茶叶充分浸泡。\
    几分钟之后，可以取出茶包，然后就可以喝茶了。\
    如果有需要，可以加入牛奶或糖。\
    就这样，你就可以享受一杯美味的茶了。
    """
  
prompt = f"""
    你将获得一段文本，是三个引号括起来的文本内容。\
    如果它包含一些列的指令，则按照下面的格式重写这些指令。\
    第一步：
    第二步：
    第三步：
    ……
    第N步：
    如果不包括指令，则输出：未识别出有效指令。
    """{input_text}"""
    """
response = get_completion(prompt)
print(response)
```

输出结果：

```
第一步：把水烧开。
第二步：拿一个杯子并把茶叶放进去。
第三步：等到水烧开了，就把开始倒在茶叶上。
第四步：等待几分钟，让茶叶充分浸泡。
第五步：取出茶包。
第六步：如果需要，可以加入牛奶或糖。
第七步：享受一杯美味的茶。
```

**示例2：** 输入另一段没有包括明确指令的内容，让模型来判断。

```
text = f"""今天阳光明媚，鸟儿在歌唱。\
    这是一个去公园散步的美好日子。\
    鲜花盛开，树枝在微风中轻轻摇曳。\
    人们外出享受着这美好的天气，有些人在野餐，有些人在玩游戏或者在草地上放松。\
    这是一个完美的日子，可以在户外度过并欣赏大自然的美景。"""
​
prompt = f"""
    你将获得一段文本，是三个引号括起来的文本内容。\
    如果它包含一些列的指令，则按照下面的格式重写这些指令。\
    第一步：
    第二步：
    第三步：
    ……
    第N步：
    如果不包括指令，则输出：未识别出有效指令。
    """{input_text}"""
    """
response = get_completion(prompt)
print(response)
```

输出结果：

```
未识别出有效指令。
```

#### **策略4：提供少量示例，要求模型按示例格式输出结果**

我们可以要求模型在执行实际任务之前，按照提供给它的少量示例，来执行剩余的任务。

在下面的示例中，我们以老师和学生的对话为例。

先提供一个对话的示例，然后要求模型按一致的语气和相同的格式，输出后续的内容。

```
prompt = f"""
    你的任务是以一致的风格来回答问题。
    <学生>：教我耐心。\
    <老师>：挖出最深峡谷的河流源于一处不起眼的泉眼；最宏伟的交响乐从单一的音符开始；最复杂的挂毯以一根孤独的线开始编织。\
    <学生>：教我坚韧。
    """
response = get_completion(prompt)
print(response)
```

输出结果：

```
<老师>：坚韧不是一蹴而就的，它需要不断的练习和磨砺。就像锻炼肌肉一样，只有经过反复的挑战和克服，才能让自己变得更加坚韧。同时，也要学会接受失败和挫折，从中吸取经验教训，不断前行。
```

#### **策略5：给模型指定完成任务所需的步骤**

人类在没有足够时间时计算的答案可能会犯错误。

模型也一样，模型也可能在短时间内（或少量文字无法完成的任务的情况下）给出错误的答案。

如果模型匆忙得出了错误的结论，您可以尝试重新构思查询，请求模型在提供最终答案之前进行一系列相关的推理。

在这些情况下，您可以指示模型花更多时间思考问题。

下面我们以一个示例来展示这个过程。

```
text = f"""
    在一个迷人的村庄里，兄妹杰克和吉尔出发去一个山顶井里打水。\
    他们一边唱着欢乐的歌，一边往上爬，\
    然而不幸降临——杰克绊了一块石头，从山上滚了下来，吉尔紧随其后。\
    虽然略有些摔伤，但他们还是回到了温馨的家中。\
    尽管出了这样的意外，他们的冒险精神依然没有减弱，继续充满愉悦地探索。
    """
​
prompt_1 = f"""
    执行以下操作：
    1、用一句话概括下面用三个反引号括起来的文本。
    2、将摘要翻译成法语。
    3、在法语摘要中列出每个人名。
    4、输出一个 JSON 对象，其中包含以下键：French_summary，num_names。
​
    请用换行符分隔您的答案。
​
    Text:
    ```{text}```
    """
response_1 = get_completion(prompt_1)
print(response_1)
```

输出结果：

```
1、兄妹在山上打水时发生意外，但仍然保持冒险精神。
2、Dans un charmant village, les frère et sœur Jack et Jill partent chercher de l'eau dans un puits au sommet d'une montagne. Ils chantent joyeusement en montant, mais malheureusement, Jack trébuche sur une pierre et tombe de la montagne, suivi de près par Jill. Bien qu'ils soient légèrement blessés, ils retournent chez eux chaleureusement. Malgré cet accident, leur esprit d'aventure ne diminue pas et ils continuent à explorer avec joie.
3、Jack, Jill.
4、{"English_summary": "Brother and sister have an accident while fetching water on a mountain but continue to explore with joy.", "num_names": 2}
```

在吴恩达老师的视频里，这里的输出认为是**有问题的**。例如，键“姓名”会被替换为法语。

但是由于我不懂法语，也没太理解这里的问题所在。

吴恩达老师的原始视频中，是通过使用了更好的Prompt，使得模型最终输出了合理的结果。

**修改后的Prompt如下：**

```
text = f"""
    在一个迷人的村庄里，兄妹杰克和吉尔出发去一个山顶井里打水。\
    他们一边唱着欢乐的歌，一边往上爬，\
    然而不幸降临——杰克绊了一块石头，从山上滚了下来，吉尔紧随其后。\
    虽然略有些摔伤，但他们还是回到了温馨的家中。\
    尽管出了这样的意外，他们的冒险精神依然没有减弱，继续充满愉悦地探索。
    """
​
prompt_2 = f"""
    执行以下操作：
    1、用一句话概括下面用<>括起来的文本。
    2、将摘要翻译成英语。
    3、在英语摘要中列出每个人名。
    4、输出一个 JSON 对象，其中包含以下键：English_summary，num_names。
​
    请使用以下格式：
    文本：<要总结的文本>
    摘要：<摘要>
    翻译：<摘要的翻译>
    名称：<英语摘要中的名称列表>
    输出 JSON：<带有 English_summary 和 num_names 的 JSON>
​
    Text:
    ```{text}```
    """
​
response_2 = get_completion(prompt_2)
print(response_2)
```

输出结果：

```
摘要：兄妹杰克和吉尔在迷人的村庄里去山顶井打水，但杰克不幸滚下山来，他们虽然受了些伤，但仍然充满冒险精神继续探索。
翻译：In a charming village, siblings Jack and Jill set out to fetch water from a well on a mountaintop. While singing joyfully and climbing up, unfortunately, Jack stumbled on a rock and rolled down the mountain, with Jill following closely behind. Despite some injuries, they returned to their cozy home. Despite the mishap, their adventurous spirit remained undiminished, and they continued to explore with joy.
名称：Jack，Jill
输出 JSON：{"English_summary": "In a charming village, siblings Jack and Jill set out to fetch water from a well on a mountaintop. While singing joyfully and climbing up, unfortunately, Jack stumbled on a rock and rolled down the mountain, with Jill following closely behind. Despite some injuries, they returned to their cozy home. Despite the mishap, their adventurous spirit remained undiminished, and they continued to explore with joy.", "num_names": 2}
```

#### **策略6：引导模型在下结论之前找出一个自己的解法**

有时候，我们让模型直接判断我们的输入是否正确，模型可能会得到错误的结果。

这时候我们可以指示模型，不要直接判断我们的输入，而是先让模型自行解答，再通过对比两个结果，来判断我们的输入是否正确。

接下来我们会给出一个问题和一个学生的解答，要求模型判断解答是否正确。

```
prompt = f"""
    判断学生的解决方案是否正确。
​
    问题:
    我正在建造一个太阳能发电站，需要帮助计算财务。
    土地费用：每平方英尺100美元
    太阳能电池板：每平方英尺250美元
    维护费用：每年需要支付固定的100000美元，并额外支付每平方英尺10美元
    作为平方英尺数的函数，首年运营的总费用是多少。
​
    学生的解决方案：
    设x为发电站的大小，单位为平方英尺。
    费用：
    土地费用：100*x
    太阳能电池板费用：250*x
    维护费用：100000+100*x
    总费用：100*x+250*x+100000+100*x=450*x+100000
    """
    response = get_completion(prompt)
    print(response)
response = get_completion(prompt)
print(response)
```

输出结果：

```
该学生的解决方案是正确的。
```

但是，实际上学生的解决方案实际上是错误的。**错误的地方在于：维护费用里每平方英尺是10美元，而学生计算过程错误地写成100\*x 了。**

我们可以通过指导模型先自行找出一个解法来解决这个问题。

在接下来这个 Prompt 中，我们要求模型先自行解决这个问题，再根据自己的解法与学生的解法进行对比，从而判断学生的解法是否正确。

同时，我们给定了输出的格式要求。通过明确步骤，让模型有更多时间思考，有时可以获得更准确的结果。

```
prompt = f"""
    请判断学生的解决方案是否正确，请通过如下步骤解决这个问题：
    步骤：
    首先，自己解决问题。
    然后将你的解决方案与学生的解决方案进行比较，并评估学生的解决方案是否正确。
    在自己完成问题之前，请勿决定学生的解决方案是否正确。
​
    使用以下格式：
    问题：问题文本
    学生的解决方案：学生的解决方案文本
    实际解决方案和步骤：实际解决方案和步骤文本
    学生的解决方案和实际解决方案是否相同：是或否
    学生的成绩：正确或不正确
​
    问题：
        我正在建造一个太阳能发电站，需要帮助计算财务。 
        - 土地费用为每平方英尺100美元
        - 购买太阳能电池板每平方英尺250美元
        - 每年需要支付固定的100000美元，并额外支付每平方英尺10美元
        作为平方英尺数的函数，首年运营的总费用是多少？
​
    学生的解决方案：
        设x为发电站的大小，单位为平方英尺。
        费用：
        1. 土地费用：100*x
        2. 太阳能电池板费用：250*x
        3. 维护费用：100000+100*x
        总费用：100*x+250*x+100000+100*x=450*x+100000
​
    实际解决方案和步骤：
    """
response = get_completion(prompt)
print(response)
```

最终，按照新的Prompt引导模型先自行解决，再跟学校的结果做对比之后，模型就能发现学生的解答是错误的。

新的正确的输出结果：

```
实际解决方案：
        设x为发电站的大小，单位为平方英尺。
        费用：
        1. 土地费用：100*x
        2. 太阳能电池板费用：250*x
        3. 维护费用：100000+10*x
        总费用：100*x+250*x+100000+10*x=360*x+100000
​
    学生的解决方案和实际解决方案是否相同：
        不相同
​
    学生的成绩：
        不正确

```

#### 参考资料：

[www.deeplearning.ai/short-cours…](https://link.juejin.cn/?target=https%3A%2F%2Fwww.deeplearning.ai%2Fshort-courses%2Fchatgpt-prompt-engineering-for-developers%2F "https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/")
