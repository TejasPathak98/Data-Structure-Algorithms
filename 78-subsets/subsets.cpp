class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        
        vector<vector<int>> ans;
        vector<int> subset;

        helper(ans,nums,0,subset);
        return ans;
    }

private:

    void helper(vector<vector<int>>& ans,vector<int>& nums,int index,vector<int>& subset)
    {
        if(index >= nums.size())
        {
            ans.push_back(subset);
            return;
        }

        subset.push_back(nums[index]);
        helper(ans,nums,index + 1,subset);

        subset.pop_back();
        helper(ans,nums,index + 1,subset);
    }


};