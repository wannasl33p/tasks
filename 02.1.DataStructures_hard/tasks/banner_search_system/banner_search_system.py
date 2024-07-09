import re
from collections import defaultdict
from collections import Counter

def normalize(
        text: str
        ) -> str:
    """
    Removes punctuation and digits and convert to lower case
    :param text: text to normalize
    :return: normalized query
    """
    lower_string = text.lower()

    no_number_string = re.sub(r'\d+','',lower_string)
    no_punc_string = re.sub(r'[^\w\s]','', no_number_string) 
    return no_punc_string
    

def get_words(
        query: str
        ) -> list[str]:
    """
    Split by words and leave only words with letters greater than 3
    :param query: query to split
    :return: filtered and split query by words
    """

    return [word for word in query.split() if len(word)>3 ]


def build_index(
        banners: list[str]
        ) -> dict[str, list[int]]:
    """
    Create index from words to banners ids with preserving order and without repetitions
    :param banners: list of banners for indexation
    :return: mapping from word to banners ids
    """
    
    new_dict :dict[str, list[int]] = {}
    
    i=0
    
    print(Counter(banners))
    
    for key, value in Counter(banners).items():
        for j in range(value):
            if j==0:
                new_dict[key] = [i]
            else :
                new_dict[key]+= [i:=i+1]
            
    
    
    return new_dict


print(build_index(['jopa' , 'hui', 'chlen' , 'chlen' , 'peinis' , 'jopa']))
        
    


def get_banner_indices_by_query(
        query: str,
        index: dict[str, list[int]]
        ) -> list[int]:
    """
    Extract banners indices from index, if all words from query contains in indexed banner
    :param query: query to find banners
    :param index: index to search banners
    :return: list of indices of suitable banners
    """


#########################
# Don't change this code
#########################

def get_banners(
        query: str,
        index: dict[str, list[int]],
        banners: list[str]
        ) -> list[str]:
    """
    Extract banners matched to queries
    :param query: query to match
    :param index: word-banner_ids index
    :param banners: list of banners
    :return: list of matched banners
    """
    indices = get_banner_indices_by_query(query, index)
    return [banners[i] for i in indices]

#########################
