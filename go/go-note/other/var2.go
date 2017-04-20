package main

func main() {
    x := 100
    println(&x)

    x, y := 200, "abc"      // 注意: x退化为赋值操作，仅有y是变量定义

    println(&x, x)
    println(y)
}
// 0xc420039f70             // 对比变量内存地址可以确认x属于统一变量
// 0xc420039f70 200
// abc
