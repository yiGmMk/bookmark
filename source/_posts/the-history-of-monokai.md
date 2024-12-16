```
### Monokai 的历史

Monokai 颜色方案的历史和 Monokai Pro 的演变

*   [主页](https://monokai.pro/)
*   [Sublime Text](https://monokai.pro/sublime-text)
*   [VSCode](https://monokai.pro/vscode)

Monokai 的历史
----------------------

如何捕获开发者世界的颜色彩

自编码早期以来，开发人员一直在寻找使他们的工作更容易和更吸引人的环境。 **Monokai**，具有其生动的颜色调色板，已经成为编辑器、IDE 和终端中受欢迎的选择。 本文深入探讨了这个标志性颜色方案的起源、成长和持久的吸引力。

### Monokai 的起源

Monokai 的旅程始于 2006 年，荷兰设计师和开发人员 Wimer Hazenberg。 受到现有不吸引人、过于饱和的编辑主题的挫折，Wimer 决定创建一些新鲜和功能性的东西 - 一个优先考虑可读性和美观的颜色方案。 他选择的工具是 macOS 上的 TextMate，在那里他用黑色背景和明亮、精心选择的颜色进行了实验：关键字的粉色、字符串的香草黄色和细微的对比度，以突出代码结构，同时淡化不太重要的元素，如注释。

```javascript
const fibonacci = (n: number) => {
    console.log(`Called fibonacci(${n})`);

    // 基本情况：返回 n 如果 0 或 1
    if (n <= 1) {
        return n;
    }

    // 递归调用
    return fibonacci(n - 1) + fibonacci(n - 2);
};
```

原始 Monokai 颜色的示例代码

Wimer 在 TextMate 的 wiki 上共享了他的主题，并以自己的互联网别名命名它，没有太多考虑。 令他惊讶的是，Monokai 很快在编码社区中获得了牵引力，引起了开发人员对新鲜替代方案的共鸣。 从那里，Monokai 作为开发人员友好、视觉吸引人的方案的声誉传播开来。

### Monokai：一个有生命的名字

“Monokai” 这个名字经常引起好奇，因为它听起来有点像日本，导致许多人将其与极简主义或禅宗美学联系起来。 然而，它的真正起源是基于感觉。

大约在 2003 年，作为 Wimer 的互联网别名和公司名称，“Monokai” 没有任何特定的含义，主要是因为它“感觉正确”。 然而，它也代表了对项目的个人方法。 “Mono” 部分表示专注于个人共鸣的想法，反映了设计和开发中的个人努力。 同时，“kai” 部分有一个引人入胜的声音和令人愉悦的响声，“AI” 微妙地暗示了他在人工智能方面的背景。

最初作为个人项目的处理程序，现在已经与颜色调色板意外地联系在一起。 要了解更多关于 Wimer 在其 Monokai 别名下进行的个人项目，请访问 [monokai.com](https://monokai.com/)。

### 混音和非官方端口

随着 Monokai 跨越开发世界，它启发了无数混音和改编，产生了几乎所有编辑器上非官方的“Monokai 启发”的主题。 Textmate 主题的开放性使开发人员能够轻松适应和定制以满足他们特定的需求，从而在各种编辑器中创建独特的分支。 尽管这些改编不是由 Wimer 创建的，但它们的多样性凸显了该方案对全球开发人员的影响和影响。

### 与 Sublime Text 的决定性时刻

Monokai 的受欢迎程度在成为 **Sublime Text** 的默认主题时又上了一个台阶，这是一款因其精美的设计和速度而受到赞誉的编辑器。 这次合作将 Monokai 带到了更广泛的受众面前，巩固了它作为全球开发人员的首选主题的地位。 对于许多人来说，Sublime 和 Monokai 成为了新型、流线型代码编辑方法的不可分割的象征。

### Monokai Pro：现代版本

随着 Monokai 持续受欢迎，Wimer 看到了改进和扩展其原始主题的机会。 2017 年，他推出了 **Monokai Pro**，这是原始 Monokai 的现代化、功能丰富的演变。

Monokai Pro 不仅仅是一个简单的更新；它包括一套针对当代开发人员需求的增强功能，包括用户界面设计和自定义图标包。 Monokai Pro 提供了几种颜色过滤器，例如“光谱”、“Ristretto”和经典的“Monokai”，现在重新命名为 **Monokai 经典**。 这些选项使开发人员能够选择最适合其工作区的外观和感觉。

```javascript
async function fetchJson(url: string): Promise<any> {
    const response = await fetch(url);

    if (!response.ok) throw new Error('Invalid response');

    return await response.json();
}

