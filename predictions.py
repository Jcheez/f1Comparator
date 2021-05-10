import json


class Prediction:
    def __init__(self):
        self.predictions = {}

    @staticmethod
    def create_predictions():
        new_file = open("predictions.txt", "w+")
        drivers = []
        teams = []
        default = True
        default2 = True
        prediction = {}
        name = input("Please input name of user making the prediction: ")
        prediction[name] = {}
        print("Input the names of driver in order from first to last")
        while default:
            driver = input("Please input surname of driver: ")
            drivers.append(driver)
            print(drivers)
            response = input("Do you have another driver to add?(y/n) ")
            if response == "n":
                default = False
        print("Input the names of teams in order from first to last")
        while default2:
            team = input("Please input name of team: ")
            teams.append(team)
            print(teams)
            response = input("Do you have another team to add?(y/n) ")
            if response == "n":
                default2 = False
        prediction[name]["drivers"] = drivers
        prediction[name]["teams"] = teams
        new_file.write(str(prediction))
        new_file.close()
        return Prediction()

    @staticmethod
    def add_predictions():
        try:
            open("predictions.txt")
        except FileNotFoundError:
            print("Please create a prediction first")
            return
        drivers = []
        teams = []
        default = True
        default2 = True
        file = open("predictions.txt")
        prediction = json.loads(file.readline().replace("\'", "\""))
        file.close()
        name = input("Please input name of user making the prediction: ")
        prediction[name] = {}
        print("Input the names of driver in order from first to last")
        while default:
            driver = input("Please input surname of driver: ")
            drivers.append(driver)
            print(drivers)
            response = input("Do you have another driver to add?(y/n)")
            if response == "n":
                default = False
        print("Input the names of teams in order from first to last")
        while default2:
            team = input("Please input name of team: ")
            teams.append(team)
            print(teams)
            response = input("Do you have another team to add?(y/n)")
            if response == "n":
                default2 = False
        prediction[name]["drivers"] = drivers
        prediction[name]["teams"] = teams
        file = open("predictions.txt", "w+")
        file.write(str(prediction))
        file.close()
        return Prediction()

    def initialise_prediction(self):
        try:
            file = open("predictions.txt")
            self.predictions = json.loads(file.readline().replace("\'", "\""))
            file.close()
            return self
        except FileNotFoundError:
            print("Please create a prediction first")
            return self

    def view_prediction(self, name):
        if name in self.predictions:
            return self.predictions[name]
        else:
            print("User has not keyed in a prediction")
            return self

    def delete_prediction(self, name):
        if name in self.predictions:
            del self.predictions[name]
            file = open("predictions.txt", "w+")
            file.write(str(self.predictions))
            file.close()
            print("Prediction deleted!")
            return self
        else:
            print("Name is not found")
            return self
