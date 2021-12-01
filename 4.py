'''
--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
'''

list = []
with open("4-input.txt", "r") as f:  # log.txt file has line separated values,
    for i in f.readlines():
        list.append(i.strip())
print(list)

passports = [{}]
passRow = 0


for row in list:
    if row == '':
        passRow +=1
        passports.append({})
        continue
    items = row.split()
    for item in items:
        key, value = item.split(':')
        passports[passRow][key] = value


# Part 1 #
legal = 0
for i in passports:
    if len(i) == 8 or (len(i) == 7 and 'cid' not in i):
        legal += 1
        print(i)
print(legal)


# Part 2 #
def validate(passport):
    if len(i) <= 6 or (len(i) == 7 and 'cid' in i):
        return False
    if not val_byr(passport):
        return False
    if not val_iyr(passport):
        return False
    if not val_eyr(passport):
        return False
    if not val_hgt(passport):
        return False
    if not val_hcl(passport):
        return False
    if not val_ecl(passport):
        return False
    if not val_pid(passport):
        return False
    return True


def val_byr(passport):
    return 1920 <= int(passport['byr']) <= 2002


def val_iyr(passport):
    return 2010 <= int(passport['iyr']) <= 2020


def val_eyr(passport):
    return 2020 <= int(passport['eyr']) <= 2030


def val_hgt(passport):
    if passport['hgt'][-2:] == 'cm':
        return 150 <= int(passport['hgt'][:-2]) <= 193
    if passport['hgt'][-2:] == 'in':
        return 59 <= int(passport['hgt'][:-2]) <= 76
    return False


def val_hcl(passport):
    if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
        try:
            int(passport['hcl'][1:], 16)
            return True
        except ValueError:
            return False
    return False


def val_ecl(passport):
    return passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def val_pid(passport):
    try:
        int(passport['pid'])
    except ValueError:
        return False
    return len(passport['pid']) == 9


legal = 0
for i in passports:
    if validate(i):
        legal += 1
print(legal)
