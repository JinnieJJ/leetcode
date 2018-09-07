class Solution{
public:
	string minWindow(string s, string t){
	    if (s.size() < t.size())
	        return "";
		map<char, int> chrMap; //保存最初t的字母
		for (int i = 0; i < t.size(); i++) {
			chrMap[t[i]]++;
		}
		int start = 0;
		int end = 0;
		int count = 0; //window中包含所需字符的数量
		int minWindowLen = INT_MAX;
		int curWindow; //当前window大小
		int minStart = 0; //当前window最小值时start的位置
		int minEnd = 0; //当前window最小值时end的位置
		map<char, int> tempMap(chrMap.begin(), chrMap.end());//临时map，用于计算
		while (end < s.size()) {
			if (tempMap.find(s[end]) == tempMap.end()) { //t中没有s[end]
				end++;
				continue;
			}
			tempMap[s[end]]--; //t中有s[end]
			if (tempMap[s[end]] >= 0)
				count++; //记录已找到的t中的字母数量
            
			if (count == t.size()) { //找满一次窗口
				while (start != end) {
					if (chrMap.find(s[start]) == chrMap.end()){ //start不在T的map里面
						start++;
						continue;
					}
                    //start属于T里面
					if (tempMap[s[start]] < 0) { //window中对于同一字符找重了，此时要向前移动并且补上
						tempMap[s[start]]++; 
						start++;
						continue;
					}
					else
						break; //window中字符只出现了一次
				}
                
				curWindow = end - start + 1;
				if (curWindow < minWindowLen)
				{
					minWindowLen = curWindow;
					minStart = start;
					minEnd = end;
				}
			}
			end++;
		}
		if (minWindowLen == INT_MAX)
			return "";
		return s.substr(minStart, minWindowLen);
    }
};
