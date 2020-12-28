# meet them
try:
    print('hi, i am zordion 1.44')
    a = input('who are you(type it in please)')
    print('hi ' + a)
    input('you are cool[click enter to continue]')
    haha = input('type in a joke ')
    input('hahahaha, that is sooo funny[click enter]')
    b = input('lets be friends, i have a riddle for you,what can read fast but can not read books?[type aneser on the side')
    print('a computer!!!')
    # math man!!!
    c = input('lets do some math, what is 2*2*2*2*2*30000')
    print(c)
    print(32 * 30000)
    print('i hope you got it right!')
    # guess game
    print('lets play a guess game, try to pick the same number as i did[it is a one digit number')
    secret_number = 2
    guess_count = 0
    guess_limit = 3
    isGreatJob = False
    while guess_count < guess_limit:
        guess =int(input("guess"))
        if guess == secret_number:
            print('you did it!!!great job!!!')
            isGreatJob = True
            break
        guess_count += 1
    if not isGreatJob:
        print('nice try, but it was 2')
    # symbol thingie
    input('ok, lets do secret code, i did this with my friend george once, if you type in :), it means your happy, :( means you are sad(click enter)')

    message = input('>')
    words = message.split(' ')
    emoji = {":)" : 'yay,you are happy',
             ":(": 'aww,you are sad'
    }
    for word in words:
        output = ""
        output += emoji.get(word, word) + ' '
        print(output)
    print('now watch these videos, they are my favorite songs!!!https://www.youtube.com/watch?v=LT_XUvaYIEk and https://www.youtube.com/watch?v=w2Ov5jzm3j8')

    import random

    yo = (
    'the floss', 'orange justice', 'the worm', 'ride the pony', 'breakin', 'disco fever', 'take the l', 'swole cat')
    print(
        'now, lets play another fun game, i will tell you a random fortnite dance, if you do not know it then go to this link- https://www.youtube.com/watch?v=YQhprWbyQD8&t=81s (click enter to see what danct you got')
    print('and you got ' + random.choice(yo))
except ValueError:
    print('you need to put in a right value, so you have to redo it. sorry about that.')
    # things before ext man
exit('sit tight, updates are coming!!!')