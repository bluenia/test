class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #my solution
        """
        rtype = []
        for i in range(0, len(nums)):
            tmp = target - nums[i]
            if 1:
                try:
                    index = nums.index(tmp)
                    if index != i:
                        rtype.append(i)
                        rtype.append(index)
                        rtype.sort()
                        break
                except:
                    index = -1
                    
        return rtype
        """

        #pretty smart solution
        rtype = {}
        for i, val in enumerate(nums):
            remaining = target - val
            #print("step:",i,val,remaining)

            #check index
            #if u need check value : if ... in rtype.value
            if remaining in rtype:
                #print(rtype[remaining])
                return (rtype[remaining], i)

            rtype[val] = i
            #print("rtype:",rtype)
        
def main():
    nums = [1,2,-3,2]
    target = 4
    print(Solution().twoSum(nums, target))

if __name__ == "__main__":
    main()