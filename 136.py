def main():
    two, three, five = [2**i for i in range(30)], [3**i for i in range(30)], [5**i for i in range(30)]
    two_three, two_five, three_five = cross(two, three), cross(two, five), cross(three, five)
    two_three_five = cross(two_three, five)
    ugly = list(set(extend([1], [two, three, five, two_three, two_five, three_five, two_three_five])))
    ugly.sort()
    print("The 1500'th ugly number is {}.".format(ugly[1499]))


def cross(a, b):
    cross_list = []
    for i in a:
        for j in b:
            cross_list.append(i*j)
    return cross_list


def extend(to_extend, to_add):
    for i in to_add:
        to_extend.extend(i)
    return to_extend


main()
