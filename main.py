import scrapper as sc
import predictions as pre

default = True
s = sc.Scrapper()
p = pre.Prediction()

while default:
    response = input("What would you like to access: ")
    if response == "/createLinks":
        s.create_links()
        print("Links created")
    elif response == "/editLinks":
        s.edit_links()
    elif response == "/viewStandings":
        s.initialise_links()
        if s.driver == "" or s.constructor == "":
            print("Please initialise links first!")
        else:
            print(s.scrape_driver())
            print(s.scrape_constructor())
    elif response == "/makeNewPrediction":
        p.create_predictions()
        print("New prediction created.")
    elif response == "/addAnotherPrediction":
        p.add_predictions()
        print("New prediction created.")
    elif response == "/viewPrediction":
        name = input("Whose Prediction would you like to view? ")
        result = p.initialise_prediction().view_prediction(name)
        if type(result) == dict:
            print(result)
    elif response == "/deletePrediction":
        name = input("Whose Prediction would you like to delete? ")
        p.initialise_prediction().delete_prediction(name)
    elif response == "/end":
        print("Ending Program...")
        default = False
    else:
        print("Wrong Command... Please try a valid command")