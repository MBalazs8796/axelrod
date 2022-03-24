import importlib
import inspect
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-g', '--game_len', required=True, metavar='', help='How many games should be played between players?')
    arg_parser.add_argument('-m', '--match_len', required=True, metavar='', help='How long should a game be?')
    args = arg_parser.parse_args()

    classes = list()

    module = importlib.import_module("players")
    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            if obj.__name__ not in ["ABC", "Player"]:
                classes.append(
                    {
                        'class' : obj,
                        'wins' : 0,
                        'won_against' : list(),
                        'lost_against' : list()
                    }
                )

    for i in range(len(classes)):
        for j in range(len(classes)):
            if i != j:
                p1_score = 0
                p2_score = 0
                for _ in range(int(args.game_len)):
                    if match(classes[i]['class'], classes[j]['class'], int(args.match_len)):
                        p2_score += 1
                    else:
                        p1_score += 1
                
                if p1_score >= p2_score:
                    classes[i]['wins'] += 1
                    classes[i]['won_against'].append(classes[j]['class'].__name__)
                else:
                    classes[i]['lost_against'].append(classes[j]['class'].__name__)


    print(classes)

def match(p1, p2, len):
    p1_instance = p1()
    p2_instance = p2()

    p1_score = 0
    p2_score = 0

    for _ in range(len):
        m1 = p1_instance.move()
        m2 = p2_instance.move()
        
        p1_instance.learn(m1)
        p2_instance.learn(m2)

        if m1 + m2 == 2:
            p1_score += 6
            p2_score += 6

        elif m1 + m2 == 0:
            p1_score += 2
            p2_score += 2
        else:
            if m1 == 1:
                p2_score += 8
            else:
                p1_score += 8
    
    return p1_score < p2_score

if __name__ == "__main__":
    main()