def solution(sticker):

    val1 = 0
    val2 = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(sticker)):

        if i % 2:

            val1 += sticker[i]

        else:

            val2 += sticker[i]

    if val1 > val2:

        return  val1

    else:

        return val2



num = [14, 6, 5, 11, 3, 9, 2, 10]


print(sum(num[0::2]))
print(sum(num[1::2]))
