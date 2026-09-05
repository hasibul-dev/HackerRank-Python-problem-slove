import operator

def person_lister(f):
    def inner(people):
        # Sort by age (index 2) converted to int using itemgetter or a key function
        # Python's sorted() is stable, preserving input order for equal ages
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
