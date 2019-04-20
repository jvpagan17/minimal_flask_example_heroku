# I'm not going to read in the packages & data again since it's 
# already in our current environment.

def create_keywordProcessor(list_of_terms, remove_stopwords=True, 
                            custom_stopword_list=[""]):
    """ Creates a new flashtext KeywordProcessor and opetionally 
    does some lightweight text cleaning to remove stopwords, including
    any provided by the user.
    """
    # create a KeywordProcessor
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(list_of_terms)

    # remove English stopwords if requested
    if remove_stopwords == True:
        keyword_processor.remove_keywords_from_list(stopwords.words('english'))

    # remove custom stopwords
    keyword_processor.remove_keywords_from_list(custom_stopword_list)
    
    return(keyword_processor)

def apply_keywordProcessor(keywordProcessor, text, span_info=True):
    """ Applies an existing keywordProcessor to a given piece of text. 
    Will return spans by default. 
    """
    keywords_found = keywordProcessor.extract_keywords(text, span_info=span_info)
    return(keywords_found)
    

# create a keywordProcessor of python packages    
py_package_keywordProcessor = create_keywordProcessor(list_of_packages, 
                                                      custom_stopword_list=["kaggle", "http"])

# apply it to some sample posts (with apply_keywordProcessor function, omitting
# span information)
for post in sample_posts:
    text = apply_keywordProcessor(py_package_keywordProcessor, post, span_info=False)
    print(text)
