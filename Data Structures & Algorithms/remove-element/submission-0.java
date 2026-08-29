class Solution {
    public int removeElement(int[] nums, int val) {
        List<Integer> updatedList = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++)
        {
            if(nums[i] != val)
            {
                updatedList.add(nums[i]);
            }
        }
        for(int i = 0; i < updatedList.size(); i++)
        {
            nums[i] = updatedList.get(i);
        }
        return updatedList.size();
    }
}