import pandas as pd
#Replace ; with :
file_name = "E_2019_08_23__13_50_24.csv"
def replace_to_comma(data):
    text = open(data, "r")
    text = ''.join([i for i in text]) \
        .replace(";", ",")
    x = open(file_name, "w")
    x.writelines(text)
    x.close()
    drop_a()

#Drop the empty column
def drop_a():
    file = pd.read_csv(file_name)

    del file['a']

    file.to_csv(file_name,index=False)

# replace_to_comma("../dataset/Team Tosca/E_2019_08_23__13_50_24.csv")


#Add a team column

file = pd.read_csv("../dataset/Team Toccata/E_2019_03_18__07_11_07.csv")

file.insert(4,"Team", "Team Toccata")
file.to_csv("E_2019_03_18__07_11_07.csv", index=False)
