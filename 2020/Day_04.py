def sol1(batch):
    fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    return sum(set(b[:3] for b in a.replace('\n', ' ').split(' ')) in [fields, fields - {'cid'}] for a in batch.split("\n\n"))

def sol2(batch):
    rnge = lambda a, x, y: x <= int(a) <= y if a else None
    yr = lambda a, x, y: sum(c.isdigit() for c in a) == len(a) == 4 and rnge(a, x, y)
    fields = {
        'byr': lambda a: yr(a, 1920, 2002), 
        'iyr': lambda a: yr(a, 2010, 2020),
        'eyr': lambda a: yr(a, 2020, 2030), 
        'hgt': lambda a: all(c.isdigit() for c in a[:-2]) and [rnge(a[:-2], 150, 193), rnge(a[:-2], 59, 76), 0][(a[-2:] == "cm") + 2*(a[-2:] == "in") - 1], 
        'hcl': lambda a: a[0] == '#' and sum(rnge(ord(c), 48, 57) or rnge(ord(c), 97, 102) for c in a[1:]) == len(a[1:]) == 6,
        'ecl': lambda a: a in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], 
        'pid': lambda a: sum(c.isdigit() for c in a) == len(a) == 9,
        'cid': lambda a: True
    }
    fields_keys = set(fields.keys())
    return sum(set(b[:3] * fields[b[:3]](b[4:]) for b in a.replace('\n', ' ').split(' ')) in [fields_keys, fields_keys - {'cid'}] for a in batch.split("\n\n"))

sbatch = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

sbatchinv = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

sbatchval = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022'''

batch = open("Inputs/Day_04.txt", "r").read()

print(sol1(batch))
print(sol2(batch))

