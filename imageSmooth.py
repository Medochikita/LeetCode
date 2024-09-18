'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight 
surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, 
we do not consider it in the average (i.e., the average of the four cells in the red smoother).
'''

# TODO Not finnished, this only does the job if all 8 surrounding cells are present
# TODO Dont wanna look at the solution, wanna figure it myself

import math

class Solution:
    def imageSmoother(img: list) -> list:
        for i in range(1, len(img)-1):
            for k in range(1, len(img[i])-1):
                avg = (img[i-1][k-1] + img[i-1][k] + img[i-1][k+1]
                       + img[i][k-1] + img[i][k] + img[i][k+1]
                       + img[i+1][k-1] + img[i+1][k] + img[i+1][k+1])/9
                
                img[i][k] = math.floor(avg)


        return img
    

print(Solution.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
print(Solution.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))