import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

Data_File_Path = '/config/workspace/aps_failure_training_set1.csv'
Database_Name = 'aps'
Collection_Name = 'sensor'

if __name__ == "__main__":
    df = pd.read_csv(Data_File_Path)
    print(f"Rows and Columns: {df.shape}")

    # convert csv to Json to insert into MongoDB

    df.reset_index(drop =True,inplace = True)
    Json_record = list(json.loads(df.T.to_json()).values())
    print(Json_record[0])

    # insert Json_record to MongoDB
    client[Database_Name][Collection_Name].insert_many(Json_record)