// http://stackoverflow.com/questions/10858787/what-are-the-uses-for-tags-in-go

// Here is a really simple example of tags being used with the `encoding/json` package
// to control how fields are interpreted during encoding and decoding:

package main
import (
    "fmt"
    "encoding/json"
)
type Person struct {
    FirstName   string  `json:"first_name"`
    LastName    string  `json:"last_name"`
    MiddleName  string  `json:"middle_name,omitempty"`
}
func main() {
    json_string := `
    {
        "first_name": "John",
        "last_name": "Smith"
    }`
    person := new(Person)
    json.Unmarshal([]byte(json_string), person)
    fmt.Println(person)

    new_json, _ := json.Marshal(person)
    fmt.Printf("%s\n", new_json)
}
// &{John Smith }
// {"first_name":"John","last_name":"Smith"}
