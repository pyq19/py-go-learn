// http://stackoverflow.com/questions/18537257/golang-how-to-get-the-directory-of-the-currently-running-file
// How to get the directory of the currently running file?

// In node I use __dirname.
// What is the equivalent of this in Golang?
// _, filename, _, _ := runtime.Caller(1)
// f, err := os.Open(path.Join(path.Dir(filename), "data.csv"))
// But is it the right way to idiomatic way to do in Golang?

///////////////////
/*
// This should do it:
package main
import (
    "fmt"
    "log"
    "os"
    "path/filepath"
)
func main() {
    dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
    if err != nil {
        log.Fatal(err)
    }
    fmt.Println(dir)
}
*/
// /var/folders/4q/07lxxrr573b6x7s4skxy2tqm0000gn/T/go-build083334147/command-line-arguments/_obj/exe
//////////////////////////
/*
// As of Go 1.8 (Released February(2月) 2017)
// the recommended way of doing this is with `os.Executable`:
// To get just the directory of the executable you can use `path.Dir`.
package main
import (
    "fmt"
    "os"
    "path"
)
func main() {
    ex, err := os.Executable()
    if err != nil {
        panic(err)
    }
    exPath := path.Dir(ex)
    fmt.Println(exPath)
}
// /var/folders/4q/07lxxrr573b6x7s4skxy2tqm0000gn/T/go-build860142684/command-line-arguments/_obj/exe
*/
///////////////

