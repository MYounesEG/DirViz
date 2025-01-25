# DirViz

This Python script allows you to visualize the directory tree structure of a specified root directory and display the content of all files within that directory and its subdirectories. It saves the output to a text file named `Summary.txt`, which can also be used to assist AI applications in understanding your project's structure and solving related problems.

---

## Features

- **Display Directory Tree**: Visualize your project's folder structure in an organized and readable tree format.
- **Display File Contents**: Automatically read and display the contents of files in the specified directory.
- **Save Output**: The script saves the entire directory tree and file content details into a `Summary.txt` file for documentation purposes.
- **AI-Friendly Project Summary**: The `Summary.txt` file can be used to explain your project to AI applications, such as ChatGPT or other intelligent systems, enabling them to understand your project and help solve specific problems.

---

## Usage

1. **Run the script**:
   ```bash
   python DirViz.py
   ```
2. **Provide the root directory**: 
    When prompted, enter the path to the root directory you wish to analyze.

3. **View the output**:
    When prompted, enter the path to the root directory you wish to analyze.

## Example Output
### Directory Tree
```mathematica
ProjectRoot
│   ├── main.py
│   ├── utils
│   │   ├── helper.py
│   │   ├── data_processor.py
│   │   └── config.json
│   ├── templates
│   │   ├── index.html
│   │   └── layout.html
│   └── static
│       ├── css
│       │   └── style.css
│       ├── js
│       │   └── script.js
│       └── images
│           ├── logo.png
│           └── banner.jpg
```
### File Content
```ruby
# ProjectRoot/main.py
import os

def main():
    print("Hello, world!")

if __name__ == "__main__":
    main()

--------------------------------------------------------------------------------

# ProjectRoot/utils/helper.py
def helper_function():
    return "This is a helper function."

--------------------------------------------------------------------------------

# ProjectRoot/utils/data_processor.py
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        return [item.upper() for item in self.data]

--------------------------------------------------------------------------------

# ProjectRoot/templates/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to the Home Page!</h1>
</body>
</html>

--------------------------------------------------------------------------------

# ProjectRoot/static/css/style.css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

--------------------------------------------------------------------------------

# ProjectRoot/static/js/script.js
document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript is running!");
});
```

## Benefits of Using `Summary.txt`

<ul>
  <li>
    <strong>AI Assistance</strong>: Share <code>Summary.txt</code> with AI tools
    (e.g., ChatGPT, Copilot) to explain your project's structure and code. This
    helps the AI understand your project's context, making it easier to debug,
    solve problems, or generate new features.
  </li>
  <li>
    <strong>Collaboration</strong>: Use it as a quick reference for team members
    unfamiliar with the project's structure.
  </li>
  <li>
    <strong>Documentation</strong>: Maintain a clear, up-to-date record of your
    project's layout and contents for future use.
  </li>
</ul>

## Notes

<ul>
  <li>
    The script gracefully handles errors, such as invalid directory paths or
    unreadable files.
  </li>
  <li>
    It sorts directories and files for clarity, displaying directories first.
  </li>
  <li>
    The <code>Summary.txt</code> file is overwritten each time the script is
    run, ensuring it always contains the latest information.
  </li>
</ul>

## Example Scenarios
<ol>
  <li>
    <strong>Troubleshooting Code</strong>: When debugging, provide
    <code>Summary.txt</code> to AI tools to help them better understand how
    files relate to each other in your project.
  </li>
  <li>
    <strong>Team Collaboration</strong>: Share <code>Summary.txt</code> with
    your team for a quick overview of the project.
  </li>
  <li>
    <strong>Project Onboarding</strong>: New team members can use the file to
    familiarize themselves with the project's layout and content.
  </li>
</ol>
