// http://stackoverflow.com/questions/20895552/how-to-read-input-from-console-line
// How to read input from console line?
/*
// I would like to read input from the command line,
// but my attempts have ended with the program exiting before I'm prompted for input.
// I'm looking for the equivalent of Console.ReadLine() in C#.
// This is what I currently have:
package main
import (
    "bufio"
    "fmt"
    "os"
)
func main() {
    reader := bufio.NewReader(os.Stdin)
    fmt.Print("Enter text: ")
    text, _ := reader.ReadString('\n')
    fmt.Println(text)

    fmt.Println("Enter text: ")
    text2 := ""
    fmt.Scanln(text2)
    fmt.Println(text2)

    ln := ""
    fmt.Sscanln("%v", ln)
    fmt.Println(ln)
}
*/
//////////////////////
/*
// I'm not sure what's wrong with the block

reader := bufio.NewReader(os.Stdin)
fmt.Print("Enter text: ")
text, _ := reader.ReadString('\n')
fmt.Println(text)
*/
//////////////////

// I think a more standard way to do this would be:
/*
package main
import "fmt"
func main() {
    fmt.Print("Enter text: ")
    var input string
    fmt.Scanln(&input)
    fmt.Print(input)
}
// Enter text: 111
// 111%
*/
//////////////////
/*
package main
import (
    "fmt"
    "bufio"
    "os"
)
func main() {
    scanner := bufio.NewScanner(os.Stdin)
    var text string
    for text != "q" {   // break the loop if text == "q"
        fmt.Print("Enter your text: ")
        scanner.Scan()
        text = scanner.Text()
        if text != "q" {
            fmt.Println("Your text was: ", text)
        }
    }
}
// Enter your text: 123
// Your text was:  123
// Enter your text: asd
// Your text was:  asd
// Enter your text: vbb
// Your text was:  vbb
*/
