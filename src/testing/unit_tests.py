import unittest
import difflib
import sys
import os
from dotenv import load_dotenv
sys.path.append('../')

import text_to_sql_api as f
from text_to_sql_api import *

load_dotenv("../config.env")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")
HOST = os.getenv("DB_HOST")
PASSWORD = os.getenv("DB_PASSWORD")


f.config["password"] = PASSWORD
f.config["host"] = HOST
f.config['user'] = DB_USER
f.headers['Authorization'] = AUTH_TOKEN

f.config['database'] = f.database_M
f.data['schema'] = f.schema_M


class TestTextToSQL(unittest.TestCase):
    def test_changeDB(self):
        self.assertEqual(f.DB_LOADED, "metabolic_syndrome")
        self.assertEqual(f.SCHEMA, "metabolic_syndrome (seqn: int, Age: int, Sex: text, Marital: text, Income: text, Race: text, WaistCirc: double, BMI: double, Albuminuria: int, UrAlbCr: double, UricAcid: double, BloodGlucose: int, HDL: int, Triglycerides: int, MetabolicSyndrome: int)")
        swapDB()
        self.assertEqual(f.DB_LOADED, "financial")
        self.assertEqual(f.SCHEMA,"indexprocessed (Index: text, Date: text, Open: double, High: double, Low: double, Close: double, Adj Close: double, Volume: double, CloseUSD: double)")
        swapDB()
        self.assertEqual(f.DB_LOADED, "metabolic_syndrome")
        self.assertEqual(f.SCHEMA, "metabolic_syndrome (seqn: int, Age: int, Sex: text, Marital: text, Income: text, Race: text, WaistCirc: double, BMI: double, Albuminuria: int, UrAlbCr: double, UricAcid: double, BloodGlucose: int, HDL: int, Triglycerides: int, MetabolicSyndrome: int)")

    def test_toSQL_MEDICAL(self):
        f.config['database'] = f.database_M
        f.data['schema'] = f.schema_M

        example_prompt = "how many age are under 40"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*)  FROM metabolic_syndrome  WHERE Age < 40;"))

        example_prompt = "how many have a marital status of single"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*)  FROM metabolic_syndrome  WHERE Marital = 'Single';"))

        example_prompt = "show me all the records for Males"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT *  FROM metabolic_syndrome  WHERE Sex = 'Male';"))


    def test_toSQL_FINANCIAL(self):
        f.config['database'] = f.database_F
        f.data['schema'] = f.schema_F
    
        example_prompt = "how many have a high price greater than 700"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*) FROM indexprocessed WHERE High > 700;"))
        
        example_prompt = "how many close at over 2000"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT COUNT(*) FROM indexprocessed WHERE Close > 2000;"))

        example_prompt = "what trades have 0 volume"
        self.assertEqual(True, string_similar(toSQL(example_prompt), "SELECT * FROM indexprocessed WHERE Volume = 0;"))

def string_similar(string1, string2, threshold=0.8):
    similarity = difflib.SequenceMatcher(None, string1, string2).ratio()
    
    if similarity < threshold:
        print("\n" + string1 + " != " + string2)
   
    return similarity >= threshold
        
if __name__ == '__main__':
    unittest.main()