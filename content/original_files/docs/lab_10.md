---
title: The Snorting Narwhals
type: docs
weight: 10
BookToC: true
---
# **Lab Session #10**

# Agenda

1) RegExp to (N)FSA: Thompson’s Construction
2) FSA to RegExp: Kleene’s Algorithm

---

## From Regular Expression to (N)FSA.
### **The Thompson’s Construction**

- It is an algorithm for transforming a regexp into an equivalent
(N)FSA.

- I This (N)FSA can be used to match strings against the regular
expression.

---

### **The Algorithm**

- The algorithm works recursively by splitting an expression into its
constituent subexpressions, from which the (N)FSA will be
constructed using a set of rules (see below).

---

### **Rule: the Empty Expression**

The empty-expression {{< katex >}}ϵ{{< /katex >}} is converted to:

![1](/images/lab10/1.jpg)

---

### **Rule: a symbo**

A symbol a of the input alphabet is converted to

![2](/images/lab10/2.jpg)

---

### **Rule: Concatenation Expression**

The concatenation expression st is converted to

![3](/images/lab10/3.jpg)

N(s) and N(t) are the (N)FSA of the subexpression s and t,
respectively.

---

### **Rule: Union Expression**

The union expression s|t is converted to

![4](/images/lab10/4.jpg)

N(s) and N(t) are the (N)FSA of the subexpression s and t,
respectively.

---

### **Rule: Kleene Star Expression**

The Kleene star expression  {{< katex >}}s
^∗{{< /katex >}}
is converted to

![5](/images/lab10/5.jpg)

N(s) is the (N)FSA of the subexpression s.

---

### **Example 1**

Build a (N)FSA for  {{< katex >}}(1 | 01)^*{{< /katex >}}

**Solution**:

{{< expand >}}
- step 1:


![6](/images/lab10/6.jpg)


- step 2:


![7](/images/lab10/7.jpg)

- step 3:


![8](/images/lab10/8.jpg)

- step 4:


![9](/images/lab10/9.jpg)

- step 5:


![10](/images/lab10/10.jpg)

{{< /expand >}}

---

### **Exercises**

Build a (N)FSA for:
1.  {{< katex >}}01^*{{< /katex >}}
2.  {{< katex >}}(0 | 1)01{{< /katex >}}
3.  {{< katex >}}00(0 | 1)^*{{< /katex >}}

### **Solution.**

{{< expand >}}
1)- (N)FSA for {{< katex >}}01^*{{< /katex >}}
![19](/images/lab10/19.jpg)

2)- (N)FSA for {{< katex >}}(0 | 1)01{{< /katex >}}
![20](/images/lab10/20.jpg)

3_- (N)FSA for {{< katex >}}00(0 | 1)^*{{< /katex >}}
![21](/images/lab10/21.jpg)
{{< /expand >}}

---

## **FSA to RegExp**

### **Kleene’s Algorithm: from FSA to Regular Expression**

It transforms a given finite state automaton (FSA) into a regular
expression.
Description: Given an FSA {{< katex >}} M = (Q, A, δ, q_0, F){{< /katex >}}, with

{{< katex >}}Q = {q0, . . . , qn}{{< /katex >}}its set of states, the algorithm computes
-  the sets {{< katex >}}R^k_{ij}{{< /katex >}}of all strings that take M from state{{< katex >}}q_{ij}{{< /katex >}}to{{< katex >}}q_j{{< /katex >}} without going through any state numbered higher than k.

 - each set {{< katex >}}R^k_{ij}{{< /katex >}}represented by a regular expression.

- the algorithm computes them step by step for {{< katex >}}k = −1, 0, . . . , n.
{{< /katex >}}

-  since there is no state numbered higher than n, the regular
expression{{< katex >}}R^n_{0j}{{< /katex >}}represents the set of all strings that take M
from its start state {{< katex >}}q_i{{< /katex >}}to{{< katex >}}q_j{{< /katex >}}.

- If {{< katex >}}F = {q_i
, . . . , q_f }{{< /katex >}}  is the set of accept states, the regular
expression {{< katex >}}R^
n
_{0i}
| . . . | R^
n
_{0f}{{< /katex >}}represents the language accepted by
M.

---

### **Kleene’s Algorithm**

The initial regular expressions, for k = −1, are computed as

- {{< katex >}}R^
{−1}
_{ij} = a_1 | . . . | a_m{{< /katex >}}  if {{< katex >}}i = j{{< /katex >}},where{{< katex >}}δ (q_i
, a_1) = . . . = δ (q_i
, a_m) = q_j{{< /katex >}}

- {{< katex >}}R^
{−1}
_{ij} = a_1 | . . . | a_m|ϵ{{< /katex >}}    if {{< katex >}}i = j{{< /katex >}},where{{< katex >}}δ (q_i
, a_1) = . . . = δ (q_i
, a_m) = q_j{{< /katex >}}

