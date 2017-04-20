// 解码JSON 字符串
package main
import (
    "encoding/json"
    "fmt"
    "log"
)

var JSON = `{
    "name": "Gopher",
    "title": "programer",
    "contact": {
        "home": "1231.23.1.2312",
        "cell": "123.123.123"
    }
}`

func main() {
    var c map[string]interface{}    // 将JSON 字符串反序列化到map 变量
    err := json.Unmarshal([]byte(JSON), &c)
    if err != nil {
        log.Println("ERROR: ", err)
        return
    }

    fmt.Println("name ->", c["name"])
    fmt.Println("title ->", c["title"])
    fmt.Println("contact")
    fmt.Println("H ->", c["contact"].(map[string]interface{})["home"])
    fmt.Println("C ->", c["contact"].(map[string]interface{})["cell"])

}
// name -> Gopher
// title -> programer
// contact
// H -> 1231.23.1.2312
// C -> 123.123.123
