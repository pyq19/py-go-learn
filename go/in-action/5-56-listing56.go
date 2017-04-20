// 将嵌入类型应用于接口
package main
import "fmt"

type notifier interface {
    notify()
}

type user struct {
    name string
    email string
}

func (u *user) notify() {
    fmt.Printf("sending user email to %s<%s>\n", u.name, u.email)
}

type admin struct {
    user
    level string
}

func main() {
    ad := admin{
        user: user{
            name: "john",
            email: "email@email.com",
        },
        level: "super",
    }

    sendNotification(&ad)
}

func sendNotification(n notifier) {
    n.notify()
}
//sending user email to john<email@email.com>
