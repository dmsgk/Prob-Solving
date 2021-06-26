# [Swift] Code Snippets for PS

코테에 자주 사용되는 구문

## 반복문

### for문

- index로 for문 돌리기: `arr.indices`

  ```swift
  var nums = [1,2,3,4]
  
  for index in nums.indices {
      print("(index: \(index) num: \(nums[index]))")    
    /* 
    (index: 0 num: 1) 
    (index: 1 num: 2)
    (index: 2 num: 3) 
    (index: 3 num: 4) 
    */
  }
  ```

- 배열의 인덱스와 값 함께 조회하기 : `enumerated()`

  ```swift
  let arr = ["s","w","i","f","t"]
  
  for (idx, val) in arr.enumerated() {
    print("index: \(idx), value: \(val)")
  }
  
  /*
  index: 0, value: s
  index: 1, value: w
  index: 2, value: i
  index: 3, value: f
  index: 4, value: t
  */
  ```

- 
- 

## 배열

- #### 정렬

  ```swift
  var arr = [3,8,4,7,9,2,1]
  
  // 원본 정렬하지 않고 정렬한 값 따로 저장: arr.sorted()
  var sortedArr = arr.sorted()
  
  //원본 정렬: arr.sort()
  arr.sort()  // 오름차순(기본값) // [1, 2, 3, 4, 7, 8, 9]
  arr.sort(by: >) // 내림차순 // [9, 8, 7, 4, 3, 2, 1]
  ```

- 슬라이싱

  ```swift
  var arr = [1, 5, 2, 6, 3, 7, 4]
  type(of: arr[2...4]) //ArraySlice<Int>.Type
  
  // 2번째부터 5번째까지 잘라 Array 타입으로 변환하여 사용
  var slicedArr = Array(arr[2...5])  //[2, 6, 3, 7]
  print(slicedArr[0]) // 2
  ```

  

- ㅇㅇ

## 문자열

- #### 특정 문자로 분리 : `split(separator: "해당문자")`

- #### 문자열 배열 합치기: `joined(separator: "해당문자")`

- #### 대소문자 변경

  - 첫 번째 문자만 대문자로 변경: `str.capitalized`
  - 전체 대문자로 변경: `str.uppercased()`
  - 전체 소문자로 변경: `str.lowercased()`

- #### 특정 문자열이 포함됐는지 true/false 반환하는 메소드 : `contains()`

  ```swift
  var str = "apple"
  str.contains("a")  // true
  str.contains("ap")  // true
  str.contains("zzz")  // false
  ```

- #### String 인덱스 처리

  ```swift
  var str = "abcdef"
  
  // 문자열 원소 접근
  //str[0] // 직접 접근 불가. String 인덱스로 접근해야
  str[str.startIndex] // "a"
  
  // 3번째 문자 가져오기
  let index = str.index(str.startIndex, offsetBy: 3 - 1)
  str[index] // "c"
  
  // 일정 범위의 문자열만 가져오기
  let sub = str[str.startIndex...index] // "abc"
  
  // 특정 원소의 인덱스
  str.firstIndex(of: "c")
  ```

- dd



## 딕셔너리

- 파이썬과 다르게, 대괄호 `[ ]`를 이용한다. 



## 고차함수

`map`

`filter`

`reduce`

