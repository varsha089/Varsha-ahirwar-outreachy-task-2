from email import message
import pywikibot

site = pywikibot.Site('en', 'wikipedia')
repo = site.data_repository()

#method to print content of task 1 page
def get_task1_outreachy(task1_outreachy):

    message = task1_outreachy.get()
    task1_outreachy.message = message
    try:
        print(message)
    except:
        print("This page is not available!")

def get_task1_outreachy_page(Qid):
    return  pywikibot.ItemPage(repo, Qid)

#method to add message 'Hello' at the end of an article
def edit_article(page, addmessage= "Hello , Hello "):
    message = page.get()
    message = message + "\n" + addmessage
    page.message = message
    try:
        print(message)
        page.save("test edit is being saved")
        return 1
    except:
        print("It is not working!")
        return 0

#method to print first and last name of author
def get_claims_name(page_info, Pid, error):
    
    try:
        for claim in page_info['claims'][Pid]:
            instance_value = claim.getTarget()
            instance_page_info = instance_value.get()
            print('\t' + instance_page_info['labels']['en'])
            print('\t\tQ identifier: ' + instance_value.title() + '\n')
    except:
        print(error)

# method to print qualifier information of author
def get_qualifiers_author_statement(claim, Pid, title):

    if Pid in claim.qualifiers:
        qualifier = claim.qualifiers[Pid]
        print('\t'+ title +': ' + qualifier[0].getTarget())


def print_article(wd_item):
    """Prints article information from the wikidata site."""
    item_code = wd_item.title()
    page_info = wd_item.get()

    #method for printing title and Q identifier of article.
    try:
        print('\nTitle of article: \n' + page_info['labels']['en'])
        print('\nQ identifier of article:\n \t' + item_code + '\n')
    except:
        print('Item Name: This item has no English label!' + '\n')

    
    #method for Printing author information in article.
    try:
        for claim in page_info['claims']['P50']:
            print('Author Information:')
            name_value = claim.getTarget()
            name_page_info = name_value.get()
            title = name_value.title()
            
            print('\tName: ' + name_page_info['labels']['en'])
            print('\tQ identifier: ' + title + '\n')
            
            print('\tQualifiers:')
            get_qualifiers_author_statement(claim, 'P1932', 'Stated as')
            get_qualifiers_author_statement(claim, 'P1545', 'Series ordinal')
            
            #Print given name and family name of author
            print('\n\tName info:')
            name_of_author = pywikibot.ItemPage(repo, title)
            author_dict = name_of_author.get()
            print('\tGiven name:') 
            get_claims_name(author_dict, 'P735', '\t\t*No Given name info*')
            print('\tFamily name:')
            get_claims_name(author_dict, 'P734', '\t\t*No family name info*')
            print('\n')

    except:
        pass
    try:
        for claim in page_info['claims']['P2093']:
            print('Author Name String:')
            name_string_value = claim.getTarget()
            print('\tName: ' + name_string_value)
            get_qualifiers_author_statement(claim, 'P1545', 'Series ordinal')
            get_qualifiers_author_statement(claim, 'P1932', 'Stated as')
            print('\n')
    except:
        pass

def print_all_articles(articles):
    """Prints all articles in Outreachy task 1 which are passed in articles variable."""
    for item in articles:
        article = get_task1_outreachy_page(item)
        print_article(article)


task1_outreachy = pywikibot.Page(repo, 'User:Varsha ahirwar from India/Outreachy 1')
articles = ['Q86839085','Q58889074','Q110028642','Q33360138','Q60101261' , 'Q38193292','Q74515767','Q59065222']
article = get_task1_outreachy_page('Q4115189')
get_task1_outreachy(task1_outreachy)
edit_article(task1_outreachy)
print_article(article)
print_all_articles(articles)
