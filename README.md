# HashToCrack-Report

A Python-based CLI tool to transform HashToCrack analytics text reports into visual dashboards and comprehensive markdown reports.

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)](https://github.com)

## Features
- **Automated Parsing**: Extracts cracked vs. uncracked stats, length distribution, top 10 passwords, and policy compliance directly from text reports.
- **Visual Analytics**: Generates 4 distinct PNG charts (pie and bar charts) with professional styling.
- **Report Generation**: Creates complete markdown reports with embedded base64 images.
- **Multilingual Support**: Built-in templates for English (`EN`) and Spanish (`ES`).
- **Custom Templates**: Use your own markdown templates with placeholder support.
- **Customizable Output**: Define your own output directory for generated files.

## Installation

This tool is designed to be used with [uv](https://github.com/astral-sh/uv).

### Global Install (Recommended)
You can install the tool directly from GitHub:
```bash
uv tool install git+https://github.com/fisher0x/HashToCrack-Report
```

### Local Development Install

If you have cloned the repository locally:
```bash
uv tool install .
```

## Usage

Once installed, use the `hashtocrack_report` command:

```bash
# Basic usage - generates charts and report with English template
hashtocrack_report analytics.txt

# Spanish report with custom output folder
hashtocrack_report analytics.txt -l ES -o ./reports

# Use custom template
hashtocrack_report analytics.txt -t my_template.md -o ./output

# Generate only charts without report
hashtocrack_report analytics.txt --charts-only
```

## Arguments

| Argument            | Short | Description                                      | Default  |
|---------------------|-------|--------------------------------------------------|----------|
| file                |       | Path to the analytics text file                   | Required |
| --language          | -l    | Language for built-in templates (EN or ES)        | EN       |
| --outdir            | -o    | Directory where files will be saved               | ./data   |
| --template          | -t    | Path to custom template file                      | None     |
| --charts-only       |       | Generate only charts without report               | False    |

## Output Files

The tool generates the following files in the output directory:

### Charts (PNG images):
- `general_stats.png` - Pie chart showing cracked vs not cracked passwords
- `length_distribution.png` - Bar chart of password length distribution
- `top_10_passwords.png` - Horizontal bar chart of most used passwords
- `compliance_analysis.png` - Pie chart of password policy compliance

### Report:
- `password_statistics_EN.md` or `password_statistics_ES.md` - Complete markdown report with embedded images

## Custom Templates

You can create your own markdown templates using the following placeholders:

### Available Placeholders:
- `{{TOTAL_AMOUNT_OF_CREDS}}` - Total number of credentials
- `{{RECOVERED_AMOUNT_OF_CREDS}}` - Number of cracked passwords
- `{{RECOVERED_AMOUNT_OF_CREDS_PERCENTAGE}}` - Recovery percentage
- `{{HIGHEST_PASSWORD_LENGTH_DISTRIBUTION}}` - Most common password length
- `{{SECOND_HIGHEST_PASSWORD_LENGTH_DISTRIBUTION}}` - Second most common length
- `{{COMPLIANCE_PASSWORD_PERCENTAGE}}` - Percentage of compliant passwords

### Image Placeholders:
Use the format `![Alt Text](base64/imagedata)` in your template. The tool will automatically replace these with base64-encoded images. Make sure your alt text matches one of the default chart names or use generic placeholders.

Example:
```markdown
## Password Statistics

Out of {{TOTAL_AMOUNT_OF_CREDS}} credentials, {{RECOVERED_AMOUNT_OF_CREDS}} were cracked.

![General Statistics](base64/imagedata)
```


### Generated Charts
The tool produces the following visualizations:

- General Statistics: Pie chart of cracked vs. not cracked accounts. 
- Length Distribution: Vertical bar chart showing password length frequency. 
- Top 10 Passwords: Horizontal bar chart of the most frequent passwords. 
- Compliance Analysis: Pie chart showing policy requirement adherence.
