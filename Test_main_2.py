#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import main 
class Testmain(unittest.TestCase):
 
    def test_load_dataset(self):
        pathCSV = r'/Users/saikatduttatanu/Desktop/Coding/SoftwareTechnologies/Project Final/Crash Statistics Victoria.csv'
 
        with open(pathCSV, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for item in row:
                    try:
                        getattr(Victoria.myClass, item)()
                    except AttributeError:
                        print("Unknown attribute", item, "ignored")
 
    @staticmethod
    def test_load_dataset():
        load_dataset = unittest.TestSuite()
        load_dataset.addTest(Testmain('completeTest'))
        return load_dataset
 
if __name__== "__main__":
    runner.run(Victoria.TestFinals.load_dataset())

