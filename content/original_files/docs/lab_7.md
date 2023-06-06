---
title: The Hilarious Hippos
type: docs
weight: 7
BookToC: true
---

# **Lab Session #7**

# Agenda

- Turing Machine  
    - Formal definition
    - Example
    - Exercices 

------

## Turing Machine
### **Formal definition**

A Turing Machine (TM) with k-tapes is a tuple 

{{< katex display >}} T = ⟨Q, I, Γ, δ, q_0, Z_0, F⟩ {{< /katex >}} 

where:

- {{< katex >}}Q{{< /katex >}} is a finite set of states;

- {{< katex >}}I{{< /katex >}} is the input language;

- {{< katex >}}Γ{{< /katex >}} is the memory alphabet;

- {{< katex >}}δ{{< /katex >}} is the transition function;

- {{< katex >}}q_0 \in Q{{< /katex >}} is the initial state;

- {{< katex >}}Z_0 \in Γ{{< /katex >}} is the initial memory symbol;

- {{< katex >}}F \subseteq Q{{< /katex >}} is the set of final states.

------

### **Transition Function**

The transition function is defined as

{{< katex display >}}δ : (Q - F)×(I \cup \{\_\})×(Γ \cup \{\_\})^k → Q×(Γ \cup \{\_\})^k×\{R, L, S\}^{k+1}{{< /katex >}}

where elements of {{< katex >}}\{R, L, S\}{{< /katex >}} indicate “directions” of the head of the TM:

- {{< katex >}}R{{< /katex >}} : move the head one position to the right;

- {{< katex >}}L{{< /katex >}} : move the head one position to the left;

- {{< katex >}}S{{< /katex >}} : stand still.

**Remarks:**

- the transition function can be partial;

- the transition function can be partial;

- the transition function can be partial;

------

### **Moves**

Moves are based on

- one symbol read from the input tape,

- k symbols, one for each memory tape,

- state of the control device.

Actions

- Change state.

- Write a symbol replacing the one read on each memory tape.

- Move the {{< katex >}}k+1{{< /katex >}} heads.

------

### **Moves: Graphically**

![Moves Graphically](/images/lab7/MovesGraphicallyImage.PNG)

- {{< katex >}}q \in Q − F{{< /katex >}} and {{< katex >}}q′ \in Q{{< /katex >}}

- {{< katex >}}i{{< /katex >}} is the input symbol,

- {{< katex >}}A_j{{< /katex >}} is the symbol read from the {{< katex >}}jth{{< /katex >}} memory tape,

- {{< katex >}}A′_j{{< /katex >}} is the symbol replacing {{< katex >}}A_j{{< /katex >}},

- {{< katex >}}M_0{{< /katex >}} is the direction of the head of the input tape,

- {{< katex >}}M_j{{< /katex >}} is the direction of the head of the {{< katex >}}jth{{< /katex >}} memory tape.where {{< katex >}}1 \leq j \leq k{{< /katex >}}

------

### **Configuration**

A configuration (a snapshot) {{< katex >}}c{{< /katex >}} of a TM with {{< katex >}}k{{< /katex >}} memory tapes is
the following {{< katex >}}(k+2){{< /katex >}}-tuple:


{{< katex display >}}c = ⟨q, x↑y, α_1↑β_1, . . . , α_k ↑β_k ⟩{{< /katex >}}

where:
- {{< katex >}}q \in Q{{< /katex >}}
- {{< katex >}}x \in (I \cup \{\_\})^∗, y = y'.\_{{< /katex >}} with {{< katex >}}y' \in I^∗{{< /katex >}}
- {{< katex >}}α_r \in (Γ \cup \{\_\})^∗{{< /katex >}} and {{< katex >}} β'_r = β'_r.\_{{< /katex >}} with {{< katex >}}β'_r \in Γ^∗{{< /katex >}} and {{< katex >}}1 \leq r \leq k{{< /katex >}}
- {{< katex >}}\uparrow \notin I \cup Γ{{< /katex >}}

------

### **Acceptance Condition**

