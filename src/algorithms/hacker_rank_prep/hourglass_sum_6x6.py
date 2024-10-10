from collections import Counter

def hourglassSum(arr):
    rowSize = len(arr)
    pool = []

    for i in range(rowSize - 2):
        for j in range(rowSize -2):
            top = 0 
            mid = 0 
            down = 0
            # the hourglass shape
            for k in range(rowSize-3):
                top += arr[i][j+k]
                if k == 1:
                    mid += arr[i+1][j+k]
                down += arr[i+2][j+k]
            hourglass_sum = top + mid + down
            # update pool
            pool.append(hourglass_sum)
            
    return max(pool)
            
    # for i := 0; i < rowSize-2; i++ {
    #     for k := 0; k < rowSize-2; k++ {
    #         top := int32(0)
    #         mid := int32(0)
    #         down := int32(0)
    #         for j := 0; j < rowSize-3; j++ {
    #             top = top + arr[i][j+k]
    #             if j == 1 {
    #                 mid = arr[i+1][j+k]
    #             }
    #             down = down + arr[i+2][j+k]  
    #         }
    #         sum = top + mid + down
    #         sumPool = append(sumPool, sum)
    #     }
    # }
    
    # for _, total := range sumPool {
    #     if total > res {
    #         res = total
            
    return res

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr = []

#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = hourglassSum(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

demo = '1 1 1 0 0 0\n0 1 0 0 0 0\n1 1 1 0 0 0\n0 0 2 4 4 0\n0 0 0 2 0 0\n0 0 1 2 4 0'
# '1 1 1 0 0 0 0 1 0 0 0 0 1 1 1 0 0 0 0 0 2 4 4 0 0 0 0 2 0 0 0 0 1 2 4 0'
print(demo.split())
arr = ['1 1 1 0 0 0', '0 1 0 0 0 0', '1 1 1 0 0 0', '0 0 2 4 4 0', '0 0 0 2 0 0', '0 0 1 2 4 0']
# for _ in range(6):
#     arr.append(list(map(int, demo.rstrip().split())))

result = hourglassSum(arr)
