import argparse
from datetime import datetime, timedelta
import json
import sys
import urllib.parse
import urllib.request


def fetch(url):
    headers = {
        'Authorization': 'Bearer {}'.format(args.apikey)
    }
    url = urllib.parse.urljoin('https://api.aleth.io/', url)
    print('.', end='', flush=True, file=sys.stderr)
    req = urllib.request.Request(url, headers=headers)
    raw = urllib.request.urlopen(req).read()
    return json.loads(raw)


def fetch_collection(url):
    params = urllib.parse.urlencode({'page[limit]': 100})
    url = '?'.join([url, params])
    while 1:
        res = fetch(url)
        for item in res['data']:
            yield item
        if res['meta']['page']['hasNext']:
            url = res['links']['next']
        else:
            break


def fetch_account_txs(account):
    url = '/v1/accounts/{address}/transactions'.format(address=account)
    return fetch_collection(url)


def fetch_account_txs_after(account, date):
    for tx in fetch_account_txs(account):
        if datetime.fromtimestamp(tx['attributes']['blockCreationTime']) >= date:
            yield tx
        else:
            break


def fetch_account_counterparties_after(account, date):
    print('Fetching counterparties for {} after {} '.format(
        account, date), end='', file=sys.stderr)
    counterparties = set()
    tx_count = 0
    for tx in fetch_account_txs_after(account, date):
        counterparties.add(tx['relationships']['from']['data']['id'])
        counterparties.add(tx['relationships']['to']['data']['id'])
        tx_count += 1
    counterparties.remove(account)
    print('\n  {} counterparties found in {} transactions'.format(
        len(counterparties), tx_count), file=sys.stderr)
    return counterparties


def scan_account(account, days):
    def print_lines(lines):
        for address in lines:
            print(address)

    date_cutoff = datetime.utcnow() - timedelta(days=7)
    seed_counterparties = fetch_account_counterparties_after(account, date_cutoff)
    print_lines(seed_counterparties)

    level2_counterparties = set()
    for cp in seed_counterparties:
        for ccp in fetch_account_counterparties_after(cp, date_cutoff):
            level2_counterparties.add(ccp)    
    print_lines(level2_counterparties)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan Ethereum account counterparties')
    parser.add_argument('account', help='Address of the starting account')
    parser.add_argument('--apikey', default='sk_main_0123456789abcdef', help='The Alethio API key')
    parser.add_argument('--days', type=int, default=7, help='Analyze activity in the last X days')

    args = parser.parse_args()
    scan_account(args.account, args.days)
