/*
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

    The first passport is valid - all eight fields are present. 
    The second passport is invalid - it is missing hgt (the Height field).
    The third passport is interesting; the only missing field is cid, 
    so it looks like data from North Pole Credentials, not a passport at all! 
    Surely, nobody would mind if you made the system temporarily ignore missing cid fields. 
    Treat this "passport" as valid.

    The fourth passport is missing two fields, cid and byr. 
    Missing cid is fine, but missing any other field is not, so this passport is invalid.

    According to the above rules, your improved system would report 2 valid passports.

    Count the number of valid passports - those that have all required fields. 
    Treat cid as optional. In your batch file, how many passports are valid?

*/

// dotnet-script 4.cs


class Day2
{
    static string DATA=@"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in";

    public static void Run(string[] args)
    {
        string[] lines = DATA.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
        foreach (var line in lines)
        {
             Console.WriteLine(line);
        }
        /*int[] testdata = new int[] { 1721, 979, 366, 299, 675, 1456 };
        int res = GetMultOfTwoNumbersMatching(2020, testdata, true);
        Console.WriteLine("Result="  + res);
        Util.AssertEqual(res, 514579);

        string[] lines = Util.ReadInput(@"1.data");
        //int[] myInts = arr.Select(int.Parse).ToArray();
        int[] myInts = Array.ConvertAll(lines, int.Parse);
        res = GetMultOfTwoNumbersMatching(2020, myInts, true);
        Console.WriteLine("Result="  + res);
        Util.AssertEqual(res, 259716);
        */
    }
}

string[] args = new string[Args.Count];
Args.CopyTo(args, 0);
Day2.Run(args)