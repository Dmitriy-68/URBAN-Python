class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.replace(',', '')
                    line = line.replace('.', '')
                    line = line.replace('=', '')
                    line = line.replace('!', '')
                    line = line.replace('?', '')
                    line = line.replace(';', '')
                    line = line.replace(':', '')
                    line = line.replace(' - ', ' ')
                    words += line.lower().split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        find_words = {}
        for name, words in self.all_words.items():
            if word.lower() in words:
                find_words[name] = words.index(word.lower()) + 1
        return find_words

    def count(self, word):
        count_words = {}
        for name, words in self.all_words.items():
            count_words[name] = words.count(word.lower())
        return count_words


finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT')) # 4 слова teXT в тексте всего