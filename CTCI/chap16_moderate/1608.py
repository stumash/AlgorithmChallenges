def digit_s(c) -> str:
    if c == '1': return 'One'
    if c == '2': return 'Two'
    if c == '3': return 'Three'
    if c == '4': return 'Four'
    if c == '5': return 'Five'
    if c == '6': return 'Six'
    if c == '7': return 'Seven'
    if c == '8': return 'Eight'
    if c == '9': return 'Nine'
    else: return ''

def hundreds_s(c):
    if c == '0': return ''
    else:
        cs = digit_s(c)
        if cs is None: return ''
        return cs + ' Hundred'

def tens_s(s) -> str:
    ones, tens = s[0], s[1]
    if tens == '1':
        if ones == '0': return 'Ten'
        if ones == '1': return 'Eleven'
        if ones == '2': return 'Twelve'
        if ones == '3': return 'Thirteen'
        if ones == '4': return 'Fourteen'
        if ones == '5': return 'Fifteen'
        if ones == '6': return 'Sixteen'
        if ones == '7': return 'Seventeen'
        if ones == '8': return 'Eighteen'
        if ones == '9': return 'Nineteen'
        else: return ''
    tens_s = ''
    if tens == '2': tens_s = 'Twenty '
    if tens == '3': tens_s = 'Thirty '
    if tens == '4': tens_s = 'Fourty '
    if tens == '5': tens_s = 'Fifty '
    if tens == '6': tens_s = 'Sixty '
    if tens == '7': tens_s = 'Seventy '
    if tens == '8': tens_s = 'Eighty '
    if tens == '9': tens_s = 'Ninety '
    ones_s = digit_s(ones)
    return tens_s + (ones_s if ones_s is not None else '')


def english_int(n):
    s = ''.join(reversed(str(n)))
    if len(s) % 3 != 0:
        s = s + ('0' * (3 - (len(s) % 3)))

    retval = []
    groups = ['', ' Thousand', ' Million', ' Billion', ' Trillion']
    for g, gname in enumerate(groups):
        digits = s[(g*3):((g*3)+3)]
        if digits == '': break
        curr_h = hundreds_s(digits[2])
        curr_t = tens_s(digits[:2])
        curr = []
        if curr_h != '': curr.append(curr_h)
        if curr_t != '': curr.append(curr_t)
        if len(curr) != 0 and gname != '': curr.append(gname)
        if curr != []: retval.extend(curr)
    return ' '.join(retval)


print(english_int(125))

