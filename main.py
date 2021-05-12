import scrapper as sc
import predictions as pre
import statistics as st

default = True
s = sc.Scrapper()
p = pre.Prediction()
stats = st.Statistics()


def commands():
    coms = "/createLinks          --> Creating links for drivers standings and constructor standings\n" \
            "/editLinks            --> Editing the links for driver standings and constructor standings\n" \
            "/viewStandings        --> View the current standings for driver standings and constructor standings\n" \
            "/makeNewPrediction    --> Add a new prediction of how the drivers and teams will rank\n" \
            "/addAnotherPrediction --> Adding another prediction of how the drivers and teams will rank\n" \
            "/viewPrediction       --> Viewing a prediction\n" \
            "/deletePrediction     --> Delete a prediction\n" \
            "/showZeros            --> Show the number of teams/drivers who have not gained points\n" \
            "/calculateScore       --> Calculate the inaccuracy score for the predictions\n" \
            "/end                  --> Ends the program"
    return coms


while default:
    response = input("What would you like to access: ")
    if response == "/createLinks":
        s.create_links()
        print("Links created")
    elif response == "/commands":
        print(commands())
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
    elif response == "/showZeros":
        response = input("Driver or Team?(d/t) ")
        if response == "d":
            print(stats.check_stats().initialise_stats().count_driver_zeros())
        elif response == "t":
            print(stats.check_stats().initialise_stats().count_team_zeros())
    elif response == "/calculateScore":
        print("driver")
        print("---------")
        stats.check_stats().initialise_stats().calculate_all_deviation("driver")
        print("team")
        print("---------")
        stats.check_stats().initialise_stats().calculate_all_deviation("team")
    elif response == "/end":
        print("Ending Program...")
        default = False
    else:
        print("Wrong Command... Please try a valid command")
