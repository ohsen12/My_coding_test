# [level 0] 조건 문자열 - 181934 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181934) 

### 성능 요약

메모리: 10.2 MB, 시간: 0.03 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 08일 14:10:55

### 문제 설명

<p>문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.  </p>

<ul>
<li>두 수가 <code>n</code>과 <code>m</code>이라면

<ul>
<li>"&gt;", "=" : <code>n</code> &gt;= <code>m</code></li>
<li>"&lt;", "=" : <code>n</code> &lt;= <code>m</code></li>
<li>"&gt;", "!" : <code>n</code> &gt; <code>m</code></li>
<li>"&lt;", "!" : <code>n</code> &lt; <code>m</code> </li>
</ul></li>
</ul>

<p>두 문자열 <code>ineq</code>와 <code>eq</code>가 주어집니다. <code>ineq</code>는 "&lt;"와 "&gt;"중 하나고, <code>eq</code>는 "="와 "!"중 하나입니다. 그리고 두 정수 <code>n</code>과 <code>m</code>이 주어질 때, <code>n</code>과 <code>m</code>이 <code>ineq</code>와 <code>eq</code>의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한 사항</h5>

<ul>
<li>1 ≤ <code>n</code>, <code>m</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>ineq</th>
<th>eq</th>
<th>n</th>
<th>m</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"&lt;"</td>
<td>"="</td>
<td>20</td>
<td>50</td>
<td>1</td>
</tr>
<tr>
<td>"&gt;"</td>
<td>"!"</td>
<td>41</td>
<td>78</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>20 &lt;= 50은 참이기 때문에 1을 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>41 &gt; 78은 거짓이기 때문에 0을 return합니다.</li>
</ul>

<hr>

<p>※ 2023.05.31 테스트 케이스가 수정되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.</p>

---

### 다른 사람 풀이
- 내가 푼 코드 업그레이드 버전이다.
  ```python
  def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    return int(eval(f'{n}{ineq}{eq}{m}'))
  ```
  - eq를 빈 문자열로 설정해주면 f'{n}{ineq}{eq}{m}' 여기서도 없는 걸로 인식되기 때문에 코드를 줄일 수 있는 좋은 방법인 것 같다.
  - 그나저나 eval 함수는 신뢰할 수 없는 사용자 입력을 eval에 전달하면 악의적인 코드를 실행할 수 있기 때문에 현업에서는 사용을 지양한다고 한다.

  
> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
