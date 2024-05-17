"""
    Rae Adimer

    How to use:
        1. Download wikitext as file.txt, e.g., from https://meta.wikimedia.org/wiki/Global_message_delivery/Targets/Tech_ambassadors
        2. run this
        3. look at resulting csv! :D
"""

def get_wikis():
    wiki_list = []
    with open("file.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line[0] == '*':
                wiki_list.append(line.strip().split('site=')[-1][:-2].split('.org')[0] + '.org')
                if len(wiki_list[-1]) > 20:
                    wiki_list[-1] = wiki_list[-1].split('site =')[-1].strip()
    return wiki_list

def count_wikis(wiki_list):
    wikis = {}
    for i in wiki_list:
        wikis[i] = wikis.get(i, 0) + 1
    return wikis

def export_wikis(wikis):
    with open("output.csv", "w") as f:
        for n in wikis:
            f.write(f'{n},{wikis[n]}\n')

def main():
    export_wikis(count_wikis(get_wikis()))

if __name__ == "__main__":
    main()
