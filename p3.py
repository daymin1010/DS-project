# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    """
    곰이 벌집을 먹으면서 자신의 크기를 키워가는 과정을 구현한 함수입니다.

    Args:
        input (list): 2차원 리스트로 이루어진 입력 데이터

    Returns:
        int: 곰이 모든 벌집을 먹는데 걸린 총 시간
    """
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]

    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    while True:
        # 가까운 벌집 찾기
        closest_honeycomb_distance = float('inf')
        closest_honeycomb_x, closest_honeycomb_y = -1, -1
        for i in range(N):
            for j in range(N):
                if forest[i][j] > 0:
                    distance = abs(bear_x - i) + abs(bear_y - j)
                    if distance < closest_honeycomb_distance:
                        closest_honeycomb_distance = distance
                        closest_honeycomb_x, closest_honeycomb_y = i, j
                    elif distance == closest_honeycomb_distance and (i < closest_honeycomb_x or (i == closest_honeycomb_x and j < closest_honeycomb_y)):
                        closest_honeycomb_x, closest_honeycomb_y = i, j

        # 가까운 벌집이 없다면 종료
        if closest_honeycomb_x == -1 and closest_honeycomb_y == -1:
            break

        # 곰이 벌집까지 이동
        while (bear_x, bear_y) != (closest_honeycomb_x, closest_honeycomb_y):
            if bear_x < closest_honeycomb_x:
                bear_x += 1
            elif bear_x > closest_honeycomb_x:
                bear_x -= 1
            elif bear_y < closest_honeycomb_y:
                bear_y += 1
            else:
                bear_y -= 1
            time += 1

        # 벌집 먹기
        forest[closest_honeycomb_x][closest_honeycomb_y] = 0
        honeycomb_count += 1

        # 곰의 크기 증가
        if honeycomb_count == bear_size:
            bear_size += 1
            honeycomb_count = 0
            time += 1 # 곰의 크기가 증가할 때마다 1초 추가

    result = time
    return result

result = problem3(input)


assert result == 14
print(result)
print("정답입니다.")

