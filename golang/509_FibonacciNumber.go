// Solution 1; Space O(n) 
func fib(n int) int {
    if n < 2 {
        return n
    }

    return fib(n - 1) + fib(n - 2)
}


// Solution 2; Space O(1)
func fibonacci() func() int {
	fib1, fib2 := 0, 1

	return func() int {
		temp := fib1
		fib1, fib2 = fib2, (fib1 + fib2)
		return temp
	}

}

func fib(n int) int {
    f := fibonacci()
    for i := 0; i < n; i++ {
        f()
    }

    return f()
}
