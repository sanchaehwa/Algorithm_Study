# [Platinum IV] 할 수 있다 - 1287 

[문제 링크](https://www.acmicpc.net/problem/1287) 

### 성능 요약

메모리: 37168 KB, 시간: 116 ms

### 분류

임의 정밀도 / 큰 수 연산, 사칙연산, 많은 조건 분기, 구현, 수학, 파싱, 문자열

### 제출 일자

2025년 6월 24일 22:21:27

### 문제 설명

<p>당신은 사칙연산을 할 줄 아는가? 식이 주어지면, 그 식을 계산하여서 사칙연산을 할 줄 안다는 것을 보여라.</p>

<p>이 문제에서 계산할 <strong>식</strong>은 다음의 문법으로 정의되는 <code><expr></code>이다.</p>

<pre><digit> = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
<number> = <digit> | <number> <digit>
<expr> = <number> | <expr> '+' <expr> | <expr> '-' <expr> | <expr> '*' <expr> | <expr> '/' <expr> | '(' <expr> ')'
</pre>

### 입력 

 <p>첫째 줄에 계산해야 하는 식이 주어진다. 식은 <code>()*/+-0123456789</code>의 문자로만 이루어져 있으며, 길이는 1,000자 이하이다.</p>

### 출력 

 <p>식의 계산 결과를 출력한다. 만약 식이 올바르지 않아 계산할 수 없는 경우라면 <code>ROCK</code>을 출력한다.</p>

<ul>
	<li>식을 계산할 때는 일반적인 연산의 우선순위를 따른다. 즉 괄호(<code>()</code>) 안의 식 → 곱하기(<code>*</code>)와 나누기(<code>/</code>) → 더하기(<code>+</code>)와 빼기(<code>-</code>) 순서대로 계산하며, 같은 순위의 연산이 여러 개일 경우 왼쪽부터 순서대로 계산한다.</li>
	<li>주어진 식이 위의 문법을 만족할 경우, 식을 계산하는 과정에서 나눗셈이 등장한다면 반드시 나눗셈의 결과가 정수로 나누어떨어지거나 제수(나누는 수)가 0임이 보장된다. 이때, 제수가 0인 경우가 등장한다면 식이 올바르지 않은 것으로 간주한다.</li>
</ul>

