class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        vector<int>fr(SHRT_MAX * SCHAR_MAX);             // 1
        for(auto i: intervals) fr[i[0]]++, fr[i[1]+1]--; // 2
        partial_sum(begin(fr), end(fr), begin(fr));      // 3
        return *max_element(begin(fr), end(fr));
    }


};
