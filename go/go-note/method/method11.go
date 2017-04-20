package main


func test(x int) func() { // 返回函数类型
    return func() {       // 匿名函数
        println(x)        // 闭包
    }
}

func main() {
    x := 100
    f := test(x)
    f()
}

// 100
