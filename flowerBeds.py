class Solution:
    def canPlaceFlowers(flowerbed: list, n: int) -> bool:
            for i in range(0, len(flowerbed), 1):
                if n > 0:
                    if i == 0:
                        if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            n = n - 1
                    elif i == len(flowerbed)-1:
                        if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                            flowerbed[i] == 1
                            n = n - 1
                    else:
                        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                            flowerbed[i] = 1
                            n = n - 1
                else:
                    break


            if n == 0:
                return True
            else:
                return False
    

print(Solution.canPlaceFlowers([1, 0, 0, 1, 1], 1))