If {{< katex >}}T = ⟨Q, I, Γ, δ, q_0, Z_0, F⟩{{< /katex >}} is a TM and {{< katex >}}s \in I^∗, s{{< /katex >}} is accepted by {{< katex >}}T{{< /katex >}} if {{< katex >}}c_0⊢∗c_F{{< /katex >}}

where:
1. {{< katex >}}c_0{{< /katex >}}is an initial configuration defined as {{< katex >}}c_0 = ⟨q_0, ↑s, ↑Z_0, . . . , ↑Z_0⟩ {{< /katex >}} where

    - {{< katex >}}x = ϵ{{< /katex >}}
    - {{< katex >}}y = s_\_{{< /katex >}}
    - {{< katex >}}α_r = ϵ, β_r = Z_0{{< /katex >}}, for any {{< katex >}}1 \leq r \leq k.{{< /katex >}}

2. {{< katex >}}c_F{{< /katex >}} is a final configuration defined as {{< katex >}}c_F = ⟨q,s′↑y, α_1↑β_1, . . . , α_k ↑β_k ⟩{{< /katex >}} where

    - {{< katex >}}q \in F{{< /katex >}}
    - {{< katex >}}x = s^′{{< /katex >}}

{{< katex >}}L(T) = \{s \in I∗| x{{< /katex >}} is accepted by {{< katex >}}T\} {{< /katex >}}

------

### **Example**

A TM {{< katex >}}T{{< /katex >}} that recognises the language {{< katex >}}A^nB^nC^n=\{a^nb^nc^n | n > 0\}{{< /katex >}}


![Turing Machine Example](/images/lab7/TMExampleImage.PNG)


------

### **Exercices**

Build TMs that recognise the following languages:

- {{< katex >}}L_1 = \{wcw | w \in \{a, b\}^+\} {{< /katex >}}
- {{< katex >}}L_2 = \{wcw^R | w \in \{a, b\}^+\} {{< /katex >}}, where {{< katex >}}w^R{{< /katex >}} is the reversed string {{< katex >}}w{{< /katex >}}.
- {{< katex >}}L_3 = \{w | w \in \{a, b\}^∗\} {{< /katex >}}, where {{< katex >}}w{{< /katex >}} is a palindrome.
- {{< katex >}}L_4 = \{a^nb^n | n \ge 0\} \cup \{a^nb^{2n} | n \ge 0\}{{< /katex >}}

**Solutions**:

{{< expand >}}
**Solution(1)**:

<p>A TM {{< katex >}}T{{< /katex >}} that recognises the language {{< katex >}}L_1 = \{wcw | w \in \{a, b\}^+\} {{< /katex >}}</p>

![Solution 1](/images/lab7/Solution1Image.PNG)

**Solution(2)**:

<p>A TM {{< katex >}}T{{< /katex >}} that recognises the language {{< katex >}}L_2 = \{wcw^R | w \in \{a, b\}^+\} {{< /katex >}}, where {{< katex >}}w^R{{< /katex >}} is the reversed string {{< katex >}}w{{< /katex >}}.</p>

![Solution 2](/images/lab7/Solution2Image.PNG)

**Solution(3)**:

<p>A TM {{< katex >}}T{{< /katex >}} that recognises the language {{< katex >}}L_3 = \{w | w \in \{a, b\}^∗\} {{< /katex >}}, where {{< katex >}}w{{< /katex >}} is a palindrome.</p>

![Solution 3](/images/lab7/Solution3Image.PNG)


**Solution(4)**:
<p>A TM {{< katex >}}T{{< /katex >}} that recognises the language {{< katex >}}L_4 = \{a^nb^n | n \ge 0\} \cup \{a^nb^{2n} | n \ge 0\}{{< /katex >}}</p>

![Solution 4](/images/lab7/Solution4Image.PNG)

{{< /expand >}}

------

### **Homework Exercices**

Build TMs that recognise the following languages:

 - {{< katex >}}L_5 = \{(ab)^n, n \ge 0\}{{< /katex >}}
 - {{< katex >}}L_6 = \{a^nb^{2n}c{3n}, n \ge 0\}{{< /katex >}}