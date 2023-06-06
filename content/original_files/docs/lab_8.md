---
title: The Smiling Snails
type: docs
weight: 8
BookToC: true
---
# **Lab Session #8**

# Agenda

- Non-deterministic FSA
- NDFSA to (D)FSA 
- Regular Expressions (RegExp)


## **Non-deterministic Finite State Automata (NDFSA)**
### **Definition**  

A NDFSA is a tuple {{< katex >}} \lang Q, I, \delta, q_0, F\rang {{< /katex >}}, where {{< katex >}}Q, I, q_0, F {{< /katex >}} are defined as in (D)FSA and the transition function is defined as

{{< katex display>}} \delta : Q \times I \to \mathbb{P}(Q) {{< /katex >}}


<p style="text-align: center;">{{< katex>}} \mathbb{P} {{< /katex >}} is the powerset function (i.e. set of all possible students)</p>


A NDFSA modifies the definition of a FSA to permit transitions at
each stage to either zero, one, or more than one states.


------

### **The extended transition δ\* for NDFSA**

Let {{< katex >}} M = \lang Q, I, \delta, q_0, F\rang {{< /katex >}} be a NDFSA. We define the extended transition function as follows:
1. For every {{< katex >}} q \in Q{{< /katex >}}, {{< katex >}} \delta^\ast(q,\epsilon) = \{q\}{{< /katex >}}
2. For every {{< katex >}} q \in Q{{< /katex >}}, every {{< katex >}} y \in I^\ast{{< /katex >}}, and every {{< katex >}} i \in I{{< /katex >}},

{{< katex display>}} \delta^\ast(q,yi) = \bigcup_{q'\in\delta^\ast(q,y)}\delta(q',i){{< /katex >}}

------

### **Acceptance by a NDFSA**

Let {{< katex >}} M = \lang Q, I, \delta, q_0, F\rang {{< /katex >}} be a NDFSA. and let {{< katex >}} x \in I^\ast {{< /katex >}}. The string {{< katex >}} x {{< /katex >}} is accepted by {{< katex >}} M {{< /katex >}} if 

{{< katex display >}} \delta^\ast(q_0,x)\cap F \neq \varnothing{{< /katex >}}

and it is rejected by {{< katex >}} M {{< /katex >}} otherwise.

**Notion:** Among the various possible runs (with the same input) of the NDFSA, it is sufficient that one of them succeeds to accept the input string.


------

### **Exercises on NDFSA**

Build NDFSAs that recognise the following languages:

- {{< katex >}} L_a = \{x \in \{0, 1\}^* \mid  x {{< /katex >}} ends with {{<  katex >}}101\} {{< /katex >}};
- {{< katex >}} L_b = \{xy \mid x \in \{a\}^* \wedge y \in \{a, b\}^* \wedge y {{< /katex >}} does not start with {{<  katex >}}\text{\textquoteleft}b\text{\textquoteright} \wedge {{< /katex >}} every {{<  katex >}}\text{\textquoteleft} a  \text{\textquoteright}{{< /katex >}} in {{<  katex >}}y {{< /katex >}} is followed by exactly one {{<  katex >}}\text{\textquoteleft}b\text{\textquoteright}\} {{< /katex >}};
- {{< katex >}} L_a = \{x \in \{a, b, c\}^* \mid  x {{< /katex >}} ends with either {{<  katex >}}ab{{< /katex >}}, {{<  katex >}}bc{{< /katex >}} or {{<  katex >}}ca\}{{< /katex >}}; 

{{< expand Solutions>}}
NDFSA that recognises the language:

{{< katex >}} L_a = \{x \in \{0, 1\}^* \mid  x {{< /katex >}} ends with {{<  katex >}}101\} {{< /katex >}};

![sol1](/images/lab8/sol1.png)

NDFSA that recognises the language:

{{< katex >}} L_b = \{xy \mid x \in \{a\}^* \wedge y \in \{a, b\}^* \wedge y {{< /katex >}} does not start with {{<  katex >}}\text{\textquoteleft}b\text{\textquoteright} \wedge {{< /katex >}} every {{<  katex >}}\text{\textquoteleft} a  \text{\textquoteright}{{< /katex >}} in {{<  katex >}}y {{< /katex >}} is followed by exactly one {{<  katex >}}\text{\textquoteleft}b\text{\textquoteright}\} {{< /katex >}};

![sol2](/images/lab8/sol2.png)

NDFSA that recognises the language:

{{< katex >}} L_a = \{x \in \{a, b, c\}^* \mid  x {{< /katex >}} ends with either {{<  katex >}}ab{{< /katex >}}, {{<  katex >}}bc{{< /katex >}} or {{<  katex >}}ca\}{{< /katex >}}; 

![sol3](/images/lab8/sol3.png)
{{< /expand >}} 



------


## **NDFSA to DFSA**

### **Algorithm for NDFSA to DFSA**

