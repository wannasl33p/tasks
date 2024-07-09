

def count_util(text: str, flags: str | None = None) -> dict[str, int]:
    """
    :param text: text to count entities
    :param flags: flags in command-like format - can be:
        * -m stands for counting characters
        * -l stands for counting lines
        * -L stands for getting length of the longest line
        * -w stands for counting words
    More than one flag can be passed at the same time, for example:
        * "-l -m"
        * "-lLw"
    Ommiting flags or passing empty string is equivalent to "-mlLw"
    :return: mapping from string keys to corresponding counter, where
    keys are selected according to the received flags:
        * "chars" - amount of characters
        * "lines" - amount of lines
        * "longest_line" - the longest line length
        * "words" - amount of words
    """
    dct :dict[str, int] ={}
    
    if flags == None or flags=='' :
      
        dct["chars"]=len(text)

        lines = text.split('\n')
       
        dct["lines"]=len(lines)-1

        max_len =0
        for line in lines :
            if len(line)>max_len:
                max_len=len(line)
        dct["longest_line"]=max_len  
      
        dct["words"]=len(text.split())
   
        
    else:
        if '-' in flags:
            if 'm' in flags :
                 dct["chars"]=len(text)
            if 'l' in flags :
                lines = text.split('\n')
                dct["lines"]=len(lines)-1
            if 'L' in flags :
                lines = text.split('\n')
                max_len =0
                for line in lines :
                    if len(line)>max_len:
                        max_len=len(line)
                dct["longest_line"]=max_len
            if 'w' in flags:
                dct["words"]=len(text.split())
    
  
    return dct

text = '''\n'''
print(count_util(text, flags='-wlLm'))
