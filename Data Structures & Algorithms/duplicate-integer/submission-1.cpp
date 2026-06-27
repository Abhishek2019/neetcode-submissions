// class Solution {
// public:
//     bool hasDuplicate(vector<int>& nums) {
        
//     }
// };

class Solution{
public: bool hasDuplicate(vector<int>& nums){

    int n = nums.size();
    unordered_set <int> uset;
    for(int i=0; i < n; i++){

        if (uset.count(nums[i])){
            return true;
        }

        uset.insert(nums[i]);

    }

    return false;

}
};