1. Create state table from the given NDFA
2. Create a blank state table under possible input alphabets for the equivalent DFA
3. Mark the start state of the DFA by {{<katex>}}q_0{{</katex>}} (Same as the NDFA)
4. Find out the combination of States {{<katex>}}q_0, q_1, ..., q_n{{</katex>}} for each possible input alphabet
5. Each time we generate a new DFA state under the input alphabet columns, we have to apply step {{<katex>}}4{{</katex>}} again, otherwise go to step {{<katex>}}6{{</katex>}}
6. The states which contain any of the accepting states of the
NDFA are the accepting states of the equivalent DFA


------

### **Simple example (1)**

![ex1](/images/lab8/ex1.png)

{{<expand DFSA>}}
![ex1sol](/images/lab8/ex1sol.png)
{{</expand>}}

![ex2](/images/lab8/ex2.png)

{{<expand "DFSA (table representation)" >}}

![ex2sol](/images/lab8/ex2sol.png)
{{</expand>}}


------

### **Example with steps**

Let us consider the following NDFSA:

![NDFSA](/images/lab8/NDFSA.jpg)

First, we build a transition table for NDFSA:

{{<expand "Step 1" >}}

![step1](/images/lab8/step1.png)
{{</expand>}}

Using table from previous step, let us create a similar table, but this time for FSA. Initially, the table is empty:

{{<expand "Step 2" >}}

![step2](/images/lab8/step2.png)
{{</expand>}}

We begin by adding the initial state and the set of states:

{{<expand "Step 3" >}}

![step3](/images/lab8/step3.png)
{{</expand>}}

The initial state can take us to two new states that are not yet in the table. Note that we treat a set of states as a single state now!

The next step is to find possible states for {{<katex>}}\{q_1,q_2\}{{</katex>}} and {{<katex>}}q_3{{</katex>}}. For {{<katex>}}q_3{{</katex>}} it is trivial, you just need to look it up in the original NDFSA table. However, the transition for {{<katex>}}\{q_1,q_2\}{{</katex>}} will be a union of sets:
   {{<katex display>}}\delta({q_1,q_2},0) = \delta(q_1,0) \cup \delta(q_2,0) = \{q_3\} {{</katex>}}
   {{<katex display>}}\delta({q_1,q_2},1) = \delta(q_1,1) \cup \delta(q_2,1) = \{q_0,q_1,q_3\}{{</katex>}}


{{<expand "Step 4" >}}
![step4](/images/lab8/step4.png)
{{</expand>}}

Repeat the steps above until we have included all states from the original NDFSA and there are no new states.

{{<expand "Step 5">}}
![step5](/images/lab8/step5.png)
![step5_2](/images/lab8/step5_2.png)

...
{{</expand>}}

After repeating previous steps and depicting final states we will arrive to the following table:

{{<expand "Step 6">}}
![step6](/images/lab8/step6.png)
{{</expand>}}

The result will be the following:
{{<expand "Result (table representation)">}}
![final](/images/lab8/final.png)
{{</expand>}}
{{<expand "Result (graphical representation)">}}
![DFSA](/images/lab8/DFSA.jpg)
{{</expand>}}

------

### **Exercise 1**

Build DFSA from the NDFSA that recognizes the language:

{{< katex >}} L_1 = \{x \in \{0, 1\}^* \mid  x {{< /katex >}} ends with {{<  katex >}}101\} {{< /katex >}};

![sol1](/images/lab8/sol1.png)

------

### **Exercise 2**

Build DFSA from the NDFSA that recognizes the language:

{{< katex >}} L_2 = \{xy \mid x \in \{a\}^* \wedge y \in \{a, b\}^* \wedge y {{< /katex >}} does not start with {{<  katex >}}\text{\textquoteleft}b\text{\textquoteright} \wedge {{< /katex >}} every {{<  katex >}}\text{\textquoteleft} a  \text{\textquoteright}{{< /katex >}} in {{<  katex >}}y {{< /katex >}} is followed by exactly one {{<  katex >}}\text{\textquoteleft}b\text{\textquoteright}\} {{< /katex >}};

![sol2](/images/lab8/sol2.png)

------

### **Exercise 3**

Build DFSA from the NDFSA that recognizes the language:

{{< katex >}} L_3 = \{x \in \{a, b, c\}^* \mid  x {{< /katex >}} ends with either {{<  katex >}}ab{{< /katex >}}, {{<  katex >}}bc{{< /katex >}} or {{<  katex >}}ca\}{{< /katex >}}; 

![sol3](/images/lab8/sol3.png)

------


## **Regular Expressions (RegExp)**
  
### **Definition**

Inductive definition of RegExps over an alphabet {{<katex>}}\Sigma{{</katex>}}:
**Basis.**
- Symbol {{<katex>}}\emptyset{{</katex>}} is a regular expression (denoting the langauge {{<katex>}}\emptyset{{</katex>}});
- Symbol {{<katex>}}\epsilon{{</katex>}} is a RegExp (denoting the language {{<katex>}}\{\epsilon\}{{</katex>}});
- Each symbol {{<katex>}}\sigma{{</katex>}} of {{<katex>}}\Sigma{{</katex>}} is a RegExp
<p style="text-align: center;">{{<katex>}}L(\sigma) = \{\sigma\}{{</katex>}} for each {{<katex>}}\sigma\in\Sigma{{</katex>}}</p>

