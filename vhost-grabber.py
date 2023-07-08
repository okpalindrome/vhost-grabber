import requests
import os
import argparse


def trim_url(url):
    url = url.replace("http://","").replace("https://","")

    if url.endswith("/"):
        url = url[:-1]

    parts = url.split("/")
    valid_domain = parts[0]

    return valid_domain


def censys_scan(target, scan_type):
    next = ""
    while True:
        parameters = {'per_page':100, 'virtual_hosts':scan_type, 'q':target, 'cursor':next}
        url = 'https://search.censys.io/api/v2/hosts/search'
        headers = {'Accept':'application/json'}
        CENSYS_API_ID = os.environ.get('CENSYS_API_ID')
        CENSYS_API_SECRET = os.environ.get('CENSYS_API_SECRET')

        auth = (CENSYS_API_ID, CENSYS_API_SECRET)

        response = requests.get(url, params=parameters, headers=headers, auth=auth)

        if response.status_code == 200:
            data = response.json()
            
            if 'result' in data and 'total' in data['result']:
                print("Found total vhosts -> " + str(data["result"]['total']))
                print("---------------------------------------------------------------")
        
            hits = data["result"]["hits"]

            for hit in hits:
                if 'name' in hit:
                    print(hit['name'])
                # If domain name is not present, print it's IP
                elif 'ip' in hit:
                    print(hit['ip'])

        
            if 'links' in data and 'next' in data['links']:
                next = data["links"]["next"]
                print(next)
            else:
                break
        else:
            print('something went wrong!')
            print(response.content)
            break
        

def main():
    parser = argparse.ArgumentParser(description='Grab all vhosts of a target from Censys Search Engine.')
    
    parser.add_argument('--domain', '-d', type=str, required=True, help='Please enter the target domain')
    parser.add_argument('--type', '-t', type=str, choices=['exclude', 'include', 'only'], help='Type of scan', default='only')
    args = parser.parse_args()

    target = trim_url(args.domain)

    print("---------------------------------------------------------------")
    print(f'Target set to -> {target}')
    print(f'Scan type set to -> {args.type}')

    censys_scan(target, args.type)


if __name__ == '__main__':
    main()
