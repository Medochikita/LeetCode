'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight 
surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, 
we do not consider it in the average (i.e., the average of the four cells in the red smoother).

(img[i-1][k-1] + img[i-1][k] + img[i-1][k+1]
+ img[i][k-1] + img[i][k] + img[i][k+1]
+ img[i+1][k-1] + img[i+1][k] + img[i+1][k+1])/9

'''

# TODO Not finnished, this only does the job if all 8 surrounding cells are present
# TODO Dont wanna look at the solution, wanna figure it myself

import math

class Solution:
    def imageSmoother(img: list) -> list:
        for i in range(0, len(img)):
            for k in range(0, len(img[i])):
                s = 0
                counter = 0
                if img[i-1][k-1]:
                    s += img[i-1][k-1]
                    counter += 1
                if img[i-1][k]:
                    s += img[i-1][k]
                    counter += 1
                if img[i-1][k+1]:
                    s += img[i-1][k+1]
                    counter += 1
                if img[i][k-1]:
                    s += img[i][k-1]
                    counter += 1
                s += img[i][k]
                counter += 1
                if img[i][k+1]:
                    s += img[i][k+1]
                    counter += 1
                if img[i+1][k-1]:
                    s += img[i+1][k-1]
                    counter += 1
                if img[i+1][k]:
                    s += img[i+1][k]
                    counter += 1
                if img[i+1][k+1]:
                    s += img[i+1][k+1]
                    counter += 1
                


                
                img[i][k] = math.floor(s/counter)


        return img
    

print(Solution.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
print(Solution.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))