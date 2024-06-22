# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    """
    주어진 리스트의 평균과 중앙값을 계산하여 반환하는 함수

    Args:
        input (list): 숫자로 이루어진 리스트

    Returns:
        list: 평균과 중앙값을 담은 리스트
    """
    # 이곳에 코드를 작성하세요.
    mean = 0
    median = 0
    result = [0,0]

    # 평균 계산
    mean = sum(input) / len(input)

    # 중앙값 계산
    sorted_input = sorted(input)
    n = len(sorted_input)
    median = sorted_input[n//2]

    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
print(int(result[0]))
print(result[1])
