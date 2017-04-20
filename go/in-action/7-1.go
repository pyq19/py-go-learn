// runner 包管理处理任务的运行和生命周期
// runner 包用于展示如何使用通道来监视程序的执行时间，如果程序运行时间太长，
// 也可以用runner 包来终止程序

package runner

import (
    "errors"
    "os"
    "os/signal"
    "time"
)


