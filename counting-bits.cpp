//https://leetcode.com/problems/counting-bits/
#include <vector>
using namespace std;

class Solution {
public:

    int numberOnes(int n){
        int count = 0;
        while(n!=0){
            count+= (n & 1);
            n >>= 1;
        }
        return count;
    }
    vector<int> countBits(int n) {
        vector<int> res;
        for(int i=0; i<=n; i++){
            res.push_back(numberOnes(i));
        }
        return res;
    }
};