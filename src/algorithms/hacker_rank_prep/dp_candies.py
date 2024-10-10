def candies(n, arr):
    # arr is the score
    candy_bag = [1 for x in range(n)]
    
    for i in range(1, n, 1):
        if arr[i] > arr[i-1]:
            candy_bag[i] = candy_bag[i-1] +1
    
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i] and candy_bag[i-1] <= candy_bag[i]:
            candy_bag[i-1] = candy_bag[i] +1
    
    # print(sum(candy))
    return sum(candy_bag)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr_item = int(input().strip())
#         arr.append(arr_item)

#     result = candies(n, arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# function candies($n, $ratings) {
#     // Initialize candies array
#     $candies = array_fill(0, $n, 1);
    
#     // Left to right pass
#     for ($i = 1; $i < $n; $i++) {
#         if ($ratings[$i] > $ratings[$i - 1]) {
#             $candies[$i] = $candies[$i - 1] + 1;
#         }
#     }
    
#     // Right to left pass
#     for ($i = $n - 2; $i >= 0; $i--) {
#         if ($ratings[$i] > $ratings[$i + 1]) {
#             $candies[$i] = max($candies[$i], $candies[$i + 1] + 1);
#         }
#     }
    
#     // Calculate the total number of candies
#     return array_sum($candies);
# }

# // Example usage:
# $n = 5;
# $ratings = [1, 0, 2, 1, 0];
# echo candies($n, $ratings); // Output: 7