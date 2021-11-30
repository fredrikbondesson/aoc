#!/usr/bin/env dotnet-script
Console.WriteLine("Hello world");

foreach (var arg in Args)
{
    Console.WriteLine("Arg:" + arg);
}
