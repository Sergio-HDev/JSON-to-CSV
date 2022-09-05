import sys
import pandas as pd
import time


def transform(input: str, output: str) -> str:
    """
    Function 'transform' which takes two string arguments (input, output) and returns 'export_name'.
    This function takes a JSON file and convert it into a CSV file.
    """

    df = pd.read_json(str(input))   # create dataframe with input json

    export_name = r"{}".format(str(output)) # format output to raw string
    if export_name.rfind(".csv") != -1: # check if output name has ".csv"
        export_name = export_name
    else:   # if not, add ".csv" to the name
        export_name = export_name + ".csv"

    df.to_csv(export_name, index=None) # export dataframe to csv

    return export_name


if __name__ == "__main__":  # this checks if program is being used as script
    start = time.perf_counter()
    try:
        export_name = transform(sys.argv[1], sys.argv[2])    # if there are two arguments
    except IndexError:
        export_name = transform(sys.argv[1], sys.argv[1][:sys.argv[1].rfind(".json")])   # if not, output name is input name without '.json'. Then, transform adds '.csv'
    finally:
        end = time.perf_counter()
        time_elapsed = end - start  # timer for execution
        print("\nSuccesfully converted to {} in {:.5f}s\n".format(export_name, time_elapsed))
