// 使用接口展示多态行为

package main
import "fmt"

// notifier 是定义了通知类行为的接口
type notifier interface {
    notify()
}

// user 在程序里定义一个用户类型
type user struct {
    name string
    email string
}

// notify 使用指针接收者实现了notifier 接口
func (u *user) notify() {
    fmt.Printf("sending user email to %s<%s>\n", u.name, u.email)
}

// admin 定义了程序里的管理员
type admin struct {
    name string
    email string
}

// notify 使用指针接收者实现了notifier 接口
func (a *admin) notify() {
    fmt.Printf("sending admin email to %s<%s>\n", a.name, a.email)
}

func main() {
    // 创建一个user 值，并传给sendNotification
    bill := user{"bill", "bill@123.com"}
    sendNotification(&bill)

    // 创建一个admin值并给sendNotification
    lisa := admin{"lisa", "lisa@123.com"}
    sendNotification(&lisa)
}

// sendNotification 接受一个实现了notifier 接口的值，并发送通知
func sendNotification(n notifier) {
    n.notify()
}

// sending user email to bill<bill@123.com>
// sending admin email to lisa<lisa@123.com>
