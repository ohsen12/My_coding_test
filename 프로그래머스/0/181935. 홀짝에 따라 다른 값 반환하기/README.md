# [level 0] 홀짝에 따라 다른 값 반환하기 - 181935 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/181935) 

### 성능 요약

메모리: 9.98 MB, 시간: 0.02 ms

### 구분

코딩테스트 연습 > 코딩 기초 트레이닝

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 12월 08일 13:30:26

### 문제 설명

<p>양의 정수 <code>n</code>이 매개변수로 주어질 때, <code>n</code>이 홀수라면 <code>n</code> 이하의 홀수인 모든 양의 정수의 합을 return 하고 <code>n</code>이 짝수라면 <code>n</code> 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>1 ≤ <code>n</code> ≤ 100</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>7</td>
<td>16</td>
</tr>
<tr>
<td>10</td>
<td>220</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p>입출력 예 #1</p>

<ul>
<li>예제 1번의 <code>n</code>은 7로 홀수입니다. 7 이하의 모든 양의 홀수는 1, 3, 5, 7이고 이들의 합인 1 + 3 + 5 + 7 = 16을 return 합니다.</li>
</ul>

<p>입출력 예 #2</p>

<ul>
<li>예제 2번의 <code>n</code>은 10으로 짝수입니다. 10 이하의 모든 양의 짝수는 2, 4, 6, 8, 10이고 이들의 제곱의 합인 2<sup>2</sup> + 4<sup>2</sup> + 6<sup>2</sup> + 8<sup>2</sup> + 10<sup>2</sup> = 4 + 16 + 36 + 64 + 100 = 220을 return 합니다.</li>
</ul>

---

### 다른 사람 풀이
- 이거 말고도 리스트 컴프리헨션으로 한 줄로 쓴 코드들이 많았는데, 음.. 연산과정을 한 줄로 줄여버리니 가독성이 떨어져서, 가독성 좋고 깔끔한 풀이를 가져왔다.
  ```python
  def solution(n):
    answer = 0
    if n%2:
        for i in range(1,n+1,2):
            answer += i
    else:
        for i in range(2,n+1,2):
            answer += i**2
    return answer
  ```
  - 나는 for문 안에서 숫자시퀀스 내에서 홀짝 구한다고 또 if문을 사용했는데 그냥 애초에 숫자시퀀스를 만들 때 시작점을 정하고, 간격을 2로 띄워주면 되는 것이었다!


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges
