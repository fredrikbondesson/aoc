#!/usr/bin/env dotnet-script

using System.Diagnostics;

//dotnet tool install -g dotnet-script


foreach (var arg in Args)
{
    Console.WriteLine("Arg:" + arg);
}


class Util
{
    public static string[] ReadInput(in string filepath, bool log=false)
    {
        string[] lines = System.IO.File.ReadAllLines(filepath);
        if (log) {
            foreach (string line in lines)
            {
                Console.WriteLine(line);
            }
        }
        return lines;
    }

    public static void AssertEqual(int value1, int value2, string msg = null) 
    {
        if (value1 != value2)
        {
            string message = "AssertedMsg=" + msg;
            throw new System.ArgumentException(String.Format("{0} is not equal to {1}", value1, value2));
        }
    }

    public static void Assert(bool condition, string msg = null)
    {
        if (!condition)
        {
            string message = "AssertMsg:" + msg;
            throw new System.ArgumentException(String.Format("Condition is not correct: {0}", message));
        }
    }

    public static void Log(string msg, bool log=false) 
    {
        if (log)
        {
            Console.WriteLine(msg);
        }
    }
}


class Day1
{
    static int GetMultOfTwoNumbersMatching(int value, int[] numbers, bool log=false)
    {
        foreach (var number1 in numbers)
        {
            foreach (var number2 in numbers)
            {
                if (number1 + number2 == value) {
                    Util.Log(String.Format("{0} * {1} = {2}", number1, number2, value), log);
                    return number1 * number2;
                }
            }
        }
        return -1;
    }

    public static void Run(string[] args)
    {
        int[] testdata = new int[] { 1721, 979, 366, 299, 675, 1456 };
        int res = GetMultOfTwoNumbersMatching(2020, testdata, true);
        Console.WriteLine("Result="  + res);
        Util.AssertEqual(res, 514579);

        string[] lines = Util.ReadInput(@"1.data");
        //int[] myInts = arr.Select(int.Parse).ToArray();
        int[] myInts = Array.ConvertAll(lines, int.Parse);
        res = GetMultOfTwoNumbersMatching(2020, myInts, true);
        Console.WriteLine("Result="  + res);
        Util.AssertEqual(res, 259716);
    }
}

string[] args = new string[Args.Count];
Args.CopyTo(args, 0);
Day1.Run(args)