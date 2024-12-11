Title: Debugging Till Dawn: How Git Bisect Saved My Demo

URL Source: https://www.mikebuss.com/posts/debugging-till-dawn

Markdown Content:
It was Monday at 2 a.m. and I was frantically troubleshooting a bug before a demo I had to give in 7 hours. For the life of me, I could not figure out why the issue was happening. But, I knew one thing: this bug didn’t exist in the previous version.

The project consisted of two components: a device running firmware I wrote in C, and an iPadOS application I wrote in Swift. I was fairly confident the bug existed on the firmware side.

![Image 4: An example iPad and microcontroller](https://www.mikebuss.com/_next/image?url=%2Fimages%2Fposts%2Fdebugging-till-dawn%2Fdevices.jpg&w=3840&q=75)

There were over 100 commits between the working version and the buggy version, so it wasn’t immediately obvious what change caused the bug.

That's when I remembered **git bisect**. This command uses a binary search algorithm to help pinpoint the exact commit that introduced a bug. It was time to put it to work.

How does Git Bisect work?
-------------------------

Press 'Play' to start the demo.

I started by marking the current HEAD as "bad" and the last known good commit as "good":

```
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
```

Git then checked out a commit halfway between these two points. This is where the magic of binary search comes into play. Instead of checking each commit one by one, which would have taken ages with over 100 commits to sift through, **git bisect** strategically selects commits to test, halving the search space with each iteration.

Luckily, this was a bug that I could verify with a script. So, I added a script to check if the bug was present and made **git bisect** run the tests for each commit.

```
git bisect run ./test_for_bug.sh
```

And off it went! Git checked out different commits, ran my script, and narrowed down the search.

After a few seconds, Git announced:

```
b1f3d2c is the first bad commit
commit b1f3d2c5e8a9f0d4c3b2a1098765432100fedcba
Author: Mike Buss <mike@mikebuss.com>
Date:   Fri Jun 9 11:23:45 2024 -0700

    Added a feature that definitely won’t break anything
```

The culprit was found. It turned out that in my zealous attempt to optimize memory usage, I had introduced a subtle bug in the sensor data processing routine. The optimization worked fine for most cases but failed under specific conditions – exactly the conditions present in my demo scenario.

With the problematic commit identified, fixing the bug became much easier. I was able to zero in on the exact changes that caused the issue and make the necessary corrections.

By 5 a.m., four hours before my demo, the bug was fixed.

This experience reinforced a valuable lesson: knowing your tools is just as important as knowing your code. **git bisect** turned what could have been hours of manual debugging into one command.

In the vast forest of code, the right tool can be your compass. Remember the power of **git bisect** – it might just be the lifeline you need in your next debugging adventure.
