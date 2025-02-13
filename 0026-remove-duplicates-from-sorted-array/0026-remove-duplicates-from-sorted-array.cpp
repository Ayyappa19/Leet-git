class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i=0,j=1;
        // 0 0 1 1 1 2 2 3 3 4 
        // i
        //   j
        while(i<nums.size() and j<nums.size()){
            if(nums[i]!=nums[j]){
                i++;
                nums[i]=nums[j];
                
                
            }
            j++;
        }
        return i+1;
    }
};