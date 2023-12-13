import random
word_list = ['осень', 'кость', 'метла', 'конфета', 'кошка', 'котёл', 'костюм', 'дракула', 'волнение', 'фонарик', 'страх', 'испуг', 'упырь', 'гоблин', 'кладбище', 'маска', 'монстр', 'ночь', 'сова', 'зелье', 'тыква', 'тень', 'скелет', 'череп', 'заклинание', 'паук', 'дух', 'вампир', 'чернокнижник', 'оборотень', 'ведьма', 'зомби']
def get_word():
  return random.choice(word_list).upper()
def display_hangman(tries):
    stages = [
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / \\
                |
                |  ПИЗДЕЦ!
                
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    / 
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    \|/
                |     |
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    \|
                |     |
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |     |
                |     |
                |     
                |  
                ''',
                '''
                _______
                |     |
                |     O
                |    
                |     
                |    
                |  
                ''',
                '''
                _______
                |     |
                |     
                |    
                |       
                |  
                '''
    ]
    return stages[tries]
def play(word):
   word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
   guessed = False                    # сигнальная метка
   guessed_letters = []               # список уже названных букв
   guessed_words = []                 # список уже названных слов
   tries = 6                          # количество попыток
   print('Давайте играть в угадайку слов!')
   print(display_hangman(tries))
   print(word_completion)
   while not guessed and tries > 0:
        guess = input('Введите букву или слово: ').upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Вы уже называли эту букву')
            elif guess not in word:
                print(guess, 'не входит в слово.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Отлично!', guess, 'входит в слово!')
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)

                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Вы уже называли это слово.')
            elif guess != word:
                print(guess, 'не верное слово.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Некорректный ввод.')

        print(display_hangman(tries))
        print(word_completion)

   if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
   else:
        print('Извините, вы исчерпали все попытки. Загаданное слово было:', word)
secret_word = get_word()
play(secret_word)