# Functions for get address, state, cost, from a description
import re
from typing import List


def parse_street_str(value: str, mark) -> List[str]:
    result = re.findall(r"[-0-9]+\s[\sA-Z]+\s" + mark, value)
    return result if len(result) > 0 else 'None'.split()


def get_cost(value: List[str]) -> List[str]:
    cost_list = [''.join(re.findall(r'\$[.0-9]+', i)).replace('$', '') for i in value]
    cost = []
    for i in cost_list:
        if len(i) == 0:
            cost.append('0.0')
        else:
            cost.append(i)
    return cost


def get_street_address(value: List[str]) -> List[str]:
    address = []
    for i in value:
        if re.findall(r'\sST\s', i):
            address += parse_street_str(i, 'ST')
        elif 'AVE' in i:
            address += parse_street_str(i, 'AVE')
        elif 'RD' in i:
            address += parse_street_str(i, 'RD')
        elif 'WAY' in i:
            address += parse_street_str(i, 'WAY')
        elif 'DR' in i:
            address += parse_street_str(i, 'DR')
        else:
            address.append('None')
    return address


def get_state(value: List[str]) -> List[str]:
    state = []
    for i in value:
        if 'STATE' in i:
            result = re.findall(r'STATE\s[A-Z]+', i)
            state += result if len(result) > 0 else 'None'.split()
        else:
            state.append('None')
    return state


def get_zip(value: List[str]) -> List['str']:
    zip_ = []
    for i in value:
        if 'LOTS' in i:
            result = re.findall(r'LOTS\s[&\s0-9A-Z]+\sSP\s[0-9]+-[A-Z]', i)
            zip_ += result if len(result) > 0 else 'None'.split()
        elif 'LOT' in i:
            result = re.findall(r'LOT\s[&\s0-9A-Z]+\sSP\s[0-9]+-[A-Z]', i)
            zip_ += result if len(result) > 0 else 'None'.split()
        elif 'SP' in i:
            result = re.findall(r'SP\s[0-9]+-[A-Z]', i)
            zip_ += result if len(result) > 0 else 'None'.split()
        else:
            zip_.append('None')
    return zip_
