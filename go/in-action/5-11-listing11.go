// 声明并使用方法

package main
import "fmt"

type user struct {
    name string
    email string
}

// notify 使用值接收者实现了一个方法
func (u user) notify() {
    fmt.Printf("sending user email to %s<%s>\n",
        u.name,
        u.email)
}

// changeEmail 使用指针接收者实现了一个方法
func (u *user) changeEmail(email string) {
    u.email = email
}

func main() {
    // user类型的值可以用来调用
    // 使用值接收者声明的方法
    bill := user{"bill", "bill@123.com"}
    bill.notify()

    // 指向user类型值的指针也可以用来调用
    // 使用值接收者声明的方法
    lisa := &user{"lisa", "lisa@123.com"}
    lisa.notify()

    // user类型的值可以用来调用
    // 使用指针接收者声明的方法
    bill.changeEmail("bill@new.com")
    bill.notify()

    // 指向user类型值的指针可以用来调用
    // 使用指针接收者声明的方法
    lisa.changeEmail("lisa@new.com")
    lisa.notify()
}
// sending user email to bill<bill@123.com>
// sending user email to lisa<lisa@123.com>
// sending user email to bill<bill@new.com>
// sending user email to lisa<lisa@new.com>
