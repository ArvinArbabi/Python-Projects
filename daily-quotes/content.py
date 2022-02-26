import csv, random

def get_random_quote(quotes_file = "quotes.csv"):
    try: #load motivational quotes from csv file
        with open(quotes_file) as csvFile:
            quotes = [{'author':line[0], 'quote':line[1]}
            for line in csv.reader(csvFile, delimiter = '|')]
    except Exception as e:
        quotes = [{'author': 'Eric Idle',
                   'quote': 'Always Look on the Bright Side of Life.'}]
    return random.choice(quotes)

if __name__ == '__main__':
    ##### test get_random_quote() #####
    print('\nTesting quote generation...')

    quote = get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" - {quote["author"]}')
    
    quote = get_random_quote(quotes_file = None)
    print(f' - Default quote is "{quote["quote"]}" - {quote["author"]}')
