class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size() ){
            return false;
        }
        int n = s.size();

        unordered_map <char,int> umap1;
        unordered_map <char,int> umap2;

        for (int i =0; i<n;i++){

            umap1[s[i]]++;
            umap2[t[i]]++;

        }

        if (umap1 != umap2){

            return false;

        }
        return true;


    }
};
