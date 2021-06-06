# FileSearch


Instructions
- Print out all files with same extension from a directory of your choice

Topic Displayed
- file search


```python
import os                                                            
import glob                                                          
                                                                     
                                                                     
# print out the list of contents in a directory of your chose        
path = os.listdir('/Users/cianikaingram/Desktop/Data')               
for p in path:                                                       
    print(p)                                                         
                                                                     
                                                                     
# print out all sql files in directory                               
import glob, os                                                      
os.chdir("/Users/cianikaingram/Desktop/Data")                        
for file in glob.glob("*.sql"):                                      
    print(file)                                                      
                                                                     
```
