# Practice assignment from MentorMate

Used Python 3.8.

The solution is сovered by tests.

I solved the task with lists. To begin with, visually divided MM into two parts.

```console
---***---***---
--*****-*****--
-***-*****-***-
***---***---***
```
Then divide into 2 parts:

s1(var name in code):
```console
---***---***---
--*****-*****--
```
s2(var name in code):
```console
-***-*****-***-
***---***---***
```
Having analyzed s1 and s2, we see that the "-" and "*" alternate through one.

So using list comprehension we create s1 and s2. There should be 5 elements in s1 ['---', '\*\*\*', '---', '\*\*\*', '---']. There must be 7 elements in s2 ['---', '\*\*\*', '---', '\*\*\*', '---', '\*\*\*', '---'].

In s1, the first and last elements of 5 elements decrease by 1, the second and fourth elements increase by 2, and the third element decreases by 2. In s2 we do it similarly.

Then through the loop we display the list as strings

## Task

Create a console application that displays the MM logo, according to the parameter N, showing the size of the letter in the upper edge of the logo. For free space use "-", and for letters use "*".

## Constraint

2 < N < 10000, N is always an odd number.

## Examples

N = 3
```console
---***---***------***---***---
--*****-*****----*****-*****--
-***-*****-***--***-*****-***-
***---***---******---***---***
```
N = 5
```console
-----*****-----*****----------*****-----*****-----
----*******---*******--------*******---*******----
---*********-*********------*********-*********---
--*****-*********-*****----*****-*********-*****--
-*****---*******---*****--*****---*******---*****-
*****-----*****-----**********-----*****-----*****
```
N = 7
```console
-------*******-------*******--------------*******-------*******-------
------*********-----*********------------*********-----*********------
-----***********---***********----------***********---***********-----
----*************-*************--------*************-*************----
---*******-*************-*******------*******-*************-*******---
--*******---***********---*******----*******---***********---*******--
-*******-----*********-----*******--*******-----*********-----*******-
*******-------*******-------**************-------*******-------*******
```