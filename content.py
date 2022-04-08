def get_random_quote(quotes_file='quotes.csv'):
    try: # load motivational quotes from csv file
       with open(quotes_file) as csvfile:
           # List comprehension that creates a list of dictionaries
           # Sets delimiter as pipe character
           quotes = [{'author': line[0],
                      'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]
    # Uses a default quote in case the programme is
    # unable to open the quotes file 
    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright Side of Life.'}]

def get_weather_forecast():
    pass

def get_youtube_shorts():
    pass

def get_wikipedia_article():
    pass

if __name__ == '__main__':
    # test get_random_quote()
    print('\nTesting quote generation:')

    quote = get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" - {quote["author"]}'')

    quote = get_random_quote(quotes_files = None)
    print(f' - Default quote is "{quote["quote"]}" - {quote["author"]}')
