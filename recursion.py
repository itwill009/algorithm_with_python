def countdown(i):

    print(i)

    if i <= 1:

        return

    else:

        countdown(i-1)

recur = countdown(5)

print(recur)


def fact(x):

    if x == 1:

        return 1

    else:

        return x * fact(x-1)
