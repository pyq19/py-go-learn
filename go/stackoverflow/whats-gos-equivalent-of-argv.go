// http://stackoverflow.com/questions/3356011/whats-gos-equivalent-of-argv0
// What's Go's equivalent of argv[0]?

// How can I get my own program's name at runtime?
// What's Go's equivalent of C/C++'s argv[0]?
// To me it is useful to generate the usage with the right name.
/*
package main
import (
    "flag"
    "fmt"
    "os"
)
func usage() {
    fmt.Fprintf(os.Stderr, "usage: myprog [inputfile]\n")
    flag.PrintDefaults()
    os.Exit(2)
}
func main() {
    flag.Usage = usage
    flag.Parse()

    args := flag.Args()
    if len(args) < 1 {
        fmt.Println("input file is missing.")
        os.Exit(1)
    }
    fmt.Printf("opening %s\n", args[0])
}
// go run whats-gos-equivalent-of-argv.go
// input file is missing.
// exit status 1
// go run whats-gos-equivalent-of-argv.go HELLO! HELLO!
// opening HELLO!
*/
///////////////
/*
import "os"
os.Args[0]  // name of the command that it is running as
os.Args[1]  // first command line parameter, ...

// Arguments are exposed in the `os` package

// If you're going to do argument handling, the `flag` package is the preferred way.
// Specifically for your case `flag.Usage`

func usage() {
    fmt.Fprint(os.Stderr, "usage: %s [inputfile]\n", os.Args[0])
    flag.PrintDefaults()
    os.Exit(2)
}
*/
///////////////////

package main
import "os"
func main() {
    println("os.Args[0] ->", os.Args[0])
    println("os.Args[1] ->", os.Args[1])
}
// go run whats-gos-equivalent-of-argv.go 1111
// os.Args[0] -> /var/folders/4q/07lxxrr573b6x7s4skxy2tqm0000gn/T/go-build462883509/command-line-arguments/_obj/exe/whats-gos-equivalent-of-argv
// os.Args[1] -> 1111
