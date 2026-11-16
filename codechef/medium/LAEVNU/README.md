# LAEVNU

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Largest Even Number from String

You are given a string $S$ containing letters, digits, and special characters. A  **digit**  is any character from `0` to `9`.

Extract all digits from $S$ and rearrange them to form the largest possible even number. Ignore all non-digit characters.  **Every extracted digit must be used exactly once**, including repeated occurrences.

Print the resulting number without leading zeros. If all extracted digits are zero, print `0`.

If $S$ contains no digits, or no even number can be formed, print `-1`.

### Input Format

A single line contains the string $S$.

### Output Format

Print the largest possible even number that can be formed using all the extracted digits, or $-1$ if it is impossible.

### Constraints
- $1 \le |S| \le 1000$
- Every character of $S$ has an ASCII value between $33$ and $126$, inclusive. Thus, $S$ may contain English letters, digits, and punctuation symbols, but no spaces or other whitespace.
### Sample 1:
Input
Output

```
asdf@75483
```

```
87534
```

### Explanation:

The extracted digits are $7$, $5$, $4$, $8$, and $3$. The largest even number that can be formed using all of them is $87534$.

### Sample 2:
Input
Output

```
a1#7b5
```

```
-1
```

### Explanation:

All extracted digits are odd, so no arrangement can form an even number.

### Sample 3:
Input
Output

```
x0@0y
```

```
0
```

### Explanation:

Both extracted digits are zero. The resulting number is printed as $0$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-16T15:51:08.462Z  

```py
# cook your dish here
S=input()
l=[]
for i in S:
    if i.isdigit():
        l.append(i)
flag=False
for j in l:
    if int(j)%2==0:
        flag=True
        break
if flag==False:
    print(-1)
else:
    l.sort()
    if int(l[0])%2==0:
        print(int("".join(l[::-1])))
    else:
        for i in l:
            if int(i)%2==0:
                l.remove(i)
                break
        print(int("".join(l[::-1])+i))
```

---

[View on CodeChef](https://www.codechef.com/problems/LAEVNU)