# [level 0] 배열의 유사도 - 120903 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/120903) 

### 성능 요약

메모리: 9.93 MB, 시간: 0.00 ms

### 구분

코딩테스트 연습 > 코딩테스트 입문

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 11일 09:43:20

### 문제 설명

<p>두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 <code>s1</code>과 <code>s2</code>가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 길이 ≤ 100</li>
<li>1 ≤ <code>s1</code>, <code>s2</code>의 원소의 길이 ≤ 10</li>
<li><code>s1</code>과 <code>s2</code>의 원소는 알파벳 소문자로만 이루어져 있습니다</li>
<li><code>s1</code>과 <code>s2</code>는 각각 중복된 원소를 갖지 않습니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>s1</th>
<th>s2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>["a", "b", "c"]</td>
<td>["com", "b", "d", "p", "c"]</td>
<td>2</td>
</tr>
<tr>
<td>["n", "omg"]</td>
<td>["m", "dot"]</td>
<td>0</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>"b"와 "c"가 같으므로 2를 return합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>같은 원소가 없으므로 0을 return합니다.</li>
</ul>

---

### 다른 사람 풀이⭐️
- set을 사용한 방법이 많이 보인다.
  ```python
  def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return len(s1.intersection(s2))
  ```
  - 교집합을 사용하기 위해 자료형을 셋으로 변경해준 후 **(셋 자료형은 집합연산을 지원한다.)** 교집합의 길이를 구한다.
  ```python
  def solution(s1, s2):
    return len(set(s1)&set(s2))
  ```
  - 셋 자료형에서 교집합을 구할 때 s1.intersection(s2) 방법 대신 & 연산자를 사용할 수도 있다
 
---

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
