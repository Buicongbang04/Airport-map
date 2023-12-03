import pickle


class Tool:
    def saveToFile(file_name, data):
        with open(file_name, "wb") as file:
            pickle.dump(data, file)
            print("Saved file successfully!")

    def loadFromFile(file_name):
        with open(file_name, "rb") as file:
            data = pickle.load(file)
            print("Loaded file successfully!")
            return data
