
# Python Quick Reference

## 이번 3차시에서 꼭 기억할 기호

### `=`
값을 저장합니다.

```python
name = "민서"
```

### `()`
함수나 명령을 실행합니다.

```python
print(name)
len(name)
```

### `[]`
목록을 만들거나, 순서로 값을 꺼낼 때 씁니다.

```python
fruits = ["사과", "바나나", "포도"]
print(fruits[0])
```

### `{}`
이름표와 값을 묶을 때 씁니다. 이를 딕셔너리라고 부릅니다.

```python
student = {"name": "민지", "grade": 1}
print(student["name"])
```

### `:`
아래에 묶인 코드가 시작된다는 뜻입니다.

```python
for item in items:
    print(item)
```

### 들여쓰기
같은 블록이라는 뜻입니다.

```python
if score >= 80:
    print("통과")
```

### `.`
어떤 도구의 기능을 꺼내 쓸 때 보입니다.

```python
import random
random.choice(["A", "B", "C"])
```

## 자주 나오는 문법 읽기

### 출력
```python
print("안녕하세요")
```

### 변수
```python
age = 17
```

### 리스트
```python
scores = [70, 80, 90]
```

### 반복문
```python
for score in scores:
    print(score)
```

### 조건문
```python
if score >= 80:
    print("좋아요")
```

## 자주 보는 오류

### `NameError`
이름이 아직 만들어지지 않았을 때 자주 나옵니다.  
보통 셀 실행 순서가 꼬였거나 변수 이름을 다르게 쓴 경우입니다.

### `SyntaxError`
괄호, 따옴표, 콜론 `:` 등을 잘못 쓴 경우가 많습니다.

### `IndentationError`
들여쓰기가 맞지 않을 때 생깁니다.

## AI에게 코드 설명을 요청할 때 쓸 문장

- 이 코드의 각 줄을 쉬운 말로 설명해줘.
- 변수 값이 어떻게 바뀌는지 표로 보여줘.
- 이 코드의 출력 결과를 먼저 예측하고 이유를 설명해줘.
- 리스트, 반복문, 조건문이 어디인지 표시해줘.
- 한 줄만 바꿔서 결과가 달라지게 해줘.
