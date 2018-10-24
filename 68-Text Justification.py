class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # Algorithm: Add as many words as possible to line with 
        # spaces in between and increase size of spaces as needed.
        result = []
        
        word_idx = 0
        while word_idx < len(words):
            next_line = []
            char_count = word_count = space_count = 0
            
            # Add words and a space while we have words and if there are available characters
            while (
                word_idx < len(words) and
                len(words[word_idx]) <= (maxWidth - (char_count + space_count))
            ):
                next_word = words[word_idx]
                next_line.append(next_word)
                next_line.append(" ")
                char_count += len(next_word)
                word_count += 1
                space_count += 1
                word_idx += 1

            # Ignore the last space in our count of valid spaces
            space_count -= 1

            # Get the number of free characters left (not including spaces)
            char_difference = maxWidth - char_count

            # Case 1: if we're out of words or have only
            # one word on the line, then just increase the
            # number of spaces after the last word in the line.
            #
            # The number of spaces added should be the difference
            # in max width and non-space characters less the number
            # of spaces not accounted for in the difference.
            if word_idx == len(words) or word_count == 1:
                next_line[-1] *= (char_difference - space_count)
            
            # Case 2: otherwise, increase the space size after each
            # character as evenly as possible. Prefer left spaces to
            # apply extra spaces. Drop the last space at the end
            else:
                next_line.pop()
                num_spaces = char_difference / space_count
                num_slots_with_extra_spaces = char_difference % space_count

                for space_idx in range(1, word_count+space_count, 2):
                    if num_slots_with_extra_spaces:
                        next_line[space_idx] *= num_spaces+1
                        num_slots_with_extra_spaces -= 1
                    else:
                        next_line[space_idx] *= num_spaces
                
            result.append("".join(next_line))
        return result
