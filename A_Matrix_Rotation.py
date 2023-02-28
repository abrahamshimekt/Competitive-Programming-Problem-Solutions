def rotate(mat):
    temp = mat[0][1]
    mat[0][1] = mat[0][0]
    temp2  = mat[1][1]
    mat[1][1] = temp
    temp3 = mat[1][0] 
    mat[1][0] = temp2
    mat[0][0] = temp3
    return mat
def beautiful(mat):
    if int(mat[0][0]) < int(mat[0][1]) and int(mat[1][0]) < int(mat[1][1]) and int(mat[0][0]) < int(mat[1][0]) and int(mat[0][1]) < int(mat[1][1]):
        return True
    return False

T = int(input())
for t in range(T):
    mat = []
    mat.append(input().split())
    mat.append(input().split())

    if beautiful(mat):
        print("YES")
    else:
        b = False
        for i in range(3):
            mat = rotate(mat)
            if beautiful(mat):
                b = True
                break
        if b:
            print("YES")
        else:
            print("NO")


    
        

