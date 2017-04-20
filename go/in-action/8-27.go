// 解码JSON 字符串

package main
import (
    "encoding/json"
    "fmt"
    "log"
)

type Contact struct {
    Name    string  `json:"name"`
    Title   string  `json:"title"`
    Contact struct  {
        Home    string  `json:"home"`
        Cell    string  `json:"cell"`
    }   `json:"contact"`
}

var JSON = `{
    "name": "Gopher",
    "title": "programer",
    "contact": {
        "home": "1231.23.1.2312",
        "cell": "123.123.123"
    }
}`

func main() {
    var c Contact   // 将JSON字符串反序列化到变量
    err := json.Unmarshal([]byte(JSON), &c)
    if err != nil {
        log.Println("ERROR: ", err)
        return
    }

    fmt.Println(c)
}
// {Gopher programer {1231.23.1.2312 123.123.123}}
