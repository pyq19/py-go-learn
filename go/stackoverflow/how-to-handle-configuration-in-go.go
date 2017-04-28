// conf.json:
/*
{
    "Users": ["UserA", "UserB"],
    "Groups": ["GroupA"]
}
*/

// Program to read the configuration
package main
import (
    "encoding/json"
    "os"
    "fmt"
)
type Configuration struct {
    Users   []string
    Groups  []string
}

func main() {
    file, _ := os.Open("conf.json")
    decoder := json.NewDecoder(file)
    configuration := Configuration{}
    err := decoder.Decode(&configuration)
    if err != nil {
        fmt.Println("errer ->", err)
    }
    fmt.Println(configuration.Users)    // output: [UserA UserB]
}
