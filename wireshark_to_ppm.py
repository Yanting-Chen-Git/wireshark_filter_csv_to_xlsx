import subprocess
import os
import tkinter as tk
from tkinter import messagebox

################################################################################
#------ please ensure that the below file keywords and paths are correct ------#
################################################################################

# wireshark_filtered.py
wireshark_filtered_script_path = r'path' # Call the wireshark_filtered.py script after processing
keywords = ["220_TEST", "abc"] #filtered file name keywords
os.environ['KEYWORDS'] = ','.join(keywords) # Join the keywords into a string and set as an environment variable
os.environ['WIRESHARK_FILTERED_INPUT_PATH'] = r'path'
os.environ['WIRESHARK_FILTERED_OUTPUT_PATH'] = r'path'
filter_expr = '((ptp.v2.messagetype == 0x0) && (eth.src == 00:00:00:00:00:00)) || ((ptp.v2.messagetype == 0x8) && (eth.src == 00:00:00:00:00:00))' # Define the filter expression
os.environ['FILTER_EXPR'] = filter_expr  # Set the filter expression as an environment variable

# main.py  purpose : converter .filtered .pcapng to ppm .csv
main_script_path = r'path'  # Call the main.py script after processing

# csv_to_xlsx.py
csv_to_xlsx_script_path = r'path' # Call the csvtoxlsx.py script after main.py completes
os.environ['CSV_TO_XLSX_INPUT_PATH'] = r'path' # Set the source folder (location of CSV files)
os.environ['CSV_TO_XLSX_OUTPUT_PATH'] = r'path' # Set the destination folder (to save the converted Excel files)

#Reminder: must to check the wireshark_filter.py & csvtoxlsx.py input/output folder path.#


################################################################################
#------ please ensure that the above file keywords and paths are correct ------#
################################################################################

# Call the wireshark_filtered.py script after processing
#wireshark_filtered_script_path = r'path'
try:
    subprocess.run(["python", wireshark_filtered_script_path], check=True)
    print("Successfully executed wireshark_filtered")
except subprocess.CalledProcessError as e:
    print(f"Failed to execute wireshark_filtered: {e}")


# Call the main.py script after processing
#main_script_path = r'path'
try:
    subprocess.run(["python", main_script_path], check=True)
    print("Successfully executed main.py")
except subprocess.CalledProcessError as e:
    print(f"Failed to execute main.py: {e}")

# Call the csvtoxlsx.py script after main.py completes
#csv_to_xlsx_script_path = r'path'
try:
    subprocess.run(["python", csv_to_xlsx_script_path], check=True)
    print("Successfully executed csv_to_xlsx_script_path")
except subprocess.CalledProcessError as e:
    print(f"Failed to execute csv_to_xlsx_script_path: {e}")
'''
    # This function will be used to display a "Conversion Completed" message
def show_completion_message():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showinfo("Completion", "All files have been processed and conversion is complete.")
    root.destroy()

# Display the "Conversion Completed" window
show_completion_message()
'''
