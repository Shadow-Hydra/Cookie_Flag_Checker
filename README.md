#Cookie Flags Checker


This script checks the presence of the secure and httponly flags in cookies for a given list of domains. It uses the "aiohttp" library for asynchronous HTTP requests.

Disclaimer: This script is intended for educational and ethical purposes only. By using this script, you agree that you are solely responsible for any actions you take. Be sure to use this script responsibly and in compliance with applicable laws and regulations.

Usage:

Clone the repository or download the code files.

Install the required dependencies by running the following command:
Copy code
pip install aiohttp
Prepare a text file (gov_url_final_result) containing a list of domains, with each domain on a separate line.
Update the session_ids list in the code if needed, to include the session ID names you want to check. By default, the script checks the following session IDs:
ASP.NET_SessionId
PHPSESSID
JSESSIONID
Run the script using the following command:
Copy code
python your_script_name.py
Make sure to replace your_script_name.py with the actual name of your script file.
The script will check each domain in the list and print the results indicating if the secure and httponly flags are present or missing for each session ID. The results will also be written to the console.
Note: The script uses asyncio and aiohttp to perform asynchronous HTTP requests, which can improve the overall performance when checking multiple domains.

Contributing
If you have any suggestions, improvements, or bug fixes, please feel free to contribute! Fork the repository, make your changes, and submit a pull request.

