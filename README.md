# JSON to CSV
This python script allows you to transform a JSON file to a CSV file. It can be used as script or a module for your projects.
Feel free to use it or make any changes for your purpose.

The code is on 'json2csv.py'.

It has a function called 'transform' which makes the conversion. This function takes two string arguments (input, output) and returns 'export_name'.

Used as script, if you want, you can pass only the input name and it generates the ouput name with the input without '.json' and ending with '.csv'. Because the names are formated as raw strings, you can add the directory you want it to be searched or stored. If output name does not have '.csv' ending, the transform function adds it.

# Examples

Example of script use on Linux:

```
python json2csv.py ../../input.json ../output.csv
```

In this example, the input file is two directories above the .py script and the output will be stored one directory above.

Example of module use:

```
import json2csv

json2csv.transform("input.json", "output")
```

In this example, the output does not have the '.csv' ending, but the program detects that and adds it.

