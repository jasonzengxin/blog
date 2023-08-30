---
title: Clean Code
date: 2023-08-30 14:31:16
tags:
---
## Basic Principles

- 简单暴力   **KISS (Keep it simple, stupid)**
  - Clarity First，Optimization second. 能让人看懂是最优先， 性能再好都是其次
  - 傻x都能写出能work的代码，好程序员写出来的是人类能懂的 “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.” — Martin Fowler**
  - 著名的雷神之锤代码 Q_rsqrt <https://github.com/id-Software/Quake-III-Arena/blob/master/code/game/q_math.c>
  {% asset_img 1693377274242.jpg code1%}

- 快速试错 [Rapid Iterative Testing and Evaluation (RITE)](https://about.gitlab.com/handbook/product/ux/ux-research/rite/)
  - 找到问题的根源，在根源上改。 think before you code, don't make adhoc change or tweak some if condition without much thinking
  - 重复代码 重复逻辑 不利于试错 不收敛 DRY (Don’t Repeat Yourself) principle
  - 一切都是代码，ut和ft也是代码需要review."Talk is cheap. Show me the code." -- Linus Torvalds
- 没有绝对的正确，核心是我们怎么妥协  ***“There are no solutions, only tradeoffs - Thomas Sowell”***
  - 做一个有态度的 reviewer - Having a clear direction helps us converge quickly.
    - code review 包含了主观的偏好 subjective [IMO] objective[FACT]
    - senior 一定是对的吗 I disagree with your disagreement
    - Let's appeal to rules that all team member respect （We Make Up the Rules as We Go Along）
