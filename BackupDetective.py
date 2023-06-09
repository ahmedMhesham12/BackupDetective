import sys
import requests

def generate_backup_file_names(domain):
    backup_extensions = [
        '',
        '.bak', '.backup',
        '.old', '.old1', '.old2',
        '.bkp', '.bkup', '.bck',
        '.zip', '.tar', '.tar.gz', '.tar.bz2', '.tgz', '.tbz2',
        '.gz', '.bz2', '.rar', '.7z',
        '.sql', '.sql.gz', '.sql.bz2',
        '.db', '.db.gz', '.db.bz2',
        '.dump', '.dump.gz', '.dump.bz2',
        '.log', '.log.gz', '.log.bz2',
        '.txt', '.txt.gz', '.txt.bz2',
        '.dat', '.dat.gz', '.dat.bz2',
        '.csv', '.csv.gz', '.csv.bz2',
        '.xls', '.xls.gz', '.xls.bz2',
        '.xlsx', '.xlsx.gz', '.xlsx.bz2',
        '.mdb', '.mdb.gz', '.mdb.bz2',
        '.accdb', '.accdb.gz', '.accdb.bz2',
        '.json', '.json.gz', '.json.bz2',
        '.xml', '.xml.gz', '.xml.bz2',
        '.html', '.html.gz', '.html.bz2',
        '.htm', '.htm.gz', '.htm.bz2',
        '.php', '.php.gz', '.php.bz2',
        '.asp', '.asp.gz', '.asp.bz2',
        '.jsp', '.jsp.gz', '.jsp.bz2',
        '.css', '.css.gz', '.css.bz2',
        '.js', '.js.gz', '.js.bz2',
        '.jpg', '.jpeg', '.png', '.gif', '.bmp',
        '.mp3', '.mp4', '.avi', '.mkv', '.mov',
        '.doc', '.docx', '.ppt', '.pptx', '.pdf'
    ]

    backup_file_names = []

    for extension in backup_extensions:
        backup_file_names.append(f"{domain}/{domain}{extension}")

    return backup_file_names

def check_backup_files(domain_list):
    for domain in domain_list:
        domain = domain.strip()  # Remove leading/trailing whitespace
        domain = domain.replace("https://", "").replace("http://", "").replace("www.", "")
        backup_files = generate_backup_file_names(domain)

        for file_name in backup_files:
            url = f"http://{file_name}"
            response = requests.get(url)

            if response.status_code == 200:
                print(f"{domain}/{file_name}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a domain list file as an argument.")
        sys.exit(1)

    domain_file_name = sys.argv[1]

    try:
        with open(domain_file_name, 'r') as domain_file:
            domain_list = domain_file.readlines()
            check_backup_files(domain_list)
    except FileNotFoundError:
        print(f"Domain list file '{domain_file_name}' not found.")
        sys.exit(1)