After that, in each step the expressions {{< katex >}}R^k_il{{< /katex >}}
 are computed from the
previous ones by

{{< katex >}}R^k_{ij}{{< /katex >}} = {{< katex >}}R^{k-1}_{ik}{{< /katex >}} {{< katex >}}(R^{k-1}_{kk})^*{{< /katex >}} {{< katex >}}R^{k-1}_{kj}{{< /katex >}} | {{< katex >}}R^{k-1}_{ij}{{< /katex >}}

---

### **Kleene’s Algorithm: Example**

Give a regular expression that describes the language accepted by:

![11](/images/lab10/11.jpg)

Initial Regular Expression (Step -1)

 {{< katex >}}R^{-1}_{00}{{< /katex >}} = 0 | {{< katex >}}ϵ{{< /katex >}}

{{< katex >}}R^{-1}_{01}{{< /katex >}} = 1

{{< katex >}}R^{-1}_{10}{{< /katex >}} = 0 

{{< katex >}}R^{-1}_{11}{{< /katex >}} = {{< katex >}}ϵ{{< /katex >}}

Step 0

{{< katex >}}R^{0}_{00}{{< /katex >}} =
 {{< katex >}}(0 |ϵ){{< /katex >}}
 {{< katex >}}(0 |ϵ)^*{{< /katex >}}
  {{< katex >}}(0 |ϵ){{< /katex >}}|
   {{< katex >}}(0 |ϵ){{< /katex >}}= {{< katex >}}0^*{{< /katex >}}

{{< katex >}}R^{0}_{01}{{< /katex >}} =
 {{< katex >}}(0 |ϵ){{< /katex >}}
 {{< katex >}}(0 |ϵ)^*{{< /katex >}}1 |1=
  {{< katex >}}0^*1{{< /katex >}}

{{< katex >}}R^{0}_{10}{{< /katex >}} =
0 {{< katex >}}(0 |ϵ)^*{{< /katex >}}
 {{< katex >}}(0 |ϵ){{< /katex >}} | 0
 = {{< katex >}}00^*{{< /katex >}}

{{< katex >}}R^{0}_{11}{{< /katex >}} =
0{{< katex >}}(0 |ϵ)^*{{< /katex >}}1 |
  {{< katex >}}ϵ{{< /katex >}} = 
    {{< katex >}}00^*1{{< /katex >}} | 
      {{< katex >}}ϵ{{< /katex >}}

step 1

  {{< katex >}}R^1_{00}{{< /katex >}} =
  {{< katex >}}(0^*1){{< /katex >}}
  {{< katex >}}(00^*1| ϵ)^*{{< /katex >}}
  {{< katex >}}(00^*)|0^*{{< /katex >}}= 
  {{< katex >}}(0^*1){{< /katex >}}
  {{< katex >}}(00^*1)^*{{< /katex >}}
  {{< katex >}}(00^*)|0^*{{< /katex >}}

Do we need to compute the rest?
(i.e {{< katex >}}R^{1}_{01},R^{1}_{10},R^{1}_{11}{{< /katex >}})

---

### **Exercises**

Give a regular expression that describes the language accepted by:

![16](/images/lab10/16.jpg)


### **solution**
{{< expand >}}



(Step -1)

  {{< katex >}}R^{-1}_{00}{{< /katex >}} = {{< katex >}}0|ϵ{{< /katex >}}

---

  {{< katex >}}R^{-1}_{01}{{< /katex >}} = 0

---

  {{< katex >}}R^{-1}_{10}{{< /katex >}} ={{< katex >}}∅{{< /katex >}}

---

  {{< katex >}}R^{-1}_{11}{{< /katex >}} = {{< katex >}}0|ϵ{{< /katex >}}

---

  (step 0)

{{< katex >}}R^{0}_{00}{{< /katex >}} =
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}|R^{-1}_{00}{{< /katex >}}=
 {{< katex >}}(1 |ϵ){{< /katex >}}
 {{< katex >}}(1 |ϵ)^*{{< /katex >}}
  {{< katex >}}(1 |ϵ){{< /katex >}}|
   {{< katex >}}(1 |ϵ){{< /katex >}}= {{< katex >}}1^*{{< /katex >}}
---
{{< katex >}}R^{0}_{01}{{< /katex >}} =
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{01}{{< /katex >}}
 {{< katex >}}|R^{-1}_{01}{{< /katex >}}=
 {{< katex >}}(1 |ϵ){{< /katex >}}
 {{< katex >}}(1 |ϵ)^*{{< /katex >}}
  {{< katex >}}0|0{{< /katex >}} = {{< katex >}}1^*0{{< /katex >}}

---
{{< katex >}}R^{0}_{10}{{< /katex >}} =
{{< katex >}}R^{-1}_{10}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}|R^{-1}_{10}{{< /katex >}}=
 {{< katex >}}∅(1 |ϵ)^*{{< /katex >}}
 {{< katex >}}(1 |ϵ){{< /katex >}}
  {{< katex >}}|∅{{< /katex >}} = {{< katex >}}∅{{< /katex >}}
