import numpy
import random


def main():
    def merge(A1: list, A2: list):
        i = j = k = 0
        A = [0] * (len(A1) + len(A2))
        while i < len(A1) and j < len(A2):
            if A1[i] <= A2[j]:
                A[k] = A1[i]
                i += 1
                k += 1
            elif A2[j] <= A1[i]:
                A[k] = A2[j]
                j += 1
                k += 1
        while i < len(A1):
            A[k] = A1[i]
            k += 1
            i += 1
        while j < len(A2):
            A[k] = A2[j]
            k += 1
            j += 1
        return A

    def mergesort(A: list):
        '''
        :param A: array to be sorted
        :return: sorted array
        '''
        l = 1
        while l < len(A):
            i = 0
            while i < len(A):
                l1 = i
                r1 = i + l - 1
                l2 = i + l
                r2 = i + 2 * l - 1
                if l2 >= len(A):
                    break
                if r2 >= len(A):
                    r2 = len(A) - 1
                temp = merge(A[l1:r1 + 1], A[l2:r2 + 1])
                for j in range(0, r2 - l1 + 1):
                    A[i + j] = temp[j]
                i = i + 2 * l
            l = 2 * l
        return A

    # aa = [4, 5, 7, 3, 9, 1, 0, 44, 33, 2, 1, 0, 13]
    # a = [45]
    # b = [12]
    # atest = merge(a, b)
    # btest = merge(b, a)

    # print(atest, btest)
    # print(A[0:5])
    # Asorted = mergesort(aa)

    # print(Asorted)

    def Test_sorts_equal(A: list):
        if mergesort(A) == list(numpy.sort(A)):
            return True
        else:
            return False

    def generate_lists(maxlen: int, num_lists: int):
        lists = [[random.randint(0, 1000) for i in range(random.randint(40, maxlen))] for j in range(num_lists)]
        return lists

    listlist = generate_lists(1000, 10)
    for i in range(len(listlist)):
        equal = Test_sorts_equal(listlist[i])
        print(equal)
        #print(listlist[i])


if __name__ == "__main__":
    main()
