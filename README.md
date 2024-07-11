
# Automated Google Forms Submission

This Python script automates the process of filling out and submitting a Google Form multiple times using Selenium WebDriver.

## Features

- **Form Filling**: Automatically fills out specific elements of the Google Form.
- **Submission**: Submits the form and waits for confirmation.
- **Looping**: Iteratively submits the form multiple times.

## Requirements

- Python 3.6 or higher
- `selenium` library (`pip install selenium`)
- Chrome browser
- ChromeDriver compatible with your Chrome browser version (automatically managed by `webdriver_manager`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/google-forms-automation.git
   cd google-forms-automation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Modify `fillForms(driver)` function in `google_forms_automation.py` to fill out the Google Form according to your specific requirements.

2. Run the script `google_forms_automation.py`:

   ```bash
   python google_forms_automation.py
   ```

   - The script opens the Google Form URL specified (`url` variable in `main()` function).
   - It fills out the form repeatedly (`for` loop in `main()`) and submits it each time.

## Script Workflow

1. **Setup**: Sets up the Chrome WebDriver with necessary options (`--window-size=1920,1080`).
2. **Form Access**: Opens the specified Google Form URL (`url` variable).
3. **Form Filling**: Iteratively fills out form elements using Selenium WebDriver.
4. **Submission**: Submits the form after filling it out.
5. **Loop**: Repeats the above steps for the specified number of iterations (`for` loop in `main()`).
6. **Cleanup**: Closes the WebDriver and quits the browser.

## Notes

- **WebDriver Manager**: Uses `ChromeDriverManager` from `webdriver_manager` to automatically manage the ChromeDriver executable.
- **Sleep Intervals**: Includes `time.sleep()` calls to ensure elements are fully loaded before interaction. Adjust these intervals based on your network speed and system performance.
- **Error Handling**: Basic error handling (`try...except`) is implemented to catch and print any exceptions during form filling and submission.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