**Induction.**
Let {{<katex>}}r{{</katex>}} and {{<katex>}}s{{</katex>}} be two RegExps, then
- {{<katex>}}(r\cdot{s}){{</katex>}} is a RegExp (for simplicity, the dot is often omitted);
{{<katex display>}}L((r\cdot{s})) = \{ww'\mid(w \in L(r) \wedge w' \in L(s))\}{{</katex>}}
- {{<katex>}}(r|s){{</katex>}} is a RegExp
{{<katex display>}}L((r|s)) = L(r) \cup L(s){{</katex>}}
- {{<katex>}}r^*{{</katex>}} is a RegExp
{{<katex display>}}L(r^*) = L(r)^*{{</katex>}}

If {{<katex>}}A{{</katex>}} and {{<katex>}}B{{</katex>}} are RegExp, then
- {{<katex>}}A\cdot{B}  = \{xy\text{\textbar}x \in A{{</katex>}} and {{<katex>}}y \in B\}{{</katex>}}
- {{<katex>}}A\text{\textbar}B  = \{x\text{\textbar}x \in A{{</katex>}} or {{<katex>}}x \in B\}{{</katex>}}
- {{<katex>}}A^*  = \{x_1\cdot{x_2}\cdot{x_3}\cdot{...}\cdot{x_k}\text{\textbar}k\geq 0{{</katex>}} and each {{<katex>}}x_i \in A\}{{</katex>}}

are also RegExp.

It is also possible to use the following notation:

{{<katex>}}A^+ = \{x_1\cdot{x_2}\cdot{x_3}\cdot{...}\cdot{x_k}\text{\textbar}k\geq 1{{</katex>}} and each {{<katex>}}x_i \in A\}{{</katex>}}

### **Exercises (1)**

Consider the alphabet {{<katex>}}\Sigma = \{0, 1\}{{</katex>}}. Give English descriptions of the languages of the following regular expressions.
1. {{<katex>}}\emptyset{{</katex>}};
2. {{<katex>}}\emptyset{^*}{{</katex>}};
3. {{<katex>}}(0 ^ \ast 1 ^ \ast )^\ast 000 ( 0 \text{\textbar} 1 )^\ast{{</katex>}};
4. {{<katex>}}(1\text{\textbar}\epsilon)(00^\ast 1)^\ast 0^\ast{{</katex>}};

{{<expand Solutions>}}
1. An empty set;
2. A set containing only the empty string;
3. A set of strings containing 3 consecutive 0's;
4. A set of strings that do not have adjacent 1's. 
{{</expand>}}

### **Exercises (2)**

Consider the alphabet {{<katex>}}\Sigma = \{a, b\}{{</katex>}}. Build Regular Expressions for:
5. The set of strings that consist of alternating {{<katex>}}a{{</katex>}}'s and {{<katex>}}b{{</katex>}}'s;
6. The set of strings that contain an odd number of {{<katex>}}a{{</katex>}}'s;
7. The set of strings that end with {{<katex>}}b{{</katex>}} and do not contain the substring {{<katex>}}aa{{</katex>}};
8. The set of strngs in which both the number of {{<katex>}}a{{</katex>}}'s and the number of {{<katex>}}b{{</katex>}}'s are even.

{{<expand Solutions>}}
5. Answer:

{{<katex>}}(\epsilon|a)(ba)^\ast(\epsilon|b){{</katex>}}
6. Answer:

{{<katex>}}(b|ab^\ast a)^\ast ab^\ast{{</katex>}}
7. Answer:

{{<katex>}}(b|ab)^\ast (b|ab^\ast){{</katex>}}
8. Answer:

{{<katex>}}(aa|bb|(ab|ba)(aa|bb)^\ast(ab|ba))^\ast{{</katex>}}
{{</expand>}}

## **Homework on NDFSA**

A. Construct NDFSAs over alphabets {{<katex>}}\Sigma_1 = \{a, b\}{{</katex>}} and {{<katex>}}\Sigma_2 = \{0, 1\}{{</katex>}}
1. {{<katex>}} L_0 = \{x \in \Sigma_2^\ast \mid{{</katex>}} any {{<katex>}}0{{</katex>}} in {{<katex>}}x{{</katex>}} is followed by at least a {{<katex>}}1\}{{</katex>}}.

Strings examplle: {{<katex>}}010111{{</katex>}}, {{<katex>}}1111{{</katex>}}, {{<katex>}}01110111011{{</katex>}}

2. {{<katex>}} L_1 = \{x \in \Sigma_1^\ast \mid x{{</katex>}} contains the substring {{<katex>}}abbaab\}{{</katex>}}.

3. {{<katex>}} L_2 = \{x \in \Sigma_1^\ast \mid |x| \geq 2 \wedge {{</katex>}} final two symbols are the same {{<katex>}}\}{{</katex>}}.

4. {{<katex>}} L_3 = \{x \in \Sigma_2^\ast \mid x{{</katex>}} contains exactly {{<katex>}}5{{</katex>}} zeros {{<katex>}}\}{{</katex>}}.

B. Convert NDFSAs from part A to DFSAs applying the algorithm presented in the lab.