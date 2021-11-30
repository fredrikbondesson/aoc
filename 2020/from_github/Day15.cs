﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

//namespace day_15
//{
    class Day15
    {
        public static void Run()
        {
            //string[] input = File.ReadAllText(Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "puzzleInput_day15.txt")).Split(",");
            string[] input = File.ReadAllText("puzzleInput_day15.txt").Split(",");

            List<long> inputs = (Array.ConvertAll(input, s => Int64.Parse(s))).ToList();
            
            Stopwatch sw = new Stopwatch();
            sw.Start();
            Console.WriteLine($"Part one solution:  {MemoryGame(inputs, 2020)}");
            sw.Stop();
            Console.WriteLine("Elapsed={0}", sw.Elapsed);
            sw.Start();
            Console.WriteLine($"Part two solution:  {MemoryGame(inputs, 30000000)}");
            sw.Stop();
            Console.WriteLine("Elapsed={0}", sw.Elapsed);
        }

        private static long MemoryGame(List<long> inputs, int numberSpoken)
        {
            Dictionary<long, List<long>> numberOfOccurence = new Dictionary<long, List<long>>();
            List<long> occurence = new List<long>();
            for (int i = 1; i <= numberSpoken; i++)
            {
                if (numberOfOccurence.Count < inputs.Count)
                {
                    numberOfOccurence.Add(inputs.ElementAt(i - 1), new List<long>() { i });
                    occurence.Add(inputs.ElementAt(i - 1));

                    continue;
                }

                long lastNumber = occurence.Last();
                if (numberOfOccurence.ContainsKey(lastNumber))
                {
                    if (numberOfOccurence[lastNumber].Count == 1)
                    {
                        if (numberOfOccurence.ContainsKey(0))
                        {
                            numberOfOccurence[0].Add(i);
                        }
                        else
                        {
                            numberOfOccurence.Add(0, new List<long>() { i });
                        }

                        occurence.Add(0);
                    }
                    else
                    {
                        var list = numberOfOccurence[lastNumber];
                        long lastOccurence = list.ElementAt(list.Count - 1);
                        long previuosOccurence = list.ElementAt(list.Count - 2);
                        long newNumber = lastOccurence - previuosOccurence;

                        if (numberOfOccurence.ContainsKey(newNumber))
                        {
                            numberOfOccurence[newNumber].Add(i);
                        }
                        else
                        {
                            numberOfOccurence.Add(newNumber, new List<long>() { i });
                        }

                        occurence.Add(newNumber);
                    }
                }
            }

            return occurence.Last();
        }
    }
//}
Day15.Run()