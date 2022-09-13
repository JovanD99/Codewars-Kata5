using System;
using System.Linq;


public class weight_sort
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Enter string:");
        string userInput = Console.ReadLine();
        List<string> words = new List<string>();
        words = userInput.Split(" ").ToList();
        words.Sort((x, y) => sum_digits(x).CompareTo(sum_digits(y)));
        List<string> words_copy = new List<string>(words);
        List<object> list_of_lists = new List<object>();
        List<string> result = new List<string>();


        foreach (string word in words)
        {
            List<string> list = new List<string>();
            list = words_copy.FindAll(x => sum_digits(x) == sum_digits(word)).ToList();
            list.Sort();
            words_copy.RemoveAll(x => sum_digits(x) == sum_digits(word));
            list_of_lists.Add(list);
            
        }

        foreach(List <string> l in list_of_lists)
        {
            result.AddRange(l);
        }

        Console.WriteLine(String.Join(" ", result));
        Console.ReadLine();



        
    }

    public static int sum_digits(string number)
    {
        int sum = 0;
        foreach (char c in number)
            sum += int.Parse(c.ToString());
        return sum;
    }
}