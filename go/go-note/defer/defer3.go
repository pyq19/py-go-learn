package main

func test() (z int) {
    defer func() {
        println("defer ->", z)
        z += 100                // 修改命名返回值
    }()
    return 100                  // 实际执行次序z=100, call defer, ret
}

func main() {
    println("test ->", test())
}
// defer -> 100
// test -> 200
