class Program
{
    static void Main(string[] args)
    {
        string eingabe1, eingabe2;
        double zahl1, zahl2,summe;
        bool isOK1, isOK2;

        Console.WriteLine("Zahlenaddition");

        Console.Write("Zahl");
        eingabe1 = Console.ReadLine();

        Console.Write("Zahl");
        eingabe2 = Console.ReadLine();

        isOK1 = Double.TryParse(eingabe1, out zahl1);
        isOK2 = Double.TryParse(eingabe2, out zahl2);

        if(isOK1 == true && isOK2 == true)
        {
            summe = zahl1 + zahl2; 
            Console.WriteLine("Summe {0} + {1} = {2}",zahl1 , zahl2 ,summe);
        }
        else
        {
            Console.WriteLine("Fehlerhafte Eingabe");

        }
        Console.ReadKey();
    }
}