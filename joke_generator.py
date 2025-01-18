import requests

# This joke generator uses the Official Joke API
# GitHub repository :- https://github.com/15Dkatz/official_joke_api?tab=readme-ov-file
# Website :- https://official-joke-api.appspot.com

# Other cool free API's can be found here:- https://apipheny.io/free-api/#apis-without-key

base_link = "https://official-joke-api.appspot.com/"

joke_types_link = "types"
joke_types = {
    "general": "/jokes/general/random",
    "programming": "/jokes/programming/random",
    "knock-knock": "/jokes/knock-knock/random",
    "dad": "/jokes/dad/random",
}
random_joke = "random_joke"


def main():
    while True:
        print("------------------------------\nWelcome to the Joke generator!")
        a = input(
            "Commands: \n R - Random joke \n T - View types of jokes \n RT - A random joke on entered type \n E - Exit the program \n Enter your input: "
        ).upper()

        if a == "R":
            url = base_link + random_joke
            joke = requests.get(url=url).json()
            print("------------------------------")
            print("Joke type: " + joke["type"])
            print("Joke ID: " + str(joke["id"]) + "\n")
            print(joke["setup"] + "\n")
            print(joke["punchline"] + "\n------------------------------")
        elif a == "T":
            url = base_link + joke_types_link
            types = requests.get(url).json()
            for i, type in enumerate(types):
                print(f"{i + 1}. {type.capitalize()} jokes.")

        elif a == "RT":
            joke_type = input(
                "Enter joke type(g for general,p for programming,k for knock-knock,d for dad):"
            ).lower()
            if joke_type == "g":
                url = base_link + joke_types["general"]
                joke = requests.get(url=url).json()[0]
            elif joke_type == "p":
                url = base_link + joke_types["programming"]
                joke = requests.get(url=url).json()[0]
            elif joke_type == "k":
                url = base_link + joke_types["knock-knock"]
                joke = requests.get(url=url).json()[0]
            elif joke_type == "d":
                url = base_link + joke_types["dad"]
                joke = requests.get(url=url).json()[0]

            print("------------------------------")
            print("Joke type: " + joke["type"])
            print("Joke ID: " + str(joke["id"]) + "\n")
            print(joke["setup"] + "\n")
            print(joke["punchline"] + "\n------------------------------")

        elif a == "E":
            print("Thanks for using the joke generator! Goodbye!")
            break
            quit()


if __name__ == "__main__":
    main()
