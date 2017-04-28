// http://stackoverflow.com/questions/5884154/read-text-file-into-string-array-and-write
// Read text file into string array (and write)

// The ability to read (and write) a text file into and out of a string array
// is I believe a fairly common requirement.
// It is also quite useful when starting with a language removing the need initially to
// access a database. Does one exist in Golang?
// e.g. `func ReadLines(sFileName string, iMinLines int) ([]string, bool)`
// and `func WriteLines(saBuff[]string, sFilename string) (bool)`
// I would prefer to use an existing one rather than duplicate.

////////////////////
/*
// `bufio.Scanner`

package main
import (
    "bufio"
    "fmt"
    "log"
    "os"
)
// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
    file, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer file.Close()

    var lines []string
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
        lines = append(lines, scanner.Text())
    }
    return lines, scanner.Err()
}

// writeLines writes the lines to the given file.
func writeLines(lines []string, path string) error {
    file, err := os.Create(path)
    if err != nil {
        return err
    }
    defer file.Close()

    w := bufio.NewWriter(file)
    for _, line := range lines {
        fmt.Fprintln(w, line)
    }
    return w.Flush()
}

func main() {
    lines, err := readLines("input.txt")
    if err != nil {
        log.Fatalf("readLines: %s", err)
    }
    for i, line := range lines {
        fmt.Println(i, line)
    }

    if err := writeLines(lines, "output.txt"); err != nil {
        log.Fatalf("writeLines: %s", err)
    }
}
*/
///////////////////////////
/*
package main
import (
    "os"
    "bufio"
    "bytes"
    "io"
    "fmt"
    "strings"
)
// Read a whole file into the memory and store it as array of lines
func readLines(path string) (lines []string, err error) {
    var (
        file *os.File
        part []byte
        prefix bool
    )
    if file, err = os.Open(path); err != nil {
        return
    }
    defer file.Close()

    reader := bufio.NewReader(file)
    buffer := bytes.NewBuffer(make([]byte, 0))
    for {
        if part, prefix, err = reader.ReadLine(); err != nil {
            break
        }
        buffer.Write(part)
        if !prefix {
            lines = append(lines, buffer.String())
            buffer.Reset()
        }
    }
    if err == io.EOF {
        err = nil
    }
    return
}

func writeLines(lines []string, path string) (err error) {
    var (
        file *os.File
    )

    if file, err = os.Create(path); err != nil {
        return
    }
    defer file.Close()

    // writer := bufio.NewWriter(file)
    for _, item := range lines {
        // fmt.Println(item)
        _, err := file.WriteString(strings.TrimSpace(item) + "\n")
        // file.Write([]byte(item))
        if err != nil {
            // fmt.Println("debug")
            fmt.Println(err)
            break
        }
    }
    // content := strings.Join(lines, "\n")
    // _, err = writer.WriteString(content)
    return
}

func main() {
    lines, err := readLines("input.txt")
    if err != nil {
        fmt.Println("Error: %s\n", err)
        return
    }
    for _, line := range lines {
        fmt.Println(line)
    }
    // array := []string{"7.0", "8.7", "9.9"}
    err = writeLines(lines, "output.txt")
    fmt.Println(err)
}
*/
////////////////////////
/*
// If the file is small
package main
import (
    "os"
    "bufio"
    "bytes"
    "fmt"
)
// Read a whole file into the memory and store it as array of lines
func readLines(path string) (lines []string, err os.Error) {
    var (
        file *os.File
        part []byte
        prefix bool
    )
    if file, err = os.Open(path); err != nil {
        return
    }
    reader := bufio.NewReader(file)
    buffer := bytes.NewBuffer(make([]byte, 1024))
    for {
        if part, prefix, err = reader.ReadLine(); err != nil {
            break
        }
        buffer.Write(part)
        if !prefix {
            lines = append(lines, buffer.String())
            buffer.Reset()
        }
    }
    if err == os.EOF {
        err = nil
    }
    return
}
func main() {
    lines, err := readLines("input.txt")
    if err != nil {
        fmt.Println("error: %s\n", err)
        return
    }
    for _, line := range lines {
        fmt.Println(line)
    }
}
// ./read-text-file-into-string-array-and-write.go:161: undefined: os.Error
// ./read-text-file-into-string-array-and-write.go:182: undefined: os.EOF
*/

