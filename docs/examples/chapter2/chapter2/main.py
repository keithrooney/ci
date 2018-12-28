import os
import json

from ci import recommendations


with open(os.path.join(os.path.dirname(__file__), "resources", "recommendations.json")) as fp:
    critics = json.load(fp)


def transform(critic, other):
    return [(critic[key], other[key]) for key in sorted(critic.keys() & other.keys())]


def run():
    names = sorted(critics.keys())
    for i in range(0, len(names)):
        critic = names[i]
        for j in range(i + 1, len(names)):
            other = names[j]
            score = recommendations.euclidean_distance(*zip(*transform(critics[critic], critics[other])))
            print("{0},{1},{2}".format(critic, other, score))


if __name__ == "__main__":
    run()
