class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1

        while left<=right:
            mid = (left+right)//2

            if matrix[mid][0]<=target and matrix[mid][-1]>=target:
                rw = mid

                l,r = 0, len(matrix[rw])-1

                while l<=r:
                    m = (l+r)//2

                    if matrix[rw][m]== target:
                        return True
                    elif matrix[rw][m]<target:
                        l = m+1
                    else:
                        r = m-1

                break
            elif matrix[mid][0]<target:
                left = mid+1
                print(mid)
            else:
                right = mid-1
                print(mid)

        return False