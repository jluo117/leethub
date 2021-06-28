class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justify = []
        c = 0
        for word in words:
		    # add new word
            success = self.add_word(justify, c, word, maxWidth)
            if not success:
			    # add extra spaces
                self.fill_spaces(justify, c, maxWidth)
                c += 1
				# add failed word
                self.add_word(justify, c, word, maxWidth)
        
		# add extra spaces for the last line
        self.fill_spaces(justify, c, maxWidth, index=len(justify[c]), last_line=True)
        
        return [''.join(sublist) for sublist in justify]
    
    def add_word(self, justify, c, word, maxWidth):
        if len(justify) != (c+1):
            justify.append([])
            justify[c] = [word]
        elif len(''.join(justify[c])) + 1 + len(word) <= maxWidth:
            justify[c].append(' ')
            justify[c].append(word)
        else:
            return False
        return True

    def fill_spaces(self, justify, c, maxWidth, index=1, last_line=False): 
        while len(''.join(justify[c])) < maxWidth:
            if not index < len(justify[c]):
                justify[c].append(' ')
            else:
                justify[c][index] = justify[c][index] + ' '
            if not last_line:
                index = index + 2 if index < (len(justify[c])-2) else 1