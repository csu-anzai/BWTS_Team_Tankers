import pandas as pd

def combination(filename1, filename2):
    # load the different files in the Dataframe
    file1 = pd.read_csv(filename1)
    file2 = pd.read_csv(filename2)

    # combine the two files into one
    # also save the Dataframe as a CSV file
    result = pd.concat([file2, file1],sort=True)
    result.to_csv('E_combined.csv', index=False)
    print("Done")

combination("E_combined.csv" , "../dataset/Team Tosca/E_2019_08_23__13_50_24.csv")
