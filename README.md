<h1 align="center">LeetCode Daily Practice</h1>

<p align="center">
  Daily LeetCode solutions focused on consistency, readability, and long-term reference.
</p>

<p align="center">
  <a href="https://github.com/vhlima1008/leetcode"><img alt="Language" src="https://img.shields.io/badge/language-Python-blue" /></a>
  <a href="https://github.com/vhlima1008/leetcode/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/vhlima1008/leetcode" /></a>
  <a href="https://github.com/vhlima1008/leetcode/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/vhlima1008/leetcode" /></a>
  <a href="https://github.com/vhlima1008/leetcode/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/vhlima1008/leetcode?style=flat" /></a>
</p>

---

## Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Tech Stack](#-tech-stack)
- [Setup](#-setup)
- [How to Run a Solution](#-how-to-run-a-solution)
- [Style Guide](#-style-guide)
- [Optional: Organize by Topic (without breaking the streak)](#-optional-organize-by-topic-without-breaking-the-streak)
- [Contributing](#-contributing)
- [License](#-license)

---

## Overview

This repository tracks my **daily LeetCode practice**.

Each day, I add at least one solution inside `Python/`, using **clear filenames that match the original problem title**. The goals are:

- **Consistency**: keep a daily practice streak
- **Readability**: clean code and naming
- **Revisitability**: quick to understand later (notes + complexity when useful)

Use this repo as a study log, a reference library, or a source of alternative approaches.

---

## Repository Structure

Current structure:

```txt
.
├── Python/
│   ├── 3433_Count_Mentions_Per_User.py
│   ├── 3531_Count_Covered_Buildings.py
│   └── ...
└── README.md
````

**Naming conventions**

* All solutions have a language, like: `Python/`
* Filenames: aligned with the LeetCode problem name
* Prefer readable names over cryptic abbreviations

---

## Tech Stack

* **Python 3**
* **LeetCode**
* **Git**

Links:

* Python Docs: [https://docs.python.org/3/](https://docs.python.org/3/)
* LeetCode: [https://leetcode.com/](https://leetcode.com/)
* Git: [https://git-scm.com/](https://git-scm.com/)

---

## Setup

### Prerequisites

* Python 3 installed

### Optional dependencies

If you add a `requirements.txt` in the future:

```bash
pip install -r requirements.txt
```

---

## How to Run a Solution

If a file contains a runnable block like:

```py
if __name__ == "__main__":
    ...
```

Run it with:

```bash
python "Python/<file-name>.py"
```

Example:

```bash
python "Python/9_Palindrome_Number.py"
```

---

## Style Guide

To keep solutions consistent and easy to review, I follow these rules:

1. **Header comment**

   * Problem name
   * Approach summary (1–3 lines)
   * Time/space complexity

2. **Readable first**

   * Prefer clarity over clever one-liners
   * Use descriptive variable names

3. **Complexity**

   * Add `Time:` and `Space:` notes when non-trivial

4. **Minimal but helpful docs**

   * A short explanation is better than none
   * Add edge-case notes if relevant

### Suggested solution template

```py
"""
LeetCode: <Problem Name>
Approach: <brief description>
Time: O(...)
Space: O(...)
"""

from typing import List

class Solution:
    def solve(self, ...):
        ...
        
if __name__ == "__main__":
    # Optional quick sanity checks
    pass
```

## Contributing

Contributions are welcome—especially improvements to clarity, correctness, edge cases, or additional approaches.

1. Fork this repository and clone it locally
2. Create a new branch:

   ```bash
   git checkout -b my-branch
   ```
3. Commit your changes:

   ```bash
   git add .
   git commit -m "feat: 67_Add_Binary.py"
   ```
4. Push to your fork:

   ```bash
   git push origin my-branch
   ```
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE).

```
