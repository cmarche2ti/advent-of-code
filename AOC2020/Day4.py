# Part 1 - Test

test = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# Part 2 - Test

invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""


count = 0


def load_passport_file(filename):
    f = open(filename)
    filedata = f.readlines()
    passports = "".join(filedata)
    passports = passports.split("\n\n")
    f.close()
    passports = [val.replace("\n", " ") for val in passports]
    passports = [val.split() for val in passports]
    return passports


passports = load_passport_file("data/Day4.txt")

# Part 1

# for passport in passports:
#     pass_dict = {}
#     for record in passport:
#         key, val = record.split(":")[0], record.split(":")[1]
#         pass_dict[key] = val
#     test_keys = set(pass_dict.keys())
#     print(fields - test_keys)
#     if fields - test_keys == {"cid"} or test_keys == fields:
#         count += 1

# print(count)


# Part 2

fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])


def test_valid(p):
    if int(p["byr"]) in range(1920, 2003):
        if int(p["iyr"]) in range(2010, 2021):
            if int(p["eyr"]) in range(2020, 2031):
                if p["hcl"][0] == "#" and len(p["hcl"]) == 7:
                    if len(p["pid"]) == 9:
                        if p["ecl"] in [
                            "amb",
                            "blu",
                            "brn",
                            "gry",
                            "grn",
                            "hzl",
                            "oth",
                        ]:

                            if "cm" in p["hgt"] and int(p["hgt"][:-2]) in range(
                                150, 194
                            ):
                                return True
                            if "in" in p["hgt"] and int(p["hgt"][:-2]) in range(59, 77):
                                return True
    return False


for passport in passports:
    pass_dict = {}
    for record in passport:
        key, val = record.split(":")[0], record.split(":")[1]
        pass_dict[key] = val
    test_keys = set(pass_dict.keys())
    if fields - test_keys == {"cid"} or test_keys == fields:
        if test_valid(pass_dict):
            count += 1

print(count)
