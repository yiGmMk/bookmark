Title: The history of Monokai

URL Source: https://monokai.pro/history

Markdown Content:
*   [home](https://monokai.pro/)
*   [Sublime Text](https://monokai.pro/sublime-text)
*   [VSCode](https://monokai.pro/vscode)

The history of Monokai
----------------------

How a Color Scheme Captured the Developer World
-----------------------------------------------

Since the early days of coding, developers have sought environments that make their work easier and more engaging. **Monokai**, with its vibrant color palette, has become a beloved choice across editors, IDEs, and terminals. This article delves into the origins, growth, and lasting appeal of this iconic color scheme.

### The Genesis of Monokai

The Monokai journey began in 2006 with Wimer Hazenberg, a Dutch designer and developer. Frustrated with exisiting uninspired, oversaturated editor themes, Wimer decided to create something fresh and functional — a color scheme that prioritized readability and aesthetics. His tool of choice was TextMate on macOS, where he experimented with a dark background and bright, carefully selected colors: a pink for keywords, a vanilla yellow for strings, and subtle contrasts to highlight code structure while dimming less critical elements like comments.

```
const fibonacci = (n: number) => {
	console.log(`Called fibonacci(${n})`);

	// Base case: return n if 0 or 1
	if (n <= 1) {
		return n;
	}

	// Recursive calls
	return fibonacci(n - 1) + fibonacci(n - 2);
};
```

Example code in the original Monokai colors

Wimer shared his theme on TextMate’s wiki, naming it after his own internet alias without giving it much thought. To his surprise, Monokai quickly gained traction in the coding community, resonating with developers seeking a fresh alternative. From there, Monokai’s reputation as a developer-friendly, visually appealing scheme spread.

### Monokai: A Name with a Life of Its Own

The name “Monokai” often sparks curiosity, as it sounds vaguely Japanese, leading many to associate it with minimalism or Zen aesthetics. However, its true origin is rather based on feeling.

Created around 2003 as Wimer’s internet alias and company name, “Monokai” didn’t have any specific meaning and mostly just “felt right”. However, it also represents a personal approach to projects. The “Mono” part signifies a focus on ideas that resonate personally, reflecting a solo endeavor in design and development. Meanwhile, the “kai” portion had an intriguing sound and pleasant ring, with the “AI” subtly hinting at his background in Artificial Intelligence.

What started as a personal project handle has now become unexpectedly linked to a color palette. To explore more about Wimer’s personal projects under his Monokai alias, visit [monokai.com](https://monokai.com/).

### Remixes and Unofficial Ports

As Monokai spread across the development world, it inspired countless remixes and adaptations, spawning unofficial “Monokai-inspired” themes for nearly every editor on the market. The open nature of Textmate themes made it easy for developers to adapt and customize to their specific needs, creating unique offshoots in various editors. While these adaptations were not created by Wimer, their diversity highlighted the scheme’s impact and influence on developers worldwide.

### A Defining Moment with Sublime Text

Monokai’s popularity took another leap when it became the default theme in **Sublime Text**, an editor celebrated for its sleek design and speed. This partnership brought Monokai to an even broader audience, cementing it as a go-to theme for developers worldwide. For many, Sublime and Monokai became inseparable symbols of a new, streamlined approach to code editing.

### Monokai Pro: The Definitive Modern Version

With Monokai’s ongoing popularity, Wimer saw a chance to refine and expand upon his original theme. In 2017, he launched **Monokai Pro** — a modern, feature-rich evolution of the original Monokai.

Monokai Pro is much more than a simple update; it includes a suite of enhancements tailored to the needs of contemporary developers, including a user interface design and a custom-made icon pack. Monokai Pro offers several color filters, such as “Spectrum,” “Ristretto,” and the classic “Monokai,” now rebranded as **Monokai Classic**. These options allow developers to choose the look and feel that best suits their workspace.

```
async function fetchJson(url: string): Promise<any> {
	const response = await fetch(url);

	if (!response.ok) throw new Error('Invalid response');

	return await response.json();
}

fetchJson(`${API}/data.json`)
	.then(data => console.log(data))
	.catch(error => console.error('Fetch error:', error));
```

Example code in Monokai Pro colors

Monokai Pro includes a custom-made icon pack of more than 70+ icons

Unlike many themes that separate the UI and syntax highlighting, Monokai Pro follows **an integrated design approach** where every element of the interface is cohesive and visually unified. Wimer personally uses and fine-tunes Monokai Pro, evolving it with each iteration to maintain both its aesthetic and functional appeal. This hands-on approach keeps Monokai Pro authentic to its origins while adapting to the demands of modern coding.

### A Note On Designing Color Palettes

Selecting the right colors is a complex endeavor. In Text editors, you want colors to have the same lightness, so code can be read effortlessly. However, there isn’t a definitive mathematical formula for determining a color’s perceived “lightness,” and even established color spaces like CIELAB and OKLAB have their limitations. While contrast ratio tools can be suggested for readability, they don’t universally apply to all color combinations.

Capturing colors in a mathematical model that precisely matches our perception is an illusion. Our perception of color is intricate and subjective, and even the most sophisticated approaches can’t fully capture it in an algorithm. This makes selecting a color palette more of an art than a science, with designers relying on intuition, experience, and feedback to create harmonious and functional combinations.

### Monokai in Pop Culture

Monokai’s influence even extends beyond the tech world. It’s featured in shows like **Silicon Valley**, **Mr. Robot** and several others, where its recognizable colors add authenticity to on-screen developer environments.

Its color palette has been used by illustrators, generative artists, and designers in various fields.

### Monokai Pro Expands: Introducing a Light Theme

For years, developers had been requesting a light theme for Monokai Pro. Taking this on meant more than simply brightening colors — contrast behaves differently on a light background, and bold tones can easily become overwhelming.

After extensive testing, Wimer introduced **Monokai Pro Light** in 2024 along with a new “Sun” filter, designed to retain Monokai’s clarity and readability in bright environments. Monokai Pro Light offers warm, balanced hues that are easy on the eyes yet vibrant, making it perfect for naturally lit spaces. The light theme expands Monokai’s appeal while staying true to its thoughtful, functional design, giving developers the experience they know in a refreshing, light palette.

```
function isPalindrome(str: string): boolean {
	const sanitized = str.replace(/[W_]/g, '').toLowerCase();

	return sanitized === sanitized.split('').reverse().join('');
}

console.log(isPalindrome('never odd or even')); // true
```

Example code in Monokai Pro Light colors

### Looking ahead

From a simple TextMate theme to an iconic tool, Monokai’s journey highlights the power of thoughtful design in coding. Monokai Pro remains the authentic evolution of Wimer’s vision, continuously adapting to modern software needs while staying true to its roots in clarity and simplicity. As code evolves, so does Monokai — an enduring reminder of how careful design can enhance both function and flow in the developer’s workspace.