---
{{< katex >}}R^{0}_{11}{{< /katex >}} =
{{< katex >}}R^{-1}_{10}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{01}{{< /katex >}}
 {{< katex >}}|R^{-1}_{11}{{< /katex >}}=
 {{< katex >}}∅(1 |ϵ)^*0{{< /katex >}}
 {{< katex >}}|(0 |ϵ){{< /katex >}}  = {{< katex >}}(0 |ϵ){{< /katex >}}
---
step(1)

{{< katex >}}R^{1}_{01}{{< /katex >}} =
{{< katex >}}R^{0}_{01}{{< /katex >}}
 {{< katex >}}(R^{0}_{11})^*{{< /katex >}}
 {{< katex >}}R^{0}_{11}{{< /katex >}}
 {{< katex >}}|R^{0}_{01}{{< /katex >}}
 {{< katex >}}= (1^
∗0)(0|ϵ)^
∗
(0 |ϵ) | 1^
∗0 
= 1^
∗00^∗
| 1^
∗0 = 1^
∗00^∗
{{< /katex >}}

Do we need to compute the rest? (i.e

{{< katex >}}R^{1}_{01},R^{1}_{10},R^{1}_{11}{{< /katex >}})

---

### **Exercise 2 Solution**

(Step -1)

 {{< katex >}}R^{-1}_{00}{{< /katex >}} =0| {{< katex >}}ϵ{{< /katex >}}

---

{{< katex >}}R^{-1}_{01}{{< /katex >}} = 1

---

{{< katex >}}R^{-1}_{10}{{< /katex >}} = 1

---

{{< katex >}}R^{-1}_{11}{{< /katex >}} = {{< katex >}}0|ϵ{{< /katex >}}

---

(step 0)

{{< katex >}}R^{0}_{00}{{< /katex >}} =
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}|R^{-1}_{00}{{< /katex >}}=
 {{< katex >}}(0 |ϵ){{< /katex >}}
 {{< katex >}}(0 |ϵ)^*{{< /katex >}}
  {{< katex >}}(0 |ϵ){{< /katex >}}|
   {{< katex >}}(0 |ϵ){{< /katex >}}= {{< katex >}}0^*{{< /katex >}}
---
{{< katex >}}R^{0}_{01}{{< /katex >}} =
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{01}{{< /katex >}}
 {{< katex >}}|R^{-1}_{01}{{< /katex >}}=
 {{< katex >}}(0 |ϵ){{< /katex >}}
 {{< katex >}}(0 |ϵ)^*{{< /katex >}}
  {{< katex >}}1|1{{< /katex >}} = {{< katex >}}0^*1{{< /katex >}}

---
{{< katex >}}R^{0}_{10}{{< /katex >}} =
{{< katex >}}R^{-1}_{10}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{00}{{< /katex >}}
 {{< katex >}}|R^{-1}_{10}{{< /katex >}}=
 {{< katex >}}1(0 |ϵ)^*{{< /katex >}}
 {{< katex >}}(0 |ϵ){{< /katex >}}
  {{< katex >}}|1{{< /katex >}} = {{< katex >}}10^*{{< /katex >}}
---
{{< katex >}}R^{0}_{11}{{< /katex >}} =
{{< katex >}}R^{-1}_{10}{{< /katex >}}
 {{< katex >}}(R^{-1}_{00})^*{{< /katex >}}
 {{< katex >}}R^{-1}_{01}{{< /katex >}}
 {{< katex >}}|R^{-1}_{11}{{< /katex >}}=
 {{< katex >}}1(0 |ϵ)^*1{{< /katex >}}
 {{< katex >}}|(0 |ϵ){{< /katex >}}  = {{< katex >}}10^*1|(0 |ϵ){{< /katex >}}
---
step(1)

{{< katex >}}R^{1}_{01}{{< /katex >}} =
{{< katex >}}R^{0}_{01}{{< /katex >}}
 {{< katex >}}(R^{0}_{11})^*{{< /katex >}}
 {{< katex >}}R^{0}_{11}{{< /katex >}}
 {{< katex >}}|R^{0}_{01}{{< /katex >}}
 {{< katex >}}= 0^
∗1(10^∗1 | (0 |ϵ))^∗10^∗
| 0^
∗ 
= (0^
∗10^∗10^∗
)
∗
| 0^
∗ = (10^∗1 | 0)^
∗
{{< /katex >}}

Do we need to compute the rest? (i.e

{{< katex >}}R^{1}_{01},R^{1}_{10},R^{1}_{11}{{< /katex >}})

---

{{< /expand >}}

---

## **Homework**

1. Give a regular expression that describes the language accepted
by:

![18](/images/lab10/18.jpg)

2. Build a (N)FSA for:{{< katex >}}(11)^*(0 | 1){{< /katex >}}