""" A quiz program. """


class TopicQuestions:

    # fields would be the topic name, 
    # dictionary of Q and A 
    def __init__(self, topic_name, questions_and_answers):
        self.topic_name = topic_name
        self.questions_and_answers = questions_and_answers



def get_topic(topic_list):
    for topic in topic_list:
        print(topic)

    user_topic = input('Choose your topic')
    # todo validation - is this a valid topic? 
    return user_topic


def main():
    total_score = 0

    # lists, dictionaries, combinations - e.g. list of dictionaries, dictionaries with list keys.... 
    # A number of questions 

    # Questions are keys, the associated value is the answer 
    # Questions and answers are paired, or matched 
    # dictionary (Object in JS, HashMap/HashTable)
    art_questions_and_answers = { 
        'Who painted the Mona Lisa?': 'Vincent Van Gogh',
        'What precious stone is used to make the artist\'s pigment ultramarine?': 'Lapiz Lazuli'
        # etc.
    }

    space_questions_and_answers = {
        'Which planet is closest to the sun?': 'Mercury',
        'Which planet spins in the opposite direction to all the others in the solar system?': 'Venus'
        # etc, other questions... 
    }

    topics = ['art', 'space', 'sport']

    space = TopicQuestions('Space', space_questions_and_answers)
    art = TopicQuestions('Art', art_questions_and_answers)

    all_questions = [ space, art ]  # add more topics & questions as needed

    # Or, we could do a dictionary of dictionaries, for example 

    all_questions = { 
        'art' : art_questions_and_answers,
        'space': space_questions_and_answers 
    } 


    topic = get_topic()  # can we pass a list of topics into this function? 




    if topic == 'art':

        for question, correct_answer in art_questions_and_answers.items():
            print(question)
            user_answer = input('Enter your answer: ')
            if user_answer == correct_answer:  # todo case insensitive
                print('correct!')
                # add 1 to the score 
            else: 
                # print incorrect message 
                print('Sorry the answer is ' + correct_answer)


        print('End of quiz!')
        print(f'Your total score on {topic} questions is {total_score} out of 3.')

        if total_score == 3:
            print('You got all the answers correct!')


    elif topic == 'space':
        
        print('Which planet is closest to the sun?')
        answer = input('Enter your answer: ')
        if answer == 'Mercury':
            print('Correct!')
            total_score += 1
        else:
            print('Sorry, the correct answer is Mercury.')

        print('Which planet spins in the opposite direction to all the others in the solar system?')
        answer = input('Enter your answer: ')
        if answer == 'Venus':
            print('Correct!')
            total_score += 1
        else:
            print('Sorry, the correct answer is Venus.')

        print('How many moons does Mars have?')
        answer = input('Enter your answer: ')
        if answer == '2':
            print('Correct!')
            total_score += 1
        else:
            print('Sorry, the correct answer is 2.')

        print('End of quiz!')
        print(f'Your total score on {topic} questions is {total_score} out of 3.')

        if total_score == 3:
            print('You got all the answers correct!')

    else:
        print('That is not a valid topic. Restart the program to try again.')


main()