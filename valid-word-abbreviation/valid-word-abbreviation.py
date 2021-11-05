class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        def is_int(char):
            try:
                int(char)
                return True
            except ValueError:
                return False
        def get_int(index):
            if abbr[index] == '0':
                return 0,index+1
            curnum = 0
            while index < len(abbr) and is_int(abbr[index]):
                curnum = (curnum * 10) + int(abbr[index])
                index += 1
            return curnum,index
        cur_index = 0
        word_index = 0
        while cur_index < len(abbr) and word_index < len(word):
            if is_int(abbr[cur_index]):
                shift_num,new_index = get_int(cur_index)
                if shift_num == 0:
                    return False
                word_index += shift_num
                cur_index = new_index
            else:
                if abbr[cur_index] != word[word_index]:
                    return False
                cur_index += 1
                word_index += 1
        return word_index == len(word) and cur_index == len(abbr)
                
            
        