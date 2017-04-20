package main
import "fmt"

func main() {
    m := make(map[string] int)  // 创建字典类型对象
    m["a"] = 1                  // 添加或设置
    x, ok := m["b"]             // 使用ok-idiom获取值，可知道key/value是否存在
    fmt.Println(x, ok)

    delete(m, "a")              // 删除
}
// 0 false
