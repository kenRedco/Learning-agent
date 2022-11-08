import random

greetings = ["Hello!", "What's up?!", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]
check = []

keywords = ["music", "pet", "book", "game"]
responses = ["Music is so relaxing!", "Dogs are man's best friend!", "I know about a lot of books.",
             "I like to play video games."]
print(random.choice(greetings))
def chat():

    user = input("Say something (or type bye to quit): ")
    if user != "" and user != "bye":
        user = user.lower()
        check = user.split()
        for i in check:
            if (i in keywords):
                user = i
        keyword_found = True

        if (  user != "bye"):
            keyword_found = False

        for index in range(len(keywords)):
            if keywords[index] in user:
                print("Bot: " + responses[index])
                keyword_found = True

        if (keyword_found == False):
            new_keyword = input("I'm not sure how to respond. What keyword should I respond to? ")
            # keywords.insert(0,new_keyword)
            if new_keyword not in user:
                print("the keyword is not in your sentence!")
                chat()
            keywords.append(new_keyword)
            new_response = input("How should I respond to " + new_keyword + "? ")

            # responses.insert(0,new_keyword)
            responses.append(new_response)
        chat()
    else:
        print(random.choice(goodbyes))

chat()