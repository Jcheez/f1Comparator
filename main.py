import scrapper as sc

default = True
s = sc.Scrapper()
while default:
    response = input("What would you like to access: ")
    if response == "/create":
        s.create_links()
        print("Links created")
    elif response == "/edit":
        s.edit_links()
    elif response == "/result":
        s.initialise_links()
        if s.driver == "" or s.constructor == "":
            print("Please initialise links first")
        else:
            print(s.scrape_driver())
            print(s.scrape_constructor())
    elif response == "/end":
        print("Ending Program...")
        default = False
    else:
        print("Wrong Command... Please try a valid command")