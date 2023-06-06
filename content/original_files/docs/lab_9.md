---
title: The Snorting Narwhals
type: docs
weight: 9
BookToC: true
---
# **Lab Session #9**

# Agenda

- Non-determinism:  
1) PDA
2) TM  

------

## Non-deterministic Pushdown Automaton (NDADA)

### **Definition: NDPDA**  

A NDPDA is a tuple {{< katex >}}<Q,I,Γ,δ,q0,Z0,F>{{< /katex >}}, where {{< katex >}}Q,I,Γ,δ,q0,Z0,F{{< /katex >}} are defined as in (D)PDA and the transition function is defined as

{{< katex >}}δ:Q×(I∪{eps})×Γ→P_F(Q×Γ^∗){{< /katex >}}


where {{< katex >}}P_F{{< /katex >}} indicates finite subsets.

------

### **Exercices**  

Build NDPDAs that recognise the following languages:
1) {{< katex >}}L1=\{ww^R|w∈{a,b}^+\}{{< /katex >}} where {{< katex>}}w^R{{< /katex >}} is the reversed string {{< katex >}}w{{< /katex>}}.
2) {{< katex >}}L2=\{a^{n}b^{n}|n≥1\}∪\{a^{n}b^{2n}|n≥1\}{{< /katex >}}.
3) {{< katex >}} L3=\{a^{i}b^{j}c^{k}d^{l}|(i=k{{< /katex >}} **or** {{< katex>}}j=l),i≥1,j≥1\} {{< /katex >}}.

{{< expand Solutions>}}

### (1)

{{< katex >}}L1=\{ww^R|w∈{a,b}^+\}{{< /katex >}} where {{< katex>}}w^R{{< /katex >}} is the reversed string {{< katex >}}w{{< /katex>}}.

NDPDA that recognises this language:

![P1L1](/images/lab9/P1L1.PNG)

### (2)

{{< katex >}}L2=\{a^{n}b^{n}|n≥1\}∪\{a^{n}b^{2n}|n≥1\}{{< /katex >}}.

PDA that recognises this language:

![P1L21](/images/lab9/P1L1.PNG)

Another valid PDA that recognises this language:

![P1L22](/images/lab9/P1L1.PNG)

NDPDA that recognises this language:

![P1L23](/images/lab9/P1L1.PNG)

### (3)

{{< katex >}} L3=\{a^{i}b^{j}c^{k}d^{l}|(i=k{{< /katex >}} **or** {{< katex>}}j=l),i≥1,j≥1\} {{< /katex >}}.

NDPDA that recognises this language:

![P1L3](/images/lab9/P1L1.PNG)

{{< /expand >}}



------

## Non-deterministic Turing Machine (NDTM)

To define a NDTM, we need to change the transition function (all the other elements reamin as in a (D)TM):

### **Definition: NDTM**  

A NDTM is a tuple {{< katex >}}<Q,I,Γ,δ,q0,Z0,F>{{< /katex >}}, where {{< katex >}}Q,I,Γ,δ,q0,Z0,F{{< /katex>}} are defined as in (D)TM and the transition function is defined as

{{< katex >}}δ:(Q−F)×(I∪\{\_\})×(Γ∪\{\_\})^k→P(Q×(Γ∪\{\_\})^k×\{R,L,S\}^{k+1}) {{< /katex>}}

**Acceptance:** Among the various possible runs (with the same input) of the NDTM, it is sufficient that one of the run (instances) reaches the final state. The input string may not be fully consumed to be considered as 'accepted'.

------

### **Exercices**

Build NDTMs that recognise the following languages:
1) {{< katex >}}L1=\{ww|w∈\{a,b\}^+\}{{< /katex >}}.
2) {{< katex >}}L2=\{ww^R|w∈\{a,b\}^+\}{{< /katex >}}, where {{< katex >}}w^R{{< /katex >}} is the reversed string {{< katex >}}w{{< /katex >}}.

------


{{< expand Solutions>}}

### (1)

{{< katex >}}L1=\{ww|w∈\{a,b\}^+\}{{< /katex >}}.

NDTM that recognises this language:

![P1L1](/images/lab9/P2L1.PNG)

### (2)
{{< katex >}}L2=\{ww^R|w∈\{a,b\}^+\}{{< /katex >}}, where {{< katex >}}w^R{{< /katex >}} is the reversed string {{< katex >}}w{{< /katex >}}.

NDTM that recognises this language:

![P2L2](/images/lab9/P1L1.PNG)

{{< /expand>}}