// 直接调用匿名字段的方法，可以实现与继承类似的功能

package main
import "fmt"

type user struct {
    name string
    age byte
}

func (u user) ToString() string {
    return fmt.Sprintf("%+v", u)
}

type manager struct {
    user
    title string
}

func main() {
    var m manager
    m.name = "Tom"
    m.age = 29

    println(m.ToString())   // 调用user.ToString()
}
// {name:Tom age:29}
