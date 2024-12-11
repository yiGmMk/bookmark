# Debugging Till Dawn: How Git Bisect Saved My Demo
- URL: https://www.mikebuss.com/posts/debugging-till-dawn
- Added At: 2024-12-11 07:57:07
- [Link To Text](2024-12-11-debugging-till-dawn-how-git-bisect-saved-my-demo_raw.md)

## TL;DR
作者在演示前7小时发现了一个bug，使用git bisect工具找到了问题所在的commit，并在4小时内修复了bug。git bisect是一个使用二分法算法来找出引入bug的具体commit的工具。通过启动git bisect、标记commit、运行测试脚本，git bisect可以快速找到引入bug的具体commit。作者通过分析commit的内容找到了问题所在，并修复了bug。git bisect是一个非常有用的工具，可以帮助开发者快速找到引入bug的具体commit，节省调试时间。

## Summary
1. **调试经历**：作者在演示前7小时内发现了一个bug，通过git bisect工具找到了问题所在的commit，并在4小时内修复了bug。

2. **项目背景**：项目由两个部分组成：一个使用C编写的固件和一个使用Swift编写的iPadOS应用，作者怀疑bug出现在固件部分。

3. **问题描述**：在工作版本和buggy版本之间有100多个commit，作者需要找到引入bug的具体commit。

4. **git bisect简介**：git bisect是一个使用二分法算法来找出引入bug的具体commit的工具。

5. **使用git bisect**：
   - **启动git bisect**：通过`git bisect start`命令启动git bisect。
   - **标记commit**：通过`git bisect bad HEAD`和`git bisect good v1.0.0`命令标记当前HEAD为"bad"和最后一个已知好的commit为"good"。
   - **运行测试脚本**：通过`git bisect run ./test_for_bug.sh`命令让git bisect运行测试脚本来检查每个commit是否存在bug。

6. **git bisect的工作原理**：git bisect使用二分法算法来找出引入bug的具体commit，通过每次测试来缩小搜索范围。

7. **调试结果**：git bisect找到了引入bug的具体commit，作者通过分析commit的内容找到了问题所在。

8. **修复bug**：作者通过分析commit的内容找到了问题所在，并在4小时内修复了bug。

9. **结论**：git bisect是一个非常有用的工具，可以帮助开发者快速找到引入bug的具体commit，节省调试时间。
