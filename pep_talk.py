import random


def pep_talk():
    """
    Designed to automate the pep talk generator built by Raccoon Society
    at https://theraccoonsociety.com/
    and posted on social media.
    """
    pep1 = ['Champ', 'Fact:', 'Everybody says', 'Dang...', 'Check it:',
            'Just saying...', 'Superstar', 'Tiger,', 'Self,',
            'Know this...', 'News alert:', 'Girl,', 'Ace,',
            'Excuse me but', 'Experts agree:', 'In my opinion',
            'Hear ye, hear ye:', 'Okay, listen up']
    pep2 = ['the mere idea of you', 'your soul', 'your hair today',
            'everything you do', 'your personal style',
            'every thought you have', 'what you got going on',
            'that sparkle in your eye', 'your presence here',
            'the essential you', "your life's journey",
            'that saucy personality', 'your DNA', 'that brain of yours',
            'your choice of attire', 'the way you roll',
            'whatever your secret is', "all of y'all"]
    pep3 = ['has serious game,', 'rains magic,', 'deserves the Nobel Prize,',
            'raises the roof,', 'breeds miracles,', 'is paying off big time,',
            'just shimmers,', 'is a national treasure,',
            'gets the party hopping,', 'is the next best thing,',
            'roars like a lion,', 'is a rainbow factory,',
            'is made of diamonds,', 'makes birds sing,',
            'should be taught in school,', "makes my world go 'round,",
            'is 100% legit,']
    pep4 = ['24/7.', 'can I get an amen?', "and that's a fact.",
            'so treat yourself.', 'you feel me?', "that's just science.",
            'would I lie?', 'for reals.', 'mic drop.', 'you hidden gem.',
            'snuggle bear.', 'period.', 'can I get an amen?',
            "now let's dance.", 'high five.', 'say it again!',
            'according to CNN.', 'so get used to it.']
    saying = f'{random.choice(pep1)} {random.choice(pep2)} {random.choice(pep3)} {random.choice(pep4)}'
    return saying


if __name__ == '__main__':
    print(pep_talk())
