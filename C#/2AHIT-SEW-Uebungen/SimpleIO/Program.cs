
class Program
{
    static void Main(string[] args)
    {
        string vorname, nachname;

        Console.Write("Vorname:");
        vorname = Console.ReadLine();

        Console.Write("Nachname:");
        nachname = Console.ReadLine();

        Console.WriteLine("Ihr Name ist {0} {1}",vorname,nachname);
    }
}