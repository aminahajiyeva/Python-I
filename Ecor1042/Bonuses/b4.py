# Exersise 1:
"""
user_values = []
Q = True
while Q:
        user = input("please enter integer values, once complete press Q to exit the program ")
        if user.upper() == 'Q':
                Q = False
        else:
                user_values.append((user))
print("questions complete")

for i in range(len(user_values)):
        min_idx = i
        for j in range(i + 1, len(user_values)):
                if user_values[min_idx] < user_values[j]:
                        min_idx = j
        user_values[i], user_values[min_idx] = user_values[min_idx], user_values[i]

print(user_values)

"""
# Exersise 2:
#insertion_sort_books([(2005, "Second Book", 5),(1999, "First Book", 1),(2023,"Third Book", 3)], "rating")
def insertion_sort_books(books: list, sort: str):

        if sort.lower() == "year":
                for i in range(1, len(books)):
                        key = books[i]
                        j = i - 1
                        while j >= 0 and key < books[j]:
                                books[j + 1] = books[j]
                                j -= 1
                        books[j + 1] = key

        elif sort.lower() == "book":
                for i in range(0, len(books)):
                        key = books[i][1]
                        j = i - 1
                        while j >= 0 and key <= books[j - 1][1]:
                                books[j + 1] = books[j]
                                j -= 1
                        books[j + 1] = key
        elif sort.lower() == "rating":
                for i in range(1, len(books)):
                        key = books[i]
                        j = i - 1
                        while j >= 0 and key < books[j]:
                                books[j + 1] = books[j]
                                j = 1
                        books[j + 1] = key
                books.reverse() == books


        return books