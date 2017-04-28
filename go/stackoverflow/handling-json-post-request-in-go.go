// http://stackoverflow.com/questions/15672556/handling-json-post-request-in-go

// Go handling a POST request of JSON data
// Here is an example request: curl -X POST -d "{\"test\": \"that\"}" http://localhost:8082/test
// Here is the code, with the logs embedded:
/*
package main
import (
    "encoding/json"
    "log"
    "net/http"
)
type test_struct struct {
    Test string
}
func test(rw http.ResponseWriter, req *http.Request) {
    req.ParseForm()
    log.Println(req.Form)

    var t test_struct
    for key, _ := range req.Form {
        log.Println(key)

        err := json.Unmarshal([]byte(key), &t)
        if err != nil {
            log.Println(err.Error())
        }
    }
    log.Println(t.Test)
}
func main() {
    http.HandleFunc("/test", test)
    log.Fatal(http.ListenAndServe(":8082", nil))
}
// 2017/04/28 13:28:20 map[{"test": "that"}:[]]
// 2017/04/28 13:28:20 {"test": "that"}
// 2017/04/28 13:28:20 that
*/

/////////////////////
/*
// Please use `json.Decoder` instead of `json.Unmarshal`.
package main
import (
    "encoding/json"
    "log"
    "net/http"
)
type test_struct struct {
    Test string
}
func test(rw http.ResponseWriter, req *http.Request) {
    decoder := json.NewDecoder(req.Body)
    var t test_struct
    err := decoder.Decode(&t)
    if err != nil {
        panic(err)
    }
    defer req.Body.Close()
    log.Println(t.Test)
    log.Println(t)
}
func main() {
    http.HandleFunc("/test", test)
    log.Fatal(http.ListenAndServe(":8082", nil))
}
// 2017/04/28 13:31:22 that
// 2017/04/28 13:34:09 {that}
*/
//////////////////////////
/*
// You need to read from `req.Body`. The `ParseForm` method is reading from the `req.Body`
// and then parsing it in standard HTTP encoded format.
// What you want is to read the body and parse it in JSON format.
// Here is your code update
package main
import (
    "encoding/json"
    "log"
    "net/http"
    "io/ioutil"
)
type test_struct struct {
    Test string
}
func test(rw http.ResponseWriter, req *http.Request) {
    body, err := ioutil.ReadAll(req.Body)
    if err != nil {
        panic(err)
    }
    log.Println(string(body))
    var t test_struct
    err = json.Unmarshal(body, &t)
    if err != nil {
        panic(err)
    }
    log.Println(t.Test)
}
func main() {
    http.HandleFunc("/test", test)
    log.Fatal(http.ListenAndServe(":8082", nil))
}
// 2017/04/28 13:42:31 {"test": "that"}
// 2017/04/28 13:42:31 that
*/
/////////////////////////
/*
package main
import (
    "encoding/json"
    "fmt"
    "io"
    "log"
    "strings"
)
func main() {
    const jsonStream = `
        {"Name": "Ed", "Text": "Knock knock."}
        {"Name": "Sam", "Text": "Who's there?"}
        {"Name": "Ed", "Text": "Go fmt."}
        {"Name": "Sam", "Text": "Go fmt who?"}
        {"Name": "Ed", "Text": "Go fmt yourself!"}
    `
    type Message struct {
        Name, Test string
    }
    dec := json.NewDecoder(strings.NewReader(jsonStream))
    for {
        var m Message
        if err := dec.Decode(&m); err == io.EOF {
            break
        } else if err != nil {
            log.Fatal(err)
        }
        fmt.Printf("%s: %s\n", m.Name, m.Test)
    }
}
// The key here being that the OP was looking to decode
type test_struct struct {
    Test string
}
// ...in which case we would drop the `const jsonStream`, and replace the `Message` struct with the `test_struct`.
func test(rw http.ResponseWriter, req *http.Request) {
    dec := json.NewDecoder(req.Body)
    for {
        var t test_struct
        if err := dec.Decode(&t); err == io.EOF {
            break
        } else if err != nil {
            log.Fatal(err)
        }
        log.Printf("%s\n", t.Test)
    }
}
// Since JSON does not normally look like `{"Test": "test", "SomeKey": "SomeVal"}`,
// but rather `{"test": "test", "somekey": "some value"}`, you can restructure your struct like this:
type test_struct struct {
    Test string `json:"test"`
    SomeKey string `json:"some-key"`
}
*/
