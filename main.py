from nltk.corpus import wordnet as wn
from random import *
from PyDictionary import PyDictionary
import pyttsx3


def t2s(word):
    engine = pyttsx3.init('sapi5')
    engine.say(word)
    engine.setProperty("rate", 178)
    engine.runAndWait()


if __name__ == '__main__':
    print("*************** HangMan Game Made By Karim Tarek  ***************")
    Total_chances = 11
    all_nouns = []
    for synset in wn.all_synsets('n'):
        all_nouns.extend(synset.lemma_names())
    chosen_word = choice(all_nouns).lower()
    dash_flag = False
    while True:
        for i in chosen_word:
            if i == '-':
                dash_flag = True
        if dash_flag:
            chosen_word = choice(all_nouns)
        else:
            break
    word_letters = list(chosen_word)
    guessed_list = ["-"] * len(word_letters)
    guessed_letters = []
    flag = False
    dictionary = PyDictionary()
    word_meanings = dictionary.meaning(chosen_word)
    first_value = list(word_meanings.keys())[0]
    value_list = word_meanings['Noun']
    if len(value_list) >= 3:
        print("HINT:", value_list[2])
        t2s(value_list[2])
    elif len(value_list) >= 2:
        print("HINT:", value_list[1])
        t2s(value_list[1])
    elif len(value_list) >= 1:
        print("HINT:", value_list[0])
        t2s(value_list[0])
    print("The word is: ", end=" ")
    for i in guessed_list:
        print(i, end=" ")
    while True:
        print("\n")
        user_pick = input("Guess a letter: ")
        if user_pick not in guessed_letters and user_pick.isalpha():
            guessed_letters.append(user_pick.lower())
        else:
            print("*You have guessed this letter before, Try a new one!*")
            t2s("You have guessed this letter before, Try a new one")
            print("The word is: ", end=" ")
            for i in guessed_list:
                print(i, end=" ")
            print("\n")
            print("The letters you guessed are: ", guessed_letters)
            continue
        for j in range(0, len(word_letters)):
            if user_pick.lower() == word_letters[j]:
                guessed_list[j] = user_pick.lower()
                flag = True
        if flag:
            text = "Correct! You have guessed it right!, Keep going! You still have " + str(Total_chances) + " chances left"
            print(text)
            t2s(text)
        else:
            Total_chances -= 1
            text = "Incorrect! You have guessed it wrong!, You have now " + str(Total_chances) + " chances left"
            print(text)
            t2s(text)
            if Total_chances == 6:
                warn = "you need to relax and think"
                t2s(warn)
                if len(value_list) >= 2:
                    print("ANOTHER HINT:", value_list[1])
                    t2s("ANOTHER HINT:")
                    t2s(value_list[1])
            if Total_chances == 3:
                warn = "careful, you are running out of chances"
                t2s(warn)
                if len(value_list) >= 3:
                    print("ANOTHER HINT:", value_list[0])
                    t2s("ANOTHER HINT:")
                    t2s(value_list[0])
        flag = False
        print("The word is: ", end=" ")
        for i in guessed_list:
            print(i, end=" ")
        if word_letters == guessed_list:
            print("\n")
            print("Congratulations, you nailed it!")
            t2s("Congratulations, you nailed it")
            break
        print("\n")
        print("The letters you guessed are: ", guessed_letters)
        print("****************************************************************************************")
        if Total_chances == 0:
            text = "You have lost this game, The word was: " + chosen_word
            print(text)
            t2s(text)
            break
    ex = input("Type any key to quit: ")
    quit()









