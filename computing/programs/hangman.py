def hangman(word, guesses, lives):
    remaining_letters = set([c for c in word])
    current_status = ['_' for i in range(len(word))]
    for c in guesses:
        if c in remaining_letters:
            remaining_letters.remove(c)
            for i, l in enumerate(word):
                if l == c:
                    current_status[i] = c
        else:
            lives -= 1

        print(''.join(current_status), '\t', c, 'guessed,', lives, 'lives remaining')
        if len(remaining_letters) == 0:
            print('Word correctly guessed')
            return
        elif lives == 0:
            print('Game over')
            return
    print('Game incomplete')
    return

#hangman("lion", "euiaoblnxy", 6)
hangman("gorgonzola", "aglmnxyzpqrs", 6)
hangman("gupibagha", "abcdefghi", 6)
