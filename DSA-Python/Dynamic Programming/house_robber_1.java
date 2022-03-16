class house_robber_1 {
    class Solution {
        public int rob(int[] nums) {
            if(nums.length == 0)return 0; // if number of houses is zero the max amount which i can  rob is 0
            if(nums.length == 1) return nums[0]; // if the no of houses is one the max amount which we can rob is that house amount itsel
            if (nums.length == 2) return Math.max(nums[0],nums[1]); // if the number of houses is 2 then max amount of houses i can rob may be the first house or 2nd house.
            int dp[] = new int[nums.length]; // dp table is used to store the max amount i can stole at that particular index
            dp[0] = nums[0];  // if i am at the 0 th house i can max rob the 0 th housse
            dp[1] = Math.max(nums[0],nums[1]); // if i am at first house i can rob maximum of first house cost or zero th house cost
            for(int i =2;i<dp.length;i++){
                dp[i] = Math.max(nums[i]+dp[i-2],dp[i-1]); // if i am at 2nd house then i can rob the max that house profit + 2 houses behind profit or the back house profit 
            }
            return dp[dp.length-1];
        }
    }
}