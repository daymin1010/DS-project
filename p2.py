# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    """
    올바르지 않은 괄호열이 주어졌을 때, 올바른 괄호열로 복원하기 위해 앞과 뒤에 붙여야 할 괄호의 최소 개수를 구합니다.

    Args:
        input (str): 올바르지 않은 괄호열

    Returns:
        int: 앞과 뒤에 붙여야 할 괄호의 최소 개수
    """
    stack = []
    left_count = 0
    right_count = 0

    for char in input:
        print(char)
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                right_count += 1

    left_count = len(stack)
    result = left_count + right_count
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
print(result)
