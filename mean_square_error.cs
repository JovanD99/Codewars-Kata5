using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
  public static double Solution(int[] firstArray, int[] secondArray)
  {
      int[] array1 = firstArray;
      int[] array2 = secondArray;
      List<double> array3 = new List<double>();

      for (int i = 0; i < array1.Length; i++)
      {
          double val = Math.Abs(array1[i] - array2[i]);
          val = Math.Pow(val, 2);
          array3.Add(val);   
      }
      return array3.Sum() / array3.Count();
  }
}