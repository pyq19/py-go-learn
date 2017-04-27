// http://stackoverflow.com/questions/1821811/how-to-read-write-from-to-file-using-golang

/* start with the basices
package main
import (
    "io"
    "os"
)
func main() {
    // open input file
    fi, err := os.Open("input.txt")
    if err != nil {
        panic(err)
    }
    // close fi on exit and check for its returned error
    defer func() {
        if err := fi.Close(); err != nil {
            panic(err)
        }
    }()

    // open output file
    fo, err := os.Create("output.txt")
    if err != nil {
        panic(err)
    }
    // close fo on exit and chech for its returned error
    defer func() {
        if err := fo.Close(); err != nil {
            panic(err)
        }
    }()

    // make a buffer to keep chunks that are read
    buf := make([]byte, 1024)
    for {
        // read a chunk
        n, err := fi.Read(buf)
        if err != nil && err != io.EOF {
            panic(err)
        }
        if n == 0 {
            break
        }

        // write a chunk
        if _, err := fo.Write(buf[:n]); err != nil {
            panic(err)
        }
    }
}
*/

/*
// using bufio
package main
import (
    "bufio"
    "io"
    "os"
)
func main() {
    // open input file
    fi, err := os.Open("input.txt")
    if err != nil {
        panic(err)
    }
    // close fi on exit and check for its returned error
    defer func() {
        if err := fi.Close(); err != nil {
            panic(err)
        }
    }()
    // make a read buffer
    r := bufio.NewReader(fi)

    // open output file
    fo, err := os.Create("output.txt")
    if err != nil {
        panic(err)
    }
    // close fo on exit and check for its returned error
    defer func() {
        if err := fo.Close(); err != nil {
            panic(err)
        }
    }()
    // make a write buffer
    w := bufio.NewWriter(fo)

    // make a buffer to keep chunks that are read
    buf := make([]byte, 1024)
    for {
        // read a chunk
        n, err := r.Read(buf)
        if err != nil && err != io.EOF {
            panic(err)
        }
        if n == 0 {
            break
        }

        // write a chunk
        if _, err := w.Write(buf[:n]); err != nil {
            panic(err)
        }
    }

    if err = w.Flush(); err != nil {
        panic(err)
    }
}
*/

// using ioutil
/*
package main
import (
    "io/ioutil"
)
func main() {
    // read the whole file at once
    b, err := ioutil.ReadFile("input.txt")
    if err != nil {
        panic(err)
    }

    // write the whole body at once
    err = ioutil.WriteFile("output.txt", b, 0644)
    if err != nil {
        panic(err)
    }
}
*/

// another version
/*
package main
import "io/ioutil"
func main() {
    contents, _ := ioutil.ReadFile("input.txt")
    println(string(contents))
    ioutil.WriteFile("output.txt", contents, 0644)
}
*/

/*
// using io.Copy
package main
import (
    "io"
    "log"
    "os"
)
func main() {
    // open files r and w
    r, err := os.Open("input.txt")
    if err != nil {
        panic(err)
    }
    defer r.Close()

    w, err := os.Create("output.txt")
    if err != nil {
        panic(err)
    }
    defer w.Close()

    // do the actual work
    n, err := io.Copy(w, r)
    if err != nil {
        panic(err)
    }
    log.Printf("Copied %v bytes\n", n) // 2017/04/27 13:57:53 Copied 23 bytes
}
*/

// another version2 // error
/*
package main
import (
    "fmt"
    "os"
)
func main() {
    inNane := "input.txt"
    inPerm := 0666
    inFile, inErr := os.Open(inName, os.O_RDONLY, inPerm)
    if inErr == nil {
        inBufLen := 16
        inBuf := make([]byte, inBufLen)
        n, inErr := inFile.Read(inBuf)
        for inErr == nil {
            fmt.Println(n, inBuf[0:n])
            n, inErr = inFile.Read(inBuf)
        }
    }
    inErr = inFile.Close()
}
*/