fetchJson(`${API}/data.json`)
    .then(data => console.log(data))
    .catch(error => console.error('Fetch error:', error));
```

Monokai Pro 颜色的示例代码

Monokai Pro 包括 70 多个自定义图标

与许多将 UI 和语法突出显示分开的主题不同，Monokai Pro 遵循 **集成设计方法**，其中界面的每个元素都是协调的和视觉统一的。 Wimer 个人使用和微调 Monokai Pro，随着每次迭代而演变，以保持其美观和功能吸引力。 这种亲力亲为的方法使 Monokai Pro 保持其原始的真实性，同时适应现代编码的需求。

### 关于设计颜色调色板的说明

选择合适的颜色是一项复杂的任务。 在文本编辑器中，您希望颜色具有相同的亮度，因此代码可以轻松阅读。 然而，不存在确定颜色感知“亮度”的明确数学公式，即使像 CIELAB 和 OKLAB 这样的成熟颜色空间也有其局限性。 尽管对比度工具可以建议可读性，但它们并不能普遍应用于所有颜色组合。

捕捉颜色并在数学模型中精确匹配我们对颜色的感知是一种幻觉。 我们对颜色的感知是复杂而主观的，即使最复杂的方法也无法完全捕捉它。 这使得选择颜色调色板成为一种艺术而不是科学，设计师依赖于直觉、经验和反馈来创建和谐和功能的组合。

### Monokai 在流行文化中的地位

Monokai 的影响甚至延伸到了技术世界之外。 它在诸如 **Silicon Valley**、**Mr. Robot** 等节目中被提及，其中其可识别的颜色为屏幕上的开发人员环境增添了真实感。

它的颜色调色板已被插画师、生成艺术家和各个领域的设计师使用。

### Monokai Pro 扩展：引入浅色主题

多年来，开发人员一直要求为 Monokai Pro 提供浅色主题。 这意味着不仅仅是使颜色变亮 - 对比度在浅色背景上表现不同，粗体颜色很容易变得令人眼花缭乱。

经过大量测试，Wimer 于 2024 年推出了 **Monokai Pro Light**，并推出了一个名为“Sun”的新过滤器，旨在保持 Monokai 的清晰度和可读性在明亮的环境中。 Monokai Pro Light 提供了温暖、平衡的色调，易于眼睛却充满活力，使其成为自然照明空间的理想选择。 浅色主题扩展了 Monokai 的吸引力，同时保持其细致入微的功能设计，为开发人员提供了他们熟悉的体验，但具有清新的浅色调色板。

```javascript
function isPalindrome(str: string): boolean {
    const sanitized = str.replace(/[W_]/g, '').toLowerCase();

    return sanitized === sanitized.split('').reverse().join('');
}

console.log(isPalindrome('never odd or even')); // true
```

Monokai Pro Light 颜色的示例代码

### 展望未来

从简单的 TextMate 主题到标志性的工具，Monokai 的旅程凸显了编码中细致入微的设计的力量。 Monokai Pro 仍然是 Wimer 愿景的真实演变，随着现代软件需求的不断演变而不断适应，同时保持其在清晰度和简洁性方面的根基。 随着代码的演变，Monokai 也在演变 - 这是一个持久的提醒，细致入微的设计如何增强开发人员工作区中的功能和流畅度。
```