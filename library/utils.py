# -*- coding: utf-8 -*-


def to_isbn10(isbn):
    '''
    Convert 13-digit isbn to 10-digit isbn
    '''
    inner = isbn[3: -1]
    sum = 0
    for index, digit in enumerate(inner):
        sum += (10 - index) * int(digit)
    check = 11 - sum % 11
    if check == 11:
        checksum = '0'
    elif check == 10:
        checksum = 'X'
    else:
        checksum = str(check)
    return inner + checksum


def to_isbn13(isbn):
    '''
    Convert 10-digit isbn to 13-digit isbn
    '''
    temp = '978' + isbn[:-1]
    sum = 0
    sumb = 0
    for i in range(1, 13, 2):
        sum += int(temp[i])
    for i in range(0, 12, 2):
        sumb += int(temp[i])
    checksum = str((sum * 3 + sumb) % 10)
    return temp + checksum
