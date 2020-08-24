import string, random

sentence = 'methinks it is like a weasel'


def random_sentence(N):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(N))


def compare_sentences(sent_one=sentence, sent_two=''):
    u = zip(sent_one,sent_two)
    d = dict(u)

    x = 0
    for i, j in d.items():
        if i == j:
            x += 1
    return x


result = 0
count = 0
best_result = 0
best_string = ''
total = 0
best_result_ever = 0
while result != len(sentence):
    count += 1
    total += 1
    guess = random_sentence(len(sentence))
    result = (compare_sentences(sentence,guess))
    if result > best_result:
        best_result = result
        best_string = guess
    if result > best_result_ever:
        best_result_ever = result
    if count >= 1000:
        print('after {count} test we have {best_string} with {best_result} matches'.format(count=count, best_string=best_string, best_result=best_result))
        print('total counter: ' + total.__str__())
        print('and the best result so far is: ' + best_result_ever.__str__())
        print('')
        count = 0
        best_result = 0
        best_string = ''
print('FOUND - ' + best_string + ' - after ' + total.__str__() + ' attempts!!!')
