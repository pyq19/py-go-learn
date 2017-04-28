// http://stackoverflow.com/questions/24512112/golang-how-to-print-struct-variables-in-console
// How to print struct variables in console?

// How can I print (in the console) the `Id`, `Title`, `Name`, etc. of this struct in Golang?
/*
type Project struct {
    Id int64            `json:"project_id"`
    Title string        `json:"title"`
    Name string         `json:"name"`
    Data Data           `json:"data"`
    Commits Commits     `json:"commits"`
}
*/
////////////////////////////

// To print the name of the fields in a struct:

// fmt.Printf("%+v\n", yourProject)

// From the `fmt` package:
// when printing structs, the plus flag (%+v) adds field names

// That supposes you have an instance of Project (in 'yourProject')
// The article `JSON and Go` will give more details on how to retrieve the values from a JSON struct.
/*
type Response2 struct {
    Page int        `json:"page"`
    Fruits []string `json:"fruits"`
}
res2D := &Response2 {
    Page: 1,
    Fruits: []string{"apple", "peach", "pear"}
}
res2B, _ := json.Marshal(res2D)
fmt.Println(string(res2B))
// {"Page":1,"Fruits":["apple","peach","pear"]}

// If you don't have any instance, then you need to use reflection to display the name of the field of a given
// struct.

type T struct {
    A int
    B string
}
t := T{23, "skidoo"}
s := reflect.ValueOf(&t).Elem()
typeOfT := s.Type()

for i := 0; i < s.NumField(); i++ {
    f := s.Field(i)
    fmt.Printf("%d: %s %s = %v\n", i, typeOfT.Field(i).Name, f.Type(), f.Interface())
}
*/
/////////////////////
package main
import (
    "fmt"
    "reflect"
)
func main() {
    type Book struct {
        Id      int
        Name    string
        Title   string
    }
    book := Book{1, "Let us C", "Enjoy programming with practice"}
    e := reflect.ValueOf(&book).Elem()

    for i := 0; i < e.NumField(); i++ {
        fieldName := e.Type().Field(i).Name
        fmt.Printf("%v\n", fieldName)
    }
}
// Id
// Name
// Title
