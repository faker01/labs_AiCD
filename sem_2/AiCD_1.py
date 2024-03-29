def rotate(A,B,C):
    return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


def algorithm_Jarvis(lst):
    n = len(lst)
    lst_of_points = list(range(n))
    # start point
    for i in range(1, n):
        if lst[lst_of_points[i]][0] < lst[lst_of_points[0]][0]:
            lst_of_points[i], lst_of_points[0] = lst_of_points[0], lst_of_points[i]
    H = [lst_of_points[0]]
    del lst_of_points[0]
    lst_of_points.append(H[0])
    while True:
        right = 0
        for i in range(1, len(lst_of_points)):
            if rotate(lst[H[-1]], lst[lst_of_points[right]], lst[lst_of_points[i]]) < 0:
                right = i
        if lst_of_points[right] == H[0]:
            break
        else:
            H.append(lst_of_points[right])
            del lst_of_points[right]
    return H



a = [[0, 0], [3, 0], [14, 7], [7, 7], [6, 0], [2, 1], [4, 2]]
print(algorithm_Jarvis(a))