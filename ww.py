# 1-masala
def get_vote_count(votes):
    yoqqanlar = votes["upvotes"]
    yoqmaganlar = votes["downvotes"]

    return yoqqanlar - yoqmaganlar


print(get_vote_count({"upvotes": 13, "downvotes": 0}))
print(get_vote_count({"upvotes": 2, "downvotes": 33}))
print(get_vote_count({"upvotes": 132, "downvotes": 132}))

# # 2-masala
def first_last(lst):
    return [lst[0], lst[-1]]


print(first_last([5, 10, 15, 20, 25]))
print(first_last(["edabit", 13, None, False, True]))
print(first_last([None, 4, "6", "hello", None]))
# 3-misol
def forbidden_letter(harif, royxat):
    for x in royxat:
        for i in x:
            if harif == i:
                return False

            else:
                return True

print(forbidden_letter("r", ["rock", "paper", "scissors"]))
print(forbidden_letter("a", ["spoon", "fork", "knife"]))
print(forbidden_letter("m", []))