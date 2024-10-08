'''
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

    For example, flipping [1,1,0] horizontally results in [0,1,1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

    For example, inverting [0,1,1] results in [1,0,0].
'''
def flipAndInvertImage(image: list) -> list:

    for i in range(len(image)):
        image[i].reverse()

    for i in range(len(image)):
        for k in range(len(image[i])):
            if image[i][k] == 0:
                image[i][k] = 1
            else:
                image[i][k] = 0

    return image

print(f"result:   {flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])}")
print("expected: [[1,0,0],[0,1,0],[1,1,1]]")