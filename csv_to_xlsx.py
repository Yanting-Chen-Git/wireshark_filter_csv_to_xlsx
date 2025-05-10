import os
import win32com.client as win32
################################################################################
#------ please ensure that the below file keywords and paths are correct ------#
################################################################################

'''
# csv_to_xlsx.py  if only execute csv_to_xlsx.py, please enable below
csv_to_xlsx_script_path = r'path' # Call the csvtoxlsx.py script after main.py completes
os.environ['CSV_TO_XLSX_INPUT_PATH'] = r'path' # Set the source folder (location of CSV files)
os.environ['CSV_TO_XLSX_OUTPUT_PATH'] = r'path' # Set the destination folder (to save the converted Excel files)
'''

input_folder = os.environ.get('CSV_TO_XLSX_INPUT_PATH')
output_folder = os.environ.get('CSV_TO_XLSX_OUTPUT_PATH')

################################################################################
#------ please ensure that the above file keywords and paths are correct ------#
################################################################################


# 🏗️ Create the destination folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"📁 Destination folder created: {output_folder}")

# 🏃 Launch the Excel application
excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False  # Set to True if you want to see Excel during the process

# 🔄 Iterate through all CSV files in the source folder and convert them
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        csv_path = os.path.join(input_folder, filename)
        excel_path = os.path.join(output_folder, filename.replace('.csv', '.xlsx'))

        try:
            # 📁 Open the CSV file and save it as an Excel file (.xlsx) in the destination folder
            workbook = excel.Workbooks.Open(csv_path)
            workbook.SaveAs(excel_path, FileFormat=51)  # FileFormat=51 represents .xlsx format
            workbook.Close(SaveChanges=False)
            print(f"✅ Successfully converted {filename} and saved to: {excel_path}")
        except Exception as e:
            print(f"❌ Error occurred while converting {filename}: {e}")

# 🚪 Close the Excel application
excel.Quit()
print("\n🎉 All CSV files have been successfully converted and saved to the specified folder!")
