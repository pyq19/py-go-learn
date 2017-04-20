// type embedding 嵌入类型
// 将一个类型嵌入另一个类型，以及内部类型和外部类型之间的关系 

package main
import "fmt"

type user struct {
    name string
    email string
}

func (u *user) notify() {
    fmt.Printf("sending user email to %s<%s>\n", u.name, u.email)
}

type admin struct {
    user            // 嵌入类型
    level string
}

func main() {
    ad := admin{
        user: user{
            name: "join smith",
            email: "join@123.com",
        },
        level: "super",
    }

    // 可以直接访问内部类型的方法
    ad.user.notify()

    // 内部类型的方法也被提升到外部类型
    ad.notify()
}
// sending user email to join smith<join@123.com>
// sending user email to join smith<join@123.com>
