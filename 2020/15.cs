using System;
using System.Collections.Generic;
using System.Diagnostics;
// dotnet-script 15.cs


class Day15
{

    public static TimeSpan Time(Action action)
    {
        Stopwatch stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        return stopwatch.Elapsed;
    }

    public static void AssertEqual(int value1, int value2, string msg = null) 
    {
        if (value1 != value2)
        {
            string message = "AssertedMsg=" + msg;
            throw new System.ArgumentException(String.Format("{0} is not equal to {1}", value1, value2));
        }
    }

    private static int UpdateValueIdx(Dictionary<int, int> valueAndIdx, int currentValue, int currentIndex)
    {
        int foundIndex = -1;
        if (valueAndIdx.TryGetValue(currentValue, out foundIndex))
            if (currentIndex == foundIndex)
            {
                return 0;
            }
            else
            {
                valueAndIdx[currentValue] = currentIndex;
                return currentIndex - foundIndex;
            }
            
        else
        {
            valueAndIdx.Add(currentValue, currentIndex);
            return 0;
        }

    }

    private static void Part2WithInput(Dictionary<int, int> valueAndIdx, int currentValue, int expectedValue, int endIndex=2019)
    {
        int index = valueAndIdx.Count() - 1;
        
        while (index < endIndex)
        {
            currentValue = UpdateValueIdx(valueAndIdx, currentValue, index);
            index += 1;
        }

        Console.WriteLine(currentValue);
        AssertEqual(currentValue, expectedValue);
    }

    public static void Run()
    {
        var valueAndIdx = new Dictionary<int, int>(){
            {0, 0}, 
            {3, 1}, 
            {6, 2}
        };

        Stopwatch sw = new Stopwatch();

        sw.Start();
        Part2WithInput(valueAndIdx, currentValue: 6, expectedValue: 436);
        sw.Stop();
        Console.WriteLine("valueAndIdx.Count={0}", valueAndIdx.Count());
        Console.WriteLine("Elapsed={0}", sw.Elapsed);

        valueAndIdx = new Dictionary<int, int>(){
            {0, 0}, {3, 1}, {6, 2}
        };

        TimeSpan time = Day15.Time(() =>
        {
            Part2WithInput(valueAndIdx, currentValue: 6, expectedValue: 436);
        });
        Console.WriteLine("Timespan={0}", time);

        valueAndIdx = new Dictionary<int, int>(){
            {6, 0}, {4, 1}, {12, 2}, {1, 3}, {20, 4}, {0, 5}, {16, 6}
        };

        sw.Start();
        Part2WithInput(valueAndIdx, currentValue: 16, expectedValue: 11261, endIndex: 30000000-1);
        Console.WriteLine("valueAndIdx.Count={0}", valueAndIdx.Count());
        sw.Stop();
        Console.WriteLine("Elapsed={0}", sw.Elapsed);
    }
}


Day15.Run()