#!/usr/bin/env dotnet-script

class Pelle
{
    public static void hello(bool log=false)
    {
        if (log)
        {
            Console.WriteLine("Hello Pelle");
        }
    }
}