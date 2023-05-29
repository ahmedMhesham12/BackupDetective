# BackupDetective
The BackupDetective script is a Python tool designed to detect the availability of backup files for a given list of domains. It generates various backup file names based on the domain name and checks their availability by sending HTTP requests to the corresponding URLs.

The script takes a file containing a list of domains as input and processes each domain individually. It removes common prefixes like "https://", "http://", and "www." from the domains before generating the backup file names. It then checks the availability of each backup file URL by sending a GET request and examining the response status code. If a backup file URL returns a status code of 200, it is considered available.

The script supports a wide range of backup file extensions, including common compression formats (e.g., zip, tar.gz), database dumps, log files, text files, images, and more. It generates all possible backup file names by combining the domain name with the supported extensions.

The output of the script includes the domain and the available backup file names, providing valuable information about potential backup file exposures. This can be useful for security audits, vulnerability assessments, or simply identifying unintentionally exposed backup files on websites.

The BackupDetective script offers flexibility by allowing users to provide a domain list file as a command-line argument, enabling batch processing of multiple domains in a single execution. The script is implemented using Python and utilizes the requests library to send HTTP requests.

Use the BackupDetective script to enhance your backup file detection capabilities and ensure the security of your web applications and infrastructure

```
python BackupDetective.py domainlist.txt
```
