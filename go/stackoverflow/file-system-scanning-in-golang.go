// http://stackoverflow.com/questions/6608873/file-system-scanning-in-golang
// File System Scanning in Golang

// 1. I need to write a function which when given the path of a folder scans the files rooted
// at that folder.
// 2. And then I need to display the directory structure at that folder.

// I know how to do 2 (I am going to use jstree to display it in thee browser).
// Please help me with part 1, like what/where to start to write such a function in go.

//////////////////////
/*
// This is a working example of `filepath.Walk()`. The original is below.
package main
import (
    "path/filepath"
    "os"
    "flag"
    "fmt"
)
func visit(path string, f os.FileInfo, err error) error {
    fmt.Printf("visited: %s\n", path)
    return nil
}
func main() {
    flag.Parse()
    root := flag.Arg(0)
    err := filepath.Walk(root, visit)
    fmt.Printf("filepath.Walk() returned %v\n", err)
}
// go run file-system-scanning-in-golang.go
// visited:
// filepath.Walk() returned <nil>
// go run file-system-scanning-in-golang.go .
// visited: .
// visited: README
// visited: checking-the-equality-of-two-slices.go
// visited: concatenate-two-slices.go
// ...
*/
////////////////////

package main
import (
    "fmt"
    "os"
    "path/filepath"
)
func main() {
    dirname := "." + string(filepath.Separator)
    d, err := os.Open(dirname)
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    defer d.Close()
    fi, err := d.Readdir(-1)
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    for _, fi := range fi {
        if fi.Mode().IsRegular() {
            fmt.Println(fi.Name(), fi.Size(), "bytes")
        }
    }
}
// go run file-system-scanning-in-golang.go .
// checking-the-equality-of-two-slices.go 1043 bytes
// concatenate-two-slices.go 76 bytes
// conf.json 61 bytes
// constructors-in-go.go 2766 bytes
// ...
