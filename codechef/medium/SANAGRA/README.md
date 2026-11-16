# SANAGRA

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sentence Anagrams

You are developing a feature for a plagiarism detection tool. A simple check determines whether two sentences contain the same words arranged in a different order.

Given two sentences, determine whether they are  **sentence anagrams**. Two sentences are sentence anagrams if they contain exactly the same words with the same frequencies, regardless of letter case or word order.

A  **word**  is a sequence of consecutive English letters (`A`–`Z` or `a`–`z`). All non-letter characters, including spaces, punctuation, and digits, act as separators. For example, `hello-world` contains two words: `hello` and `world`.

If neither sentence contains any words, they are considered anagrams.

### Input Format

The input consists of two lines.

- The first line contains the first sentence.
- The second line contains the second sentence.
### Output Format
- Print "The sentences are anagrams." if the two sentences are anagrams.
- Otherwise, print "The sentences are not anagrams.".
### Constraints
- The length of each sentence is between $1$ and $10^5$ characters, inclusive.
- Each character is a printable ASCII character with a value between $32$ and $126$, inclusive.
- All non-letter characters, including digits, act as word separators.
### Sample 1:
Input
Output

```
The quick brown fox
Brown fox the quick
```

```
The sentences are anagrams.
```

### Explanation:

Both sentences contain the words `the`, `quick`, `brown`, and `fox` exactly once, ignoring case.

### Sample 2:
Input
Output

```
Hello, world! Hello.
WORLD-hello hello
```

```
The sentences are anagrams.
```

### Explanation:

Both sentences contain `hello` twice and `world` once. Punctuation separates the words, and case does not affect the comparison.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-16T16:08:14.324Z  

```py
# cook your dish here
s1=input()
s2=input()
c1=""
c2=""
freq1={}
freq2={}
for i in s1:
    if i.isalpha():
        c1+=i.lower()
    else:
        c1+=""
for j in s2:
    if j.isalpha():
        c2+=j.lower()
    else:
        c2+=""        
for k in c1:
    freq1[k]=freq1.get(k,0)+1
for l in c2:
    freq2[l]=freq2.get(l,0)+1    
if freq1==freq2:
    print("The sentences are anagrams.")
else:
    print("")
```

---

[View on CodeChef](https://www.codechef.com/problems/SANAGRA)