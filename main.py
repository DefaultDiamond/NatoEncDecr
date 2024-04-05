
status = True

while status is True:
    print('1 - Зашифровать строку в алфавит НАТО')
    print('2 - Расшифровать строку')
    checker = input('Выберите режим: ')
    if checker == '1' or checker == '2':
        status = False
    else:
        print('Выберите один из режимов!')


str_ = input('Введите строку: ')


class Nato:
    str_: str
    alphabet: dict

    def __init__(self):
        self.str_ = ''
        self.alphabet = {
            'a': 'Alfa', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta',
            'e': 'Echo', 'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel',
            'i': 'India', 'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima',
            'm': 'Mike', 'n': 'November', 'o': 'Oscar', 'p': 'Papa',
            'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
            'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray',
            'y': 'Yankee', 'z': 'Zulu'
        }

    def encrypt(self, string):
        self.str_ = string.lower()
        list_ = list(self.str_)
        for s in range(len(list_)):
            if self.alphabet.get(list_[s]):
                list_[s] = self.alphabet.get(list_[s])

        result = ''.join(list_)

        return result

    def decrypt(self, string):
        self.str_ = string
        list_ = []
        counter = 0
        for _ in range(len(self.str_)):
            if len(self.str_) <= counter:
                break
            char = self.str_[counter]
            if char.lower() in self.alphabet:
                nato_word = self.alphabet.get(char.lower())
                word = str_[counter:len(nato_word) + counter]
                if nato_word.lower() == word.lower():
                    list_.append(word)
                    counter += len(nato_word)
                else:
                    length = 0
                    for ind in range(len(word)):
                        if nato_word[ind].lower() == word[ind].lower():
                            length += 1
                        else:
                            break
                    list_.append(str_[counter:length+counter])
                    counter += length
            else:
                list_.append(char)
                counter += 1
        for ind in range(len(list_)):
            word = list_[ind]
            if len(word) > 0:
                list_[ind] = word[0].lower()
            else:
                pass
        result = ''.join(list_)
        return result


if checker == '1':
    print(f'Зашифрованная строка: {Nato().encrypt(str_)}')
else:
    print(Nato().decrypt(str_))




