package main

const x, y int = 1, 2   // 多常量初始化
const s = "hello world" // 类型推断

const (                 // 常量组
    a, b = 10, 100
    c bool = false
)

func main() {
    const x = "xxxxxxx" // 未使用局部常量不会引发编译错误
}
