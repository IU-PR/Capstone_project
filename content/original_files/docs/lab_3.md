---
title: The Quirky Quokkas
type: docs
weight: 3
BookToC: true
# markup: 'mmark'
---
# **Lab Session #3**
# **Agenda**

- Finite State Transducers
- Exercises on Finite State Transducer

---

## **Finite State Transducer**

A finite-state transducer (FST) is a finite-state machine with two memory tapes, following the terminology for Turing machines: an input tape and an output tape. This contrasts with an ordinary finite-state automaton, which has a single tape. An FST is a type of finite-state automaton (FSA) that maps between two sets of symbols. An FST is more general than an FSA.

An FSA defines a formal language by defining a set of accepted strings, while an FST defines relations between sets of strings. An FST will read a set of strings on the input tape and generates a set of relations on the output tape. An FST can be thought of as a translator or relater between strings in a set. In morphological parsing, an example would be inputting a string of letters into the FST, the FST would then output a string of morphemes.

FSTs are used in a variety of applications, including:

Natural language processing: FSTs are used in natural language processing for tasks such as morphological analysis, part-of-speech tagging, and named entity recognition.
Speech recognition: FSTs are used in speech recognition for tasks such as acoustic modeling and decoding.
Machine translation: FSTs are used in machine translation for tasks such as lexical translation and grammar conversion.
Compilers: FSTs are used in compilers for tasks such as lexical analysis and syntax analysis.
FSTs are a powerful tool for modeling and manipulating strings. They are used in a variety of applications, including natural language processing, speech recognition, machine translation, and compilers.


### **Finite State Transducer formula**

A finite state transducer (FST) is a tuple {{< katex >}} \langle {{< /katex >}} {{< katex >}}Q{{</katex>}}, {{< katex >}}I{{</katex>}}, {{< katex >}}\delta{{</katex>}}, {{< katex >}}q_0{{</katex>}}, {{< katex >}}F{{</katex>}}, {{< katex >}}O{{</katex>}}, {{< katex >}}\eta{{</katex>}} {{< katex >}}\rangle{{< /katex >}}, where:

- {{< katex >}}Q{{</katex>}} is a finite set of states. Each state represents a possible configuration of the FST.
- {{< katex >}}I{{</katex>}} is a finite input alphabet. Each symbol in the input alphabet represents a possible input that the FST can read.
- {{< katex >}}\delta{{</katex>}} is the transition function. It maps a state and an input symbol to a new state.
- {{< katex >}}q_0{{</katex>}} is the initial state. This is the state that the FST starts in when it is first activated.
- {{< katex >}}F{{</katex>}} is the set of final states. A state is a final state if it represents a valid output.
- {{< katex >}}O{{</katex>}} is the output alphabet. Each symbol in the output alphabet represents a possible output that the FST can produce.
- {{< katex >}}\eta{{</katex>}} is the output function. It maps a state and an input symbol to a sequence of output symbols.
The rule that all of these variables follow is that they must be finite. This means that there can only be a finite number of states, input symbols, final states, and output symbols. This is because an FST is a finite-state machine, which is a machine that can only be in a finite number of states at any given time.

**Remark**
- the condition for acceptance remains the same as in acceptors
- the translation is performed only on accepted strings

---

