package main

var x = 100

func main() {
    println(&x, x)      // 全局变量

    x := "abc"          // 重新定义和初始化同名局部变量

    println(&x, x)
}
// 0x1096021 100        // 对比内存地址，可以看出是两个不同变量
// 0xc420039f68 abc
