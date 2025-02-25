class Solution {
    public void moveZeroes(int[] nums) {
        int i=0,j=1;
        while(j<nums.length){
            if(nums[i]==0 && nums[j]!=0){
                nums[i]=nums[j];
                
                i++;
                nums[j]=0;
            }
            else if(nums[i]!=0){
                i++;
            }
            j++;
        }
    }
}