### **Example**
Build a complete FST accepting the following language
 over the alphabet {{< katex >}} A = \{0,1 \}{{< /katex >}}. <br>
    {{<katex display>}} L = \{ x \isin A^* |  \textit { the number of }  0's \textit{ is even}  \} {{</katex>}} 

The FST outputs the string obtained by removing every odd occurrence of 0 and doubling every occurrence of 1. Examples of inputs recognised by L and their respective outputs:

- Input: {{<katex>}}010010{{</katex>}}, Output:{{<katex>}} 110110{{</katex>}}
- Input: {{<katex>}}00{{</katex>}}, Output:{{<katex>}}0{{</katex>}}
- Input: {{<katex>}}000100011{{</katex>}}, Output: {{<katex>}}011001111{{</katex>}}

{{<katex display>}} L = \{ x \isin A^* |  \textit { the number of }  0's \textit{ is even}  \} {{</katex>}} 

{{< expand Solution >}}

![placeholdertext](/images/lab3/1.png)

{{< /expand >}}

---

### **Exercises**

Build complete FSAs over the languages given below:
1. {{<katex>}} A = \{w,t,a,l,k,e,d\} {{</katex>}}that accepts only the verb ”walked” or ”talked”. The FST will translate the input verb to present form ex: walked to walk.
{{< expand Solution >}}
![Solution 1](/images/lab3/2.png)
{{< /expand >}}
1. {{<katex>}}A = \{a, b\} {{</katex>}}that accepts only strings ending with the letter b. The FST will translate the input string where every second symbol a in the input is erased.
{{< expand Solution >}}
![Solution 2](/images/lab3/3.png)
{{< /expand >}}
1. {{<katex>}}A = \{0, 1\} {{</katex>}} that accepts strings that are binary representation of integers divisible by 2. The FST will translate the input string into result of division by 2.
{{< expand Solution >}}
![Solution 3](/images/lab3/4.png)
{{< /expand >}}
1. {{<katex>}}A = \{0, 1\} {{</katex>}}that accepts strings that are binary representation of integers divisible by 3. The FST will translate the input string into result of division by 3.
{{< expand Solution >}}
![Solution 4](/images/lab3/5.png)
{{< /expand >}}

---

## **Operations on FSA**

### **Intersection**
---
#### **Intersection Formula**

Suppose {{< katex >}} M_1 = \lparen Q_1, A, \delta_1, q^1_0, F_1 \rparen {{</katex>}} and {{<katex>}} M_2 = \lparen Q_2, A, \delta_2, q^2_0, F_2 \rparen{{</katex>}} are finite state automata accepting {{<katex>}} L_1 {{</katex>}} and {{<katex>}}L_2 
{{</katex>}}, respectively. Let{{<katex>}} M {{</katex>}} be the complete {{<katex>}} \text {FSA M} = \lparen Q,A,\delta,q_0,F \rparen {{</katex>}}, \
where:

{{<katex display>}} Q = Q_1 \times Q_2 {{</katex>}}
{{<katex display>}} q_0 = \lparen q^1_0, q^2_0 \rparen 
{{</katex>}}
the transition function {{<katex>}} \delta{{</katex>}} is defined by the formula
{{<katex display>}} \delta \lparen \lparen q, p \rparen, a \rparen = \lparen \delta_1 \lparen q, a \rparen , \delta_2 \lparen p, a \rparen \rparen {{</katex>}}
for every {{<katex>}} q \isin Q_1 {{</katex>}}, every {{<katex>}} p \isin Q_2 {{</katex>}}, and every {{<katex>}} a \isin A {{</katex>}}. And the set of the final states is defined as:
{{<katex display>}} F= \lbrace \lparen q,p \rparen | q \isin F_1 \land p \isin F_2 \rbrace {{</katex>}}
{{<katex>}} M {{</katex>}} accepts the language {{<katex>}} L_1 \cap L_2 {{</katex>}}.

---

#### **Intersection Example**

Let {{<katex>}} M_1{{</katex>}} be a complete {{<katex>}}\text{FSA}{{</katex>}} defined as

{{<katex display>}} M_1 = \lang \lbrace q_0, q_1 \rbrace, \lbrace a \rbrace, \lbrace \lparen \lparen q_0,a \rparen, q_1 \rparen, \lparen \lparen q_1,a \rparen, q_0 \rparen \rbrace, q_0, \lbrace q_1 \rbrace \rang{{</katex>}}

- {{<katex>}} \lbrace q_0, q_1 \rbrace \rarr{{</katex>}} set of states; 
  
- {{<katex>}} \lbrace a \rbrace \rarr {{</katex>}} input alphabet;
- {{<katex>}} \lbrace \lparen \lparen q_0,a \rparen, q_1 \rparen, \lparen q_1,a \rparen, q_0 \rparen \rbrace \rarr {{</katex>}} partial transition function;
- {{<katex>}}  q_0 \rarr {{</katex>}} initial state;
- {{<katex>}} \lbrace q_1 \rbrace \rarr {{</katex>}} set of final states;

Let {{<katex>}} M_2{{</katex>}} be a complete {{<katex>}}\text{FSA}{{</katex>}} defined as

{{<katex display>}} M_2 = \lang \lbrace p_0 \rbrace, \lbrace a \rbrace, \lbrace \lparen \lparen p_0,a \rparen, p_0 \rparen \rbrace, p_0, \lbrace p_0 \rbrace \rang{{</katex>}}

Then :

{{<katex display>}} \lparen M_1 \cap M_2 \rparen = \lang \lbrace \lparen q_0, p_0 \rparen , \lparen q_1, p_0 \rparen \rbrace, \lbrace a \rbrace, \lbrace \lparen \lparen \lparen q_0, p_0 \rparen, a \rparen , \lparen q_1, p_0 \rparen \rparen , {{</katex>}}
{{<katex display>}}\lparen \lparen \lparen q_1, p_0 \rparen ,a \rparen , \lparen q_0,p_0 \rparen \rparen \rbrace , \lparen q_0, p_0 \rparen ,\lbrace \lparen q_1, p_0 \rparen \rbrace \rang .{{</katex>}}

---

#### **Intersection Graph**
![Intersection Graph](/images/lab3/6.png)

---

### **Union**

Suppose {{< katex >}} M_1 = \lparen Q_1, A, \delta_1, q^1_0, F_1 \rparen {{</katex>}} and {{<katex>}} M_2 = \lparen Q_2, A, \delta_2, q^2_0, F_2 \rparen{{</katex>}} are finite state automata accepting {{<katex>}} L_1 {{</katex>}} and {{<katex>}}L_2 
{{</katex>}}, respectively. Let{{<katex>}} M {{</katex>}} be the complete {{<katex>}} \text {FSA M} = \lparen Q,A,\delta,q_0,F \rparen {{</katex>}},  
where:

{{<katex display>}} Q = Q_1 \times Q_2 {{</katex>}}
{{<katex display>}} q_0 = \lparen q^1_0, q^2_0 \rparen 
{{</katex>}}
the transition function {{<katex>}} \delta{{</katex>}} is defined by the formula
{{<katex display>}} \delta \lparen \lparen q, p \rparen, a \rparen = \lparen \delta_1 \lparen q, a \rparen , \delta_2 \lparen p, a \rparen \rparen {{</katex>}}
for every {{<katex>}} q \isin Q_1 {{</katex>}}, every {{<katex>}} p \isin Q_2 {{</katex>}}, and every {{<katex>}} a \isin A {{</katex>}}. And the set of the final states is defined as:
{{<katex display>}} F= \lbrace \lparen q,p \rparen | q \isin F_1 \lor p \isin F_2 \rbrace {{</katex>}}
{{<katex>}} M {{</katex>}} accepts the language {{<katex>}} L_1 \cup L_2 {{</katex>}}.

---

### **Difference**

Suppose {{< katex >}} M_1 = \lparen Q_1, A, \delta_1, q^1_0, F_1 \rparen {{</katex>}} and {{<katex>}} M_2 = \lparen Q_2, A, \delta_2, q^2_0, F_2 \rparen{{</katex>}} are finite state automata accepting {{<katex>}} L_1 {{</katex>}} and {{<katex>}}L_2 
{{</katex>}}, respectively. Let{{<katex>}} M {{</katex>}} be the complete {{<katex>}} \text {FSA M} = \lparen Q,A,\delta,q_0,F \rparen {{</katex>}},  
where:

{{<katex display>}} Q = Q_1 \times Q_2 {{</katex>}}
{{<katex display>}} q_0 = \lparen q^1_0, q^2_0 \rparen 
{{</katex>}}
the transition function {{<katex>}} \delta{{</katex>}} is defined by the formula
{{<katex display>}} \delta \lparen \lparen q, p \rparen, a \rparen = \lparen \delta_1 \lparen q, a \rparen , \delta_2 \lparen p, a \rparen \rparen {{</katex>}}
for every {{<katex>}} q \isin Q_1 {{</katex>}}, every {{<katex>}} p \isin Q_2 {{</katex>}}, and every {{<katex>}} a \isin A {{</katex>}}. And the set of the final states is defined as:
{{<katex display>}} F= \lbrace \lparen q,p \rparen | q \isin F_1 \land p \notin F_2 \rbrace {{</katex>}}
{{<katex>}} M {{</katex>}} accepts the language {{<katex>}} L_1 \setminus L_2 {{</katex>}}.

---

### **Complement**

Suppose {{<katex>}} M = \lparen Q, A, \delta, q_0, F \rparen {{</katex>}} is a complete finite state automaton accepting {{<katex>}} L {{</katex>}}. A complement {{<katex>}} M^c{{</katex>}} is a complete {{<katex>}} \text {FSA} {{</katex>}} {{<katex>}} M^c = \lparen Q,A,\delta,q_0,F^c \rparen {{</katex>}}, where:

{{<katex display>}} F^c = Q \setminus F {{</katex>}}

{{<katex>}} M^c {{</katex>}}accepts the language {{<katex>}}L{{</katex>}}.

---

### **Summary of Operations on FSA**

Suppose {{< katex >}} M_1 = \lparen Q_1, A, \delta_1, q^1_0, F_1 \rparen {{</katex>}} and {{<katex>}} M_2 = \lparen Q_2, A, \delta_2, q^2_0, F_2 \rparen{{</katex>}} are finite state automata accepting {{<katex>}} L_1 {{</katex>}} and {{<katex>}}L_2 
{{</katex>}}, respectively. Let{{<katex>}} M {{</katex>}} be the complete {{<katex>}} \text {FSA M} = \lparen Q,A,\delta,q_0,F \rparen {{</katex>}},  
where:

{{<katex display>}} Q = Q_1 \times Q_2 {{</katex>}}
{{<katex display>}} q_0 = \lparen q^1_0, q^2_0 \rparen 
{{</katex>}}
{{<katex display>}} \delta \lparen \lparen q, p \rparen, a \rparen = \lparen \delta_1 \lparen q, a \rparen , \delta_2 \lparen p, a \rparen \rparen {{</katex>}}

The set of final states will be defined as

{{<tabs "Sets">}}
{{<tab "The Final State Of Difference">}}

{{<katex>}} L_1 \setminus L_2 : F= \lbrace \lparen q,p \rparen | q \isin F_1 \land p \notin F_2 \rbrace {{</katex>}}.
{{</tab>}}
{{<tab "The Final State Of Union">}}

{{<katex>}} L_1 \cup L_2 : F= \lbrace \lparen q,p \rparen | q \isin F_1 \lor p \isin F_2 \rbrace {{</katex>}}.
{{</tab>}}
{{<tab "The Final State Of Intersection">}}

{{<katex>}} L_1 \cap L_2 :  F= \lbrace \lparen q,p \rparen | q \isin F_1 \land p \isin F_2 \rbrace {{</katex>}}.
{{</tab>}}
{{</tabs>}}

---

## **Exercises**

### **Part 1**

Let {{<katex>}} A = \lbrace 0, 1 \rbrace {{</katex>}} be the alphabet.
1. Build a complete {{<katex>}} \text { FSA } M_1 {{</katex>}} that recognises the language:
{{<katex display>}} L_1= \lbrace x \isin A^* | x  \text { has an even number of  }  1's \rbrace {{</katex>}}
{{< expand Solution >}}
![Solution 1](/images/lab3/7.png)
{{< /expand >}}

2. Build a complete {{<katex>}} \text { FSA } M_2 {{</katex>}} that recognises the language:
{{<katex display>}} L_2= \lbrace x \isin A^* | x  \text { has an odd number of  }  0's \rbrace {{</katex>}}
{{< expand Solution >}}
![Solution 2](/images/lab3/8.png)
{{< /expand >}}

3. Build a complete {{<katex>}} \text { FSA } {{</katex>}} that accepts when either {{<katex>}} M_1 {{</katex>}} or {{<katex>}} M_2 {{</katex>}} accepts.
{{< expand Solution >}}
![Solution 3](/images/lab3/9.png)
{{< /expand >}}
   
4. Build a complete {{<katex>}} \text { FSA } {{</katex>}} that accepts when both {{<katex>}} M_1 {{</katex>}} and {{<katex>}} M_2 {{</katex>}} accept.
{{< expand Solution >}}
![Solution 4](/images/lab3/10.png)
{{< /expand >}}

5. Build a complete {{<katex>}} \text { FSA } {{</katex>}} that accepts when {{<katex>}} M_1 {{</katex>}} accepts and  {{<katex>}} M_2 {{</katex>}} rejects.
{{< expand Solution >}}
![Solution 5](/images/lab3/11.png)
{{< /expand >}}

1. Build a complement for {{<katex>}} M_1 {{</katex>}}.
{{< expand Solution >}}
![Solution 6](/images/lab3/12.png)
{{< /expand >}}

---

### **Part 2**

Construct a complement for the following {{<katex>}} \text {FSA} {{</katex>}}

![placeholdertext](/images/lab3/13.png)

{{< expand Solution >}}
First, we have to complete the FSA

![Solution](/images/lab3/14.png)

The complement:

![Solution](/images/lab3/15.png) 
{{< /expand >}}

---

### **Part 3**

Let {{<katex>}} A = \lbrace 0, 1 \rbrace {{</katex>}} be the alphabet.

1. Build a complete {{<katex>}} \text { FSA } M_a {{</katex>}} that recognises the language:
{{<katex display>}} L_a= \lbrace x \isin A^* | x  \text { is the binary representation of an integer, and it is divisible by  }  2 \rbrace {{</katex>}}
{{< expand Solution >}}
Graphical Representation - State Transition Diagram

![Solution 1](/images/lab3/16.png)

Graphical Representation — State Transition Table

![Solution 1](/images/lab3/17.png)

{{< /expand >}}

2. Build a complete {{<katex>}} \text { FSA } M_b {{</katex>}} that recognises the language:
{{<katex display>}} L_b= \lbrace x \isin A^* | x  \text { is the binary representation of an integer, and it is divisible by  }  3 \rbrace {{</katex>}}
{{< expand Solution >}}
Graphical Representation - State Transition Diagram

![Solution 2](/images/lab3/18.png) \

Graphical Representation — State Transition Table

![Solution 2](/images/lab3/19.png)

{{< /expand >}}

3. Build a complete {{<katex>}} \text { FSA } {{</katex>}} that accepts when both {{<katex>}} M_a {{</katex>}} and {{<katex>}} M_b {{</katex>}} accept.
{{< expand Solution >}}
![Solution 3](/images/lab3/20.png)
{{< /expand >}}

1. Build a complete {{<katex>}} \text { FSA } {{</katex>}} that accepts when either {{<katex>}} M_a {{</katex>}} or {{<katex>}} M_b {{</katex>}} accepts.
{{< expand Solution >}}
![Solution 4](/images/lab3/21.png)
{{< /expand >}}

1. Build a complete {{<katex>}} \text { FSA } {{</katex>}} that accepts when {{<katex>}} M_a {{</katex>}} accepts and {{<katex>}} M_b {{</katex>}} rejects.
{{< expand Solution >}}
![Solution 5](/images/lab3/22.png)
{{< /expand >}}