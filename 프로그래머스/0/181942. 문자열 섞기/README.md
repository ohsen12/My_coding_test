# [level 0] 문자열 섞기 - 181942 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181942) 

### 성능 요약

메모리: 10.1 MB, 시간: 0.01 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 07일 16:26:36

### 문제 설명

<p>길이가 같은 두 문자열 <code>str1</code>과 <code>str2</code>가 주어집니다.</p>

<p>두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.</p>

- hint
  - join 함수는 주로 문자열을 요소로하는 반복가능한객체(리스트, 튜플 등)을 결합하는 데 사용된다. '구분자'.join(반복가능한객체)
  - 리스트 컴프리헨션 [표현식 for 항목 in 반복가능한객체 조건식]의 구조에서 대괄호[]를 사용하면 결과를 리스트로 반환하고, 사용하지 않으면 결과를 바로 문자열로 결합할 수 있다.
  - zip 함수는 반복가능한객체(이터러블)의 요소들을 병렬로 묶어주는 기능을 한다. zip 함수를 사용하면 여러 이터러블을 동시에 순회할 수 있으며, 각 이터러블의 **동일한 인덱스** 위치에 있는 요소들을 튜플로 묶어 반환한다. (여기서는 zip으로 생성된 각 튜플 (a, b)에 대해 리스트컴프리헨션에서 표현식 a + b를 수행하여 새로운 문자열을 생성했다.

 
<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>str1</code>의 길이 = <code>str2</code>의 길이 ≤ 10

<ul>
<li><code>str1</code>과 <code>str2</code>는 알파벳 소문자로 이루어진 문자열입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>str1</th>
<th>str2</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>"aaaaa"</td>
<td>"bbbbb"</td>
<td>"ababababab"</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
