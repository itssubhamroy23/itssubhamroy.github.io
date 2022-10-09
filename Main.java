//java prohram to display a year is leap year or not

public class Main {

  public static void main(String[] args) {

    // Enter the year you want to check
    int year = 2012;
    boolean leap = false;

    // checking if the year is divided by 4
    if (year % 4 == 0) {

      // checking if the year is century
      if (year % 100 == 0) {

        // if it is divided by 400
        // then it is a leap year
        if (year % 400 == 0)
          leap = true;
        else
          leap = false;
      }
      
      // checking if the year is not century
      else
        leap = true;
    }
    
    else
      leap = false;

    if (leap)
      System.out.println(year + " is a leap year.");
    else
      System.out.println(year + " is not a leap year.");
  }
}
