import subprocess
import os
import tkinter as tk
from tkinter import messagebox

################################################################################
#------ please ensure that the below file keywords and paths are correct ------#
################################################################################


'''
# wireshark_filtered.py
wireshark_filtered_script_path = r'D:\yanting\Desktop\AutotestNode\wireshark_filtered.py' # Call the wireshark_filtered.py script after processing
keywords = ["219_TEST_00001_20250219101647", "abc"] #filtered file name keywords
os.environ['KEYWORDS'] = ','.join(keywords) # Join the keywords into a string and set as an environment variable
os.environ['WIRESHARK_FILTERED_INPUT_PATH'] = r'E:\ptp_pcap'
os.environ['WIRESHARK_FILTERED_OUTPUT_PATH'] = r'D:\yanting\Desktop\AutotestNode\testcases\common\integrationtest\hcp5_14p_ptp_captured_packets'
filter_expr = '((ptp.v2.messagetype == 0x0) && (eth.src == 02:7d:fa:00:10:01)) || ((ptp.v2.messagetype == 0x8) && (eth.src == 02:7d:fa:00:10:01))' # Define the filter expression
os.environ['FILTER_EXPR'] = filter_expr  # Set the filter expression as an environment variable
'''

# Get the keywords from the environment variable and split into a list
keywords_arg = os.environ.get('KEYWORDS', '')
keywords = keywords_arg.split(',')
input_folder = os.environ.get('WIRESHARK_FILTERED_INPUT_PATH')
output_folder = os.environ.get('WIRESHARK_FILTERED_OUTPUT_PATH')
filter_expr = os.environ.get('FILTER_EXPR', '')

#Reminder: must to check the wireshark_filter.py & csvtoxlsx.py input/output folder path.#

################################################################################
#------ please ensure that the above file keywords and paths are correct ------#
################################################################################



def filter_multiple_pcaps(input_folder, output_folder, filter_expression):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Add a check to confirm the input folder exists
    if not os.path.exists(input_folder):
        print(f"The input folder does not exist: {input_folder}")
        return

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the filename contains any of the specified keywords
        #if filename.endswith(".pcap") or filename.endswith(".pcapng"):
        if any(keyword in filename for keyword in keywords):
            input_file = os.path.join(input_folder, filename)
            
            # Ensure output filename ends with .pcapng
            output_filename = f"filtered_{filename}.pcapng"
            output_file = os.path.join(output_folder, output_filename)

            # Construct the tshark command
            command = [
                "tshark",
                "-r", input_file,
                "-Y", filter_expression,
                "-w", output_file
            ]

            # Execute the tshark command
            subprocess.run(command, check=True)
            print(f"Filtered {filename} and saved to {output_file}")

# Run the filtering function
filter_multiple_pcaps(input_folder, output_folder, filter_expr)

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