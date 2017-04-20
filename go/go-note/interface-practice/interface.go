package main

import "fmt"

type Stringer interface {
    String() string
}

type Printer interface {
    Stringer        // 接口嵌入
    Print()
}

type User struct {
    id int
    name string
}

func (self *User) String() string {
    return fmt.Sprintf("user %d, %s", self.id, self.name)
}

func (self *User) Print() {
    fmt.Println(self.String())
}

func main() {
    var t Printer = &User{1, "Tom"}     // *User方法集合包含String Print
    t.Print()
}
// user 1, Tom
