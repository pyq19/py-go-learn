// 使用接口
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

// notify 是使用指针接收者实现的方法
func (u *user) notify() {
    fmt.Printf("sending user email to %s<%s>\n", u.name, u.email)
}

func main() {
    // 创建一个user 类型的值，并发送通知
    u := user{"bill", "bill@123.com"}

//    sendNotification(u)

    // 不能将u（类型是user）作为sendNotification 的参数类型notifier
    // user 类型并没有实现notifier(notify 方法使用指针接收者声明)
    // ./5-36-listing36.go:25: cannot use u (type user) as type notifier in argument to sendNotification:
    //    user does not implement notifier (notify method has pointer receiver)

    sendNotification(&u)
    // 传入地址，不再有错误
}

// sendNotification 接收实现notifier 接口的值，并发送通知
func sendNotification(n notifier) {
    n.notify()
}

// sending user email to bill<bill@123.com>
