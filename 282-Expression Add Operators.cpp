class Solution {
public:
    vector<string> addOperators(string num, int target) {
        vector<string> result;
        if(num.size() == 0)   
            return result;
        helper(&result, "", num, target, 0, 0, 0);
        return result;
    }
    void helper(vector<string> *result, string path, string num, int target, int pos, long cur, long prev) {
        if (pos == num.size()){ //已经到达num的最后了
            if (cur == target)  //符合target的要求
                (*result).push_back(path);
            return;
        }
        for (int i = pos; i < num.size(); i++){
            /*** corner-case-added-code ***/
            if (num[pos]=='0' && i > pos) //数字的第一位不能是0
                break;
            string _str = num.substr(pos, i-pos+1);
            long _value = stol(_str);
            if (pos == 0)  {
                helper(result, path+_str, num, target, i+1, _value, _value);
            }
            else{
                helper(result, path+"+"+_str, num, target, i+1, cur+_value, _value);
                helper(result, path+"-"+_str, num, target, i+1, cur-_value, -_value);
                helper(result, path+"*"+_str, num, target, i+1, cur-prev+prev*_value, prev*_value);
            }
        }
    }
};
