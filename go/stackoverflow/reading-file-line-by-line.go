// http://stackoverflow.com/questions/8757389/reading-file-line-by-line-in-go 

/*
package main
import (
    "bufio"
    "fmt"
    "log"
    "os"
)
func main() {
    file, err := os.Open("./input.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }
}
*/

///////////////

// The Readln(*bufio.Reader) function returns a line (sans \n)
// from the underlying bufio.Reader struct.

// Readln returns a single line (without the ending \n)
// from the input buffered reader.
// An error is returned iff there is an error with the 
// buffered reader.
func Readln(r *bufio.Reader) (string, error) {
    var (isPrefix bool = true
         err error = nil
         line, ln []byte
        )
    for isPrefix && err == nil {
        line, isPrefix, err = r.ReadLine()
        ln = append(ln, line...)
    }
    return string(ln), err
}

// You can use Readln to read every line from a file.
// The following code reads every line in a file and outputs each line to stdout.
f, err := os.Open(fi)
if err != nil {
    fmt.Printf("error opening file: %v\n", err)
    os.Exit(1)
}
r := bufio.NewReader(f)
s, e := Readln(r)
for e == nil {
    fmt.Prinln(s)
    s, e = Readln(r)
}
