#include <iostream>
#include <vector>

void helloWorld();
void conditionals();
void loop();
void printing();
void printing2();
void fizzbuzz();
void fahrenheitCelsius();
void tuples();

int main(int argc, char *argv[])
{
    //helloWorld();
    //conditionals();
    //loop();
    //printing();
    //printing2();
    //fizzbuzz();
    //fahrenheitCelsius();
    tuples();

    return 0;
}

void helloWorld()
{
    std::cout << "Hello World!" << std::endl;
}

void conditionals()
{
    auto a { 0 };
    auto b { 0 };

    std::cin >> a;
    std::cin >> b;

    if (a > b)
    {
        std::cout << "A greater than B" << std::endl;
    }
    else if (b > a)
    {
        std::cout << "A smaller than B" << std::endl;
    }
    else
    {
        std::cout << "A equal to B" << std::endl;
    }
}

void loop()
{
    auto a { 1024 };

    while (a > 0)
    {
        std::cout << a << std::endl;
        a /= 2;
    }
}

void printing()
{
    for (int i = 1; i <= 5; i++)
    {
        std::cout << (i % 2 ? "|     |" : "-------") << std::endl;
    }
}

void printing2()
{
    for (int i = 1; i <= 17; i++)
    {
        std::cout << (i % 6 ? (i % 2 ? "  |  |  H  |  |  H  |  |  " : "--+--+--H--+--+--H--+--+--") : "========+========+========")  << std::endl;
    }
}

void fizzbuzz()
{
    auto s { 0 };

    for (int i = 1001; i > 0; i--)
    {
        if (i % 3 == 0 or i % 5 == 0)
        {
            s += i;
        }
    }

    std::cout << s << std::endl;
}

void fahrenheitCelsius()
{
    auto f { 0 };

    std::cout << "Temperature F? ";
    std::cin >> f;

    printf("It is %.2f degrees Celsius.\n", (f - 32) * (5 / 9.));
}

void tuples()
{
    auto a { 0 };
    auto b { 0 };
    auto c { 0 };

    std::cin >> a;
    std::cin >> b;

    while (a)
    {
        c = a;
        a = b;
        b = c % b;
    }

    std::cout << a << std::endl;
}