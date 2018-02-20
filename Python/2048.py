# 2048游戏初步实现
import random

# 初始化游戏矩阵
def init(matrix):
    random_x = random.sample(range(4), 2)
    random_y = random.sample(range(4), 2)
    matrix[random_x[0]][random_y[0]] = 2
    matrix[random_x[1]][random_y[1]] = 2
    return matrix

#打印当前矩阵
def printmatrix(matrix):
    cutline = '+' + (('-') * 4 + '+') * 4
    for i in range(4):
        print(cutline)
        for j in range (4):
            print('|',end='')
            print('{0:' '>4}'.format(matrix[i][j]), end='')
        print('|')
    print(cutline)

#移动指令
def move(command, matrix):
    if command == 'u':
        for j in range(4):
            for i in range(3):
                    for x in range(i + 1, 4):
                        if matrix[x][j] != 0 and matrix[i][j] == 0:
                            matrix[i][j] = matrix[x][j]
                            matrix[x][j] = 0
                        elif matrix[x][j] != 0 and matrix[i][j] == matrix[x][j]:
                            matrix[i][j] *= 2
                            matrix[x][j] = 0
                            break

    elif command == 'd':
        for j in range(4):
            for i in range(3, 0, -1):
                for x in range(i - 1, -1, -1):
                    if matrix[x][j] != 0 and matrix[i][j] == 0:
                        matrix[i][j] = matrix[x][j]
                        matrix[x][j] = 0
                    elif matrix[x][j] != 0 and matrix[i][j] == matrix[x][j]:
                        matrix[i][j] *= 2
                        matrix[x][j] = 0
                        break




    elif command == 'l':
        for i in range(4):
            for j in range(3):
                for x in range(j + 1, 4):
                    if matrix[i][x] != 0 and matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][x]
                        matrix[i][x] = 0
                    elif matrix[i][x] != 0 and matrix[i][j] == matrix[i][x]:
                        matrix[i][j] *= 2
                        matrix[i][x] = 0
                        break

    elif command == 'r':
        for i in range(4):
            for j in range(3, 0, -1):
                for x in range(j - 1, -1, -1):
                    if matrix[i][x] != 0 and matrix[i][j] == 0:
                        matrix[i][j] = matrix[i][x]
                        matrix[i][x] = 0
                    elif matrix[i][x] != 0 and matrix[i][j] == matrix[i][x]:
                        matrix[i][j] *= 2
                        matrix[i][x] = 0
                        break

    return matrix


def gameover(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                break
                print('Congratuation!')
                return False
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return False

    return True


def insert(matrix):
    while gameover(matrix):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if matrix[x][y] == 0:
            matrix[x][y] = 2
            return matrix
    print('Game is over!')
    return matrix


#开始游戏
def Game():
   matrix = [[0 for i in range(4)] for j in range(4)]
   matrix = init(matrix)

   printmatrix(matrix)

   while(True):
       command = input('Please input your next step(u express up, d express down, l express left, r express right): ')
       matrix = move(command, matrix)
       matrix = insert(matrix)
       printmatrix(matrix)


if __name__ == '__main__':
    Game()